# Generated by Django 2.2 on 2019-10-13 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0025_objectchange_time_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='webhook',
            name='ca_file_path',
            field=models.CharField(blank=True, max_length=4096, null=True),
        ),
    ]