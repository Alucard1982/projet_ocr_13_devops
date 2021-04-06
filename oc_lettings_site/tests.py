from bs4 import BeautifulSoup
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_should_use_correct_template_to_render_a_view(client):
    url = reverse('index')
    response = client.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find('title')
    assert title.text == 'Holiday Homes'
    assert response.status_code == 200
    assertTemplateUsed(response, 'index.html')
