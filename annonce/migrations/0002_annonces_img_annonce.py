# Generated by Django 3.2.8 on 2022-01-06 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonces',
            name='img_annonce',
            field=models.ImageField(default='img', upload_to='media/annonces'),
        ),
    ]