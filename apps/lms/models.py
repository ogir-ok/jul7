from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    groups = models.ManyToManyField('Group', related_name='students')

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()


class Group(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    teacher = models.ForeignKey('Teacher', on_delete=models.PROTECT, related_name='groups')


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()