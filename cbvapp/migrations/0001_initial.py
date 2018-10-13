# Generated by Django 2.1.1 on 2018-10-11 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('principal_name', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=200)),
                ('contact_no', models.PositiveIntegerField()),
            ],
        ),
    ]
