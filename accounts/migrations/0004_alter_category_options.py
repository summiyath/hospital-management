# Generated by Django 3.2.9 on 2022-06-13 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220613_1803'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Catagory', 'verbose_name_plural': 'Catagories'},
        ),
    ]