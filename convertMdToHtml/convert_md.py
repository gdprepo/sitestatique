#!/usr/bin/python

import markdown
import codecs

def convert_to_html():
    fichier = codecs.open("markdown.md", mode="r", encoding="utf-8")
    text = fichier.read()
    html = markdown.markdown(text)

    return (html)

def create_html(html):
    fichier = open("./HTML/index.html", "w")
    fichier = open("./HTML/index.html", "a")
    fichier.write(html)


html = convert_to_html()
create_html(html)