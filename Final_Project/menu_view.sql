CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `user00`@`%` 
    SQL SECURITY DEFINER
VIEW `Menu_View` AS
    SELECT 
        `Orders`.`OrderID` AS `OrderID`,
        `Orders`.`TotalCost` AS `TotalCost`,
        `Customer`.`CustomerID` AS `CustomerID`,
        `Customer`.`CustomerName` AS `CustomerName`,
        `Menu`.`Starters` AS `Starters`,
        `Menu`.`Entrees` AS `Entrees`,
        `Menu`.`MenuID` AS `MenuID`
    FROM
        ((`Orders`
        JOIN `Customer` ON ((`Orders`.`OrderID` = `Customer`.`CustomerID`)))
        JOIN `Menu` ON ((`Customer`.`CustomerID` = `Menu`.`MenuID`)))