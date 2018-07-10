from selenium import webdriver
import math
import os
import shutil
import time
import config

class Crawler:
    def getPages(self, search):
        path = config.SAVE_DIR + search
        if os.path.isdir(path):
            shutil.rmtree(path)
        os.mkdir(path)

        ## Disable firefox pdf viewer
        fp = webdriver.FirefoxProfile()
        fp.set_preference("browser.download.folderList", 2)
        fp.set_preference("browser.download.manager.showWhenStarting", False)
        fp.set_preference("browser.download.dir", path)
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf,application/x-pdf")
        fp.set_preference("pdfjs.disabled", True)
        self.browser = webdriver.Firefox(firefox_profile=fp)

        ## Get number of result pages
        self.browser.get("http://papers.cumincad.org/cgi-bin/works/Search?search=" + search + "&x=0&y=0&first=0")
        results = self.browser.find_element_by_class_name("SEARCHTITLES")
        result = results.text.split()
        hits = int(result[5])

        pages = int(math.ceil(hits / 20))

        returnValue = []
        for i in range(pages):
            firstPage = i * 20
            href = ("http://papers.cumincad.org/cgi-bin/works/Search?search=" + search + "&x=0&y=0&first=" + str(firstPage))
            returnValue.append(href)
        # print(returnValue)
        return returnValue

    def getPaper(self, href):
        returnValue = []
        self.browser.get(href)
        linksNum = len(self.browser.find_elements_by_xpath('//a[@href]//b'))
        for i in range(linksNum):
            self.browser.get(href)
            links = self.browser.find_elements_by_xpath('//a[@href]//b')
            print(links[i].text)
            links[i].click()
            ## Download paper file
            try:
                file = self.browser.find_element_by_link_text('file.pdf')
                url = file.get_attribute("href")
                print(url)
                filename = url.rsplit('/', 1)[-1]
                print(filename)
                file.click()
                # time.sleep(3)
            except:
                print("no pdf")
                filename = ""
                url = ""

            ## Get paper data
            ## Create data dictionary
            data_dict = {
                'authors': "",
                'year': "",
                'title': "",
                'source': "",
                'summary': "",
                'keywords': "",
                'series': "",
                'content': filename,
                'url': url,
                'email': "",
            }

            data = self.browser.find_elements_by_class_name("DATA")
            for row in data:
                key = row.text.split(' ', 1)[0]
                value = row.text.split(' ', 1)[1]
                data_dict[key] = value
            print(data_dict)
            print("---")
            returnValue.append(data_dict)

        return returnValue
