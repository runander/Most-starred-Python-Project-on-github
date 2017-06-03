import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
response_dict = r.json()
print("总项目数量:",response_dict['total_count'])
repos = response_dict['items']
print('打印项目信息:')
#打印项目总数

#获取项目的详细信息
for repo in repos:
    print('\nName:',repo['name'])#项目名称
    print('\nOwner:',repo['owner']['login'])#项目拥有者
    print('\nStars:',repo['stargazers_count'])#星级数目
    print('\nUrl:',repo['html_url'])#项目的Url
    print('\nDescription:',repo['description'])#项目描述

#使用pygal进行分析
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
name,stars = [],[]
#创建两个列表来存储名字和星数
for repo in repos:
    name.append(repo['name'])
    stars.append(repo['stargazers_count'])
#创建样式
my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart.title = 'Python Project'#名称
chart.x_labels = name#横坐标为项目名称
chart.add('',stars)
chart.render_to_file('python.svg')
