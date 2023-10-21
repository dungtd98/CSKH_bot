# Generated by Django 4.2 on 2023-04-07 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botmodel',
            name='botMessage_backgroundColor',
            field=models.CharField(default='#edf2f7', max_length=20),
        ),
        migrations.AlterField(
            model_name='botmodel',
            name='botMessage_color',
            field=models.CharField(default='#000000', max_length=20),
        ),
        migrations.AlterField(
            model_name='botmodel',
            name='boxChat_backgroundColor',
            field=models.CharField(default='#000000', max_length=20),
        ),
        migrations.AlterField(
            model_name='botmodel',
            name='isMessage',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='botmodel',
            name='system_message',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='botmodel',
            name='userMessage_backgroundColor',
            field=models.CharField(default='#1a94da', max_length=20),
        ),
        migrations.AlterField(
            model_name='botmodel',
            name='userMessage_color',
            field=models.CharField(default='#fff', max_length=20),
        ),
    ]