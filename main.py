from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

url = 'https://www.jobstreet.com.ph/en/job-search/computer-software-it-jobs/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
# your version here: chrome://settings/help
# update here: https://www.whatismybrowser.com/guides/the-latest-user-agent/chrome

html_text = requests.get(url, headers=headers).text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_='sx2jih0 zcydq852 zcydq842 zcydq872 zcydq862 zcydq82a zcydq832 zcydq8d2 zcydq8cq')

for job in jobs:

    # find inside job
    title = job.find('div', class_='sx2jih0 _2j8fZ_0 sIMFL_0 _1JtWu_0').text.replace(' ','')
    # find company
    com = job.find('span', class_='sx2jih0 zcydq82q _18qlyvc0 _18qlyvcv _18qlyvc1 _18qlyvc8').text.replace(' ','')
    # find location
    place = job.find('span', class_='sx2jih0 zcydq82q zcydq810 iwjz4h0').text.replace(' ','')

    # print(time)


    print(f'''
    JOB TITLE: {title}
    LOCATION: {com}, {place}   DATE: -time-     
    PAY: -pay-
    ''')
    print('\n\n')





# #allows to open file
# with open("https://www.jobstreet.com.ph/en/job-search/job-vacancy.php?specialization=186%2C191%2C192%2C102", 'r') as html_file:
#     content = html_file.read()
    
#     soup = BeautifulSoup(content, 'lxml')
#     job_title = soup.find_all('div', class_='sx2jih0 _2j8fZ_0 sIMFL_0 _1JtWu_0') #for specific tags; turns it into list
    
#     for job in job_title:         # prints each find from the list
#         print(i.text)
