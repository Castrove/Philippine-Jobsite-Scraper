from bs4 import BeautifulSoup
import requests, re

url = 'https://www.jobstreet.com.ph/en/job-search/computer-software-it-jobs/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
# your version here: chrome://settings/help
# update here: https://www.whatismybrowser.com/guides/the-latest-user-agent/chrome

site = re.search('(https://www.)([A-Za-z_0-9.-]+)', url)[0]

html_text = requests.get(url, headers=headers).text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_='sx2jih0 zcydq852 zcydq842 zcydq872 zcydq862 zcydq82a zcydq832 zcydq8d2 zcydq8cq')

for job in jobs:
    # find published date
    time = job.find('span', class_='sx2jih0 zcydq82q _18qlyvc0 _18qlyvcx _18qlyvc1 _18qlyvc6').text
    tim = re.findall('[0-9]+', time)
    t = int(tim[0])

    if 'h' in time or ('d' in time and t < 12):

        # find inside job
        title = job.find('div', class_='sx2jih0 _2j8fZ_0 sIMFL_0 _1JtWu_0').text.replace(' ','')
        # find company
        com = job.find('span', class_='sx2jih0 zcydq82q _18qlyvc0 _18qlyvcv _18qlyvc1 _18qlyvc8').text
        # find location
        place = job.find('span', class_='sx2jih0 zcydq82q zcydq810 iwjz4h0').text
        # find salary
        pay = job.find_all('span', class_='sx2jih0 zcydq82q _18qlyvc0 _18qlyvcv _18qlyvc3 _18qlyvc6')
        if len(pay) < 2:
            pay = 'none'
        else: pay = pay[1].text
        # find link
        href = job.div.h1.a['href']
        if site not in href:
            link = site + href
        else:
            link = href

        print(f'''
JOB TITLE: {title}
LOCATION: {com}, {place}   DATE: {time}     
PAY: {pay}

link: {link}   \n''')





# #allows to open file
# with open("https://www.jobstreet.com.ph/en/job-search/job-vacancy.php?specialization=186%2C191%2C192%2C102", 'r') as html_file:
#     content = html_file.read()
    
#     soup = BeautifulSoup(content, 'lxml')
#     job_title = soup.find_all('div', class_='sx2jih0 _2j8fZ_0 sIMFL_0 _1JtWu_0') #for specific tags; turns it into list
    
#     for job in job_title:         # prints each find from the list
#         print(i.text)
