from bs4 import BeautifulSoup
import requests
import time

choice = input("Would you like to filter out any specific skills you are not familiar with? [Y/N] > ")
if choice.upper() == 'Y':
    print("Enter skill you are not familiar with [ex. haskell, rust, etc.]")
    unfamiliar_skill = input('> ')
    print(f'Filtering out {unfamiliar_skill}...')
else:
    print('Proceeding with job listings...')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
            skills =  job.find('span', class_='srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if choice.upper() == 'Y':
                if unfamiliar_skill not in skills:
                    with open(f'posts/{index}.txt', 'w') as f:
                        f.write(f'Company Name: {company_name.strip()} \n')
                        f.write(f'Required Skills: {skills.strip()} \n')
                        f.write(f'More info: {more_info} \n')
                    print(f'FIle saved: {index}\n')
            else:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name: {company_name.strip()} \n')
                    f.write(f'Required Skills: {skills.strip()} \n')
                    f.write(f'More info: {more_info} \n')
                print(f'FIle saved: {index} \n')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)