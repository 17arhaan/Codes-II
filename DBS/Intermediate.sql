use UNIVERSITY;

TABLE_NAME
--------------------------------------------------------------------------------
CLASSROOM
DEPTT
COURSE
INSTRUCTOR
SECTION
TEACHES
STUDENT
TAKES
ADVISOR
TIME_SLOT
PREREQ
--------------------------------------------------------------------------------
--1
select course_id from takes where semester = 'Fall' and year = 2009
UNION
select course_id from takes where semester = 'Spring' and year = 2010;
--2
select course_id from takes where semester = 'fall' and year = 2009
INTERSECT
select course_id from takes where semester = 'spring' and year = 2010;
--3
select course_id from takes where semester = 'Fall' and year = 2009
MINUS
select course_id from takes where semester = 'Summer' and year = 2010;
--4
select title
from course natural left outer join takes
where takes.id is null;
--5
select distinct course_id
from takes
where semester = 'Fall' and year = 2009
  and course_id in (
    select course_id
    from takes
    where semester = 'Spring' and year = 2010
  );
--6
select DISTINCT count(s_ID)
from advisor
where s_ID in (
    select s_ID
    from advisor
    where i_ID = 10101
  );
--7
select distinct course_id
from takes
where (semester = 'Fall' and year = 2009)
  and course_id not in (
    select course_id
    from takes
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


