from bs4 import BeautifulSoup
import requests, re

far = ['NATIONAL', 'CEBU','ILOILO']
min_salary_k = 40

def filter(targ_sal, place, offer) :
    dist_ok = True
    sal_ok = True
    for i in range(len(far)):
                if far[i] in place.upper():
                    print(far[i], place)
                    dist_ok = False
                    break
    
    if offer == 'none':
        print('none')
    elif offer < targ_sal:
        print(offer, 'bad')
        sal_ok = False
    elif offer >= targ_sal:
        print(offer, 'good')
    
    if sal_ok == True and dist_ok ==True:
        print('OK')

    print()

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

        # find job title
        title = job.find('div', class_='sx2jih0 _2j8fZ_0 sIMFL_0 _1JtWu_0').text.replace(' ','')
        # find company
        com = job.find('span', class_='sx2jih0 zcydq82q _18qlyvc0 _18qlyvcv _18qlyvc1 _18qlyvc8').text
        # find location
        place = job.find('span', class_='sx2jih0 zcydq82q zcydq810 iwjz4h0').text
        # find salary
        pay = job.find_all('span', class_='sx2jih0 zcydq82q _18qlyvc0 _18qlyvcv _18qlyvc3 _18qlyvc6')
        if len(pay) < 2:
            pay = 'none'
        else: 
            pay = re.search('\d+', pay[1].text)
            pay = int(pay.group(0))

        filter(min_salary_k, place, pay)

#         if match == True:
                  
        
#             # find link
#             href = job.div.h1.a['href']
#             if site not in href:
#                 link = site + href
#             else:
#                 link = href

#             print(f'''-------------
# JOB TITLE: {title}
# LOCATION: {com} | {place}   DATE: {time}     
# PAY: {pay}

# link: {link}\n-------------''')

