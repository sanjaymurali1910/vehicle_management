# Generated by Django 4.0.2 on 2022-10-21 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitnessproapp', '0007_delete_offlinetraining_delete_onlinetraining_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_registration',
            name='status',
            field=models.CharField(default='user', max_length=240, null=True),
        ),
    ]