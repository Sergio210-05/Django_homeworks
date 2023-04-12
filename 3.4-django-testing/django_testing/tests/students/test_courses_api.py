import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from random import randint

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def url():
    return '/api/v1/courses/'


@pytest.fixture
def course_factory():
    def course(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return course


@pytest.fixture
def student_factory():
    def student(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return student


@pytest.mark.django_db
def test_retrieve(client, url, course_factory):
    first_course = course_factory()
    response = client.get(url)

    assert response.status_code == 200
    assert response.json()[first_course.id-1]['name'] == first_course.name


@pytest.mark.django_db
def test_list(client, url, course_factory):
    data = course_factory(_quantity=10)
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.json()) == len(data)
    for index, course in enumerate(response.json()):
        assert course['name'] == data[index].name


@pytest.mark.django_db
def test_filter_id(client, url, course_factory):
    quantity = 10
    data = course_factory(_quantity=quantity)
    min_id = data[0].id
    some_id = randint(min_id, min_id+quantity)
    response = client.get(url, data={'id': some_id})

    assert response.status_code == 200
    assert response.json()[0]['name'] == data[some_id-min_id].name


@pytest.mark.django_db
def test_filter_name(client, url, course_factory):
    quantity = 10
    data = course_factory(_quantity=quantity)
    min_id = data[0].id
    some_id = randint(min_id, min_id+quantity)
    for course in data:
        if course.name == data[some_id-min_id].name:
            some_name = course.name
            break
    response = client.get(url, data={'name': some_name})

    assert response.status_code == 200
    assert response.json()[0]['name'] == data[some_id-min_id].name


@pytest.mark.django_db
def test_course_create(client, url):
    new_course = {'name': 'History'}
    response = client.post(path=url, data=new_course)

    assert response.status_code == 201
    assert response.json()['name'] == new_course['name']


@pytest.mark.django_db
def test_course_update(client, url, course_factory):
    data = course_factory(_quantity=1)
    update_course = {'name': 'Ancient History'}
    url_id = url + str(data[0].id) + '/'
    response = client.patch(url_id, data=update_course)

    assert response.status_code == 200


@pytest.mark.django_db
def test_course_delete(client, url, course_factory):
    data = course_factory(_quantity=1)
    url_id = url + str(data[0].id) + '/'
    response_delete = client.delete(url_id)
    response = client.get(url_id)

    assert response_delete.status_code == 204
    assert response.status_code == 404

