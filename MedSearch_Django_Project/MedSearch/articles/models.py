from django.db import models


# Create your models here.
class Article(models.Model):
    PMID = models.CharField(max_length=16)
    ArticleTitle = models.TextField()
    ArticleDate = models.DateField()
    AuthorList = models.TextField()
    AbstractText = models.TextField()
    ArticleKeywords = models.TextField()
    ArticleLang = models.CharField(max_length=250)
