# To run this program do pip -install pygithub first

import base64
from github import Github
from pprint import pprint

username = "Hugo-99"
token = "93d19f42a4b9404dd1f042d4389b4cab6b412d14"
g = Github(token)
user = g.get_user()
print(user.login)

for repo in user.get_repos():

	commits = repo.get_commits()
	count = commits.totalCount

	print(repo.name, repo.get_commits().totalCount)

	for commit in commits:
		if commit.commit is not None:
			print (commit.commit.author.date, commit.commit.author)
			if commit.stats is not None:
				print("additions:" + commit.stats.additions)
				print("deletions:" + commit.stats.deletions)
			# print (commit.commit.author.date, commit.commit.author, commit.commit.message)
	

