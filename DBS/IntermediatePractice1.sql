use UNIVERSITY;

select *
from student join takes on student.ID = takes.ID;

select *
from student,takes
where student.ID = takes.Id;