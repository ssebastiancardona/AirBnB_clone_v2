-- test script that prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- GRANT type_of_permission ON database_name.table_name TO 'username'@'localhost';
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_dev_pwd';
-- CONNECT THE pasword;
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;