# Generated by Django 3.2.3 on 2021-05-19 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contentcuration', '0128_auto_20210511_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='chef_tree',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channel_chef', to='contentcuration.contentnode'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='clipboard_tree',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channel_clipboard', to='contentcuration.contentnode'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='content_defaults',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='channel',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channel_language', to='contentcuration.language'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='main_tree',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channel_main', to='contentcuration.contentnode'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='previous_tree',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channel_previous', to='contentcuration.contentnode'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='published_data',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='channel',
            name='staging_tree',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channel_staging', to='contentcuration.contentnode'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='thumbnail_encoding',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='channel',
            name='trash_tree',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channel_trash', to='contentcuration.contentnode'),
        ),
        migrations.AlterField(
            model_name='contentnode',
            name='complete',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='contentnode',
            name='extra_fields',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='contentnode',
            name='kind',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contentnodes', to='contentcuration.contentkind'),
        ),
        migrations.AlterField(
            model_name='contentnode',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='content_language', to='contentcuration.language'),
        ),
        migrations.AlterField(
            model_name='contentnode',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='contentnode',
            name='lft',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='contentnode',
            name='license',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contentcuration.license'),
        ),
        migrations.AlterField(
            model_name='contentnode',
            name='rght',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='file',
            name='file_format',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='files', to='contentcuration.fileformat'),
        ),
        migrations.AlterField(
            model_name='file',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='files', to='contentcuration.language'),
        ),
        migrations.AlterField(
            model_name='file',
            name='preset',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='files', to='contentcuration.formatpreset'),
        ),
        migrations.AlterField(
            model_name='formatpreset',
            name='kind',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='format_presets', to='contentcuration.contentkind'),
        ),
        migrations.AlterField(
            model_name='slideshowslide',
            name='metadata',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='task',
            name='metadata',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='clipboard_tree',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_clipboard', to='contentcuration.contentnode'),
        ),
        migrations.AlterField(
            model_name='user',
            name='content_defaults',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='user',
            name='feature_flags',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='information',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='policies',
            field=models.JSONField(default=dict, null=True),
        ),
    ]