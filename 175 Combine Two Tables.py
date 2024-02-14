#https://leetcode.com/problems/combine-two-tables/
select
firstname as firstName,
lastname as lastName,
city as city,
state as state
from Person as p
left join address as a
on p.personId=a.personId