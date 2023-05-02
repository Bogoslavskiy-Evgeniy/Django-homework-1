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
    course_id = course[3].id
    base_url = '/api/v1/courses/'
    url = f'{base_url}{course_id}/'
    response = client.get(url)

    assert response.status_code == 200
    data = response.json()
    assert data['id'] == course_id


@pytest.mark.django_db
def test_get_list_course(client, course_factory, student_factory):
    student = student_factory()
    course = course_factory(_quantity=5)
    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 5




@pytest.mark.django_db
def test_filter_course_id(client, course_factory, student_factory):
    student = student_factory()
    course = course_factory(_quantity=3)
    course_id = course[2].id
    response = client.get('/api/v1/courses/', {'id': course_id})

    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == course_id




@pytest.mark.django_db
def test_filter_course_name(client, course_factory, student_factory):
    student = student_factory()
    course = course_factory(_quantity=3, name='Math')
    response = client.get('/api/v1/courses/', {'name': 'Math'})

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3



@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', data={'name': 'Math'})

    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_update_course(client, course_factory, student_factory):
    student = student_factory()
    course = course_factory(name='Math')
    base_url = '/api/v1/courses/'
    url = f'{base_url}{course.id}/'
    new_data = {'name': 'History'}
    response = client.patch(url, data=new_data)

    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'History'

@pytest.mark.django_db
def test_delete_course(client, course_factory, student_factory):
    student = student_factory()
    course = course_factory()
    base_url = '/api/v1/courses/'
    url = f'{base_url}{course.id}/'
    response = client.delete(url)

    assert response.status_code == 204






