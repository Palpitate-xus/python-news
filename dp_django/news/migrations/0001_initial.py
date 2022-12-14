# Generated by Django 3.2.9 on 2021-12-03 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('timeStamp', models.IntegerField()),
                ('content', models.TextField()),
                ('splitWords', models.TextField()),
            ],
            options={
                'db_table': 'news',
            },
        ),
    ]
