from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import requests
import csv
import sqlite3

with open("jobs.csv", "w", newline="", encoding="utf-8") as f:
      writer=csv.writer(f)
      writer.writerow(["title", "company", "salary", "location", "skills", "job link"])
      c=0
      with sync_playwright() as p:
                        for pgno in range(1,12):
                            browser=p.chromium.launch(headless=True)
                            page=browser.new_page()
                            b_url= "https://internshala.com"
                            url=f"https://internshala.com/jobs/artificial-intelligence-ai,machine-learning-jobs/page-{pgno}"
                            page.goto(url)
                            content=page.content()
                            soup = BeautifulSoup(content, "lxml")
                            jobs= soup.find_all('div', class_= "internship_meta experience_meta")
                            for job in jobs:
                                job_title = job.find('a', class_="job-title-href")
                                js_url = b_url + job_title.get("href")
                                s = requests.get(js_url)
                                soup2 = BeautifulSoup(s.text, "lxml")

                                c_name = job.find('p', class_="company-name").text.strip()
                                try:
                                    sal = job.find('span', class_="desktop").text.strip()
                                except:
                                    sal = "Not Specified"
                                try:
                                    location = job.find('p', class_="row-1-item locations").text.strip()
                                except:
                                    location = "Unspecified"

                                # ✅ Skills
                                skills = [skill.text.strip().lower() for skill in soup2.find_all("span", class_="round_tabs")]
                                all = ", ".join(skills) if skills else "NoMentionedSkill"

                                # ✅ Print (for debugging)
                                print("Job Title:", job_title.text.strip())
                                print("Hiring Company:", c_name)
                                print("Salary:", sal)
                                print("Skills Required:", all)
                                print("Location(s):", location)
                                print("Job Link:", js_url, "\n")

                                # ✅ Write to CSV
                                writer.writerow([job_title.text.strip().lower(), c_name.lower(), sal, location.lower(), all.lower(), js_url])
                                c += 1
                            print(c)
                            browser.close()
                            
        