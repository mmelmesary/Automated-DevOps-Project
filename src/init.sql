CREATE USER 'admin'@'%' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON elmesary.* TO 'admin'@'%';
FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS elmesary;
USE elmesary;
CREATE TABLE user_info (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(45) NOT NULL,
  age INT NULL,
  job_title VARCHAR(200) NULL,
PRIMARY KEY (`id`));

INSERT INTO user_info(name, age, job_title) VALUES('muhammad', 23, 'DevOps_engineer');
INSERT INTO user_info(name, age, job_title) VALUES('mourad', 24, 'ML_engineer');
INSERT INTO user_info(name, age, job_title) VALUES('yusuf', 32, 'doctor');
commit;

SELECT * FROM user_info;