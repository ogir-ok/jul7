from rest_framework import serializers

from apps.lms.models import Student, Group, Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

    teacher = TeacherSerializer()


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    groups = GroupSerializer(many=True)



class StudentSerializerMin(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'birth_date']