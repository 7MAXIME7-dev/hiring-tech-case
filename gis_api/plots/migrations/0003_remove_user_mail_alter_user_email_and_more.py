# Generated by Django 4.2.3 on 2023-07-05 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plots', '0002_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mail',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
