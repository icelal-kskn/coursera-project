from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.views import APIView
from .models import *
from django.db.utils import IntegrityError
from django.contrib.auth.models import User, Group
from .serializers import *

# Create your views here.
class WritePermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_authenticated
        else :
            return request.user.is_authenticated and request.user.groups.filter(name='manager').exists()

class ManagerOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='manager').exists()

class CustomerOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        return not request.user.groups.filter(name='manager').exists() or not request.user.groups.filter(name='delivery_crew').exists()

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [WritePermission]
    queryset = MenuItem.objects.all()
    filterset_fields = ['title','featured', 'price']
    search_fields = ['title']
    ordering_fields = ['price', 'title']
    serializer_class = MenuItemSerializer


class MenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [WritePermission]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
class ManagersGroup(APIView):
    permission_classes = [ManagerOnlyPermission]
    group_name = 'manger'
    filterset_fields = ['username', 'email']
    search_fields = ['username']
    ordering_fields = ['email']
    def get(self, request):
        query = User.objects.filter(groups__name = self.group_name)
        queryList = list(query.values())
        return Response(queryList, status=status.HTTP_200_OK)
    
    def post(self, request):
        username = request.data.get('username')
        try:
            user_object = User.objects.get(username=username)
            group = Group.objects.get(name=self.group_name)
            user_object.groups.add(group)
            user_object.save()
            return Response(status=status.HTTP_201_CREATED)
        except Exception:
            return Response({"message": "user not found"}, status=status.HTTP_404_NOT_FOUND)
    
class ManagerSingle(APIView):
    permission_classes = [ManagerOnlyPermission]
    group_name = 'manager'
    def delete(self, request, pk):
        try:
            user_object = User.objects.get(pk=pk)
            group = Group.objects.get(name=self.group_name)
            user_object.groups.remove(group)
            user_object.save()
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response({"message": "user not found"}, status=status.HTTP_404_NOT_FOUND)
        
class CartView(APIView):
    permission_classes = [IsAuthenticated, CustomerOnlyPermission]
    
    def post(self, request):
        data = request.data.copy()
        data['user_id'] = request.user.id
        seriazedData = CartSerializer(data=data)
        if seriazedData.is_valid():
            try:
                seriazedData.save()
            except Exception:
                return Response({'message': "items already added"}, status=status.HTTP_400_BAD_REQUEST)
            return Response(seriazedData.data, status=status.HTTP_201_CREATED)
        else:
            return Response(seriazedData.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        try:
            carts_to_delete = Cart.objects.filter(user=request.user)
            carts_to_delete.delete()
            return Response(status=status.HTTP_200_OK)
        except IntegrityError:
            return Response({'status': 'internal error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def get(self, request):
        cartItems = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(cartItems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class OrdersView(APIView):
    permission_classes = [IsAuthenticated]
    filterset_fields = ['user', 'menuitem', 'price']
    ordering_fields = ['price']
    def post(self, request):
        userCartItems = Cart.objects.filter(user=request.user)
        cart_items_list = list(userCartItems.values())
        seriazedData = OrderItemSerializer(data=cart_items_list, many=True)
        if seriazedData.is_valid():
            try:
                seriazedData.save()
                userCartItems.delete()
            except Exception as star:
                print(star)
                print(userCartItems)
                return Response({'message': "items already added"}, status=status.HTTP_400_BAD_REQUEST)
            return Response(seriazedData.data, status=status.HTTP_201_CREATED)
        else:
            return Response(seriazedData.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        queryset = Order.objects.filter(user=request.user)
        if request.user.groups.filter(name='manager').exists():
            queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class OrderSingleViewPermission(BasePermission):
    
    def has_permission(self, request, view):
        if request.method == 'GET':
            return not request.user.groups.filter(name='manager').exists() or not request.user.groups.filter(name='delivery_crew').exists()
        elif request.method == 'DELETE':
            return request.user.groups.filter(name='manager').exists() 
        elif request.method == 'PATCH':
            return request.user.groups.filter(name='manager').exists() or request.user.groups.filter(name='delivery_crew').exists()
         
class OrderSingleView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, OrderSingleViewPermission]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        if order.user == request.user:
            queryset = OrderItem.objects.filter(user=request.user)
            serializer = OrderItemSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'status': "bad request"}, status=status.HTTP_400_BAD_REQUEST)
