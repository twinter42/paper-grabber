class Journal:
    def __init__(self):
        pass

    def get_article_list(self, no_issues):
        article_list = []
        for issue in self.get_newest_issues(n=no_issues):
            for article in self.get_articles(issue):
                article_list.append(article)
        return sorted(article_list, key=lambda a: a.score, reverse=True)


    def get_newest_issues(self, n=1):
        """
        Get urls of n newest issues.
        :param n: Number of issues.
        :return: List of urls to n newest issues.
        """
        return []

    def get_articles(self, issue_url):
        """
        Given an issue URL, get all HTML artice elements.
        :param issue_url: URL of issue
        :return: List of Article objects
        """
        return []