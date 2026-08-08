USE student_management;

INSERT INTO users (Username, Password, Role) VALUES
('admin', 'admin123', 'Admin'),
('teacher1', 'teacher123', 'Teacher'),
('student1', 'student123', 'Student');

INSERT INTO departments (DepartmentName) VALUES
('Computer Science'),
('Information Science'),
('Electronics');

INSERT INTO classes (ClassName, DepartmentID) VALUES
('CSE-A', 1),
('ISE-A', 2),
('ECE-A', 3);

INSERT INTO students (StudentName, Age, Gender, Email, Phone, Address, DepartmentID, ClassID, AdmissionDate) VALUES
('Rahul Sharma', 20, 'Male', 'rahul@example.com', '9000000001', 'Bangalore', 1, 1, '2025-08-01'),
('Anita Rao', 21, 'Female', 'anita@example.com', '9000000002', 'Mysore', 2, 2, '2025-08-01'),
('Priya Kumar', 20, 'Female', 'priya@example.com', '9000000003', 'Mangalore', 3, 3, '2025-08-01');

INSERT INTO teachers (TeacherName, Email, Phone, DepartmentID) VALUES
('Dr. Arun Kumar', 'arun@example.com', '9000000011', 1),
('Dr. Meena Rao', 'meena@example.com', '9000000012', 2),
('Dr. Ravi Kumar', 'ravi@example.com', '9000000013', 3);

INSERT INTO attendance (StudentID, AttendanceDate, Status) VALUES
(1, '2026-08-01', 'Present'),
(1, '2026-08-02', 'Present'),
(1, '2026-08-03', 'Absent'),
(2, '2026-08-01', 'Present'),
(2, '2026-08-02', 'Present'),
(3, '2026-08-01', 'Absent');

INSERT INTO marks (StudentID, Subject, Marks, Semester) VALUES
(1, 'Database Management Systems', 85, 6),
(1, 'Operating Systems', 78, 6),
(1, 'Computer Networks', 92, 6),
(2, 'Database Management Systems', 88, 6),
(2, 'Operating Systems', 81, 6),
(3, 'Database Management Systems', 76, 6),
(3, 'Operating Systems', 84, 6);