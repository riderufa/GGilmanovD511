# Generated by Django 2.2.6 on 2019-12-17 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0003_auto_20191208_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField()),
            ],
        ),
    ]