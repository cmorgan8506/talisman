import uuid
import unittest
from flask.ext.testing import TestCase
from talisman import create_app, db


class TalismanTestCase(TestCase):
    """
    This is a base class for creating unit tests
    for the Talisman app. Inherit and enjoy.
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    TESTING = True
    DEBUG = False

    def create_app(self):
        """
        Create an application object, using the test
        config data defined in this class.
        """
        self.db = db
        return create_app(self, db)

    def setUp(self):
        """
        Create all the required tables in the temporary
        database, for each test.
        """
        db.create_all()
        self.setup()

    def tearDown(self):
        """
        Destroy session and drop all tables from the db
        after every test, for a clean slate.
        """
        db.session.remove()
        db.drop_all()
        self.cleanup()

    def setup(self):
        """
        A method called during setUp, that can be used
        by tests to setup before testing.
        """
        return

    def cleanup(self):
        """
        A method called during tearDown, that can be used
        by tests to cleanup after testing.
        """
        return

    def _rand_str(self, length=None):
        """
        Generates a random UUID string of a determined size,
        to be used for test data.
        """
        return str(uuid.uuid1())[:length]

if __name__ == '__main__':
    unittest.main()
