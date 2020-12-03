# Generated by Django 2.2.2 on 2020-10-19 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('is_base_currency', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 't_currency',
            },
        ),
        migrations.CreateModel(
            name='CurrencyRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('base_currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stok.Currency')),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='currency_rate', to='stok.Currency')),
            ],
            options={
                'db_table': 't_currency_rate',
            },
        ),
    ]
