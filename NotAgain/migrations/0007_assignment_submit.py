# Generated by Django 3.2 on 2021-05-18 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('NotAgain', '0006_alter_assignment_return_assign_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment_Submit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, null=True)),
                ('reference_file', models.FileField(upload_to='media')),
                ('assign_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NotAgain.assignment_form')),
                ('student_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
