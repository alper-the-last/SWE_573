from django.test import *
from django.contrib.auth import get_user_model
from .models import *

# Create your tests here.

class urlTests(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def Results(self):
        response = self.client.get('results/')
        self.assertEqual(response.status_code, 200)


class modelTests(TestCase):
    def test_articlemodel(self):
        article = Article.objects.create(PMID="34130097",ArticleTitle="MOAT",ArticleDate="2021-06-30",AuthorList="James Joyce",AbstractText="synesthesia",ArticleKeywords="N/A")

        self.assertEqual(article.PMID, "34130097")
        self.assertEqual(article.ArticleTitle, "MOAT")
        self.assertEqual(article.ArticleDate, "2021-06-30")
        self.assertEqual(article.AuthorList, "James Joyce")
        self.assertEqual(article.AbstractText, "synesthesia")
        self.assertEqual(article.ArticleKeywords, "N/A")


User = get_user_model()

class userTests(TestCase):

    def setUpUser(self):
        user1=User(username='alper', email='alper001@gmail.com', )
        user1.set_password('donkeykong1')
        user1.save()

    def testLogin(self):
        user1= {"username": "alper", "password": "donkeykong1"}
        response=self.client.post('login/', user1, follow=True)
