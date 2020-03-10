import requests
from bs4 import BeautifulSoup

#parse content from website
html = requests.get("https://catalog.umkc.edu/course-offerings/graduate/comp-sci/")
soup = BeautifulSoup(html.content, "html.parser")
correctCourse = False

#go through all paragraph items, look for ones with courseblocktitle as a class
for item in soup.find_all('p'):
    if item.has_attr('class') and item['class'][0] == 'courseblocktitle':
        courseName = item.contents[3]
        #Look for Special Topics course, print course name when found
        if str(courseName.get_text()) == 'Special Topics':
            print(item.contents[1].get_text())
            print(courseName.get_text())
            correctCourse = True
    else:
        #print course description from the Special Topics course, break out of loop when done
        if item.has_attr('class') and item['class'][0] == 'courseblockdesc' and correctCourse:
            print(item.get_text())
            break



