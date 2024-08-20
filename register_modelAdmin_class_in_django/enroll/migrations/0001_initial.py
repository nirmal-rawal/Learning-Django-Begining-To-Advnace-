# Generated by Django 5.0.7 on 2024-08-20 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField()),
                ('stuname', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=70)),
            ],
        ),
    ]
