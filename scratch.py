from bs4 import BeautifulSoup
import requests 
import re
import csv

with open('gamblingUrls.txt','r')as f:
    urls = f.readlines()

# Creating an empty list to store the keyword match results
results = []

#iterating over the urls
for url in urls:
    # Send a GET request to the website 
    resp = requests.get(url, allow_redirects=True)
    soup = BeautifulSoup(resp.content, 'html.parser')
    text = (soup.get_text()) 
    #status code of the response to see whether its successful
    if resp.status_code == 200:
      # Extract the text from the response
        text = resp.text
        # Iterate through the keywords
        for keyword in keywords:
        # Check if the keyword is in the text
          if re.search(keyword, text):
            # If it is, add a tuple of the keyword and the URL to the results list
            results.append((keyword, url))
        # Append the text to the list
        urls.append(text)
    else:
        print("Error retrieving website content. Status code:", resp.status_code)
 
#list of words to search for
keywords = ["Online Casino", "Slots & Table Games", "LiveScore Bet UK", "Sports Spread Betting",
            "Casino", "Live Casino", "poker", "Bingo", "Please Gamble responsibly", "Safer Gambling"]

filename = "keywords.csv"

with open(filename, 'w', newline='') as csvfile:
    # creating a csv 
    writer = csv.writer(csvfile)
    # writing the column headers
    writer.writerow(['Keywords', 'Matched URL'])
    # writing the data rows
    for result in results:
        writer.writerow(result)