from mwclient import Site
site = Site('ur.wikipedia.org')


page = site.pages['شاہ ولی اللہ']
text = page.text()

for ln in page.links():
    print(ln)
