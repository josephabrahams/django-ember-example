from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rental',
            fields=[
                ('id', models.SlugField(editable=False,
                                        primary_key=True,
                                        serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('owner', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('category', models.CharField(
                    choices=[('Condo', 'Condo'),
                             ('Townhouse', 'Townhouse'),
                             ('Apartment', 'Apartment'),
                             ('Estate', 'Estate')],
                    max_length=255)),
                ('bedrooms', models.PositiveSmallIntegerField()),
                ('image', models.URLField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated_at'],
            },
        ),
    ]
