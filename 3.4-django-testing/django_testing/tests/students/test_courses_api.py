import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.mark.django_db
def test_get_course(client, course_factory, student_factory):
    student = student_factory()
    course = course_factory(_quantity=5)
    response = client.get('/api/v1/courses/3/')

    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 3


# @pytest.mark.django_db
# def test_get_list_course(client, course_factory, student_factory):
#     student = student_factory()
#     course = course_factory(_quantity=5)
#     response = client.get('/api/v1/courses/')
#
#     assert response.status_code == 200
#     data = response.json()
#     assert len(data) == 5




# @pytest.mark.django_db
# def test_filter_course_id(client, course_factory, student_factory):
#     student = student_factory()
#     course = course_factory(_quantity=3)
#     response = client.get('/api/v1/courses/2/')
#
#     assert response.status_code == 200
#     data = response.json()
#     assert data['id'] == 2




# @pytest.mark.django_db
# def test_filter_course_name(client, course_factory, student_factory):
#     student = student_factory()
#     course = course_factory(_quantity=3, name='Math')
#     response = client.get('/api/v1/courses/?name=Math')
#
#     assert response.status_code == 200
#     data = response.json()
#     assert len(data) == 3



# @pytest.mark.django_db
# def test_create_course(client):
#     count = Course.objects.count()
#     response = client.post('/api/v1/courses/', data={'name': 'Math'})
#
#     assert response.status_code == 201
#     assert Course.objects.count() == count + 1


# @pytest.mark.django_db
# def test_update_course(client, course_factory, student_factory):
#     student = student_factory()
#     course = course_factory(name='Math')
#     new_data = {'name': 'History'}
#     response = client.patch('/api/v1/courses/1/', data=new_data)
#
#     assert response.status_code == 200
#     data = response.json()
#     assert data['name'] == 'History'



@pytest.mark.django_db
def test_delete_course(client, course_factory, student_factory):
    student = student_factory()
    course = course_factory(_quantity=3)
    count = Course.objects.count()
    client.delete('/api/v1/courses/4')
    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    data = response.json()
    assert len(data) == count - 1

@pytest.mark.django_db
def test_delete_course(client, course_factory, student_factory):
    student = student_factory()
    course = course_factory()
    count = Course.objects.count()
    response_delete = client.delete('/api/v1/courses/4')
    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    data = response.json()
    assert len(data) == count - 1