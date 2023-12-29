-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Little Lemon_DB
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Little Lemon_DB
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Little Lemon_DB` ;
USE `Little Lemon_DB` ;

-- -----------------------------------------------------
-- Table `Little Lemon_DB`.`Customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Little Lemon_DB`.`Customer` (
  `CustomerID` INT NOT NULL,
  `CustomerName` VARCHAR(255) NOT NULL,
  `CustomerPhone` VARCHAR(45) NOT NULL,
  `CustomerEmail` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`CustomerID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Little Lemon_DB`.`Menu`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Little Lemon_DB`.`Menu` (
  `MenuID` INT NOT NULL,
  `Starters` VARCHAR(255) NOT NULL,
  `Entrees` VARCHAR(255) NOT NULL,
  `Desserts` VARCHAR(255) NOT NULL,
  `Drinks` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`MenuID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Little Lemon_DB`.`Staff`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Little Lemon_DB`.`Staff` (
  `StaffID` INT NOT NULL,
  `Role` VARCHAR(255) NOT NULL,
  `Salary` INT NOT NULL,
  PRIMARY KEY (`StaffID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Little Lemon_DB`.`Order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Little Lemon_DB`.`Order` (
  `OrderID` INT NOT NULL,
  `OrderDate` DATE NOT NULL,
  `Quantity` INT NOT NULL,
  `TotalCost` DECIMAL(10,2) NOT NULL,
  `MenuID` INT NOT NULL,
  `StaffID` INT NOT NULL,
  PRIMARY KEY (`OrderID`),
  INDEX `MenuID_FK_idx` (`MenuID` ASC) VISIBLE,
  INDEX `StaffID_FK_idx` (`StaffID` ASC) VISIBLE,
  CONSTRAINT `MenuID_FK`
    FOREIGN KEY (`MenuID`)
    REFERENCES `Little Lemon_DB`.`Menu` (`MenuID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `StaffID_FK`
    FOREIGN KEY (`StaffID`)
    REFERENCES `Little Lemon_DB`.`Staff` (`StaffID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Little Lemon_DB`.`Booking`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Little Lemon_DB`.`Booking` (
  `BookingID` INT NOT NULL,
  `Date` DATE NOT NULL,
  `Table` INT NOT NULL,
  `OrderID` INT NOT NULL,
  `CustomerID` INT NOT NULL,
  PRIMARY KEY (`BookingID`),
  INDEX `OrderID_FK_idx` (`OrderID` ASC) VISIBLE,
  INDEX `CustomerID_FK_idx` (`CustomerID` ASC) VISIBLE,
  CONSTRAINT `OrderID_FK`
    FOREIGN KEY (`OrderID`)
    REFERENCES `Little Lemon_DB`.`Order` (`OrderID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `CustomerID_FK`
    FOREIGN KEY (`CustomerID`)
    REFERENCES `Little Lemon_DB`.`Customer` (`CustomerID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Little Lemon_DB`.`Address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Little Lemon_DB`.`Address` (
  `AddressID` INT NOT NULL,
  `Street` VARCHAR(255) NOT NULL,
  `City` VARCHAR(255) NOT NULL,
  `State` VARCHAR(45) NOT NULL,
  `Zipcode` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`AddressID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Little Lemon_DB`.`Delivery`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Little Lemon_DB`.`Delivery` (
  `DeliveryID` INT NOT NULL,
  `OrderID` INT NOT NULL,
  `AddressID` INT NOT NULL,
  `DeliveryDate` DATE NOT NULL,
  `DeliveryStatus` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`DeliveryID`),
  INDEX `OrderID_FK_idx` (`OrderID` ASC) VISIBLE,
  INDEX `AddressID_FK_idx` (`AddressID` ASC) VISIBLE,
  CONSTRAINT `OrderID1_FK`
    FOREIGN KEY (`OrderID`)
    REFERENCES `Little Lemon_DB`.`Order` (`OrderID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `AddressID_FK`
    FOREIGN KEY (`AddressID`)
    REFERENCES `Little Lemon_DB`.`Address` (`AddressID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;