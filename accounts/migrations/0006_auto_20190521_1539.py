# Generated by Django 2.1.2 on 2019-05-21 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190521_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.ManyToManyField(blank=True, to='request_form_app.Company'),
        ),
    ]