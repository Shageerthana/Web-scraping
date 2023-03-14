#create the urls
urls = [
     'https://casino.betfair.com/'#ok
    'https://www.spreadex.com/sports/en-GB/spread-betting', #ok
    'https://www.livescorebet.com/uk/casino/', #ok
    ]

#open a text file for writing 
with open ('gamblingUrls.txt','w') as f:
    #write down each Url on a new line
    for url in urls:
        f.write(url + '\n')