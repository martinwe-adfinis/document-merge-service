# Generated by Django 3.2.16 on 2022-12-23 12:54

from django.db import migrations


def migrate_group_to_meta(apps, schema_editor):
    Template = apps.get_model("api", "Template")

    for template in Template.objects.filter(group__isnull=False):
        template.meta["group"] = template.group
        template.save()


def migrate_group_to_meta_reverse(apps, schema_editor):
    Template = apps.get_model("api", "Template")

    for template in Template.objects.filter(meta__has_key="group"):
        template.group = template.meta["group"]
        del template.meta["group"]
        template.save()


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0005_xlsx_template_engine"),
    ]

    operations = [
        migrations.RunPython(migrate_group_to_meta, migrate_group_to_meta_reverse),
        migrations.RemoveField(
            model_name="template",
            name="group",
        ),
    ]
