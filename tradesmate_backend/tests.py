from django.test import TestCase

class BasicTestCase(TestCase):
    def test_setup(self):
        """Verify that the test environment is working"""
        self.assertEqual(1 + 1, 2)