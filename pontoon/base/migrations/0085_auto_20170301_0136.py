# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0084_auto_20170228_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locale',
            name='direction',
            field=models.CharField(choices=[(b'ltr', b'left-to-right'), (b'rtl', b'right-to-left')], default=b'ltr', help_text=b'\n        Writing direction. Set to "right-to-left" if "rtl" value for the locale\n        script is set to "YES" in\n        <a href="https://github.com/unicode-cldr/cldr-core/blob/master/scriptMetadata.json">CLDR scriptMetadata.json</a>.\n        ', max_length=3),
        ),
        migrations.AlterField(
            model_name='locale',
            name='population',
            field=models.PositiveIntegerField(default=0, help_text=b'\n        Number of native speakers. Find locale code in\n        <a href="https://github.com/unicode-cldr/cldr-core/blob/master/supplemental/territoryInfo.json">CLDR territoryInfo.json</a>\n        and multiply its "_populationPercent" with the territory "_population".\n        Repeat if multiple occurrences of locale code exist and sum products.\n        '),
        ),
        migrations.AlterField(
            model_name='locale',
            name='script',
            field=models.CharField(default=b'Latin', help_text=b'\n        Script locale is written in. Find it in\n        <a href="https://github.com/unicode-cldr/cldr-core/blob/master/supplemental/languageData.json">CLDR languageData.json</a>.\n        ', max_length=128),
        ),
    ]