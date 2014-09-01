from werkzeug.security import generate_password_hash
from flask import url_for
from ..talisman_test import TalismanTestCase
from talisman.user.models import User, UserGroup, UserAddress, UserProfile


class UserViewTests(TalismanTestCase):

    render_templates = True

    def setup(self):
        self.test_password = self._rand_str(10)
        self.test_username = self._rand_str(10)
        self.test_email = "{0}@talisman.com".format(self._rand_str(length=10))

    def test_register_user(self):
        """
        Test that the register user view works
        """
        url = "/user/register"
        response = self.client.get(url)
        self.assert_200(response)

    def test_register_user_post(self):
        url = "/user/register"
        response = self.client.post(url, data=dict(
            username=self.test_username, password=self.test_password,
            confirm=self.test_password, email=self.test_email),
            follow_redirects=False)
        self.assertRedirects(response, '/user/')
        user = User.query.filter_by(username=self.test_username).first()
        assert user

    # - Test Data Helper Methods - #
    def _create_test_user(self):
        user = User(username=self._rand_str(10), email=self._rand_str(10),
                    password=generate_password_hash(self._rand_str(10)))
        self.db.session.add(user)
        self.db.session.commit()
        return user

    def _create_test_group(self):
        group = UserGroup(name=self._rand_str(10))
        self.db.session.add(group)
        self.db.session.commit()
        return group

    def _create_test_address(self):
        return UserAddress(address_1=self._rand_str(10),
                           code=self._rand_str(10),
                           city=self._rand_str(10),
                           country=self._rand_str(10),
                           province=self._rand_str(10))

    def _create_test_profile(self):
        return UserProfile(first_name=self._rand_str(10),
                           last_name=self._rand_str(10),
                           phone_primary=self._rand_str(10))
