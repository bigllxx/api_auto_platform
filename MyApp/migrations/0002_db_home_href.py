# Generated by Django 3.1 on 2020-08-27 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DB_home_href',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('href', models.CharField(max_length=2000, null=True)),
            ],
            options={
                'verbose_name': '首页传送门',
                'verbose_name_plural': '首页传送门',
            },
        ),
    ]