import requests
from bs4 import BeautifulSoup
import pprint


URL = "https://www.seek.com.au/developer-jobs-in-information-communication-technology/in-All-Melbourne-VIC?countrycode=au&savedsearchid=cd24499a-472e-11ea-bcec-479294033dc2&subclassification=6287%2C6302&worktype=243%2C245%2C244"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(attrs={"data-automation": "searchResults"})

# print(results.prettify())
# pprint.pprint(results)

# # Print out all available jobs from the scraped webpage
job_elems = results.find_all("article")
for job_elem in job_elems:
    # title_elem = job_elem.find("h1")
    title_elem = job_elem.find("a", attrs={"data-automation": "jobTitle"})
    company_elem = job_elem.find("a", attrs={"data-automation": "jobCompany"})
    link = job_elem.find("a", attrs={"data-automation": "jobTitle"})["href"]
    days_ago_elem = job_elem.find("div", class_="Eadjc1o")
    description_elem = job_elem.find("span", attrs={"data-automation": "jobShortDescription"})

    if None in (title_elem, company_elem):
        continue
    print(company_elem.text.strip())
    print(title_elem.text.strip())

    for ptag in job_elem.findAll('p'):
        if ptag.parent.name == 'span':
            print(ptag.text.strip())

    if description_elem:
        print(description_elem.text.strip())

#print(f"Apply here: https://www.seek.com.au{link}")
    print()
