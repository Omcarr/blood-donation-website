create database blooddonor;
use blooddonor;
create table donors(
	user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    blood_group VARCHAR(5),
    last_donation_date DATE,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(15)
    );
select * from donors;
alter table donors
add reg_date date;
select * from donors;