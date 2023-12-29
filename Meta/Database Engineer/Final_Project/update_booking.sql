CREATE DEFINER=`user00`@`%` PROCEDURE `UpdateBooking`(IN booking_ID INT, IN booking_date DATE)
BEGIN
UPDATE Booking SET BookingDate = booking_date WHERE BookingID = booking_ID; 
SELECT CONCAT("Booking ", booking_ID, " updated.") AS Confirmation;
END