from db import Db
from crawler import Crawler

crawler = Crawler()
db = Db()
## Create database structure - only run for the first time
# db.create()

## get user input
search = input("Search: ") or "robotics"

pages = crawler.getPages(search)
for page in pages:
    pageData = crawler.getPaper(page)
    db.savePage(pageData, search)