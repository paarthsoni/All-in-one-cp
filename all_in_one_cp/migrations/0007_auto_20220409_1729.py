# Generated by Django 3.2.5 on 2022-04-09 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_in_one_cp', '0006_user_details_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform_details',
            name='Atcoder_username',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='platform_details',
            name='Codeforces_username',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='platform_details',
            name='Interviewbit_username',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='platform_details',
            name='Leetcode_username',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='platform_details',
            name='SPOJ_username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]