---------Lab 1

create database midterm;
use midterm;

create table student (
    stu_num int(5) primary key,
    stu_name varchar(10) not null,
    stu_branch varchar(5),
    stu_gender char(1) check (stu_gender in ('M','F')),
    foreign key (stu_num) references employee(emp_num)
);

create table employee(
    emp_name varchar(10) not null,
    emp_num int(3) primary key,
    emp_age int(3) unique,
    emp_salary int(7)
);

insert into employee values('Arhaan',62050,20,1000000);
insert into employee values('Arhaa',62051,43,1000);
insert into employee values('Arha',62052,76,100);
insert into employee values('Arh',62053,12,10000);

insert into student values (62050,'Arhaan','AI ML','M');
insert into student values (62051,'Arhaa','CSE','F');
insert into student values (62052,'Arha','IT','F');
insert into student values (62053,'Arh','MechX','M');

select * from student,employee; 
select * from student;
select * from employee;

---------Lab 2

use midterm;
select * from student;
alter table student drop column stu_branch;

select stu_name , stu_branch , stu_gender ,emp_num, emp_age , emp_salary
from student
join employee on stu_num = emp_num;

--------------

use midterm;
select emp_num
from employee
where emp_name Like "%Arhaan%";

--------------

/*
DATE_FORMAT() is a MySQL function used to format dates.
%d represents the day of the month.
%b represents the abbreviated month name (e.g., Jan, Feb, Mar).
%Y represents the full year (four digits).
%y represents the year with two digits.
%m represents the month as a two-digit number.
*/

create table date(
    name varchar(10),
    birth_date int(10)
);

insert into date values("Arhaan",17012004)
insert into date values("Arhaann",19112024)

select * from date;

use midterm;

SELECT name,DATE_FORMAT(birth_date, '%d-%m-%Y') AS 'DD-MO-YYYY'
FROM date;

----------Lab 3

create table num1(
    name_one varchar(5),
    age_one int(3),
    salary_one int(5)
);
create table num2(
    name_two varchar(5),
    age_two int(3),
    salary_two int(5)
);
insert into num1 values ("ABC",10,5000)
insert into num1 values ("DEF",11,6000)
insert into num1 values ("GHI",12,7000)

insert into num2 values ("ABC",9,2000)
insert into num2 values ("DEF",11,3000)
insert into num2 values ("XYZ",20,4000)

select * from num1;
select * from num2;

select * from num1
UNION
select * from num2;

select * from num1
INTERSECT
select * from num2;

select * from num1
MINUS
select * from num2;

use midterm;


select distinct course_id
from takes
where(semester = 'Fall' and year = 2009);

-- select distinct name 
-- from student
-- where name in (
--     select name 
--     from instructor
--     where instructor.name = student.name
-- );

select distinct student.name 
from student,instructor 
where student.name = instructor.name;

use University;


----------Lab 4
