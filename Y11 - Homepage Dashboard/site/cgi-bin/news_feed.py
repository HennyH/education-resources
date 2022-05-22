#!/usr/bin/env python3
import cgi
import cgitb
from urllib.request import urlopen
from xml.etree import ElementTree

cgitb.enable()

print("Content-Type: text/html")
print()

feed_url = "https://www.abc.net.au/news/feed/4570996/rss.xml"
with urlopen(url=feed_url) as response:
    feed_xml = response.read().decode("utf-8")

feed = ElementTree.fromstring(feed_xml)
items = feed.findall(".//item")
print("<ol>")
for item in items:
    title = item.find("./title").text
    link = item.find("./link").text
    img = item.findall(".//media:content", {"media": "http://search.yahoo.com/mrss/"})[0].get("url")
    print(f"""
        <li>
            <img src="{img}" style="width: 50px; height: 50px;" />
            <a href="{link}">{title}</a>
        </li>
    """)
print("</ol>")