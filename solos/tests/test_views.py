from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from solos.views import index, SoloDetailView
from solos.models import Solo

"""
Note that RequestFactory vs self.client.get('/', {'instrument': 'drums'}) 
depends on the amount of isolation you want your unittest to be run on
with requestfactory giving more isolation
"""

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
        #* using client depends on existence of the URL unlike requestfactory
        response = self.client.get('/', {'instrument': 'drums'}) 

        solos = response.context['solos']
        
        self.assertIs(type(solos), QuerySet)
        self.assertEqual(len(solos), 1)
        self.assertEqual(solos[0].artist,'Rich')

        self.assertIs(
            type(response.context['solos']),
            QuerySet
        )


class SoloViewTestCase(SolosBaseTestCase):
    def setUp(self):
        self.factory = RequestFactory()
    
    def test_basic(self):
        """
        Test that the solo view returns a 200 response, uses
        the correct template and has the correct context
        """
        #* using request factory is independent of existence of the path and calls the view as a function.
        #* it may well be get('nonesense/') unless this argument is needed in the view function
        #* it calls the view as a regular function and tests its effects
        request = self.factory.get('/solos/1/')
        # since view is class based
        response =SoloDetailView.as_view()(
            request,
            pk=self.drum_solo.pk
        )

        self.assertEqual(response.status_code, 200) # check that the drum is in database
        self.assertEqual(response.context_data['solo'].artist, 'Rich') # check that this drummers' name is correct
        #  check that the template used for this detail is correct
        with self.assertTemplateUsed('solos/solo_detail.html'):
            # use render since we use the request factory
            response.render()
