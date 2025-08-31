from bs4 import BeautifulSoup
import requests
from playwright.sync_api import sync_playwright
while True:
    with sync_playwright() as p:
        for pgno in range(1,3):
            browser=p.chromium.launch(headless=True)
            page=browser.new_page()
            url=f"https://internshala.com/jobs/page-{pgno}"
            page.goto(url)
            content=page.content()
            source= requests.get(url)
            soup = BeautifulSoup(content, "lxml")
            jobs= soup.find_all('h3', class_= "job-internship-name")
            company_name= soup.find_all('p', class_="company-name")
            salary= soup.find_all('span', class_="desktop")
            for job, cn, s in zip(jobs, company_name, salary):
                job_title=job.find('a', class_="job-title-href")
                c_name= cn.text.strip()
                sal=s.text.strip()
                print("Job Title:", job_title.text)
                print("Hiring Company:", c_name)
                print("Salary:", sal, "\n")
