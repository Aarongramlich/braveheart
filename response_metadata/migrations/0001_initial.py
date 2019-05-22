# Generated by Django 2.1.2 on 2019-05-22 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('request_form_app', '0005_auto_20190522_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.TextField(max_length=255)),
                ('label', models.TextField(max_length=255)),
                ('field_type', models.TextField(blank=True, max_length=255)),
                ('consumer_label', models.TextField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('consumer_description', models.TextField(blank=True, max_length=255)),
                ('data_category', models.TextField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request_form_app.Company')),
            ],
        ),
    ]
