import requests
from bs4 import BeautifulSoup
url="https://internshala.com/job/detail/fresher-remote-part-time-medical-researcher-ai-trainer-job-at-taskify1754631052"
response=requests.get(url)
soup=BeautifulSoup(response.text, "lxml")
skills=soup.find_all('span', class_="round_tabs")
for skill in skills:
    print(skill.text.strip())
      


                            