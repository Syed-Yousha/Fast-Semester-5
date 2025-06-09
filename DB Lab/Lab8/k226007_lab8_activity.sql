-- Task1 a
set serveroutput on
  accept e_id number prompt 'enter employee id: ';
declare
     bonus integer := 0;
     e_sal  employees.SALARY%type;
begin
    SELECT salary INTO e_sal FROM employees WHERE EMPLOYEE_ID = &e_id;
    if(e_sal<1000 ) then
        bonus := e_sal*0.1;
    elsif (e_sal<1500 and e_sal>1000) then
        bonus := e_sal*0.15;
    elsif (e_sal>1500) then
        bonus := e_sal*0.20;
    elsif (e_sal=null) then
        bonus := 0;
    End if;
    dbms_output.put_line ('Bonus is: Rs'||bonus);
End;



select * from employees;

--task2
set serveroutput on
    accept e_id number prompt 'enter employee id: ';
declare
    e_com employees.commission_pct%type;
    e_sal employees.salary%type;
begin
    select commission_pct, salary 
    into e_com, e_sal 
    from employees 
    where employee_id = &e_id;
    
    if e_com is not NULL then
        e_sal := e_sal + (e_sal*e_com);
        
        update employees 
        set salary = e_sal 
        where employee_id = &e_id;
        
        dbms_output.put_line('Salary updated successfully.');
        
    else 
        dbms_output.put_line('employee is null');
    end if;
    
end;


--task3
declare
    e_dept_name departments.department_name%type;
begin
    select department_name 
    into e_dept_name 
    from departments 
    where department_id = 30;
    
    dbms_output.put_line('department name: ' || e_dept_name);
end;

--task4
set serveroutput on
declare
    e_job_title employees.job_title%type;
begin
    select job_title 
    into e_job_title 
    from employees 
    where deptno = 20;
    
    dbms_output.put_line('job title: ' || e_job_title);
end;


--task5
set serveroutput on
declare
    e_salary employees.salary%type;
begin
    select salary 
    into e_salary 
    from employees 
    where DEPARTMENT_ID = 20;
    
    dbms_output.put_line('salary: ' || e_salary);
end;





        