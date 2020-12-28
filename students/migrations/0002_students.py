from django.db import migrations

def create_data(apps, schema_editor):
    Student = apps.get_model('students', 'Student')
    Student(name="JAbhijit Anand", email="abhijitanand2000@gmail.com", document="21345", phone="00000000").save()

class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]