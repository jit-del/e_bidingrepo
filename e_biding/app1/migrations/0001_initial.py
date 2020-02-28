# Generated by Django 2.2.4 on 2019-12-12 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('pasw', models.CharField(max_length=50)),
                ('contact', models.IntegerField(unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(max_length=10)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='acc_image/')),
            ],
        ),
    ]
