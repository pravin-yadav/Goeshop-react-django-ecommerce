# Generated by Django 3.0.7 on 2020-09-06 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='full_name',
            new_name='name',
        ),
    ]
