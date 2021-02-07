from django.test import TestCase

from api.serializers import UsersSerializer
from users.models import User


class UsersSerializerTestCase(TestCase):
    def test_is_ok(self):
        """ Поменять пароль на другие данные и сравнить, тк хэш """

        user_1 = User.objects.create_user(email='foo1@bar.foo', password='foobar')
        user_2 = User.objects.create_user(email='foo2@bar.foo', password='foobar')
        data = UsersSerializer([user_1, user_2], many=True).data
        expected_data = [
            {
                'id': user_1.id,
                'email': 'foo1@bar.foo',
                'password': 'foobar'
            },
            {
                'id': user_2.id,
                'email': 'foo2@bar.foo',
                'password': 'foobar'
            },

        ]
        self.assertEqual(expected_data, data)
