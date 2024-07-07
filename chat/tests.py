import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import ChatRoom
from .serializers import ChatRoomSerializer


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user(db):
    user = User.objects.create_user(username='testuser', password='testpassword')
    return user

@pytest.fixture
def create_chatroom(db):
    chatroom = ChatRoom.objects.create(name="Test Room")
    return chatroom

@pytest.mark.django_db
def test_list_chatrooms(api_client, create_user):
    url = reverse('chatroom-list')
    api_client.force_authenticate(user=create_user)
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_create_chatroom(api_client, create_user):
    url = reverse('chatroom-list')
    api_client.force_authenticate(user=create_user)
    data = {
        "name": "New Chat Room"
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert ChatRoom.objects.count() == 1
    assert ChatRoom.objects.get().name == "New Chat Room"

@pytest.mark.django_db
def test_retrieve_chatroom(api_client, create_user, create_chatroom):
    url = reverse('chatroom-detail', args=[create_chatroom.id])
    api_client.force_authenticate(user=create_user)
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == create_chatroom.name

@pytest.mark.django_db
def test_update_chatroom(api_client, create_user, create_chatroom):
    url = reverse('chatroom-detail', args=[create_chatroom.id])
    api_client.force_authenticate(user=create_user)
    data = {
        "name": "Updated Chat Room"
    }
    response = api_client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    create_chatroom.refresh_from_db()
    assert create_chatroom.name == "Updated Chat Room"

@pytest.mark.django_db
def test_delete_chatroom(api_client, create_user, create_chatroom):
    url = reverse('chatroom-detail', args=[create_chatroom.id])
    api_client.force_authenticate(user=create_user)
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert ChatRoom.objects.count() == 0
