from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com/")
yc_news=response.text

soup=BeautifulSoup(yc_news,"html.parser")

articles=soup.find_all(name="a", class_="titlelink")
article_texts=[]
article_links=[]
for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.get("href"))

print(article_texts)
print(article_links)

up_vote_tags=soup.find_all(name="span",class_="score")
up_vote_points=[int(up_vote_tag.getText().split(" ")[0]) for up_vote_tag in up_vote_tags]
print(up_vote_points)

largest_num=max(up_vote_points)
largest_index=up_vote_points.index(largest_num)
print(article_texts[largest_index])




# import lxml
# with open("website.html",encoding="utf8") as file:
#     contents=file.read()
#
# soup=BeautifulSoup(contents,"html.parser")
# # print(soup.title)
# # print(soup)
# # print(soup.title.name)
#
# # print(soup.title.string)
# # print(soup.prettify())
# all_anchor_tags=soup.find_all(name="a")
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
# heading=soup.find(name="h1",id="name")
# print(heading)
# section_heading=soup.find(name="h3",class_="heading")
# print(section_heading)
#
# class_is_heading=soup.find_all(class_="heading")
# h3_heading=soup.find_all(class_="heading")
# company_url=soup.select_one("p a")
