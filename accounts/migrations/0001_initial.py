# Generated by Django 3.0.5 on 2020-09-15 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=70)),
                ('password', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
