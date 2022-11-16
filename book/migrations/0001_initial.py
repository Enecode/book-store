# Generated by Django 4.1.3 on 2022-11-16 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('isbn', models.CharField(max_length=120)),
                ('date_published', models.DateField()),
                ('date_added', models.DateField(auto_now=True)),
                ('edition', models.PositiveSmallIntegerField()),
                ('genre', models.CharField(choices=[('C', 'Comedy'), ('T', 'Tragedy'), ('TC', 'Tragicomedy'), ('CR', 'Crime'), ('R', 'Romance'), ('SF', 'Science Fiction')], default='R', max_length=2)),
            ],
        ),
    ]