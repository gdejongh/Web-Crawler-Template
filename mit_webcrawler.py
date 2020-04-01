# Basic web crawler designed to mine data from MIT Opencourseware. This can be adapted to be used on any large repository/catalogue of data.
# This tool is intended to make the process of mining data more efficient by automating the process.
# CSV Export function added by Gabe DeJongh 4/1/2020

import requests
from bs4 import BeautifulSoup
import csv

def courses_spider(max_pages):
    page = 1
    file = open("courses.csv", "w", newline='')
    writer = csv.writer(file)
    writer.writerow(["title", "subject", "url", "description"])
    while page <= max_pages:
        url = 'https://ocw.mit.edu/courses/'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        # All code from this point on needs to be adapted to the specific structure of the website that the user is attempting to mine data from.
        for link in soup.findAll('h4', {'class': 'course_title'}):
            link_title = link.find('a', {'rel': 'coursePreview'})
            href = 'https://ocw.mit.edu' + link_title.get('href').strip()
            subject = href.split('/')[4].strip()
            title = link_title.string.strip()
            title = title.replace("\n", "")
            # title = title.replace("\n", "")
            title = ' '.join(title.split())
            #print("title: " + title)
            #print("Split: " + subject)
            #print("Href: " + href)
            description = get_single_course_data(href)
            writer.writerow([title, subject, href, description])
        page += 1
    file.close()

def get_single_course_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    try:
        for item_description in soup.findAll('div', {'id': 'description'}):
            description = item_description.findAll('p')
            if description is not None:
                #print(description[0].string)
                return description[0].string
    except:
        # do nothing
        return


courses_spider(1)
print("Done")
