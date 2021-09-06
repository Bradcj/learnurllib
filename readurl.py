import urllib.request, urllib.parse, urllib.error


get_data = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in get_data:
    data = line.decode().strip()
    print(data)