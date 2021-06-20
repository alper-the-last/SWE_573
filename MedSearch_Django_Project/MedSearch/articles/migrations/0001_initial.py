# Generated by Django 3.2.3 on 2021-06-19 18:14

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
                ('PMID', models.CharField(max_length=16)),
                ('ArticleTitle', models.TextField()),
                ('ArticleDate', models.DateField()),
                ('AuthorList', models.TextField()),
                ('AbstractText', models.TextField()),
                ('ArticleKeywords', models.TextField()),
                ('ArticleLang', models.CharField(max_length=250)),
            ],
        ),
    ]
