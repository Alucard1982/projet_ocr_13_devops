import pytest
from bs4 import BeautifulSoup
from django.db.models.query import QuerySet
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from lettings.models import Letting, Address


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
    adresse = Address.objects.create(number=7217, street='Bedford Street', city='Brunswick',
                                     state='GA', zip_code=31525, country_iso_code='USA')
    letting = Letting.objects.create(title='Joshua Tree Green Haus /w Hot Tub',
                                     address_id=adresse.id)
    url = reverse('letting', args=(letting.id,))
    response = client.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find('title')
    assert title.text == 'Joshua Tree Green Haus /w Hot Tub'
    assert response.status_code == 200
    assert type(response.context['title']), QuerySet
    assert type(response.context['address']), QuerySet
    assertTemplateUsed(response, 'lettings/letting.html')
