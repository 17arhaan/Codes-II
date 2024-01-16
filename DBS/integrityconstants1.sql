use Arhaanmain;
CREATE TABLE Department03 (
    DeptNo INT PRIMARY KEY,
    DeptName VARCHAR(255) UNIQUE,
    Location VARCHAR(255)
);
CREATE TABLE Employee03 (
    EmpNo INT PRIMARY KEY,
    EmpName VARCHAR(255) NOT NULL,
    Gender CHAR(1) NOT NULL CHECK (Gender IN ('M', 'F')),
    Salary DECIMAL(10, 2) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    DNo INT,
    FOREIGN KEY (DNo) REFERENCES Department03(DeptNo)
);

INSERT INTO Department03 (DeptNo, DeptName, Location)
VALUES
    (1, 'CSE AI ML', 'New York'),
    (2, 'CSE Core', 'San Francisco'),
    (3, 'Mechanical', 'Chicago');

INSERT INTO Employee03 (EmpNo, EmpName, Gender, Salary, Address, DNo)
VALUES
    (101, 'Arhaan Girdhar', 'M', 60000.00, '123 Main St', 1),
    (102, 'Saivya Singh', 'F', 55000.00, '456 Oak St', 2),
    (103, 'Nakul Gupta', 'M', 70000.00, '789 Pine St', 3);

SELECT 
    Employee03.EmpNo,
    Employee03.EmpName,
    Employee03.Gender,
    Employee03.Salary,
    Employee03.Address,
    Department03.DeptName,
    Department03.Location
FROM 
    Employee03
JOIN 
    Department03 ON Employee03.DNo = Department03.DeptNo;

INSERT INTO Department03 (DeptNo, DeptName, Location)
VALUES
    (4,'Chemical','Ghaziabad');

INSERT INTO Employee03 (EmpNo, EmpName, Gender, Salary, Address, DNo)
VALUES
    (104,'Ayushman','G',9000.00,'Avantika',4);

DELETE FROM Department03 WHERE DeptNo = 4;

ALTER TABLE Employee03
DROP CONSTRAINT DNo_FK;

ALTER TABLE Employee03
ADD CONSTRAINT DNo_FK FOREIGN KEY (DNo)
REFERENCES Department03 (DeptNo) ON DELETE CASCADE;

ALTER TABLE Employee03
ADD CONSTRAINT scheck CHECK (SALARY >= 10000);