# Generated by Django 2.2.12 on 2021-06-30 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0009_auto_20210630_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExCollect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ex_video_id', models.CharField(max_length=11)),
                ('ex_json_dual', models.TextField(blank=True, default='n')),
                ('ex_rate', models.IntegerField(default=1)),
                ('ex_video_title', models.TextField(blank=True, default='n')),
            ],
        ),
        migrations.DeleteModel(
            name='Example',
        ),
    ]
