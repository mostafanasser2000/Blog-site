# Generated by Django 4.1.7 on 2023-05-02 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_options_post_dislikes_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='categories', to='blog.category'),
        ),
    ]
