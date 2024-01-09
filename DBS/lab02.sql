use Arhaan;

create table Deppartmenntt(
    DeptNo numeric primary key,
    DeptName varchar(20) unique,
    Location varchar(20)
);

create table Empployyees(
    EmpNo int primary key,
    EmpName varchar(10) not NULL,
    Gender char(1) check (Gender in ('M','F')) not NULL,
    Salary int(6) not null,
    Address varchar(10) not NULL,
    DNo int(5),
    foreign key (DNo) references Deppartmenntt(DeptName)
);

insert into Empployyees values(1001,'A','M',15000,'Delhi',1079);
insert into Empployyees values(1002,'B','F',20000,'Tokyo',1177);
insert into Empployyees values(1003,'C','M',10000,'London',1272);
insert into Empployyees values(1004,'D','F',50000,'Paris',1371);

insert into Deppartmenntt values(1079,'CSE Core','Chandni Chowk');
insert into Deppartmenntt values(1177,'MechX','Chuo - Dori');
insert into Deppartmenntt values(1272,'CSE AI ML','Oxford St');
insert into Deppartmenntt values(1371,'IT','Rue De Buci');

select * from Empployyees,Deppartmenntt;

insert into Employees values(1004,'E','They',50000,'Dubai',1371);
insert into Department values(1372,'DSE','Expo Road');


