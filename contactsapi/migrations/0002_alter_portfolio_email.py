# Generated by Django 4.2.2 on 2023-06-09 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactsapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
