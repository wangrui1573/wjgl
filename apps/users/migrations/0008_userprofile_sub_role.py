# Generated by Django 2.2.3 on 2019-11-04 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20191025_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='sub_role',
            field=models.CharField(blank=True, choices=[('2', '二审'), ('1', '初审'), ('0', '')], default='0', max_length=1, verbose_name='子角色'),
        ),
    ]
