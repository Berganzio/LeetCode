-- create customers table
create table
    if not exists customers (id int primary key, name varchar(255));

-- insert data into table columns
insert into
    customers (id, name)
values
    (1, 'Joe');

insert into
    customers (id, name)
values
    (2, 'Henry');

insert into
    customers (id, name)
values
    (3, 'Sam');

insert into
    customers (id, name)
values
    (4, 'Max');

-- create orders table
create table
    if not exists orders (id int primary key, customerid integer);

-- insert data into orders columns
insert into
    orders (id, customerid)
values
    (1, 3);

insert into
    orders (id, customerid)
values
    (2, 1);

-- query for finding all customers who never order anything, table in any order
select
    c.name as customers
from
    customers c
    left join orders o on c.id = o.customerid
where
    o.customerid is null;