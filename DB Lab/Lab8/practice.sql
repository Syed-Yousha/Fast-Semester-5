--Practice PL/sql
set serveroutput on

Declare 
    sec_name varchar2(20) := 'Sec-A';
    course_name varchar2(20) := 'Database system lab';
Begin
    dbms_output.put_line('This is: '|| sec_name || 'and the course is '
    ||course_name);
END;


set serveroutput on

-- integer practice
declare
    a integer := 20;
    b integer := a**2;
    c integer;
begin
    
    c := a *b + a;
    dbms_output.put_line('output of c is: '||c);
end;
    
    
-- global vars

set serveroutput on

declare
    out1 number := 100;
    out2 number := 200;

begin
    dbms_output.put_line('global var1: '|| out1);
    dbms_output.put_line('global var2: '|| out2);
    
    -- nested inner
    declare
    num1 integer := 20;
    num2 integer := 30;
    
    begin
        dbms_output.put_line('inner var1: '|| num1);
        dbms_output.put_line('inner var2: '|| num2);
    end;
end; 


-- connect tables
set serveroutput on

declare 
    e_id employees.employee_id%type;
    e_name employees.first_name%type;
    d_name departments.department_name%type;
    
begin
    select e.employee_id, e.first_name, d.department_name
    into e_id, e_name, d_name
    from employees e
    join departments d on (e.department_id = d.department_id)
    where employee_id = 100;
    
    dbms_output.put_line('Employee Id: '|| e_id);
    dbms_output.put_line('Employee name: '|| e_name);
    dbms_output.put_line('Deparment name: '|| d_name);
end; 

    
    
--views
create or replace view x  as
select * from employees
with read only;
select * from x;
update x set salary  = 50000 where employee_id = 100;


--materialized view
CREATE MATERIALIZED VIEW MAT_EMP_Det
AS
 SELECT DISTINCT EMPLOYEES.EMPLOYEE_ID, EMPLOYEES.FIRST_NAME, 
EMPLOYEES.EMAIL,DEPARTMENTS.DEPARTMENT_NAME FROM EMPLOYEES INNER JOIN DEPARTMENTS
 ON EMPLOYEES.EMPLOYEE_ID = DEPARTMENTS.DEPARTMENT_ID
 WHERE EMPLOYEES.DEPARTMENT_ID = 80;
 
 
GRANT CREATE MATERIALIZED VIEW TO hr;
GRANT SELECT ON EMPLOYEES TO hr;
GRANT SELECT ON DEPARTMENTS TO hr;


--Function
create or replace function calculateSal(d_id in number)
return number
is 
t_sal number;

begin
    select sum(salary) into t_sal from employees where department_id = d_id;
    return(t_sal);
End;



select calculateSal(80) from dual;


--Procedure : have no return values