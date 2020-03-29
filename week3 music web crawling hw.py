import requests
from bs4 import BeautifulSoup
import datetime

now = datetime.datetime.now()
nowDate = now.strftime('%Y%m%d')
nowHour = now.strftime('%H')

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/73.0.3683.86 Safari/537.36'}
rank = 1

for i in range(1, 5):
    url = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=' + nowDate + '&hh=' + nowHour + '&rtm=Y&pg=' + str(i)
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr > td.info')

for music in musics:
    music_title = music.select_one('a.title')
    artist = music.select_one('a.artist')

    music_title = music_title.text.strip()
    artist = artist.text.strip()

    print(rank, music_title, artist, )
    rank += 1
