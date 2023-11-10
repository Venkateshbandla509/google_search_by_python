#we need the googlesearch module if not exist for git
#use " pip install googlesearch-python "
#import thr search from googlesearch module
from googlesearch import search

query = input("Enter the word or sentence you need to search in google : ")

for i in search(query, num_results= 5, lang="en" , proxy=None):
    print(i)
print("My job is done")
