import urllib.request,json
from .models import Sources
from .models import Articles

# Getting api key
api_key = None
# Getting the movie base url
base_url = None
articles_base_url = None

def configure_request(app):
    global api_key ,base_url, articles_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['SOURCES_API_BASE_URL']
    articles_base_url = app.config['ARTICLES_API_BASE_URL']

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(api_key)
    print(get_sources_url)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)


    return sources_results


...
def process_results(sources_list):
 
  
    sources_results = []
    for sources_item in sources_list:
        id= sources_item.get('id')
        name= sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get ('category')
        language = sources_item.get ('language')
        country = sources_item.get('country')
      
       
        sources_object = Sources(id,name, description, url,category,language, country)
        sources_results.append(sources_object)

    return sources_results





def get_articles(source_id):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = articles_base_url.format(source_id,api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        get_articles_data = url.read()
        get_sources_response = json.loads(get_articles_data)

        articles_results = None

        if get_sources_response['articles']:
            articles_results_list = get_sources_response['articles']
            articles_results = process_articles_results(articles_results_list)


    return articles_results

...
def process_articles_results(news_list):

    articles_results = []
    for articles_item in news_list:
        author= articles_item.get('author')
        title=articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        url_to_image = articles_item.get('urlToImage')
        publishes_at = articles_item.get ('publishes_at')
        content = articles_item.get ('content')
       
      
       
        articles_object = Articles(author,title, description, url,url_to_image, publishes_at,content)
        articles_results.append(articles_object)

    return articles_results
