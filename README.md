# Projey Site Statique

## Manuel

### 1

Pour commencer placer votre fichier markdown a la racine du dossier et renommer le markdown.md

```
    Répertoire : C:\Users\Desktop\convertMdToHtml


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       14/01/2019     17:29                HTML
-a----       14/01/2019     17:29            423 convert_md.py
-a----       14/01/2019     17:14            112 markdown.md

```


### 2

Ensuite executer le programme qui convertira le fichier en html et le placera dans le dossier HTML
```
PS C:\Users\Desktop\convertMdToHtml> python .\convert_md.py
PS C:\Users\Desktop\convertMdToHtml> cd .\HTML\
PS C:\Users\Desktop\convertMdToHtml\HTML> ls


    Répertoire : C:\Users\Desktop\convertMdToHtml\HTML


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----       14/01/2019     17:36            204 index.html

```

### 3

Ensuite vous trouverai le fichier index.html qui est votre fichier markdown en html
```
PS C:\Users\Desktop\convertMdToHtml\HTML> cat .\index.html
<h1>Titre</h1>
<h2>SOUS titre</h2>
<h3>sousous titre</h3>
<p>paragraphe</p>
<p><em>texte</em></p>
<p><a href="http://www.siteduzero.com">http://www.siteduzero.com</a></p>
<ul>
<li>liste</li>
</ul>
```

