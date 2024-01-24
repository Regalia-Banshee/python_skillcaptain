
USE siddhu_pajjidb;
drop table employee_data;
CREATE TABLE `Employee_data` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `Department` varchar(255) DEFAULT NULL,
  `DateOfBirth` date DEFAULT NULL,
  `Salary` decimal(10,2) DEFAULT NULL,
  `IsActive` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO employee_data (ID, Name, Email , Department, DateOfBirth, Salary, IsActive)
VALUES
  (1, 'John Doe', 'johndoe@example.com', 'Sales', '1990-05-15', 5000.00, true),
  (2, 'Jane Smith', 'janesmith@example.com', 'Marketing', '1992-09-20', 6000.00, false);
