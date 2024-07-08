from rest_framework import status
from rest_framework.test import APIClient

class TestCreateCollection():
    def test_if_user_is_anonymous_return_401(self):
        #TODO => Format for any test => AAA (Arrange, Act, Assert)
        # Arrange
        
        # Act
        client = APIClient()
        response = client.post('/store/collections/', {'title': 'some title'})
        
        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        