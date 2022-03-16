class Sources:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,name,description, url, category, language, country):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language =  language
        self.country = country

class Articles:

     def __init__(self,author,title,description, url, url_to_image, publishes_at,content):
        self.author = author
        self.news_title = title
        self.overview = description
        self.article_url = url
        self.image = url_to_image
        self.publishes_at = publishes_at
        self.content = content
        
