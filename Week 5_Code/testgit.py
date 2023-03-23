from github import Github

mygit = Github("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")

for  repo in mygit.get_user().get_repos():
    print (repo.name)