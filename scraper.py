import urllib.request
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.indeed.com/jobs?q=Software+Developer&l=California&start=10"    

soup = BeautifulSoup(urllib.request.urlopen(URL).read(), 'html.parser')

results = soup.find_all('div', attrs={'data-tn-component': 'organicJob'})

def check_jobs():
    jobs = []
    for x in results:
        company = x.find('span', attrs={"class":"company"})
        singleJob = []
        if company:
            print('company:', company.text.strip() )
            singleJob.append( company.text.strip() )

        job = x.find('a', attrs={'data-tn-element': "jobTitle"})
        if job:
            print('job:', job.text.strip())
            singleJob.append( job.text.strip() )

        salary = x.find('nobr')
        if salary:
            print('salary:', salary.text.strip())
            singleJob.append( salary.text.strip() )

        print ('----------')
        jobs.append(singleJob)
    send_email(jobs)
    print(jobs)


def send_email(message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('stevengkeezer@gmail.com', "uxsgmkihuihmvilo" )

    subject = "New jobs for you!"
    body="check it!"

    
    msg = f"Subject: {subject}\n\n{message}"

    server.sendmail('stevengkeezer@gmail.com', 'stevengkeezer@gmail.com',msg)
    
    print("Email has been sent")

    server.quit()


while(True):
    check_jobs()
    time.sleep(100023423423980989080980980)