-- alter encoding of name to utf8
ALTER DATABASE hbtn_0c_0
ALTER TABLE second_table
MODIFY name VARCHAR(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;