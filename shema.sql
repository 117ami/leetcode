
-- Create table Submissions (sub_id int, parent_id int); 
-- Truncate table Submissions
insert into Submissions (sub_id, parent_id) values ('1', Null), 
('2', Null),
('1', Null),
('12', Null),
('3', '1'),
('5', '2'),
('3', '1'),
('4', '1'),
('9', '1'),
('10', '2'),
('6', '7'); 
