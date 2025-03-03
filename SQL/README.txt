First you need to add a connection:
1. Open the SQL folder
2. Open the DBTools extension
3. Click on the "Add Connection" button
4. Fill in the connection details:
    - Connection Name: The name of the Leetcode challenge
    - Host: localhost
    - Port: 3306
    - User: *******
    - Password: ********
    - Database: temporary type 'mysql', after the connection is created, change it to the name of the Leetcode challenge
5. Click on the "Test Connection" button to make sure the connection is working
6. Click on the "Connect Now" button to connect to the database
8. Go back to DBTools and create a new SQL file
10. Create the database:
    - 'CREATE DATABASE leetcode;'
    - 'USE leetcode;'
11. Create the table:
    - 'CREATE TABLE table_name (column_name column_type);'
12. Insert the data:
    - 'INSERT INTO table_name (column_name) VALUES (value);'
13. Write your query
14. Press CTRL+SHIFT+E to run the query