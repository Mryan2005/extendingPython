import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class GithubSearch:
    def __init__(self):
        self.driver = None

    def open_browser(self, webdriveType: str):
        if webdriveType.lower() == 'firefox':
            service = FirefoxService(GeckoDriverManager().install())
            self.driver = webdriver.Firefox(service=service)
            self.driver.implicitly_wait(10)
        elif webdriveType.lower() == 'edge':
            service = EdgeService(EdgeChromiumDriverManager().install())
            self.driver = webdriver.Edge(service=service)
            self.driver.implicitly_wait(10)
        elif webdriveType.lower() == 'chrome':
            service = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service)
            self.driver.implicitly_wait(10)

    def searchRepositories(self, keyword):
        res = []
        queue = []
        queue.append("https://github.com/search?q=" + keyword + "&type=repositories")
        while len(queue) != 0:
            url = queue.pop(0)
            self.driver.get(url)
            time.sleep(3)
            res.append(self.driver.page_source)
            self.next_page = self.driver.find_elements(By.XPATH, "//a[@rel='next' and @aria-label='Next Page']")
            if len(self.next_page) != 0:
                queue.append(self.next_page[0].get_attribute('href'))
        return res

    def searchCode(self, keyword):
        self.driver.get("https://github.com/search?q=" + keyword + "&type=code")
        time.sleep(3)
        return self.driver.page_source

    def searchUsers(self, keyword):
        self.driver.get("https://github.com/search?q=" + keyword + "&type=users")
        time.sleep(3)
        return self.driver.page_source

    def searchIssues(self, keyword):
        self.driver.get("https://github.com/search?q=" + keyword + "&type=issues")
        time.sleep(3)
        return self.driver.page_source

    def searchPullRequests(self, keyword):
        self.driver.get("https://github.com/search?q=" + keyword + "&type=pullrequests")
        time.sleep(3)
        return self.driver.page_source

    def searchDiscussions(self, keyword):
        self.driver.get("https://github.com/search?q=" + keyword + "&type=discussions")
        time.sleep(3)
        return self.driver.page_source

    def searchCommits(self, keyword):
        self.driver.get("https://github.com/search?q=" + keyword + "&type=commits")
        time.sleep(3)
        return self.driver.page_source

    def searchTopics(self, keyword):
        self.driver.get("https://github.com/search?q=" + keyword + "&type=topics")
        time.sleep(3)
        return self.driver.page_source

    def searchWikis(self, keyword):
        self.driver.get("https://github.com/search?q=" + keyword + "&type=wikis")
        time.sleep(3)
        return self.driver.page_source

    def searchPackages(self, keyword):
        self.driver.get("https://github.com/search?q=" + keyword + "&type=packages")
        time.sleep(3)
        return self.driver.page_source

    def searchMarketplace(self, keyword):
        self.driver.get("https://github.com/search?q=" + keyword + "&type=marketplace")
        time.sleep(3)
        return self.driver.page_source

    def close_browser(self):
        self.driver.quit()

    def __del__(self):
        self.close_browser()


if __name__ == '__main__':
    GITHUB = GithubSearch()
    GITHUB.open_browser('firefox')
    print(GITHUB.searchRepositories('python'))
    # baidu.close_browser()
