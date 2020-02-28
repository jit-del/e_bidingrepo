# Generated by Django 2.2.4 on 2019-12-18 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maxamout',
            fields=[
                ('maid', models.AutoField(primary_key=True, serialize=False)),
                ('maxamount', models.FloatField()),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Product')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.User')),
            ],
        ),
        migrations.CreateModel(
            name='Biding',
            fields=[
                ('bidid', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Product')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.User')),
            ],
        ),
    ]