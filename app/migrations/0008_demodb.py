# Generated by Django 4.0.1 on 2022-02-28 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='demodb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('eamil', models.CharField(max_length=255)),
            ],
        ),
    ]