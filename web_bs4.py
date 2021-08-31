from bs4 import BeautifulSoup
import  requests
import csv

html= requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text

soup = BeautifulSoup(html,'lxml')
csv_web = open('jobs_web_scrape.csv', 'w')

csv_writer = csv.writer(csv_web)
csv_writer.writerow(['Company','Req_skills','Apply_Link','Job Desc','Location'])

jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    published = job.find('span', class_='sim-posted').span.text
    if 'few' in published:

        com_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','')
        skills = job.find('span',class_='srp-skills').text.replace(' ','')
        more_info = job.header.h2.a['href']
        job_desc = job.find('ul',class_='list-job-dtl clearfix')
        try:
            location = job.find('ul',class_='top-jd-dtl clearfix').span.text
            #salary = job.find('ul',class_='top-jd-dtl clearfix').text
        except Exception as e:
            location = None
            #salary = None

        #print(f'Company Name: {com_name.strip()}')
        #print(f'Required Skills: {skills.strip()}')
        #print(job_desc.li.text.strip())
        #print(more_info)
        #print(salary)
        print(location)

        csv_writer.writerow([com_name.strip(),skills.strip(),more_info,job_desc.li.text.strip(),location])
csv_web.close()

