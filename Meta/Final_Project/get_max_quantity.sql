CREATE DEFINER=`user00`@`%` PROCEDURE `GetMaxQuantity`()
BEGIN
SELECT MAX(Quantity)
FROM Orders;
END