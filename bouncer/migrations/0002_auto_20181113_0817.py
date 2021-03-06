# Generated by Django 2.0.7 on 2018-11-13 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bouncer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('subject', models.CharField(max_length=256)),
                ('body', models.CharField(blank=True, max_length=2048, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='user',
            name='emails_received',
            field=models.ManyToManyField(to='bouncer.EmailData'),
        ),
    ]
