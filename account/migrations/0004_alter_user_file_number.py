# Generated by Django 4.1.7 on 2023-03-10 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='file_number',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True),
        ),
    ]
