CREATE DEFINER=`user00`@`%` PROCEDURE `CancelBooking`(IN booking_ID INT)
BEGIN
DELETE FROM Booking WHERE BookingID = booking_ID;

SELECT CONCAT("Booking ", booking_ID, " canceled") AS "Cancellation";

END