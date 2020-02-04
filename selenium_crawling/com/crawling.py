from libs.crawler import crawl

url = "https://www.instagram.com/explore/tags/%EC%97%AC%ED%96%89/"

pageString = crawl(url)
print(pageString)