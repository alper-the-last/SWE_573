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

class Tags(models.Model):
    MedSearchTagName = models.TextField()
    PMID = models.CharField(max_length=16)
    WikiID = models.TextField()
    WikiLabel = models.TextField()
    WikiTitle = models.TextField()
    WikiURL = models.TextField()
    WikiDescription = models.TextField()

    def __str__(self):
        return self.MedSearchTagName