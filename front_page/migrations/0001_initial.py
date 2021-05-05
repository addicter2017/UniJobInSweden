# Generated by Django 3.0.5 on 2021-04-28 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('UNIname', models.CharField(max_length=128, verbose_name='UNIname')),
                ('title', models.CharField(max_length=128, verbose_name='title')),
                ('address_time', models.CharField(max_length=128, verbose_name='address_time')),
                ('link', models.CharField(max_length=128, verbose_name='link')),
                ('application_deadline', models.CharField(max_length=128, verbose_name='application_deadline')),
            ],
            options={
                'verbose_name': 'University',
                'verbose_name_plural': 'University',
            },
        ),
    ]
