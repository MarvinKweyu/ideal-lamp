from django.test import TestCase
from django.urls import resolve

from solos.views import index


class SolosURLsTestCase(TestCase):

    def test_root_url_uses_index_view(self):
        """
        Test that the root of the site resolves to the correct
        view function
        """

        root = resolve("/")
        self.assertEqual(root.func, index)

    def test_solo_details_url(self):
        """
        Test that the URL for SoloDetail resolves to the 
        correct view function
        """
        solo_detail = resolve('/recordings/kind-of-blue/all-blues/cannonball-adderley/')

        #? test that the name of the function being called for this path is correct
        self.assertEqual(solo_detail.func.__name__, 'SoloDetailView')
        self.assertEqual(solo_detail.kwargs['album'],'kind-of-blue')
        self.assertEqual(solo_detail.kwargs['track'], 'all-blues')
        self.assertEqual(solo_detail.kwargs['artist'], 'cannonball-adderley')
