from mysql.connector.pooling import MySQLConnectionPool
from mysql.connector import Error

dbconfig = {
    "host": "your_host_mihgt_be_LocalHost",
    "user": "USERNAME",
    "password": "SUPERSECRETPASSWORD",
    "database": "WHATTHEDB"
}

try:
    connection_pool = MySQLConnectionPool(pool_name="pool_b", pool_size=2, **dbconfig)
    print("BaÄŸlantÄ± havuzu baÅŸarÄ±yla oluÅŸturuldu!")
except Error as e:
    print(f"Hata: {e}")
 #task1


 
guests = [
    (8, "Anees", "Java", "18:00", 6),
    (5, "Bald", "Vin", "19:00", 6),
    (12, "Jay", "Kon", "19:30", 6)
]

try:
    conn1 = connection_pool.get_connection()
    conn2 = connection_pool.get_connection()
    cursor1 = conn1.cursor()
    cursor2 = conn2.cursor()

    INSERT_QUERY = "INSERT INTO Bookings (TableNumber, FirstName, LastName, BookingTime, EmployeeID) VALUES (%s, %s, %s, %s, %s)"
    cursor1.executemany(INSERT_QUERY, guests[:2])
    conn1.commit()
    cursor1.close()
    conn1.close()

    cursor2.execute(INSERT_QUERY, guests[2])
    conn2.commit()
    cursor2.close()
    conn2.close()
except Error as e:
    print(f"Hata: {e}")
 #task2

try:
    conn = connection_pool.get_connection()
    cursor = conn.cursor()

    manager_query = "SELECT Name, EmployeeID FROM Employees WHERE Role = 'Manager'"
    cursor.execute(manager_query)
    manager_data = cursor.fetchone()
    manager_name, manager_employee_id = manager_data

    highest_salary_query = "SELECT Name, Role FROM Employees ORDER BY Salary DESC LIMIT 1"
    cursor.execute(highest_salary_query)
    highest_salary_data = cursor.fetchone()
    highest_salary_name, highest_salary_role = highest_salary_data

    guests_between_18_20_query = "SELECT COUNT(*) FROM Bookings WHERE BookingTime BETWEEN '18:00' AND '20:00'"
    cursor.execute(guests_between_18_20_query)
    guests_count = cursor.fetchone()[0]

    waiting_guests_query = "SELECT CONCAT(FirstName, ' ', LastName) AS FullName, BookingID FROM Bookings ORDER BY BookingSlot"
    cursor.execute(waiting_guests_query)
    waiting_guests = cursor.fetchall()

    print("Little Lemon YÃ¶neticisi:", manager_name, "EmployeeID:", manager_employee_id)
    print("En YÃ¼ksek MaaÅŸlÄ± Ã‡alÄ±ÅŸan:", highest_salary_name, "Rol:", highest_salary_role)
    print("18:00 ile 20:00 arasÄ±nda Rezervasyon Yapan Misafir SayÄ±sÄ±:", guests_count)
    print("Oturmak Ä°Ã§in Bekleyen Misafirler:")
    for guest in waiting_guests:
        print("Tam Ad:", guest[0], "BookingID:", guest[1])

    cursor.close()
    conn.close()
except Error as e:
    print(f"Hata: {e}")
#task3



try:
    connection2 = connection_pool.get_connection()
    cursor = connection2.cursor()

    sales_report_query = """
    CREATE PROCEDURE IF NOT EXISTS BasicSalesReport()
    BEGIN
        SELECT 
        SUM(BillAmount) AS TotalSale,
        AVG(BillAmount) AS AverageSale,
        MIN(BillAmount) AS MinBillPaid,
        MAX(BillAmount) AS MaxBillPaid
        FROM Orders;
    END
    """

    cursor.execute(sales_report_query)
    cursor.callproc("BasicSalesReport")

    results = next(cursor.stored_results())
    results = results.fetchall()

    for column_id in cursor.stored_results():
        cols = [column[0] for column in column_id.description]

    print("Basic Sales Report:")
    for result in results:
        print(cols[0], ":", result[0])
        print(cols[1], ":", result[1])
        print(cols[2], ":", result[2])
        print(cols[3], ":", result[3])

    connection2.close()
    print("Connection2 is closed")
except Error as e:
    print(f"Hata: {e}")
#task4 


try:
    connection3 = connection_pool.get_connection()
    cursor = connection3.cursor(buffered=True)

    upcoming_bookings_query = """
    SELECT B.BookingSlot, CONCAT(G.FirstName, ' ', G.LastName) AS GuestName, 
    CONCAT('Assigned to: ', E.Name, ' [', E.Role, ']') AS EmployeeInfo
    FROM Bookings B
    JOIN Employees E ON B.EmployeeID = E.EmployeeID
    ORDER BY B.BookingSlot ASC
    LIMIT 3;
    """

    cursor.execute(upcoming_bookings_query)
    records = cursor.fetchall()

    for record in records:
        print(record[0])
        print(record[1])
        print(record[2])
        print("\n")

    cursor.close()
    connection3.close()
except Error as e:
    print(f"Hata: {e}")
#task5