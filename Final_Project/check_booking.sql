CREATE DEFINER=`user00`@`%` PROCEDURE `CheckBooking`(booking_date DATE, table_number INT)
BEGIN
DECLARE bookedTable INT DEFAULT 0;
SELECT COUNT(bookedTable) 
	INTO bookedTable
    FROM Booking WHERE BookingDate = booking_date AND TableNumber = table_number;
    
    IF bookedTable > 0 THEN 
    SELECT CONCAT ("Table ", table_number, " is already booked.") AS BookingStatus;
    ELSE 
    SELECT CONCAT ("Table ",  table_number,  " is not booked.") AS BookingStatus;
    END IF;
END