from bs4 import BeautifulSoup
import requests

respone = requests.get(url="https://news.ycombinator.com/news")

yc_web_page = respone.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_titles = []
article_links = []
for article_tag in soup.find_all(name="span", class_="titleline"):
    article_titles.append(article_tag.getText())
    article_links.append(article_tag.find("a")["href"])

article_upvotes = []
for article in soup.find_all(name="td", class_="subtext"):
    if article.span.find(class_="score") is None:
        article_upvotes.append(0)
    else:
        article_upvotes.append(int(article.span.find(class_="score").contents[0].split()[0]))

max_points_index = article_upvotes.index(max(article_upvotes))
print(
    f"{article_titles[max_points_index]}, "
    f"{article_upvotes[max_points_index]} points, "
    f"available at: {article_links[max_points_index]}."
)







































# with open("./website.html", encoding="utf8") as file:
#     content = file.read()
    
# soup = BeautifulSoup(content,"html.parser")
# # print(soup.title)
# # print(soup.title.string)
# # print(soup)
# # print(soup.prettify())
# # all_anchor_tags = soup.find_all(name="a")
# # for tags in all_anchor_tags:
# #     print(tags.get("href"))
# # heading = soup.find(name="h1", id="name")
# # print(heading)
# # section_heading = soup.find(class_="heading",name="h3")
# # print(section_heading.get("class"))

# # company_url = soup.select_one(selector="p a")
# # print(company_url)

# name = soup.select_one(selector="#name")
# print(name)

# heading = soup.select_one(selector=".heading")
# print(heading)