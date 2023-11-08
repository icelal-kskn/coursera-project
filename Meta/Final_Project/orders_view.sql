CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `user00`@`%` 
    SQL SECURITY DEFINER
VIEW `Orders_View` AS
    SELECT 
        `Orders`.`OrderID` AS `OrderID`,
        `Orders`.`Quantity` AS `Quantity`,
        `Orders`.`TotalCost` AS `TotalCost`
    FROM
        `Orders`
    WHERE
        (`Orders`.`Quantity` > 2)