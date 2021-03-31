import pytest
import json
from bs4 import BeautifulSoup
from django.db.models.query import QuerySet
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from profiles.models import Profile


@pytest.mark.django_db
def test_index_view(client):
    url = reverse('profiles_index')
    response = client.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title =soup.find('title')
    assert title.text == 'Profiles'
    assert response.status_code == 200
    assert type(response.context['profiles_list']), QuerySet
    assertTemplateUsed(response, 'profiles/index.html')


@pytest.mark.django_db
def test_profile_view(client):
    try:
        profile = Profile.objects.get(pk=1)
    except Profile.DoesNotExist:
        profile = None
    assert profile.pk == 1