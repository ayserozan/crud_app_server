# Generated by Django 3.1.7 on 2021-03-14 01:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('hire_date', models.DateField(default=django.utils.timezone.now, editable=False)),
                ('hourly_rate', models.FloatField()),
                ('working_percentage', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_name', models.CharField(max_length=50)),
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TeamEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_lead', models.BooleanField(default=0)),
                ('employee_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='pages.employee')),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.team')),
            ],
        ),
    ]
