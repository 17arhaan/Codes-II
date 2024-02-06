use UNIVERSITY;

select * from student;
select * from takes;

select *
from student join takes on student.ID = takes.ID;

select *
from student,takes
where student.ID = takes.ID;

select student.ID as ID , name , dept_name , tot_cred , sec_id , semester , year ,grade
from student , takes
where student.ID = takes.ID;

select *
from student natural left outer join takes;

select *
from student natural right outer join takes;

select *
from ( select *
    from student
    where dept_name = 'Comp. Sci' )
    natural full outer join
    ( select * 
        from takes
        where semester = 'Spring '
);

select * 
from student left outer join takes on TRUE
where student.ID = takes.ID;