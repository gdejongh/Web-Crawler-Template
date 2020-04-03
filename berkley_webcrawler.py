# Basic web crawler designed to mine data from MIT Opencourseware. This can be adapted to be used on any large repository/catalogue of data.
# This tool is intended to make the process of mining data more efficient by automating the process.
# CSV Export function added by Gabe DeJongh 4/1/2020

import requests
from bs4 import BeautifulSoup
import csv

def courses_spider():
    file = open("lectures.csv", "w", newline='')
    writer = csv.writer(file)
    writer.writerow(["title", "lecturer", "videoURL", "Semester", ])
    url = 'http://ai.berkeley.edu/lecture_videos.html'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    # All code from this point on needs to be adapted to the specific structure of the website that the user is attempting to mine data from.
    for row in soup.findAll('tr'):
        print(row)
    file.close()




courses_spider()
print("Done")
