# Generated by Django 3.2.9 on 2022-03-02 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_auto_20220131_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_me',
            field=models.TextField(null=True),
        ),
    ]
