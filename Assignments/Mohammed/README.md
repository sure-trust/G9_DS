--NAME: SHAIK MOHAMMED SAMEER ALI

1. total number of employees
A. SELECT count(empno) FROM emp;

2. total number of departments
A. SELECT count(deptno) FROM dept;

3. all the employees
A. SELECT ename FROM emp;

4. all the departments
a.  SELECT dname FROM dept;

5. total salary paid for all employees.
A. SELECT sum(sal) FROM emp;

6. total commission paid to all employees.
A. SELECT sum(comm) FROM emp;

7. Which job titles of the employees get commission paid.
A. SELECT distinct job FROM emp
   WHERE comm is not null

8. System date
A. SELECT sysdate FROM dual;

9. Average salary paid to all employees.
A. SELECT avg(saFROM emp;

10. How many employees are there in each department?
A.  SELECT deptno, COUNT(empno) AS employee_count 
    FROM Emp
    GROUP BY deptno; 

11. Total salary of the employees in each department
A.  SELECT deptno, sum(sal) AS Total_sal  
    FROM Emp
    GROUP BY deptno; 

12. How many employees are there under each job title?
A.  SELECT job, count(job) AS groupof
    FROM Emp
    GROUP BY job; 

13. Average salary paid for each job title.
A.  SELECT job, avg(sal) AS avgof 
    FROM Emp
    GROUP BY job;

14. hire day, month, and year for each employee.
A.  select ename, hiredate 
    from emp

15. Sort the employee department wise.
A.  select * from emp
    order by deptno;

16. Sort the employee based on their job titles.
A.  SELECT empno, ename, job
    FROM Emp
    ORDER BY job;

17. Sort the employee based on descending order of their salaries.
A.  SELECT empno, ename, job, sal
    FROM Emp
    ORDER BY sal desc;

18. Sort the employee ascending order of their department and descending order of their salary.
A.  SELECT empno, ename, deptno, sal
    FROM Emp
    ORDER BY deptno asc , sal desc;

19. How many employees have their name with 6 characters.
A.  SELECT COUNT(*) AS employee_count
    FROM Emp
    WHERE LENGTH(Ename) = 6;

20. Maximum and minimum salary paid.
A.  SELECT MAX(sal) FROM emp;
    SELECT MIN(sal) FROM emp;

21. Maximum, minimum, average and sum of salary paid under each department.
A.  SELECT
    deptno,
    MAX(sal) AS max_sal,
    MIN(sal) AS min_sal,
    AVG(sal) AS avg_sal,
    SUM(sal) AS total_sal
    FROM Emp
    GROUP BY deptno;
    
22. Sort the employee based on their hire date.
A.  SELECT empno, ename, hiredate
    FROM Emp
    ORDER BY hiredate;

23. Employee who joined latest
A.  SELECT empno, ename, hiredate
    FROM Emp
    ORDER BY hiredate desc;

24. Who is the oldest employee in the organization based on their hire date?
A.  SELECT empno, ename, to_char(hiredate,'yyyy')
    FROM Emp
    WHERE  to_char(hiredate,'yyyy') <= 1980
    ORDER BY 1;
    --or if we dont know year
    SELECT empno, ename, to_char(hiredate, 'yyyy') AS hire_year
    FROM Emp
    ORDER BY hiredate ASC
    FETCH FIRST 1 ROW ONLY;

25. Sort the employee based on their hire year (descending) and department (ascending)
A.  SELECT empno, ename, deptno, hiredate
    FROM Emp
    ORDER BY  deptno asc , hiredate desc;

26. Employees who get salaries greater than or equal to the average salary of employees.
A.  SELECT empno, ename, sal
    FROM Emp
    WHERE sal >= (SELECT AVG(sal) FROM Emp);

27. Employees who get salary less than or equal to average salary of employees.
A.  SELECT empno, ename, sal
    FROM Emp
    WHERE sal <= (SELECT AVG(sal) FROM Emp);

28. Employees get salaries between 2000 and 4000.
A.  SELECT empno, ename, job, sal, deptno
    FROM emp
    WHERE sal between 2000 and 4000;

29. Which employees get the highest and lowest salary?
A.  -- Highest Salary
    SELECT empno, ename, sal, job
    FROM Emp
    ORDER BY sal DESC
    FETCH FIRST 1 ROW ONLY;
    -- Lowest Salary
    SELECT empno, ename, sal, job
    FROM Emp
    ORDER BY sal ASC
    FETCH FIRST 1 ROW ONLY;

30. We need to celebrate the joining month of the employees. We plan to buy a gift for each of them. How many gifts I need to buy for next month?
 A. SELECT empno, ename, hiredate
    FROM Emp
    WHERE EXTRACT(MONTH FROM hiredate) = 2;
