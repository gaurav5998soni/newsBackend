# Generated by Django 2.2.11 on 2020-05-31 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20200531_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='my_iamge/')),
                ('image_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
