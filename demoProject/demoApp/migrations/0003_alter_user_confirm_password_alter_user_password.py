# Generated by Django 4.0 on 2022-01-11 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoApp', '0002_alter_user_confirm_password_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirm_password',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
