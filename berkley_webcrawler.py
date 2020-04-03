# Basic web crawler designed to mine data from University of Berkley Intro to AI course materials.
# This can be adapted to be used on any large repository/catalogue of data.
# This tool is intended to make the process of mining data more efficient by automating the process.


import requests
from bs4 import BeautifulSoup
import csv


def courses_spider():
    # open file to write to and init csv writer
    file = open("lectures.csv", "w", newline='')
    writer = csv.writer(file)
    writer.writerow(["label", "title", "videoURL", "lecturer", "notes"])
    # grab html from url
    url = 'http://ai.berkeley.edu/lecture_videos.html'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    # All code from this point on needs to be adapted to the specific
    # structure of the website that the user is attempting to mine data from.
    # go through all html tables on page
    tables = soup.findChildren('table')
    for mytable in tables:
        rows = mytable.findChildren('tr', attrs={'class': None})
        # go through all rows in html table
        for row in rows:
            cells = row.findChildren('td', attrs={'class': None})
            csvrow = []
            # go through the data in each row
            for cell in cells:
                csvrow.append(cell.get_text())
                # if the cell contains a link, pull it and append it
                video = cell.find('a', href=True)
                if video is not None:
                    csvrow.append(video['href'])
            if len(csvrow) == 5:
                writer.writerow(csvrow)
    file.close()


courses_spider()
print("Done...")
