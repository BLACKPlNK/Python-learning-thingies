# Import BeautifulSoup4 and urllib2 to handle scraping
import requests 
from bs4 import BeautifulSoup
import urllib2 
from collections import defaultdict

# Default dict so any elements searched for return value of 0
d = defaultdict(lambda: 0) 

# Build an opener with a custom User-agent to somewhat bypass request limiting
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'SorryImNotUsingTheAPIYet')]
requestsString = "https://reddit.com"

# Read in the html contents of the reddit page
response = opener.open(requestsString)
page = response.read()

# Loop through the first 10 pages
for i in range(1,11):

    print("Page " + str(i) + " loading")

    # Navigate to the siteTable div to access the 25 posts listed
    soup = BeautifulSoup(page, 'html.parser')
    scream = soup.find('body')
    dream = scream.find('div', {'id' : "siteTable"})
    meme = dream.find_all('div')
 
    # Get the users of the 25 posts and add to dictionary, updating total count
    # of how many posts they have in the top 10 pages
    for x in meme:
            if x.has_attr('data-author'):
                d[x['data-author']]+= 1 

    # Get the last post on the page in order to compose the url to navigate to
    # next page. If requests were blocked, quit scraping here. 
    bleam = dream.find('div', {'data-rank' : str(i * 25)})
    if bleam == None:
        print("Loading stopped at page ", + str(i) + ".")
        break
    
    # Create the url for the next page to scrape
    stringo = bleam['data-fullname']
    requestsString = "https://reddit.com/?count=" + str(i * 25) + "&after=" + stringo
    response = opener.open(requestsString)
    page = response.read()

    if i == 10: 
        print("All pages successfully loaded") 

# Make sure that all 250 posts' users were added to the dictionary 
totalSum = 0

# Sort the dictionary based on value in descending order, and print the users
# and their amount of posts that were in the top 10 pages
for (k, v) in sorted(d.items(), key=lambda x: x[1], reverse=True):
    totalSum += v 
    print(k, v)

# Print the total number of posts counted
print(totalSum)
