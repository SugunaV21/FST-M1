REM   Script: ACTIVITY8
REM   Activity8-Aggregate functions

create table emp(empid int,ename varchar2(30),deptid int);

create table dept(deptid int,deptname varchar2(20));

insert all 
into emp values(1,'ram',10) 
into emp values(1,'r',20) 
into emp values(1,'lohitha',10) 
into emp values(1,'k',20) 
select 1 from dual;

insert all 
into dept values(10,'sales') 
into dept values(20,'finance') 
select 1 from dual;

select deptid,count(empid) from emp group by deptid;

select deptid,count(empid) from emp group by deptid order by deptid desc;

alter table emp add sal int;

alter table emp modify empid to 2 where ename='r';

update table emp set empid=2 where ename='r';

update table emp set sal=10000 where ename='ram';

select * from emp;

update emp set sal=10000 where ename='ram';

update emp set empid=2 where ename='r';

update emp set empid=3 where ename='lohitha';

update emp set empid=4 where ename='k';

select * from emp ;

update emp set sal=20000 where ename='r';

select deptid,count(deptid)from emp group by deptid having max(sal)>5000;

create table orders( 
    order_no int primary key, purchase_amount float, order_date date, 
    customer_id int, salesman_id int);

INSERT ALL 
    INTO orders VALUES(70001, 150.5, TO_DATE('2012/10/05', 'YYYY/MM/DD'), 3005, 5002)  
    INTO orders VALUES(70009, 270.65, TO_DATE('2012/09/10', 'YYYY/MM/DD'), 3001, 5005) 
    INTO orders VALUES(70002, 65.26, TO_DATE('2012/10/05', 'YYYY/MM/DD'), 3002, 5001) 
    INTO orders VALUES(70004, 110.5, TO_DATE('2012/08/17', 'YYYY/MM/DD'), 3009, 5003) 
    INTO orders VALUES(70007, 948.5, TO_DATE('2012/09/10', 'YYYY/MM/DD'), 3005, 5002) 
    INTO orders VALUES(70005, 2400.6, TO_DATE('2012/07/27', 'YYYY/MM/DD'), 3007, 5001) 
    INTO orders VALUES(70008, 5760, TO_DATE('2012/08/15', 'YYYY/MM/DD'), 3002, 5001) 
    INTO orders VALUES(70010, 1983.43, TO_DATE('2012/10/10', 'YYYY/MM/DD'), 3004, 5006) 
    INTO orders VALUES(70003, 2480.4, TO_DATE('2012/10/10', 'YYYY/MM/DD'), 3009, 5003) 
    INTO orders VALUES(70012, 250.45, TO_DATE('2012/06/27', 'YYYY/MM/DD'), 3008, 5002) 
    INTO orders VALUES(70011, 75.29, TO_DATE('2012/08/17', 'YYYY/MM/DD'), 3003, 5007) 
    INTO orders VALUES(70013, 3045.6, TO_DATE('2012/04/25', 'YYYY/MM/DD'), 3002, 5001) 
SELECT 1 FROM DUAL;

SELECT customer_id, MAX(purchase_amount) AS "Max Amount" FROM orders GROUP BY customer_id;

SELECT salesman_id, order_date, MAX(purchase_amount) AS "Max Amount" FROM orders  
WHERE order_date=To_DATE('2012/08/17', 'YYYY/MM/DD') GROUP BY salesman_id, order_date;

SELECT customer_id, order_date, MAX(purchase_amount) AS "Max Amount" FROM orders 
GROUP BY customer_id, order_date 
HAVING MAX(purchase_amount) IN(2030, 3450, 5760, 6000);

