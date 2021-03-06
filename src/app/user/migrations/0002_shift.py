# Generated by Django 3.2.8 on 2022-04-04 09:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日付')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='storename', to='user.store')),
                ('worker1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='part1', to='user.user')),
                ('worker2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='part2', to='user.user')),
                ('worker3', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='part3', to='user.user')),
                ('worker4', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='part4', to='user.user')),
            ],
        ),
    ]
