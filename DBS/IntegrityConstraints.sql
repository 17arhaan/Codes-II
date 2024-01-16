use Arhaan_Main;
CREATE TABLE Department (
    DeptNo INT PRIMARY KEY,
    DeptName VARCHAR(255) UNIQUE,
    Location VARCHAR(255)
);
CREATE TABLE Employee (
    EmpNo INT PRIMARY KEY,
    EmpName VARCHAR(255) NOT NULL,
    Gender CHAR(1) NOT NULL CHECK (Gender IN ('M', 'F')),
    Salary DECIMAL(10, 2) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    DNo INT,
    FOREIGN KEY (DNo) REFERENCES Department(DeptNo)
);

INSERT INTO Department (DeptNo, DeptName, Location)
VALUES
    (1, 'CSE AI ML', 'New York'),
    (2, 'CSE Core', 'San Francisco'),
    (3, 'Mechanical', 'Chicago');

INSERT INTO Employee (EmpNo, EmpName, Gender, Salary, Address, DNo)
VALUES
    (101, 'Arhaan Girdhar', 'M', 60000.00, '123 Main St', 1),
    (102, 'Saivya Singh', 'F', 55000.00, '456 Oak St', 2),
    (103, 'Nakul Gupta', 'M', 70000.00, '789 Pine St', 3);

SELECT 
    Employee.EmpNo,
    Employee.EmpName,
    Employee.Gender,
    Employee.Salary,
    Employee.Address,
    Department.DeptName,
    Department.Location
FROM 
    Employee
JOIN 
    Department ON Employee.DNo = Department.DeptNo;

INSERT INTO Department (DeptNo, DeptName, Location)
VALUES
    (4,'Chemical','Ghaziabad');

INSERT INTO Employee (EmpNo, EmpName, Gender, Salary, Address, DNo)
VALUES
    (104,'Ayushman','G',9000.00,'Avantika',4);

DELETE FROM Department WHERE DeptNo = 4;

ALTER TABLE Employee
DROP CONSTRAINT DNo_FK;

ALTER TABLE Employee
ADD CONSTRAINT DNo_FK FOREIGN KEY (DNo)
REFERENCES Department (DeptNo) ON DELETE CASCADE;

ALTER TABLE Employee
ADD CONSTRAINT scheck CHECK (SALARY >= 10000);


drop table Employee;
drop table Department;