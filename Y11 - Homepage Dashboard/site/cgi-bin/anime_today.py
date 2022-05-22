#!/usr/bin/env python3
import cgi
import cgitb
import datetime
from urllib.request import urlopen
from parsel import Selector

cgitb.enable()

print("Content-Type: text/html")
print()


schedule_url = "https://myanimelist.net/anime/season/schedule"
with urlopen(url=schedule_url) as response:
    schedule_html = response.read().decode("utf-8")

schedule = Selector(text=schedule_html)
name_of_today = datetime.date.today().strftime("%A")
todays_anime_list = schedule.xpath(f".//div[./div[@class = 'anime-header' and text() = '{name_of_today}']]")[0]
todays_animes = todays_anime_list.xpath(".//div[@class = 'seasonal-anime js-seasonal-anime']")
print("<ol>")
for anime in todays_animes:
    title = anime.xpath(".//h2[@class = 'h2_anime_title']/a/text()").get()
    print(f"<li>{title}</li>")
print("</ol>")