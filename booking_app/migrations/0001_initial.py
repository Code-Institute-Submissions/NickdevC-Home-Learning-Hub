# Generated by Django 3.2.16 on 2023-02-20 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_name', models.CharField(max_length=80)),
                ('child_name', models.CharField(max_length=80)),
                ('teacher_name', models.CharField(choices=[('0', 'Mr Oakley'), ('1', 'Mrs Brundle'), ('2', 'Mr Simons'), ('3', 'Miss Baxter'), ('4', 'Mrs Shepard'), ('5', 'Miss Edwards')], default='0', max_length=80)),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[('0', '15:00 - 15:15'), ('1', '15:15 - 15:30'), ('2', '15:30 - 15:45'), ('3', '15:45 - 16:00'), ('4', '16:00 - 16:15'), ('5', '16:15 - 16:30'), ('6', '16:30 - 16:45')], default='0', max_length=50)),
                ('comment', models.TextField(default=None)),
            ],
            options={
                'unique_together': {('teacher_name', 'date', 'time')},
            },
        ),
    ]
