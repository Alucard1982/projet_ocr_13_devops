import pytest
import json
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from profiles.models import Profile


@pytest.mark.django_db
def test_index_view(client):
    url = reverse('profiles_index')
    response = client.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find('title')
    assert title.text == 'Profiles'
    assert response.status_code == 200
    assert type(response.context['profiles_list']), QuerySet
    assertTemplateUsed(response, 'profiles/index.html')


@pytest.mark.django_db
def test_profile_view(client):
    user = User.objects.create(username='4meRomance', first_name='John', last_name="Rodriguez",
                               email='coemperor@famemma.net')
    Profile.objects.create(favorite_city='Buenos Aires', user_id=user.id)
    url = reverse('profile', args=(user.username, ))
    response = client.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find('title')
    assert title.text == '4meRomance'
    assert response.status_code == 200
    assert type(response.context['profile']), QuerySet
    assertTemplateUsed(response, 'profiles/profile.html')
