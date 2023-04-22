from rest_framework import serializers
from django.conf import settings
from rest_framework.exceptions import ValidationError

from students.models import Course, Student


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        # TODO: добавьте требуемую валидацию
        count_students = Student.objects.count()
        if count_students > settings.MAX_STUDENTS_PER_COURSE:
            raise ValidationError("Превышено количество студентов на курсе")

        return data