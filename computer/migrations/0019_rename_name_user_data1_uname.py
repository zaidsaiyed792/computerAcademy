# Generated by Django 4.1.9 on 2023-07-13 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0018_rename_user_data_user_data1_alter_user_details_bps_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_data1',
            old_name='name',
            new_name='uname',
        ),
    ]
