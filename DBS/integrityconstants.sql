use ChatGPT;

CREATE TABLE Departmentt (
    DeptNo INT PRIMARY KEY,
    DeptName VARCHAR(255) UNIQUE,
    Location VARCHAR(255)
);

CREATE TABLE Employeee (
    EmpNo INT PRIMARY KEY,
    EmpName VARCHAR(255) NOT NULL,
    Gender CHAR(1) NOT NULL CHECK (Gender IN ('M', 'F')),
    Salary DECIMAL(10, 2) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    DNo INT,
    FOREIGN KEY (DNo) REFERENCES Departmentt(DeptNo)
);

INSERT INTO Departmentt (DeptNo, DeptName, Location)
VALUES
    (1, 'HR', 'New York'),
    (2, 'IT', 'San Francisco'),
    (3, 'Finance', 'Chicago');

INSERT INTO Employeee (EmpNo, EmpName, Gender, Salary, Address, DNo)
VALUES
    (101, 'John Doe', 'M', 60000.00, '123 Main St', 1),
    (102, 'Jane Smith', 'F', 55000.00, '456 Oak St', 2),
    (103, 'Bob Johnson', 'M', 70000.00, '789 Pine St', 3);

select * from Employeee,Departmentt;
