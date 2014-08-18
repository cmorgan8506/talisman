from werkzeug.security import generate_password_hash
from ..talisman_test import TalismanTestCase
from talisman.user.models import User, UserGroup, UserAddress, UserProfile


class UserModelTests(TalismanTestCase):

    def setup(self):
        self.test_password = self._rand_str(10)
        self.test_username = self._rand_str(10)
        self.test_email = "{0}@talisman.com".format(self._rand_str(length=10))

    def test_user_set_password(self):
        """
        Test that User.set_password works
        """
        user = User(username=self.test_username, email=self.test_email)
        user.set_password(self.test_password)
        self.db.session.add(user)
        self.db.session.commit()
        assert user.password
        assert user.password != self.test_password

    def test_user_check_password(self):
        """
        Test that User.check_password works
        """
        user = User(username=self.test_username, email=self.test_email)
        user.password = generate_password_hash(self.test_password)
        self.db.session.add(user)
        self.db.session.commit()
        assert user.check_password(self.test_password)

    def test_user_group_relationship(self):
        """
        Test that User can have multiple UserGroups
        """
        user = self._create_test_user()
        groups = [self._create_test_group() for x in range(3)]
        user.groups += groups
        self.db.session.commit()
        for g in groups:
            assert g in user.groups

    def test_user_address_relationship(self):
        """
        Test that User can have multiple UserAddresses
        """
        user = self._create_test_user()
        addresses = [self._create_test_address() for x in range(3)]
        user.addresses += addresses
        self.db.session.commit()
        for a in addresses:
            assert a in user.addresses

    def test_user_profile_relationship(self):
        """
        Test that User can have one UserProfile
        """
        user = self._create_test_user()
        profile = self._create_test_profile()
        user.profile = profile
        self.db.session.commit()

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
