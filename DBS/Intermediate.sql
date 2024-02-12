use UNIVERSITY;
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

--1
select course_id from takes where semester = 'fall' and year = 2009
UNION
select course_id from takes where semester = 'spring' and year = 2010;
--2
select course_id from takes where semester = 'fall' and year = 2009
INTERSECT
select course_id from takes where semester = 'spring' and year = 2010;
--3
select course_id from takes where semester = 'fall' and year = 2009;
-- MINUS
select course_id from takes where semester = 'summer' and year = 2010;
--4
select course_id from takes where grade = 'null';
--5
select distinct course_id
from course
where (semester = 'Fall' and year = 2009)
  and course_id in (
    select course_id
    from course
    where semester = 'Spring' and year = 2010
  );
--6
select DISTINCT s_ID
from advisor
where i_ID in (
    select i_ID
    from advisor
    where  ID = 10101
  );
--7
select distinct course_id
from course
where (semester = 'Fall' and year = 2009)
  and course_id not in (
    select course_id
    from course
    where semester = 'Spring' and year = 2010
  );
--8
select distinct name
from student
where name in (
    select name
    from instructor
    where instructor.name = student.name
  );
--9