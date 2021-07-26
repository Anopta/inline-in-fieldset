from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    department = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    gender = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(
        'Student',
        on_delete=models.CASCADE
    )
    subject =  models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
