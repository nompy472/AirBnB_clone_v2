-- Creates a MySQL server with:
--   User hbnb_test with password hbnb_test_pwd in localhost.
--   Database hbnb_test_db.
--   Grants SELECT privilege for hbnb_test on performance_schema.
--   Grants all privileges for hbnb_test on hbnb_test_db.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
