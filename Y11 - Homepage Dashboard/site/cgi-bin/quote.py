#!/usr/bin/env python3
import cgi
import cgitb
from random import choice

cgitb.enable()

print("Content-Type: text/html")
print()

print("<h1>Quote of the Day</h1")
with open("./cgi-bin/quote_bank.txt") as quotes_fileobj:
    quotes = quotes_fileobj.readlines()
quote = choice(quotes)
author, text = quote.split(":", maxsplit=1)
print(f"""
    <figure>
        {text}
        <cite>
            {author}
        </cite>
    </figure>
""")
