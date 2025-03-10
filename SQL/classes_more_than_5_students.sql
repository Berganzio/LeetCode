create TABLE IF NOT EXISTS courses (
    student varchar(255),
    class varchar(255),
    primary key (student, class)
);
-- insert data into courses
INSERT into courses (student, class)
values ('A', 'Math');
INSERT into courses (student, class)
values ('B', 'English');
INSERT into courses (student, class)
values ('C', 'Math');
INSERT into courses (student, class)
values ('D', 'Biology');
INSERT into courses (student, class)
values ('E', 'Math');
INSERT into courses (student, class)
values ('F', 'Computer');
INSERT into courses (student, class)
values ('G', 'Math');
INSERT into courses (student, class)
values ('H', 'Math');
INSERT into courses (student, class)
values ('I', 'Math');
-- query to select classes with more students among all classes
SELECT class
FROM courses
GROUP BY class
HAVING COUNT(class) >= 5;