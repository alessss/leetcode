#https://leetcode.com/problems/employees-earning-more-than-their-managers/description/
select
e2.name as Employee
from employee as e1
inner join employee as e2
on e2.managerid = e1.id
where e1.salary < e2.salary