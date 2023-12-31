# Generated by Django 4.1.3 on 2023-12-04 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_alter_blogmodel_accuracy'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='general', max_length=10),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='accuracy',
            field=models.TextField(default='true'),
        ),
    ]
