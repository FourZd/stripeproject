# Generated by Django 4.1.1 on 2022-09-19 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_alter_item_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='order',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='items_in_order', to='items.order'),
        ),
    ]
