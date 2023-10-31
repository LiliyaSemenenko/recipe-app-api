# Generated by Django 4.2.4 on 2023-10-30 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_userprofile_gender_alter_userprofile_pronouns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('FEMALE', 'Female'), ('MALE', 'Male'), ('CUSTOM', 'Custom'), ('NONE', 'Prefer not to say')], default='NONE', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pronouns',
            field=models.CharField(choices=[('SHE', 'She/Her'), ('HE', 'He/Him'), ('THEY', 'They/Them'), ('CUSTOM', 'Custom'), ('NONE', 'Prefer not to say')], default='NONE', max_length=20),
        ),
    ]
