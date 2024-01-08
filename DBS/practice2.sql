use main;

create table default01(
    Name varchar(10),
    Id numeric(3),
    Address varchar(20),
    Age varchar(3)
);

insert into default01 values('Arhaan',170,'Noida',20);
insert into default01 values('Arhaann',171,'Delhi',21);
insert into default01 values('Arhaannn',172,'Ghaziabad',22);
insert into default01 values('Arhaannnn',173,'Gurgaon',23);

select * from default01;

drop table default01;