import pytest
from bs4 import BeautifulSoup
from django.db.models.query import QuerySet
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from lettings.models import Letting


@pytest.mark.django_db
def test_index_view(client):
    url = reverse('lettings_index')
    response = client.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find('title')
    assert title.text == 'Lettings'
    assert response.status_code == 200
    assert type(response.context['lettings_list']), QuerySet
    assertTemplateUsed(response, 'lettings/index.html')


@pytest.mark.django_db
def test_letting_view(client):
    letting = Letting.objects.get(pk=1)
    assert letting.pk == 1
    # letting_id = 1
    # url = reverse('letting', args=(letting_id,))
    # response = client.get(url)
    # assert response.status_code == 200
# assert type(response.context['title']), QuerySet
# assert type(response.context['address']), QuerySet
# assertTemplateUsed(response, 'lettings/letting.html')
