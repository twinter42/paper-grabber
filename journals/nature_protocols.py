from journals.journal_skeleton import Journal
from journals.article import Article
from datetime import datetime
import requests
from bs4 import BeautifulSoup


class NatureProtocols(Journal):
    def __init__(self):
        super().__init__()
        self.base_url = "https://www.nature.com/nprot/"

    def get_newest_issues(self, n=1):
        result = []
        # current issue is of form "journal_no/month", e.g. "94/2"
        journal_no = datetime.now().year - 2005
        month = datetime.now().month
        url_newest = self.base_url + f"volumes/{journal_no}/issues/{month}"
        # get n older issues
        for i in range(n):
            if month - i < 1:  # jump to last year's issue
                month += 12
                journal_no -= 1
            # synthesize URL and test if it can be reached
            url = self.base_url + f"volumes/{journal_no}/issues/{month-i}"
            if not requests.get(url):
                raise ConnectionError(f"Could not access issue {journal_no}/{month - i}!")
            else:
                result += [url]
        # return list of issue URLs
        return result

    def get_articles(self, issue_url):
        articles_result = []
        page = requests.get(issue_url)
        soup = BeautifulSoup(page.content, "html.parser")
        articles = soup.find_all("article", class_="u-full-height")
        for a in articles:
            href =  "https://www.nature.com" + a.find("a", class_="u-link-inherit")['href']
            title = a.find("a", class_="u-link-inherit").text
            try:
                author_item = a.find(class_="c-author-list")
                authors = [author.text for author in author_item.find_all("span")]
                articles_result.append(Article(href, title, authors))
            except AttributeError as e:
                print(f"Could not parse article: {title} due to {e}")
        return articles_result