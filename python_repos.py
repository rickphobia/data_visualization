import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url,headers= headers)
print(f"Status code = {r.status_code}")
response_dict = r.json()
print(response_dict.keys())
print(f"Total repo = {response_dict['total_count']}")

repo_dicts = response_dict['items']
print(f"Repositories returned = {len(repo_dicts)}")

for repo_dict in repo_dicts:
    print(f"Name = {repo_dict['name']}")
    print(f"Owner = {repo_dict['owner']['login']}")
    print(f"Size= {repo_dict['size']}")
    print(f"Repository = {repo_dict['html_url']}")
    print(f"Stars= {repo_dict['stargazers_count']}")
    print(f"Watchers_count = {repo_dict['description']}\n")
