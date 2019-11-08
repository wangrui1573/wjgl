# Generated by Django 2.2.3 on 2019-11-05 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_userprofile_sub_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='sub_role',
            field=models.CharField(blank=True, choices=[('2', '二审员'), ('1', '初审员'), ('0', '')], default='0', max_length=1, verbose_name='子角色'),
        ),
    ]
