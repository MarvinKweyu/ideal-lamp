from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from solos.views import index, SoloDetailView
from solos.models import Solo


class SolosBaseTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @classmethod
    def setUpClass(cls):
        # note difference with python2 which would be super(IndexViewTestCase,cls).setUpClass()
        super().setUpClass() 
        cls.drum_solo = Solo.objects.create(
            instrument='drums',
            artist='Rich',
            track='Bugle Call Rag'
        )
        
        cls.bass_solo = Solo.objects.create(
            instrument='saxophone',
            artist='Coltrane',
            track='Mr. PC'
        )
    


class IndexViewTestCase(SolosBaseTestCase):
    """ 
    Subclass from SolosBaseTestCase for DRY
    """
    def test_index_view_basic(self):
        """
        Test that the view returns a 200 response and uses
        correct template
        """
        request = self.factory.get("/")
        with self.assertTemplateUsed('solos/index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)

    def test_index_view_returns_solos(self):
        """
        Test that the index view will attempt to return solos if 
        query parameters exist
        """
        # use self.client instead of RequestFactory 
        # so that we can access response.context dictionary
        response = self.client.get(
            '/',
            {'instrument': 'drums'}
        )

        solos = response.context['solos']
        
        self.assertIs(type(solos), QuerySet)
        self.assertEqual(len(solos), 1)
        self.assertEqual(solos[0].artist,'Rich')

        self.assertIs(
            type(response.context['solos']),
            QuerySet
        )


class SoloViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    
    def test_basic(self):
        """
        Test that the solo view returns a 200 response, uses
        the correct template and has the correct context
        """
        request = self.factory.get('/solos/1/')
        # since view is class based
        response =SoloDetailView.as_view()(
            request,
            self.drum_solo.pk
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['solo'].artist, 'Rich')

        with self.assertTemplateUsed('solos/solo_detail.html'):
            # use render since we use the request factory
            response.render()
