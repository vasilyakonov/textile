# -*- coding: utf-8 -*-
import bs4
import random
import requests
import uuid
import subprocess


from bs4 import BeautifulSoup 

with open("/Users/vasilij/docs/index.html") as inf:
    txt = inf.read()
    soup = bs4.BeautifulSoup(txt, features="html.parser")
    print(soup.prettify())
    
soup.body.string=""
soup.body.append("<img src='https://res.cloudinary.com/duf9i9rcz/image/upload/v%s/pattern-neue.gif' alt='Oh No!'>" % (random.randint(1,19999999999999999999999999)))
                 
with open("/Users/vasilij/docs/index.html", "w") as outf:
    outf.write(str(soup.prettify(formatter=None)))
    print(soup.prettify())

u = uuid.uuid1()
#subprocess.call('git commit -a -m "%s"' % uuid.uuid1())
process = subprocess.Popen(["git", "commit", "-a", "-m'%s'" % uuid.uuid1()], stdout=subprocess.PIPE)
output = process.communicate()[0]
output = subprocess.check_output(["git", "push"])
