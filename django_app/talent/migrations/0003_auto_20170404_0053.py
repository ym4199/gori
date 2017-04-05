# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 15:53
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0002_auto_20170403_2131'),
        ('talent', '0002_auto_20170404_0053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('curriculum_rate', models.IntegerField(default=1, help_text='5이하의 숫자를 입력하세요',
                                                        validators=[django.core.validators.MaxValueValidator(5),
                                                                    django.core.validators.MinValueValidator(1)])),
                ('readiness_rate', models.IntegerField(default=1, help_text='5이하의 숫자를 입력하세요',
                                                       validators=[django.core.validators.MaxValueValidator(5),
                                                                   django.core.validators.MinValueValidator(1)])),
                ('timeliness_rate', models.IntegerField(default=1, help_text='5이하의 숫자를 입력하세요',
                                                        validators=[django.core.validators.MaxValueValidator(5),
                                                                    django.core.validators.MinValueValidator(1)])),
                ('delivery_rate', models.IntegerField(default=1, help_text='5이하의 숫자를 입력하세요',
                                                      validators=[django.core.validators.MaxValueValidator(5),
                                                                  django.core.validators.MinValueValidator(1)])),
                ('friendliness_rate', models.IntegerField(default=1, help_text='5이하의 숫자를 입력하세요',
                                                          validators=[django.core.validators.MaxValueValidator(5),
                                                                      django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]