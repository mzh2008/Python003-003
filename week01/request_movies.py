import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
#
# header = {'user-agent':user_agent}
#
# myurl = 'https://maoyan.com/films'
#
# response = requests.get(myurl,headers=header)
#
# print(response.text)
# print(f'返回码是: {response.status_code}')

file=open('movies.html',encoding='UTF-8')
lines=file.readlines()
content = ''.join(lines)
bs_info = bs(content, 'html.parser')


movies = []
for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    name = tags.find('span', attrs={'class': 'name'}).text
    for divs in tags.find_all('div', attrs={'class': 'movie-hover-title'}):
        for spans in divs.find_all('span', attrs={'class': 'hover-tag'}):
            if spans.text == '类型:':
                spans.replace_with('')
                movie_type = divs.text.replace(' ', '').strip()
            if spans.text == '上映时间:':
                spans.replace_with('')
                movie_date = divs.text.replace(' ', '').strip()
    movie = [name, movie_type, movie_date]
    movies.append(movie)
movie10 = pd.DataFrame(data=movies[:10])
movie10.to_csv('./movie.csv', encoding='utf-8', index=False, header=['电影名称', '电影类型', '上映时间'])