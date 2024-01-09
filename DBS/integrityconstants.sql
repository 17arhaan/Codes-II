use Arhaanmain;
CREATE TABLE Department1 (
    DeptNo INT PRIMARY KEY,
    DeptName VARCHAR(255) UNIQUE,
    Location VARCHAR(255)
);
CREATE TABLE Employee1 (
    EmpNo INT PRIMARY KEY,
    EmpName VARCHAR(255) NOT NULL,
    Gender CHAR(1) NOT NULL CHECK (Gender IN ('M', 'F')),
    Salary DECIMAL(10, 2) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    DNo INT,
    FOREIGN KEY (DNo) REFERENCES Department1(DeptNo)
);

INSERT INTO Department1 (DeptNo, DeptName, Location)
VALUES
    (1, 'CSE AI ML', 'New York'),
    (2, 'CSE Core', 'San Francisco'),
    (3, 'Mechanical', 'Chicago');

INSERT INTO Employee1 (EmpNo, EmpName, Gender, Salary, Address, DNo)
VALUES
    (101, 'Arhaan Girdhar', 'M', 60000.00, '123 Main St', 1),
    (102, 'Saivya Singh', 'F', 55000.00, '456 Oak St', 2),
    (103, 'Nakul Gupta', 'M', 70000.00, '789 Pine St', 3);

SELECT 
    Employee1.EmpNo,
    Employee1.EmpName,
    Employee1.Gender,
    Employee1.Salary,
    Employee1.Address,
    Department1.DeptName,
    Department1.Location
FROM 
    Employee1
JOIN 
    Department1 ON Employee1.DNo = Department1.DeptNo;
