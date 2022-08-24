#File management config
f = open('list.txt', 'rt')  # File open
filmlist = [line.strip() for line in f]

formatedlist = []  # Getting actual names without numeration
for i in filmlist:
    i = i.split('.')
    formatedlist.append(i[1])

# Postgresql config
host='localhost'
user='postgres'
password='admin'
dbname='filmlist'

# Parser config
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

s_url = 'https://rezka.ag/search/?do=search&subaction=search&q='