# Generated by Django 4.1.3 on 2022-11-27 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Contact', models.BigIntegerField()),
                ('Lostdate', models.DateField()),
                ('Lastseen', models.CharField(max_length=50)),
                ('Description', models.CharField(default='some string', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Contact', models.BigIntegerField()),
                ('Course', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
