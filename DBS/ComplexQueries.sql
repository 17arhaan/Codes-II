use university;

-- select course_id , count(ID) as num_students
-- from takes
-- group by course_id;

-- select count(course_ID) as num_student , dept_name
-- from (takes natural join course)
-- group by dept_name
-- having count(ID) > 10;

-- select distinct count(course_id) as num_courses , dept_name
-- from (takes natural join course)
-- group by dept_name;

-- select avg(salary) as sal , dept_name
-- from instructor
-- group by dept_name
-- having avg(salary) > 42000;

select * from course;
