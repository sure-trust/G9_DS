#  Oracle SQL Sessions : Assignment 1
Submitted by : Tafseer Kousar

1. select count(*) from emp;
2. select count(*) from dept;
3. select*from emp;
4. select*from dept;
5. select sum(sal) from emp;
6. select sum(comm) from emp;
7. select distinct job from emp where comm is not null;
8. select sysdate from dual;
9. select avg(sal) from emp;
10. select deptno, count(*) from emp group by deptno;
11. select deptno, sum(sal) from emp group by deptno;
12. select job, count(*) from emp group by job;
13. select job, avg(sal) from emp group by job;
14. select ename, to_char(hiredate,'DD'),to_char(hiredate,'MM'),to_char(hiredate,'YYYY') from emp;
15. select empno, ename,deptno from emp order by deptno;
16. select empno, ename,job from emp order by job;
17. select empno, ename,sal from emp order by sal desc;
18. select empno,ename, deptno,sal from emp order by deptno asc, sal desc;
19. select count(*) from emp where length(ename)=6;
20. select max(sal) , min(sal) from emp;
21. select deptno, max(sal), min(sal) ,avg(sal),sum(sal) from emp group by deptno;
22. select empno, ename, hiredate from emp order by hiredate;
23. select empno,ename, hiredate from emp order by hiredate desc fetch first 1 row only;
24. select empno,ename, hiredate from emp order by hiredate fetch first 1 row only;
25. select empno, ename,hiredate,deptno from emp order by to_char(hiredate,'yyyy')desc, deptno asc;
26. select empno, ename, sal from emp where sal>=(select avg(sal) from emp);
27. select empno, ename, sal from emp where sal<=(select avg(sal) from emp);
28. select empno, ename, sal from emp where sal between 2000 and 4000;
29. select empno,ename,sal from emp where sal = (select max(sal) from emp) or sal = (select min(sal) from emp);
30.select count(*) from emp where to_char(hiredate,'MM') = to_char(add_months(sysdate,1),'MM');
