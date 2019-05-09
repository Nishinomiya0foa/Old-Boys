import requests
from bs4 import BeautifulSoup

headers = {
    'Host': 'www.kanzhun.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
}


def get_site(search_company):
    search_url_less = 'https://www.kanzhun.com/companyl/search/?stype=&q='

    # 搜索结果
    search_url_result = search_url_less+search_company  # 完整搜索网址
    search_response = requests.get(search_url_result, headers=headers)

    # 搜索结果页 网页
    cont = search_response.content.decode('utf-8')
    soup = BeautifulSoup(cont, 'html.parser')

    items = soup.find('div', attrs={'class':'container-search clearfix'}).find('div', attrs={'class':'wrap_style mt15'})\
        .find('ul', attrs={'class':'company_result'}).find('li')
    # print(items.find('img').get('title'), items.find('a').get('href'))
    interview_code = items.find('a',attrs={'ka':'com1-interview'}).get('href')
    return interview_code


def get_interview(url):
    pass


if __name__ == '__main__':
    url_less = 'https://www.kanzhun.com'
    url_rest_part = 'p{}.html?ka=paging2'
    search_company = input('输入想要查询的公司：')
    interview_code = get_site(search_company)
    for i in range(2):
        url_full = url_less+interview_code+url_rest_part.format(i+1)
        # print(url_full)
        get_interview(url_full)