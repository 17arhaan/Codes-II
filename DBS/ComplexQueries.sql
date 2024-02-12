select course_id , count(ID) as num_students
from takes
group by course_id;

select count(course_ID) as num_student , dept_name
from (takes natural join course)
group by dept_name
having count(ID) > 10;

select distinct count(course_id) as num_courses , dept_name
from (takes natural join course)
group by dept_name;

select avg(salary) as sal , dept_name
from instructor
group by dept_name
having avg(salary) > 42000;

select * from course;



select distinct c1.course_id as course_ids
from course c1, prereq p1
where c1.course_id = p1.prereq_id
group by c1.course_id
order by course_ids asc;

select salary , name as instuc_name
from instructor
order by salary ASC;


select * from instructor;
select * from department;

use university;
with Max_budget as (
    select max(budget) as max_budget 
    from department )
select dept_name , budget
from department
where budget = (select max_budget from Max_budget);