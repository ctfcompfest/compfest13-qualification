# Generated by Django 3.2 on 2021-08-31 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_id', models.CharField(max_length=20)),
                ('code', models.TextField()),
                ('out', models.TextField(null=True)),
                ('err', models.TextField(null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]