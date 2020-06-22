# Generated by Django 2.2.5 on 2020-06-19 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.TextField(default='')),
                ('start_date', models.TextField(default='')),
                ('buy_price', models.TextField(default='')),
                ('over_date', models.TextField(default='')),
                ('sell_price', models.TextField(default='')),
                ('return_value', models.TextField(default='')),
            ],
            options={
                'db_table': 'history',
            },
        ),
        migrations.CreateModel(
            name='now_chose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_update', models.TextField(default='')),
                ('stock_name', models.TextField(default='')),
                ('start_date', models.TextField(default='')),
                ('start_price', models.TextField(default='')),
                ('over_date', models.TextField(default='')),
                ('current_price', models.TextField(default='')),
                ('now_return', models.TextField(default='')),
            ],
            options={
                'db_table': 'now_chose',
            },
        ),
        migrations.CreateModel(
            name='strategy_robot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monthly_return', models.TextField(default='')),
                ('monthly_0050_return', models.TextField(default='')),
                ('season_return', models.TextField(default='')),
                ('season_0050_return', models.TextField(default='')),
                ('yea_return', models.TextField(default='')),
                ('year_0050_return', models.TextField(default='')),
                ('fundamental_return', models.TextField(default='')),
                ('fundamental_amplitude', models.TextField(default='')),
                ('technology_return', models.TextField(default='')),
                ('technology_amplitude', models.TextField(default='')),
            ],
            options={
                'db_table': 'strategy_robot',
            },
        ),
    ]