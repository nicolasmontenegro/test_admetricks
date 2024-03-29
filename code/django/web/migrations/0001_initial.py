# Generated by Django 2.2.2 on 2019-06-15 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dollar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('delta', models.DecimalField(decimal_places=2, max_digits=5)),
                ('value_at', models.DateTimeField()),
            ],
            options={
                'ordering': ('value_at',),
            },
        ),
    ]
