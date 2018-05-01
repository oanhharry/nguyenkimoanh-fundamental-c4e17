
from urllib.request import urlopen
url = "http://dantri.com.vn"

#1 open connection
conn = urlopen(url)

#1.2 read data
raw_data = conn.read()

#1.3 decode
text = raw_data.decode('utf8')

# print(text)

dan_tri_file = open("dantri.html","w")

dan_tri_file.write(text)

dan_tri_file.close()
