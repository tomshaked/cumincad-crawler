from db import Db
from crawler import Crawler

crawler = Crawler()
db = Db()
## Create database structure - only enable for the first run
# db.create()

# Gets user input
search = raw_input("Search: ") or "surface"

pages = crawler.getPages(search)
for page in pages:
    pageData = crawler.getPaper(page)
    db.savePage(pageData, search)