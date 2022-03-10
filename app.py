from flask import Flask,render_template
from newsapi import NewsApiClient

app = Flask(__name__)


@app.route('/')
def index():
    newsapi = NewsApiClient(api_key="83f8de393be94ef8ad50bd4517fb123f")
    top_headlines = newsapi.get_top_headlines(sources='bbc-news')

    articles = top_headlines['articles']

    # list of content

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles= articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render_template('index.html',context=mylist)


if __name__ == "__main__":
    app.run(debug=True)
