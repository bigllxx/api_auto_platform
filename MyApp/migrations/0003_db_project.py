# Generated by Django 3.1 on 2020-08-28 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_db_home_href'),
    ]

    operations = [
        migrations.CreateModel(
            name='DB_project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='项目名称')),
                ('remark', models.CharField(max_length=1000, null=True, verbose_name='项目备注')),
                ('user', models.CharField(max_length=15, null=True, verbose_name='项目创建者名称')),
                ('other_user', models.CharField(max_length=15, null=True, verbose_name='其他创建者')),
            ],
            options={
                'verbose_name': '项目信息',
                'verbose_name_plural': '项目信息',
            },
        ),
    ]
