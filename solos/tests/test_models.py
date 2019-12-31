from django.test import TestCase
from solos.models import Solo


class SoloModelTestCase(TestCase):

    def setUp(self):
        self.solo = Solo.objects.create(
            track = 'Falling in love with love',
            artist = 'Oscar Peterson',
            instrument = 'piano'
        )
    
    def test_solo_basic(self):
        """
        Test basic functionality of Solo
        """
        self.assertEqual(self.solo.artist,'Oscar Peterson')