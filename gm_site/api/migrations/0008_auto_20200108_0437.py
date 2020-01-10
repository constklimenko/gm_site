# Generated by Django 3.0.2 on 2020-01-08 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200107_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='for_main',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='artists',
            field=models.ManyToManyField(blank=True, to='api.Artist'),
        ),
        migrations.AlterField(
            model_name='article',
            name='events',
            field=models.ManyToManyField(blank=True, to='api.Event'),
        ),
        migrations.AlterField(
            model_name='article',
            name='paintings',
            field=models.ManyToManyField(blank=True, to='api.Painting'),
        ),
        migrations.AlterField(
            model_name='article',
            name='places',
            field=models.ManyToManyField(blank=True, to='api.Place'),
        ),
        migrations.AlterField(
            model_name='event',
            name='artists',
            field=models.ManyToManyField(blank=True, to='api.Artist'),
        ),
        migrations.AlterField(
            model_name='event',
            name='paintings',
            field=models.ManyToManyField(blank=True, to='api.Painting'),
        ),
        migrations.AlterField(
            model_name='painting',
            name='genres',
            field=models.ManyToManyField(blank=True, to='api.Genre'),
        ),
    ]