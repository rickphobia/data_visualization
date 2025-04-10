from plotly.graph_objs import Bar,Layout
from plotly import offline 

import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url, headers = headers)
print(r.status_code)
response_dicts = r.json()

repo_dicts = response_dicts['items']
repo_links = [f"<a href = '{repo_dict['html_url']}'>{repo_dict['name']}</a>" for repo_dict in repo_dicts]
stars_values = [repo_dict['stargazers_count'] for repo_dict in repo_dicts]

# labels = []
# for repo_dict in repo_dicts:
#     owner = repo_dict['owner']['login']
#     desciption = repo_dict['description']
#     label = f"{owner} <br /> {desciption}"
#     labels.append(label)
# link = [repo_dict['html_url'] for repo_dict in repo_dicts]
# description = [repo_dict['description'] for repo_dict in repo_dicts]

#faster way 
labels = [f"{repo_dict['owner']['login']} <br />{repo_dict['description']}" for repo_dict in repo_dicts]

#this is wrong 
# labels = [f"{[repo_dict['owner']['login']]} <br /> {[repo_dict['description']]}" for repo_dict in repo_dicts]

data = [{
    'type' : 'bar', 
    'x' : repo_links,
    'y' : stars_values,
    'hovertext' : labels,
    'marker':{
        'color' : 'rgb(60,100,170)',
        'line' : {'width':1.5, 'color': 'rgb(25,25,25)'}
    }
}]

x_axis_config = {'title': 'Name of repos'}
y_axis_config = {'title':'Stars'}

my_layout = Layout(title = 'The top 30 Repos in terms of stars',xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data' : data,'layout': my_layout}, filename = 'The top 30 Repos in terms of stars.html')
