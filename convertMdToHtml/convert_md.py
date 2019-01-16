#!/usr/bin/python

import markdown
import codecs
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str,help="dossier markdown")
parser.add_argument("-o", "--output", type=str,help="dossier site")
args = parser.parse_args()

if args.input != None:
    pathMd = args.input
else:
    pathMd = "./Markdown/"
    pass
if args.output != None:
    pathSite = args.output
else:
    pathSite = "./sitestatique"
    pass

def convert_to_html(pathMd):
    check = 0
    if pathMd != None and pathMd != "./Markdown/markdown.md":
        md = pathMd + "markdown.md"
    else:
        pass
    fichier_md = codecs.open(md, mode="r", encoding="utf-8")
    text = fichier_md.read()
    html = markdown.markdown(text)
    fichier = open("./template/html_first.html", "w")
    fichier.write(html)
    fichier.close()
    fichier = open("./template/html_first.html", "r")
    fichier_set = open("./template/html_set.html", "w")
    for ligne in fichier:
        if check == 0:
            fichier_set.write('\t')
            check = check + 1
        fichier_set.write(ligne.replace('\n', '\n\t'))
    fichier.close()

def create_html(pathSite):
    if pathSite != None and pathSite != "./sitestatique/HTML/index.html":
        site = pathSite + "/HTML/index.html"
    else:
        pass
    fichier = open(site, "w")
    fichier = open(site, "a")
    base_html = codecs.open("./template/basehtml.txt", mode="r", encoding="utf-8")
    txt_baseHtml = base_html.read()
    body_html = codecs.open("./template/html_set.html", mode="r", encoding="utf-8")
    bodyHtml = body_html.read()
    footer_html = codecs.open("./template/fin_html.txt", mode="r", encoding="utf-8")
    footerHtml = footer_html.read()
    fichier.write(txt_baseHtml)
    fichier.write(bodyHtml)
    fichier.write(footerHtml)

def create_css():
    fichier = open("./sitestatique/CSS/index.css", "w")
    fichier = open("./sitestatique/CSS/index.css", "a")
    base_css = codecs.open("./template/basecss.txt", mode="r", encoding="utf-8")
    txt_baseCss = base_css.read()
    fichier.write(txt_baseCss)


convert_to_html(pathMd)
create_html(pathSite)
create_css()