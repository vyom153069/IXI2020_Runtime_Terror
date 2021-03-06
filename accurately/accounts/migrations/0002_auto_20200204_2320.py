# Generated by Django 2.0.1 on 2020-02-04 17:50

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='GPA',
            field=models.FloatField(default=0.0, max_length=10.0),
        ),
        migrations.AddField(
            model_name='user',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Competitions', 'Competitions'), ('Conferences', 'Conferences'), ('Exchange-Programs', 'Exchange-Programs'), ('Fellowships', 'Fellowships'), ('Internships', 'Internships'), ('Scholarships', 'Scholarships'), ('Workshops', 'Workshops')], max_length=89, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='domain',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Engineering', 'Engineering'), ('Medicine', 'Medicine'), ('Management', 'Management'), ('Humanities', 'Humanities'), ('Science', 'Science')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Non-Binary', 'Non-Binary')], max_length=22, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='qualification',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Post-Doctorate', 'Post-Doctorate'), ('Doctorate', 'Doctorate'), ('Masters', 'Masters'), ('Bachelors', 'Bachelors'), ('School', 'School')], max_length=49, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
