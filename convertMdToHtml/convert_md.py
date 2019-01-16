#!/usr/bin/python

import markdown
import codecs

def convert_to_html():
    check = 0
    fichier_md = codecs.open("markdown.md", mode="r", encoding="utf-8")
    text = fichier_md.read()
    html = markdown.markdown(text)
    fichier = open("html_first.html", "w")
    fichier.write(html)
    fichier.close()
    fichier = open("html_first.html", "r")
    fichier_set = open("html_set.html", "w")
    for ligne in fichier:
        if check == 0:
            fichier_set.write('\t')
            check = check + 1
        fichier_set.write(ligne.replace('\n', '\n\t'))
    fichier.close()

def create_html():
    fichier = open("./HTML/index.html", "w")
    fichier = open("./HTML/index.html", "a")
    base_html = codecs.open("basehtml.txt", mode="r", encoding="utf-8")
    txt_baseHtml = base_html.read()
    body_html = codecs.open("html_set.html", mode="r", encoding="utf-8")
    bodyHtml = body_html.read()
    footer_html = codecs.open("fin_html.txt", mode="r", encoding="utf-8")
    footerHtml = footer_html.read()
    fichier.write(txt_baseHtml)
    fichier.write(bodyHtml)
    fichier.write(footerHtml)

def create_css():
    fichier = open("./CSS/index.css", "w")
    fichier = open("./CSS/index.css", "a")
    base_css = codecs.open("basecss.txt", mode="r", encoding="utf-8")
    txt_baseCss = base_css.read()
    fichier.write(txt_baseCss)


convert_to_html()
create_html()
create_css()