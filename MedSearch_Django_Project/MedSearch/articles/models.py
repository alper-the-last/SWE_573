from django.db import models

# Create your models here.
class Article(models.Model):
    PMID=models.TextField(max_length=10)
    ArticleTitle=models.TextField(max_length=250)
    ArticleDate=models.DateField()
    AuthorList=models.TextField(max_length=250)
    AbstractText=models.TextField(max_length=250)
    ArticleKeywords=models.TextField(max_length=250)
    ArticleLang=models.TextField(max_length=250)