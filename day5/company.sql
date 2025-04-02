CREATE DATABASE compnay_db;
USE company_db;


CREATE TABLE employees(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name_employee VARCHAR(100) NOT NULL
);

CREATE TABLE projects(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name_project VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL
);

CREATE TABLE employee_project (
    employee_id INT,
    project_id INT,
    PRIMARY KEY (employee_id,project_id),
    FOREIGN KEY(employee_id) REFERENCES employees(id), ON DELETE CASCADE,
    FOREIGN KEY(project_id) REFERENCES projects(id),ON DELETE CASCADE,
);