from journals.journal_skeleton import Journal
from journals.article import Article
from datetime import datetime
import requests
from bs4 import BeautifulSoup


class ReviewOfScientificInstruments(Journal):
    def __init__(self):
        super().__init__()
        self.base_url = "https://aip.scitation.org/toc/rsi/"

    def get_newest_issues(self, n=1):
        result = []
        # current issue is of form "journal_no/month", e.g. "94/2"
        journal_no = datetime.now().year - 1929
        month = datetime.now().month
        url_newest = self.base_url + f"{journal_no}/{month}?size=all"
        # get n older issues
        for i in range(n):
            if month - i < 1:  # jump to last year's issue
                month += 12
                journal_no -= 1
            # synthesize URL and test if it can be reached
            url = self.base_url + f"{journal_no}/{month - i}?size=all"
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
        articles = soup.find_all(class_="card-cont")
        for a in articles:
            href = "https://aip.scitation.org" + a.find("a", class_="ref nowrap")['href']
            title = a.find("h4", class_="hlFld-Title").text
            author_item = a.find("span", class_="articleEntryAuthorsLinks")
            authors = [author.text for author in author_item.find_all("a")]
            articles_result.append(Article(href, title, authors))
        return articles_result
