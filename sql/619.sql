# Write your MySQL query statement below
select max(t.num) as num
from (select num from number group by num having count(*)=1) t
