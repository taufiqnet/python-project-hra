# Generated by Django 3.2.16 on 2023-01-27 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(help_text='leave start date', null=True, verbose_name='Start Date')),
                ('end_date', models.DateField(help_text='leave end date', null=True, verbose_name='End Date')),
                ('leave_type', models.CharField(choices=[('sick', 'Sick Leave'), ('casual', 'Casual Leave')], default='sick', max_length=25, null=True)),
                ('reason', models.CharField(blank=True, help_text='add valid reason for leave', max_length=255, null=True, verbose_name='Reason for Leave')),
                ('default_days', models.PositiveIntegerField(blank=True, default=20, null=True, verbose_name='Leave days per year counter')),
                ('status', models.CharField(default='pending', max_length=12)),
                ('is_approved', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.employee')),
            ],
            options={
                'verbose_name': 'leave',
                'verbose_name_plural': 'leaves',
                'db_table': 'leave',
                'ordering': ['-created'],
            },
        ),
    ]
