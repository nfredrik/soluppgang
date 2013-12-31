from BeautifulSoup import BeautifulSoup
import urllib2
import datetime
import json
import os

JSONFILE = 'data.json'

def load_json(file):
    data = []
    if not os.path.exists(file):
        return data
    
    with open(file, 'rb') as fp:
        data = json.load(fp)
    return data


def save_json(file, data):
    with open(file, 'wb') as fp:    
        json.dump(data, fp)


page=urllib2.urlopen('http://www.nordpoolspot.com/Market-data1/Elspot/Area-Prices/ALL1/Hourly/')
soup = BeautifulSoup(page.read())
mhw_sek=soup.findAll('td',{'align':'right'})

print "Captured from www.nordpoolspot.com"
#print "Spot price:", mhw_sek[1].renderContents(), "SEK/MWh"
cntr = 0
hours24 = []
for i in mhw_sek:
    #print cntr, ":", i.renderContents()
    if cntr % 10 == 0 and len(hours24) < 24:
        hours24.append(i.renderContents())
    cntr+=1 

print 'Selected SYS column:' 
cntr = 0   
for h in hours24:
    print 'hour',cntr, ':',  h
    cntr+= 1    
    
print 'max:', max(hours24)  
print 'min:', min(hours24) 
print 'mean:%.2f'% (sum([float(x.replace(',','.')) for x in hours24]) / float(len(hours24)))  

# Last updated:
#<span id="ctl00_FullRegion_npsGridView_lblDataUpdated" style="font-size:11px;">Last update: 30-12-2013 12:41 CET</span>

updated=soup.findAll('span')

print updated