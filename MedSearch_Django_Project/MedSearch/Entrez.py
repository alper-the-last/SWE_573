import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MedSearch.settings')
from datetime import datetime
import django

django.setup()

from articles.models import Article
import pprint
from Bio import Entrez
from django.conf import settings


def getPMID(RAW_data, i):
    PMID = RAW_data["PubmedArticle"][i]["MedlineCitation"]["PMID"][0:8]
    return PMID


def getAuthorList(RAW_data, i):
    author_List = []
    try:
        authors_from_entrez = RAW_data["PubmedArticle"][i]["MedlineCitation"]["Article"]["AuthorList"]
        for author in range(len(authors_from_entrez)):
            firstname = authors_from_entrez[author].get("ForeName")
            if firstname == None:
                firstname = ""
            lastname = authors_from_entrez[author].get("LastName")
            if lastname == None:
                lastname = ""
            full_name_of_author = firstname + " " + lastname
            author_List.append(full_name_of_author)
    except:
        author_List = ["N/A"]

    for author in author_List:
        formatted_author_list = ", ".join(author_List)

    return formatted_author_list


def getArticleTitle(RAW_data, i):
    title = RAW_data["PubmedArticle"][i]["MedlineCitation"]["Article"]["ArticleTitle"]
    return title


def getArticleDate(RAW_data, i):
    formatted_date = ""
    articleDate = RAW_data["PubmedArticle"][i]["MedlineCitation"]["Article"]["ArticleDate"]
    try:
        day = articleDate[0].get("Day")
        month = articleDate[0].get("Month")
        year = articleDate[0].get("Year")
        date = list(RAW_data["PubmedArticle"][i]["MedlineCitation"]["Article"]["ArticleDate"][0].values())
        formatted_date = year + "-" + month + "-" + day
        # formatted_date = datetime.strptime(formatted_date, "%Y %m %d")
    except:
        articleDate = RAW_data["PubmedArticle"][i]["MedlineCitation"]["DateRevised"]
        day = articleDate.get("Day")
        month = articleDate.get("Month")
        year = articleDate.get("Year")
        formatted_date = year + "-" + month + "-" + day
    return formatted_date


def getAbstractText(RAW_data, i):
    absText = RAW_data["PubmedArticle"][i]["MedlineCitation"]["Article"]["Abstract"]["AbstractText"]
    lines = ""
    for lin in range(len(absText)):
        line = RAW_data["PubmedArticle"][i]["MedlineCitation"]["Article"]["Abstract"]["AbstractText"][lin]
        lines = lines + line
    return lines


def getArticleKeywords(RAW_data, i):
    pubmed_keywords = RAW_data["PubmedArticle"][i]["MedlineCitation"]["KeywordList"]
    keywords = []

    if len(pubmed_keywords) != 0:
        pubmed_keywords = pubmed_keywords[0]
        for keyW in range(len(pubmed_keywords)):

            keyword = pubmed_keywords[keyW]
            keywords.append(keyword[:])

            for keyword in keywords:
                formatted_keywords = ", ".join(keywords)
    else:
        formatted_keywords = "N/A"

    return formatted_keywords


def getArticleLang(RAW_data, i):
    lang = RAW_data["PubmedArticle"][i]["MedlineCitation"]["Article"]["Language"][0]
    return lang


Entrez.email = "alper.pazarlioglu@boun.edu.tr"


def entrez_esearch(batch):
    if batch == 1:
        range = 0
    else:
        range = batch * 1000
    handle = Entrez.esearch(db="pubmed", retstart=range, retmax=1000, term="reflux", idtype="acc")
    records = Entrez.read(handle)
    handle.close()

    article_list = records["IdList"]
    print(len(article_list))

    PMID = ", ".join(article_list)

    return PMID


def entrez_efetch(PMID):
    handle = Entrez.efetch(db="pubmed", id=PMID, rettype="abstract", retmode="xml")
    records = Entrez.read(handle)
    handle.close()
    print("length:", len(records.get("PubmedArticle")))
    # pprint.pprint(records)
    return records


def save_to_db(x):
    for i in range(1, x, 1):
        print("batch", i)
        PMID = entrez_esearch(i)
        articles_data = entrez_efetch(PMID)

        for j in range(len(articles_data.get("PubmedArticle"))):
            if "Abstract" in articles_data["PubmedArticle"][j]["MedlineCitation"]["Article"]:
                # print(getPMID(articles_data,j))
                all_article = Article(
                PMID=getPMID(articles_data,j),
                ArticleTitle=getArticleTitle(articles_data,j),
                ArticleDate=getArticleDate(articles_data,j),
                AuthorList=getAuthorList(articles_data,j),
                AbstractText=getAbstractText(articles_data,j),
                ArticleKeywords=getArticleKeywords(articles_data,j),
                )

                all_article.save()


save_to_db(50)
