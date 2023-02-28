from journals.optica_applied_optics import AppliedOptics

my_journal = AppliedOptics()
articles = my_journal.get_article_list(no_issues=7) # return the list of articles sorted by keyword score

for a in articles:
    print(a.score, a.href, a.title)