from rest_framework import status
from rest_framework.test import APITestCase

class UserTests(APITestCase):
    def test_create_account(self):
        """
        Create new user.

        """
        url = 'http://bingeserver-stage.us-east-2.elasticbeanstalk.com/users/login/'
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

