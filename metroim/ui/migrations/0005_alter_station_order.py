# Generated by Django 3.2.9 on 2021-11-15 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0004_remove_line_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='order',
            field=models.PositiveSmallIntegerField(verbose_name='Порядок'),
        ),
    ]
