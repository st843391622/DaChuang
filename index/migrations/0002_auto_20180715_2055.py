# Generated by Django 2.0.4 on 2018-07-15 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='cid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='report',
            name='rid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]