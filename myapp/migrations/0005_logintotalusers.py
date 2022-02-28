# Generated by Django 4.0 on 2022-02-15 10:11

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_student_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginTotalUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_ids', models.JSONField(default=myapp.models.empty_dictionary)),
            ],
        ),
    ]