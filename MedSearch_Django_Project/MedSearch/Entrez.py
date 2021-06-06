from Bio import Entrez
# import pprint
import csv

def getPMID(RAW_data):
  PMID=RAW_data["PubmedArticle"][i]["MedlineCitation"]["PMID"][0:8]
  return PMID

def getAuthorList(RAW_data):
  author_List = []
  if "AuthorList" in RAW_data["PubmedArticle"][i]["MedlineCitation"]["Article"]:
    # print(RAW_data["PubmedArticle"][i]["MedlineCitation"]["Article"]["AuthorList"])
    for author in range(len(RAW_data["PubmedArticle"][i]["MedlineCitation"]["Article"]["AuthorList"])):
      firstname=RAW_data["PubmedArticle"][i]["MedlineCitation"]["Article"]["AuthorList"][author].get("ForeName")
      # print(firstname)
      if firstname == None:
        firstname = ""
      lastname = RAW_data["PubmedArticle"][i]["MedlineCitation"]["Article"]["AuthorList"][author].get("LastName")
      if lastname == None:
        lastname = ""
      author = firstname+"/"+lastname
      author_List.append(author)
  print(author_List)
  return author_List

def getArticleTitle(RAW_data):
  title = RAW_data["PubmedArticle"][i]["MedlineCitation"]["Article"]["ArticleTitle"]
  return title

def getArticleDate(RAW_data):
  if RAW_data["PubmedArticle"][i]["MedlineCitation"]["Article"]["ArticleDate"] != []:
    date=list(RAW_data["PubmedArticle"][i]["MedlineCitation"]["Article"]["ArticleDate"][0].values())
    return date

def getAbstractText(RAW_data):
  absText = RAW_data["PubmedArticle"][i]["MedlineCitation"]["Article"]["Abstract"]["AbstractText"]
  lines =""
  for lin in range(len(absText)):
    line = RAW_data["PubmedArticle"][i]["MedlineCitation"]["Article"]["Abstract"]["AbstractText"][lin]
    lines = lines+line
  return lines

def getArticleKeywords(RAW_data):
  pubmed_keywords=RAW_data["PubmedArticle"][i]["MedlineCitation"]["KeywordList"]
  keywords = []

  if len(pubmed_keywords) !=0:
    pubmed_keywords=pubmed_keywords[0]
    for keyW in range(len(pubmed_keywords)):
      keyword=pubmed_keywords[keyW]
      keywords.append(keyword[:])
  return keywords

def getArticleLang(RAW_data):
  lang= RAW_data["PubmedArticle"][i]["MedlineCitation"]["Article"]["Language"][0]
  return lang


# csv_file = open('C:\\Users\\HP\\Desktop\\BoğaziçiSWE\\SWE_573_Software Development Practice\\PyCharm Projects\\EntrezTest\\csv_file.csv','w',encoding='utf-8')
# writer = csv.writer(csv_file)

def entrez_search():

  Entrez.email = "alper.pazarlioglu@boun.edu.tr"
################################################################################################
  handle = Entrez.esearch(db="pubmed", retmax=14, term="reflux", idtype="acc")
# handle = Entrez.esearch(db="pubmed", retstart=10000, retmax=50000, term="reflux", idtype="acc")
  record = Entrez.read(handle)
  handle.close()
  return record


article_list = entrez_search()["IdList"]
print(len(article_list))
# for article in article_list:
#   print(article)
PMID=", ".join(article_list)

################################################################################################
handle2 = Entrez.efetch(db="pubmed", id=PMID, rettype="abstract", retmode="xml")
# handle2 = Entrez.efetch(db="pubmed", id=PMID, rettype="abstract", retmode="xml", retstart=10000)
record2 = Entrez.read(handle2)
handle2.close()
print("length:", len(record2.get("PubmedArticle")))
# pprint.pprint(record2)


for i in range(len(record2.get("PubmedArticle"))):
  if "Abstract" in record2["PubmedArticle"][i]["MedlineCitation"]["Article"]:
      print(getPMID(record2))