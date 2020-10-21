
The key obstacle of this question is finding a method to generate all `customer_id` between `min(customer_id)` and  `max(customer_id)`. I present in this post several solutions to do so. Any advice and unmentioned solution are welcome.

## Generating Numeric Sequences in MySQL

Below are solutions to generate numeric sequences from `1` to `n` without **relying on existing tables**.

### Solution 1: UNION Tables
```sql
SELECT 0 AS value UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3;
```

Primitive but simple for small number `n`. Shortage is obvious: `not extensible`

### Solution 2: Procedures
We can create a temporary table and fill it with the required numbers utilizing a pre-created stored procedure.

```sql
CREATE TEMPORARY TABLE temp (value BIGINT UNSIGNED NOT NULL PRIMARY KEY);

delimiter |
CREATE PROCEDURE incr(n BIGINT UNSIGNED)
BEGIN
  DECLARE i BIGINT UNSIGNED DEFAULT 0;
  WHILE i < n DO
    INSERT INTO temp VALUES(i);
    SET i = i + 1;
  END WHILE;
END|
delimiter ;

incr(100);
```

This method is quick but we have to call `incr` procedure before accessing the table; 


### Solution 3: `JSON_TABLE()`
More on `json_table()` can be found [here](https://dev.mysql.com/doc/refman/8.0/en/json-table-functions.html)
```sql 
SET @upper_bound = 10; 

SELECT temp.rowid - 1 AS value
  FROM JSON_TABLE(CONCAT('[{}', REPEAT(',{}', @upper_bound - 1), ']'),
                  "$[*]" COLUMNS(rowid FOR ORDINALITY)
       ) AS temp;
```

Quick but controversial, difficult to understand for users unfamiliar with `json_table`. 


### Solution 4: Recursive Common Table Expressions (CTE)
This is the **recommended** way. Simple and not to hard to understand.

```sql
WITH RECURSIVE seq AS (
    SELECT 0 AS value UNION ALL SELECT value + 1 FROM seq WHERE value < 100
    )

SELECT * FROM seq;
```

One drawback of the method is: the upper bound `n` must be smaller than 1000. But we can increase `cte_max_recursion_depth` can shift this limitation.

