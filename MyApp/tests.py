from rest_framework import status
from rest_framework.test import APITestCase

class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = 'http://bingeserver-stage.us-east-2.elasticbeanstalk.com/users/login/'
        response = self.client.post(url, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

