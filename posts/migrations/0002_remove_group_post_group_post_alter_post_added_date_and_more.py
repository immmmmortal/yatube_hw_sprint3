# Generated by Django 4.0.4 on 2022-06-07 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='post',
        ),
        migrations.AddField(
            model_name='group',
            name='post',
            field=models.ManyToManyField(to='posts.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='added_date',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='edited_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
