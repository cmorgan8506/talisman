from ..talisman_test import TalismanTestCase
from talisman.user.models import User


class UserModelTests(TalismanTestCase):

    def first_test_case(self):
        """
        This is a fake test case, to make sure the
        unit test skeleton is working as intended.
        """
        user = User(username='test_user', email='test_user@test.com', password='password')
        assert user
        self.db.session.add(user)
        self.db.session.commit()
        assert user.username == 'test_user'
