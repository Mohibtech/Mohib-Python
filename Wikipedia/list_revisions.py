# This script lists top 5 user revisions 
# Pre-requisite for this script is to Install mwclient using 
# pip install mwclient

from mwclient import Site
site = Site('ur.wikipedia.org')


page = site.pages['شاہ ولی اللہ']
text = page.text()
pglinks = page.links()
users = [rev['user'] for rev in page.revisions()]
unique_users = set(users)
user_revisions = [{'user': user, 'count': users.count(user)} for user in unique_users]
print(sorted(user_revisions, key=lambda x: x['count'], reverse=True)[:5])

for pg in pglinks:
    print(pg)