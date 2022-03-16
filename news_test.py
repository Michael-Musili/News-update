import unittest # Importing the unittest module
from app.models import Sources
from app.models import Articles

class TestSources(unittest.TestCase):

    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_sources = Sources("James","Muriuki","0712345678","james@ms.com") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_sources.id,"")
        self.assertEqual(self.new_sources.name,"")
        self.assertEqual(self.new_sources.description,"")
        self.assertEqual(self.new_sources.url,"")
        self.assertEqual(self.new_sources.category,"")
        self.assertEqual(self.new_sources.language,"")


if __name__ == '__main__':
    unittest.main()





class TestArticles(unittest.TestCase):

    # Items up here .......

    def setUp(self):
    
      
        self.new_articles = Articles("James","Muriuki","0712345678","james@ms.com") # create contact object


    def test_init(self):
        

        self.assertEqual(self.new_articles.author,"")
        self.assertEqual(self.new_articles.title,"")
        self.assertEqual(self.new_articles.description,"0")
        self.assertEqual(self.new_articles.url,"")
        self.assertEqual(self.new_articles.url_to_image,"")
        self.assertEqual(self.new_articles.publishes_at,"")
        self.assertEqual(self.new_articles.content,"")


if __name__ == '__main__':
    unittest.main()