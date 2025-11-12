-- create user and should not failif user exists
CREATE USER IF NOT EXISTS 'USER_0D_1'@'localhost' IDENTIFIED BY 'password_0d_1';
GRANT ALL PRIVILEGES ON *.* TO 'USER_0D_1'@'localhost';