from django.test import TestCase
from .models import Data
from django.urls import reverse
# Create your tests here.
# Create your UnitTest here.
class DataTestCase(TestCase):
    def setUp(self):
    	dummy = Data(FIPS=0,Admin2="Test")
    	dummy.save()
    def testdb(self):
        test = Data.objects(Admin2='Test')
        for a in test:
        	print(a.Admin2)
        	self.assertEqual(a.Admin2, 'Test')
    def tearDown(self):
    	Data.objects(Admin2='Test').delete()


class IndexViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
    	dummy = Data(FIPS=0,Admin2="Test")
    	dummy.save()        
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('panel:index'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('panel:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertTemplateUsed(response, 'basewithbar.html')
        self.assertTemplateUsed(response, 'base.html')        
    def test_lists_all_authors(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('panel:index'))
        self.assertTrue(len(response.context['data']) != 0)
    def tearDown(self):
    	Data.objects(Admin2='Test').delete()

class LivelogViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
    	dummy = Data(FIPS=0,Admin2="Test")
    	dummy.save()        
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/livelog')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('panel:livelog'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('panel:livelog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'livelogtest.html')
        self.assertTemplateUsed(response, 'basewithbar.html')
        self.assertTemplateUsed(response, 'base.html')        
    def test_lists_all_authors(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('panel:livelog'))
        self.assertTrue(len(response.context['data']) != 0)
    def tearDown(self):
    	Data.objects(Admin2='Test').delete()