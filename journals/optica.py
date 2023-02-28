from journals.journal_skeleton import Journal
from journals.article import Article
import requests
from bs4 import BeautifulSoup

JOURNAL_NAMES = {"optica": "Optica",
                 "josaa": "Journal of the Optical Society of America A",
                 "ao": "Applied Optics"}

def get_available_journals():
    for i in JOURNAL_NAMES:
        print(f"{JOURNAL_NAMES[i]}, short: '{i}'")

class Optica(Journal):
    def __init__(self, journal="optica"):
        super().__init__()
        self.journal = journal
        self.base_url = f"https://opg.optica.org/{journal}/"

    def get_newest_issues(self, n=1):
        result = []
        # in this case, all upcoming issues are the newest issue
        issues = [self.base_url + "upcomingissue.cfm"]
        # older issues have to be accessed differntly
        issue_list_url = self.base_url + "browse.cfm"
        issue_list = requests.get(issue_list_url)
        soup = BeautifulSoup(issue_list.content, "html.parser")
        # filter out links to upcoming issues
        # (inefficient, since not all issues are needed, use generator in the future)
        issues += [self.base_url + a['href'] for a in soup.find_all("a")
                   if "Issue " in a.text and "upcoming" not in a['href']]
        # get n latest issues
        for i in range(n):
            url = issues[i]
            if not requests.get(url):
                raise ConnectionError(f"Could not access issue {url}!")
            else:
                result += [url]
        # return list of issue URLs
        return result

    def get_articles(self, issue_url):
        articles_result = []
        page = requests.get(issue_url)
        soup = BeautifulSoup(page.content, "html.parser")
        articles = soup.find_all("div", class_="media-twbs-body")
        for a in articles:
            href = "https://opg.optica.org" + a.find("a")["href"]
            title = a.find("a").text
            authors = a.find("p", class_="article-authors").text
            articles_result.append(Article(href, title, authors))
        return articles_result
