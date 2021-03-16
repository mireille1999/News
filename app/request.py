import urllib.request,json
from .models import Source,Article

# Getting api key
api_key = None
# Getting the movie base url
sources_url = None
# Getting the article url
articles_url = None

def configure_request(app):
    global api_key , sources_url , articles_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['SOURCE_API_BASE_URL']
    articles_url = app.config["ARTICLE_API_NEWS_URL"]



def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = sources_url.format(category,api_key)
    
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)

    return sources_results

def process_sources(sources_list):
    '''
    Function  that processes the source result and transform them to a list of Objects
    Args:
        sources_list: A list of dictionaries that contain source details
    Returns :
        sources_results: A list of source objects
    '''
    sources_results = []

    for item in sources_list:
        id = item.get('id')
        name = item.get('name')
        category = item.get('category')
        description = item.get('description')
        url = item.get('url')
        language = item.get('language')

        if id:
            sources_object = Source(id,name,category,description,url,language)
            sources_results.append(sources_object)

    return sources_results


def get_articles(id):
    '''
    function to return a list
    '''
    get_articles_url=articles_url.format(id,api_key)
    with urllib.request.urlopen(get_articles_url)as url:
        articles_results=json.loads(url.read())
        articles_object=None
        if articles_results['articles']:
            articles_object=process_articles(articles_results['articles'])

    return articles_object

def process_articles(articles_list):
    '''
    function to list all articles
    '''
    articles_object=[]
    for item in articles_list:
        urlToImage = item.get('urlToImage')
        title= item.get('title')
        description = item.get('description')
        url = item.get('url')
        publishedAt = item.get('publishedAt')

        if urlToImage:
            
           articles_result=Article(urlToImage,title,description,url,publishedAt)
           articles_object.append(articles_result)

    return articles_object
