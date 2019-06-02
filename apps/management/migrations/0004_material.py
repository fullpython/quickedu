# Generated by Django 2.2.1 on 2019-06-02 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_cycle_cycletime_room_student_subscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('document', models.FileField(blank=True, null=True, upload_to='materials/')),
                ('body', models.TextField(blank=True, null=True)),
                ('cycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Cycle')),
            ],
        ),
    ]
