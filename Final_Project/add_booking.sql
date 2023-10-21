CREATE DEFINER=`user00`@`%` PROCEDURE `AddBooking`(IN booking_ID INT, IN booking_date DATE, IN table_number INT, IN customer_ID INT)
BEGIN
INSERT INTO Booking(BookingID, BookingDate, TableNumber, CustomerID) VALUES (booking_ID, booking_date, table_number, customer_ID);
SELECT "New booking added" AS Confirmation; 
END