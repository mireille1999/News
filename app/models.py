class Article:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,urlToImage,title,description,url,publishedAt):
        self.urlToImage = urlToImage
        self.title = title
        self.description = description
        self.url = url
        self.publishedAt = publishedAt


class Source:

    

    def __init__(self,id,name,category,description,url,language):
        self.id =id
        self.name = name
        self.category = category
        self.description = description
        self.url = url
        self.language = language
