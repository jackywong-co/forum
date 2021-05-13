# Generated by Django 3.2 on 2021-05-13 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0010_auto_20210509_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1),
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('post_like_id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_like_post', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
