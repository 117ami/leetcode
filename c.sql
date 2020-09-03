
-- select user_id
--     , distance
--     , sum(distance) over (partition by user_id) as total
--     , row_number() over(partition by user_id) as rownum
--     , rank() over (order by user_id) as c_rank
--     , dense_rank() over (order by user_id) as d_rank
--     , ntile(6) over (ORDER by user_id) as ntilee 
-- from rides;

select
    employee_id
    , employee_name 
    , salary 
    , lead(salary, 1, 0) over (order by employee_id) as lead_salary
    , first_value(salary) over (partition by employee_id order by employee_id) as fsal
    
    -- , percent_rank() over (order by employee_name) as prnk
    -- , cume_dist() over (partition by employee_id order by employee_name) as prnk
    
    -- , lead(salary, 1, 0) over (order by employee_id) - salary as salary_diff
    -- , sum(salary) over (partition by employee_id) as total_salary
    -- , sum(salary) over (order by employee_id rows 1 preceding) as `running total`
    -- , avg(salary) over (order by employee_id rows 1 preceding) as `running avg`
    -- , row_number() over (partition by employee_id order by employee_id) as row_num
    -- , rank() over (partition by employee_id order by employee_name) as row_rank
    -- , rank() over (order by employee_id) as rnk
    -- , dense_rank() over (order by employee_id) as drnk 
    -- , ntile(4) over(partition by employee_id) as t_ntile
from salaries

    
