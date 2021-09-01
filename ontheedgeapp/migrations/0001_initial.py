# Generated by Django 3.2.6 on 2021-09-01 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gradename', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('gradename',),
            },
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picpath', models.CharField(blank=True, max_length=200, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('itemname',),
            },
        ),
        migrations.CreateModel(
            name='ResultCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultcategory', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('resultcategory',),
            },
        ),
        migrations.CreateModel(
            name='TaskCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskcategory', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('taskcategory',),
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasknum', models.CharField(max_length=20)),
                ('lot', models.CharField(blank=True, max_length=20, null=True)),
                ('impdate', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('itemsize', models.IntegerField(default=0)),
                ('taskdate', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('memo', models.TextField(blank=True, null=True)),
                ('grade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ontheedgeapp.grade')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ontheedgeapp.item')),
                ('taskcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ontheedgeapp.taskcategory')),
            ],
            options={
                'ordering': ('-tasknum',),
            },
        ),
        migrations.CreateModel(
            name='PicRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x1', models.IntegerField(default=0)),
                ('y1', models.IntegerField(default=0)),
                ('x2', models.IntegerField(default=0)),
                ('y2', models.IntegerField(default=0)),
                ('gaus', models.IntegerField(default=1)),
                ('thrh', models.IntegerField(default=0)),
                ('inspection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ontheedgeapp.inspection')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.AddField(
            model_name='inspection',
            name='resultcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ontheedgeapp.resultcategory'),
        ),
        migrations.AddField(
            model_name='inspection',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ontheedgeapp.task'),
        ),
    ]