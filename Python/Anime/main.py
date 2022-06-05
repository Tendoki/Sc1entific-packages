import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

data = pd.read_csv('anime.csv', delimiter=',')  #1
print(data.head(10)) #2
data.loc[(data['Episodes'] == '?'), 'Episodes'] = np.nan
data['Episodes'] = data['Episodes'].astype(float)

data.columns = data.columns.str.lower().str.replace(' ', '_') #4

data['voters'] = data['voters'].str.replace(',','').replace('N/A',np.nan)
data['voters'] = data['voters'].astype(int)
#print(data['Episodes'])
print(data.dtypes)  #3

#5

perc =[.25,.75,.90]
print(data.describe(percentiles = perc, include = ['float64','int32']))

#
#print(data['genre'])
#data.groupby(['production', 'title']).sum()
print(data.info())
# data=data.fillna({'episodes':0,	'airdate':'',	'rating' :0,	'voters':0})

genresList = data['genre'].str.split(',')

#6
for column in data.columns:
    if data[column].dtypes == 'object':
        print(column,'---------------------', '\n')
        a, b = np.unique(np.array(list(data[column])), return_counts=True)
        for i in range(len(a)):
            print(a[i],':',b[i])
        print('\n')
print('\n')

#8.a
company = dict((x, list(data['production']).count(x)) for x in set(data['production']))
sorted_company = sorted(company.items(), key=lambda x: x[1])
fig1, ax1 = plt.subplots()
import random
c = np.random.rand(10,3)
ax1.bar(dict(sorted_company).keys(), dict(sorted_company).values(), color=c)
plt.xticks(rotation=90)
plt.xticks(fontsize=4)

listGeneres = sum(genresList, [])
print(list(listGeneres))
fig2, ax2 = plt.subplots()
fig2.set_figwidth(22)
fig2.set_figheight(6)
ax2.bar(list(sorted(set(listGeneres))), [listGeneres.count(x) for x in sorted(set(listGeneres))], width=0.4)
plt.xticks(fontsize=6.5)

#8.b

fig3, ax3 = plt.subplots()
eps = data.groupby(['episodes']).size()
ax3.set_xlabel('amount of episodes')
ax3.set_ylabel('amount of repeating')

fig3.set_figwidth(40)
fig3.set_figheight(10)

ep = dict((x, list(data['episodes'].dropna()).count(x)) for x in set(data['episodes'].dropna()))
ep_sorted = sorted(ep.items(), key=lambda x: x[0])
print(ep_sorted)
ax3.bar(dict(ep_sorted).keys(), dict(ep_sorted).values(), color=c)

#8.c
fig4, ax4 = plt.subplots()

src = data.groupby(['source']).size()
src1 = src.sort_values().iloc[-3:]
ax4.bar(src1.index,src1)

#8.d
themes = pd.Series([i.split(',') for i in list(data.theme)]).explode()

themes = themes.groupby(themes).size().sort_values()
fig5, ax5 = plt.subplots()
ax5.bar(themes.index,themes)
plt.xticks(rotation=90)
plt.tick_params(labelsize=10)

#8.e
import re

regex_year = re.compile('\d{4}')
years_dict = dict()
for i in range(data.shape[0]):
  date = str(data['airdate'][i])
  found_year = regex_year.findall(date)
  if len(found_year) > 0:
    if found_year[0] in years_dict:
        years_dict[found_year[0]] = years_dict[found_year[0]]+1
    else:
        years_dict[found_year[0]] = 1
#print(years)
#name = 'year'

years_dict = dict(sorted(years_dict.items()))
fig6, ax6=plt.subplots()
ax6.bar(range(len(years_dict)), list(years_dict.values()), align='center')
plt.xticks(range(len(years_dict)), list(years_dict.keys()), rotation=90)
plt.title("производство аниме в разные годы")
#print(dict(sorted_company))

#9

fig8, ax8= plt.subplots()

ratings = data.groupby(['production'])['rating'].mean().sort_values().dropna()
plt.bar(ratings.index, ratings)
plt.xticks(rotation=90)
plt.xticks(fontsize=3.5)
#ratings = data.rating.dropna().apply(int).value_counts().sort_index().rename(lambda t: f'[{t}; {t+1})')
#ax = mpl.bar(ratings.index, ratings)

#10
import math
divide_dict={i:0 for i in range(10)}
labels_x=[f"[{i}-{i+1})" for i in range(10)]
for rate in data.rating:
    if rate > 0:
        divide_dict[math.floor(rate)] += 1
fig9, ax9 = plt.subplots()
ax9.bar(labels_x,divide_dict.values())

#11

genres_dict = dict()
themes_dict = dict()
genres = set()
themes = set()

