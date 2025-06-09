--task1
select department_name from departments 
where MANAGER_ID is NULL;
    
--task2
select d.department_name, count(e.EMPLOYEE_ID)
from departments d 
join EMPLOYEES e on (d.department_id = e.department_id)
group by d.DEPARTMENT_name
having count(e.employee_id) > 5;


--task3
select e.first_name, e.last_name, e.hire_date, m.hire_date as manager_hire_date
from employees e
join employees m on (e.manager_id = m.employee_id)
where e.hire_date > m.hire_date;

--task4
select j.job_title, e.first_name 
from employees e
join jobs j on (e.job_id = j.job_id)
where salary in (select max_salary from jobs);


--task5
select d.department_name 
from departments d
join employees e on (d.department_id = e.department_id)
where (e.hire_date) <= add_months(sysdate, -36)
group by d.DEPARTMENT_NAME;  


--task6
select e.first_name, e.last_name, d.department_name, m.first_name as m_first_name, m.last_name as m_last_name
from employees e
join departments d on (e.manager_id = d.manager_id)
join employees m on (e.manager_id = m.employee_id)
order by e.MANAGER_ID;


--Task7
select j.job_title
from jobs j
left join employees e on (j.job_id = e.job_id)
where e.employee_id is NULL;

--Task 8
select department_name, avg_salary
from (
    select d.department_name, avg(e.salary) as avg_salary
    from departments d
    join employees e on (d.department_id = e.department_id)
    group by department_name
    order by avg(e.salary)
)
where rownum = 1;

--Task9
select e.first_name, e.salary
from employees e
join(
select department_id, avg(salary) as avg_salary
from employees
group by department_id
) m on (e.department_id = m.department_id)
where e.salary > m.avg_salary;


--Task10
select e.first_name, e.last_name, e.employee_id
from employees e 
where e.employee_id in (select manager_id from employees);

--Task11
select d.department_id, d.department_name
from departments d
left join employees e on (d.department_id = e.department_id)
where e.employee_id is null;

--Task12
select e.first_name, e.salary, d.department_name
from departments d
left join employees e on (d.department_id = e.department_id);

--Task13
select e.first_name, e.last_name, e.job_id, d.department_name, l.street_address, l.city
from employees e
join departments d on e.department_id = d.department_id
join locations l on d.location_id = l.location_id
where l.state_province is null;

--Task14:
select e.employee_id, e.first_name, e.last_name
from employees e
left join departments d on e.department_id = d.department_id
where d.department_id is null;


--Task15
select e.first_name, e.last_name from employees e
join departments d on (e.department_id = d.department_id)
join locations l on (d.location_id = l.location_id)
join countries c on (l.country_id = c.country_id)
where c.country_name = 'US' and l.state_province != 'Washington';



