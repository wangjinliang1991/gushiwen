import re
import requests

def parse_page(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/69.0.3497.100 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    text = response.text
    titles = re.findall(r'<div\sclass="cont".*?<b>(.*?)</b>',text,re.S)
    dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>',text,re.S)
    authors = re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>',text,re.S)
    content_tags = re.findall(r'<div class="contson".*?>(.*?)</div>',text,re.S)
    contents = []
    for content in content_tags:
        x = re.sub(r'<.*?>','',content)
        contents.append(x.strip())

    poems = []
    for value in zip(titles,dynasties,authors,contents):
        title,dynasty,author,content = value
        poem = {
            'title':title,
            'dynasty':dynasty,
            'author':author,
            'content': content
        }
        poems.append(poem)

    for poem in poems:
        print(poem)
        print("="*40)




def main():
    # url = 'https://www.gushiwen.org/default_1.aspx'
    # parse_page(url)
    for x in range(1,11):
        url = 'https://www.gushiwen.org/default_%s.aspx'%x
        parse_page(url)


if __name__ == '__main__':
    main()