for i in range(data.shape[0]):
  genres = genres.union(set(data.loc[i]['genre'].split(',')))
  themes = themes.union(set(data.loc[i]['theme'].split(',')))

popular_genre_dict = dict()
popular_theme_dict = dict()

not_popular_genre_dict = dict()
not_popular_theme_dict = dict()

popular_anime = data.loc[data.rating >= 8].reset_index(drop=True)
not_popular_anime = data.loc[data.rating < 5].reset_index(drop=True)

for i in range(popular_anime.shape[0]):
    for genre in set(popular_anime.loc[i]['genre'].split(',')):
        if genre not in popular_genre_dict:
            popular_genre_dict[genre] = 1
        else:
            popular_genre_dict[genre] = popular_genre_dict[genre] + 1
    for theme in set(popular_anime.loc[i]['theme'].split(',')):
        if theme not in popular_theme_dict:
            popular_theme_dict[theme] = 1
        else:
            popular_theme_dict[theme] = popular_theme_dict[theme] + 1

for i in range(not_popular_anime.shape[0]):
    for genre in set(not_popular_anime.loc[i]['genre'].split(',')):
        if genre not in not_popular_genre_dict:
            not_popular_genre_dict[genre] = 1
        else:
            not_popular_genre_dict[genre] = not_popular_genre_dict[genre] + 1
    for theme in set(not_popular_anime.loc[i]['theme'].split(',')):
        if theme not in not_popular_theme_dict:
            not_popular_theme_dict[theme] = 1
        else:
            not_popular_theme_dict[theme] = not_popular_theme_dict[theme] + 1


colors = dict()
for theme in themes:
  colors[theme] = (random.random(), random.random(), random.random())
#print(colors)

fig10, (ax10, ax10_1) = plt.subplots(1, 2, figsize=(40,20))
fig10.suptitle('зависимость рейтинга от темы аниме', fontsize=30)
ax10.pie(popular_theme_dict.values(), labels=popular_theme_dict.keys(),textprops={'fontsize': 5},autopct='%1.2f%%', colors=[colors[key] for key in popular_theme_dict.keys()])
ax10.set_title("популярные", fontsize=20)
ax10_1.pie(not_popular_theme_dict.values(), labels=not_popular_theme_dict.keys(),textprops={'fontsize': 5},autopct='%1.2f%%', colors=[colors[key] for key in not_popular_theme_dict.keys()])
ax10_1.set_title("непопулярные", fontsize=20)

for genre in genres:
  colors[genre] = (random.random(), random.random(), random.random())
print(colors)

fig11, (ax11, ax11_1) = plt.subplots(1, 2, figsize=(40,20))
fig11.suptitle('зависимость рейтинга от темы аниме', fontsize=30)
ax11.pie(popular_genre_dict.values(), labels=popular_genre_dict.keys(),textprops={'fontsize': 5},autopct='%1.2f%%', colors=[colors[key] for key in popular_genre_dict.keys()])
ax11.set_title("популярные", fontsize=20)
ax11_1.pie(not_popular_genre_dict.values(), labels=not_popular_genre_dict.keys(),textprops={'fontsize': 5},autopct='%1.2f%%', colors=[colors[key] for key in not_popular_genre_dict.keys()])
ax11_1.set_title("непопулярные", fontsize=20)

#12
voters_in_group = [0 for i in range(10)]
for i in range(data.shape[0]):
    anime_data = data.loc[i]
    if np.isnan(float(anime_data['rating'])) or np.isnan(int(anime_data['voters'])):
        continue
    voters_in_group[int(anime_data['rating'])] = voters_in_group[int(anime_data['rating'])] + int(anime_data['voters'])
fig12, ax12 = plt.subplots()
ax12.bar([f"[{i}-{i+1})" for i in range(10)], voters_in_group)
fig12.suptitle('зависимость рейтинга аниме от количество зрителей')

voters_in_group1 = dict()
for i in range(data.shape[0]):
    anime_data = data.loc[i]
    if np.isnan(float(anime_data['rating'])) or np.isnan(int(anime_data['voters'])):
        continue
    if round(anime_data['rating'], 1) not in voters_in_group1:
        voters_in_group1[round(anime_data['rating'], 1)] = int(anime_data['voters'])
    else:
        voters_in_group1[round(anime_data['rating'], 1)] = voters_in_group1[round(anime_data['rating'], 1)] + int(anime_data['voters'])

voters_in_group1 = dict(sorted(voters_in_group1.items()))
fig13, ax13 = plt.subplots()
ax13.plot(list(voters_in_group1.keys()),list(voters_in_group1.values()))
fig13.suptitle('линейный график зависимость рейтинга аниме от количество зрителей')

plt.show()