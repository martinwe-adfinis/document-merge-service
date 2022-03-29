# Generated by Django 3.2.9 on 2022-03-29 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_cleanup_files"),
    ]

    operations = [
        migrations.AlterField(
            model_name="template",
            name="engine",
            field=models.CharField(
                choices=[
                    (
                        "docx-template",
                        "Docx Template engine (https://github.com/elapouya/python-docx-template)",
                    ),
                    (
                        "docx-mailmerge",
                        "Docx MailMerge engine (https://github.com/Bouke/docx-mailmerge)",
                    ),
                    (
                        "xlsx-template",
                        "Xlsx Template engine (https://github.com/zhangyu836/python-xlsx-template)",
                    ),
                ],
                max_length=20,
            ),
        ),
    ]
