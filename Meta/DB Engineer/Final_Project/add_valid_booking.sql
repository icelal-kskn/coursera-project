CREATE DEFINER=`user00`@`%` PROCEDURE `AddValidBooking`(IN BookingDate DATE, IN TableNumber INT)
BEGIN
DECLARE _rollback BOOL DEFAULT 0;
DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET _rollback = 1; 
START TRANSACTION;

SELECT Validate(COUNT(*), CONCAT("Table ", TableNumber, " is already booked."))
FROM Booking
WHERE date = BookingDate AND table_number = TableNumber;

	INSERT INTO Booking(date, table_number)
    VALUES (BookingDate, TableNumber);
    
    IF _rollback THEN 
    SELECT CONCAT("Table ", TableNumber, " is already booked - booking cancelled.") AS BookingStatus;
    ROLLBACK;
    ELSE
	COMMIT;
    END IF; 
    
END