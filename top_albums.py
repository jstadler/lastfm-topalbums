import urllib
import xml.etree.ElementTree as ET
import re

# enter a user
user=''

# enter an apikey
apikey=''

data = urllib.urlopen('http://ws.audioscrobbler.com/2.0/?method=user.gettopalbums&limit=102&user=' + user + '&api_key=' + apikey)
tree = ET.parse(data)
root = tree.getroot()

album_page_links = []

for i in root:
    for j in i:
        #print j.attrib
        album_page_links.append( j[3].text )

count = 1
for j in album_page_links:
    d2 = urllib.urlopen( j ).readlines()
    print "count: " + str(count)

    for i in d2:
        if i.find('\"album-cover\"') != -1:
            m = re.search('http[^"]*', i )
            print m.group(0)
            urllib.urlretrieve(m.group(0), str(count) + ".png")
    count = count + 1
    
        
