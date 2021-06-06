# Generated by Django 3.2.3 on 2021-06-02 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PMID', models.TextField(max_length=10)),
                ('ArticleTitle', models.TextField(max_length=250)),
                ('ArticleDate', models.DateField()),
                ('AuthorList', models.TextField(max_length=250)),
                ('AbstractText', models.TextField(max_length=250)),
                ('ArticleKeywords', models.TextField(max_length=250)),
                ('ArticleLang', models.TextField(max_length=250)),
            ],
        ),
    ]