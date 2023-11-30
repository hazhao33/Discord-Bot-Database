-- Script name: inserts.sql
-- Author:      Hann Zhao
-- Purpose:     insert sample data to test the integrity of this database system
   
-- the database used to insert the data into.
Use EducationDB;

-- Institution Inserts 
INSERT INTO Institution (institution_id, institution_name, description) VALUES 
(1, 'San Francisco State University', null),
(2, 'San José State University',  null),
(3, 'City College of San Francisco',  null);
-- Role Inserts 
INSERT INTO Role (role_id, role_name, description) VALUES 
(1, 'Admin', 'Administrator role with full access'),
(2, 'Staff', 'Role for staff members'),
(3, 'Student', 'Role for students');
-- Sport_Team Inserts 
INSERT INTO Sport_Team (team_id, team_name, description) VALUES 
(1, 'Lakers', 'Lake show'),
(2, 'GS Warriors', 'Strength in Numbers'),
(3, 'Team 3', 'All way here');
-- Club Inserts 
INSERT INTO Club (club_id, club_name, description) VALUES 
(1, 'Chess Club', 'Chess for fun'),
(2, 'Photography Club', null),
(3, 'Debate Club', null);
-- Administrator Inserts 
INSERT INTO Administrator (administrator_id, register_by, name, dob) VALUES 
(1,null, 'John Doe', '1990-05-15'),
(2,1, 'Emma Smith', '1988-11-25'),
(3,1, 'Mark Johnson', '1985-09-10');
-- Student Inserts 
INSERT INTO Student (student_id,name,dob) VALUES 
(1, 'Alice Brown', '2000-02-20'),
(2, 'Bob Wilson', '2001-07-12'),
(3, 'Carol Davis', '1999-09-05');
-- Staff Inserts 
INSERT INTO Staff (staff_id,name,dob) VALUES 
(1, 'James Johnson', '1980-12-01'),
(2, 'Emily Parker', '1992-03-18'),
(3, 'Michael Thompson', '1975-06-30');
-- Semester Inserts 
INSERT INTO Semester (semester_id, institution, year, type) VALUES 
(1, 1, 2022, 'Fall'),
(2, 1, 2023, 'Spring'),
(3, 2, 2023, 'Spring');
-- Class Inserts 
INSERT INTO Class (class_id, class_name, seat_limit, price) VALUES 
(1, 'Introduction to Programming', 30, 250.00),
(2, 'Database Intro', 25, 300.00),
(3, 'Web Development', 35, 200.00);
-- Major Inserts 
INSERT INTO Major (major_id, major_name, sudent_count) VALUES 
(1, 'Computer Science', 100),
(2, 'Business Administration', 80),
(3, 'Psychology', 70);
-- Department Inserts 
INSERT INTO Department (department_id, title, staff_num) VALUES 
(1, 'Computer Science Department', 10),
(2, 'Business Department', 8),
(3, 'Psychology Department', 6);
-- Event Inserts 
INSERT INTO Event (event_id, title, location, description) VALUES 
(1, 'Conference', 'A Center', null),
(2, 'Workshop', 'B Center', 'Hands on workshop'),
(3, 'group study', 'online', null);
-- Book Inserts 
INSERT INTO Book (book_id, ISBM, name, author) VALUES 
(1,12345,'Book Z', 'Jhon'),
(2,23456, 'Book of B', 'Cook'),
(3,34567, 'A Book', 'Apple');
-- Subject Inserts 
INSERT INTO Subject (subject_id, title, description) VALUES 
(1, 'Mathematics', null),
(2, 'Business', 'Business history'),
(3, 'Computer Science', 'Principles of programming');
-- Account Inserts 
INSERT INTO Account (account_id, name, email,phone_num) VALUES 
(1, 'James Johnson', 'James@gmail.com', '123-456-7890'),
(2, 'Emma Smith', 'emma@gmail.com', '987-654-3210'),
(3, 'Alice Brown', 'mark@gmail.com', '555-123-4567');
-- User Inserts 
INSERT INTO User (user_id, account, administrator, student, staff) VALUES 
(1, 1, true, false, false),
(2, 2, false, true, false),
(3, 3, false, false, true);
-- Profile Inserts 
INSERT INTO Profile (profile_id, account, dob) VALUES 
(1, 1, '2000-02-20'),
(2, 3, '2001-07-12'),
(3, 2, '1999-09-05');
-- Library Inserts 
INSERT INTO Library (library_id, lib_name, Location,institution,book) VALUES 
(1, 'V Library', 'Main Street', 3, 1),
(2, 'V Library', 'Main Street', 3, 2),
(3, 'C Library', '1st Street', 1, 3);
-- User_Role Inserts 
INSERT INTO User_Role (userrole_id, account, role) VALUES 
(1,2,1),
(2,1,2),
(3,3,3);
-- Bank_Account Inserts 
INSERT INTO Bank_Account (bankAcc_id, acc_num, rounting_num) VALUES 
(1, 123456789, 987654321),
(2, 987654321, 123456789),
(3, 555555555, 111111111);
-- Credit_Card Inserts 
INSERT INTO Credit_Card (creditCard_id, cc_num, cvv, exp_date, name) VALUES 
(1, 1234567812345678, 123, '12/24', 'John Doe'),
(2, 9876543298765432, 456, '06/23', 'Emma Smith'),
(3, 5555444455554444, 789, '09/25', 'Mark Johnson');
-- Payment_Method Inserts 
INSERT INTO Payment_Method (payment_method_id, bank_acc, creditCard) VALUES 
(1, 1, null),
(2, null, 2),
(3, null, null);
-- Default_Payment_Method Inserts 
INSERT INTO Default_Payment_Method (default_payment_id, payment_method, student) VALUES 
(1,2,2),
(2,3,1),
(3,1,3);
-- Institutional_Role Inserts 
INSERT INTO Institutional_Role (institutional_role_id, institution, role) VALUES 
(1, 1, 1),
(2, 1, 2),
(3, 1, 3);
-- Qualification Inserts 
INSERT INTO Qualification (qualification_id, staff, education_level, school_name, degree) VALUES 
(1,1, 'high school', 'ABC school', 'high school'),
(2,2, 'college', 'sfsu', 'AS'),
(3,3, 'college', 'sfsu', 'BS');
-- Employment_History Inserts 
INSERT INTO Employment_History (employment_history_id,  company_name, position, start_year, end_year, staff) VALUES 
(1, 'ABC Company', 'Software D', '2018', '2020', 1),
(2, 'ABC Corp', 'Marketing', '2015', '2021', 2),
(3, 'ABC Ind', 'Sales', '2019', null, 3);
-- Student_Enrollment Inserts 
INSERT INTO Student_Enrollment (student_enroll_id, student, semester) VALUES 
(1, 1, 1),
(2, 1, 2),
(3, 2, 1);
-- Academic_Record Inserts 
INSERT INTO Academic_Record (academic_record_id, student, grade_level, gpa) VALUES 
(1,1, 'Sophomore', 3.5),
(2,2, 'Junior', 3.8),
(3,3, 'Senior', 1.2);
-- Medical_History Inserts 
INSERT INTO Medical_History (medical_history__id, student, time, description) VALUES 
(1, 1, '2020', 'Allergic'),
(2, 1, '2019', 'Asthma'),
(3, 1, '2021', 'knee injury');
-- Course_Enrollment Inserts 
INSERT INTO Course_Enrollment (course_enroll_id, class, student) VALUES 
(1,1,1),
(2,2,1),
(3,3,1);
-- Major_enrollment Inserts 
INSERT INTO Major_enrollment (major_enroll_id, major, student) VALUES 
(1,1,1),
(2,2,2),
(3,3,3);
-- Division Inserts 
INSERT INTO Division (division_id, department, institution) VALUES 
(1,1,1),
(2,2,1),
(3,3,1);
-- Staff_Department Inserts 
INSERT INTO Staff_Department (sd_id, staff, department) VALUES 
(1,1,3),
(2,2,2),
(3,3,1);
-- Academic_Program Inserts 
INSERT INTO Academic_Program (program_id, institution, major, class, subject) VALUES 
(1,1,1,1,3),
(2,1,1,2,3),
(3,2,1,3,3);
-- Specific_Study Inserts 
INSERT INTO Specific_Study (s_study_id, subject, major) VALUES 
(1,1,2),
(2,2,2),
(3,3,1);
-- Member Inserts 
INSERT INTO Member (member_id, institution, staff, student, administrator) VALUES 
(1,1,1,null,null),
(2,1,null,1,null),
(3,2,null,null,1);
-- Entertainment Inserts 
INSERT INTO Entertainment (entertainment_id, institution, event, sport_team, club) VALUES 
(1,1,1,1,1),
(2,1,2,2,null),
(3,2,null,3,null);
-- Calendar Inserts 
INSERT INTO Calendar (calendar_id, semester, holiday_date, holiday_name) VALUES 
(1, 1, '2022-12-25', 'Christmas'),
(2, 1, '2023-01-01', 'New Year'),
(3, 3, '2023-07-04', 'Independence Day');
-- Subject_Type Inserts 
INSERT INTO Subject_Type (subject_type_id,  subject, department) VALUES 
(1,1,2),
(2,2,2),
(3,3,1);
-- Class_Subject Inserts 
INSERT INTO Class_Subject (class_subject_id, subject, class) VALUES 
(1,1,3),
(2,2,3),
(3,3,3);