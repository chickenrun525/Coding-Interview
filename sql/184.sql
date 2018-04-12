# Write your MySQL query statement below
select e1.Name as Employee, e1.Salary as Salary, d.Name as Department
from Employee e1 join Department d on e1.DepartmentId = d.Id 
where Salary in
(select max(Salary) from Employee e2 where e1.DepartmentId = e2.DepartmentId)