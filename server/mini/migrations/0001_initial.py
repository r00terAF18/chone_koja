# Generated by Django 3.2.9 on 2021-12-04 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UID', models.PositiveSmallIntegerField(default=0, verbose_name='Original ID from website')),
                ('title', models.CharField(max_length=300, verbose_name='Title of Room')),
                ('price_per_night', models.CharField(max_length=25, verbose_name='Price Per Night(min)')),
                ('rating', models.CharField(max_length=5, verbose_name='Star Rating')),
                ('link_to_site', models.CharField(max_length=500, verbose_name='Link to original Website')),
                ('state', models.CharField(db_index=True, max_length=155, null=True, verbose_name='State')),
                ('city', models.CharField(db_index=True, max_length=155, null=True, verbose_name='City')),
            ],
        ),
    ]
