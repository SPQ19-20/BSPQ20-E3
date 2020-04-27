import logging
from django.test import TestCase
from django.urls import reverse
from .models import Data
from .githubcsv import get_csv_from_github, get_updated_csvs
from .logs import change_logger

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


class GithubRepoCSVFuncs(TestCase):

    def setUp(self):
        change_logger(nlevel=50)

    def test_get_csv_from_github(self):
        self.assertRaises(ValueError, get_csv_from_github, date=1)
        self.assertRaises(ValueError, get_csv_from_github, date=-1)
        self.assertRaises(ValueError, get_csv_from_github, date=0)
        self.assertRaises(ValueError, get_csv_from_github, date="")
        self.assertRaises(ValueError, get_csv_from_github, date="hola")
        self.assertRaises(ValueError, get_csv_from_github, date="31-02-2020")
        self.assertRaises(ValueError, get_csv_from_github, date="01-02-20")
        self.assertRaises(ValueError, get_csv_from_github, date=[""])
        self.assertRaises(ValueError, get_csv_from_github, date=(""))

        date_string = "29-05-2020"
        with self.assertLogs(level='INFO') as contextmanager:
            get_csv_from_github(date=date_string)
        self.assertEqual(contextmanager.output, [f"INFO:root:CSV file not found for this date yet: {date_string} -> HTTP Error 404: Not Found"])

        with self.assertLogs(level='DEBUG') as contextmanager:
            get_csv_from_github()
        self.assertEqual(contextmanager.output[1], "DEBUG:root:Default date to be used for csv extraction")

        date_string = "29-03-2020"
        with self.assertLogs(level='DEBUG') as contextmanager:
            get_csv_from_github(date=date_string)
        self.assertEqual(contextmanager.output[3], f"DEBUG:root:Successfully downloaded data for {date_string}")

        self.assertRaises(ValueError, get_csv_from_github, url=1)
        self.assertRaises(ValueError, get_csv_from_github, url=-1)
        self.assertRaises(ValueError, get_csv_from_github, url=0)
        self.assertRaises(ValueError, get_csv_from_github, url="")
        self.assertRaises(ValueError, get_csv_from_github, url=[""])
        self.assertRaises(ValueError, get_csv_from_github, url=(""))

    def test_get_updated_csvs(self):
        self.assertRaises(ValueError, get_updated_csvs, seconds=-1)
        self.assertRaises(ValueError, get_updated_csvs, seconds=0)
        self.assertRaises(ValueError, get_updated_csvs, seconds="hola")
        self.assertRaises(ValueError, get_updated_csvs, seconds=None)
        self.assertRaises(ValueError, get_updated_csvs, seconds=[""])
        self.assertRaises(ValueError, get_updated_csvs, seconds=(""))
        self.assertRaises(ValueError, get_updated_csvs, url=1)
        self.assertRaises(ValueError, get_updated_csvs, url=-1)
        self.assertRaises(ValueError, get_updated_csvs, url=0)
        self.assertRaises(ValueError, get_updated_csvs, url="")
        self.assertRaises(ValueError, get_updated_csvs, url=[""])
        self.assertRaises(ValueError, get_updated_csvs, url=(""))


class LoggerFuncs(TestCase):

    def setUp(self):
        change_logger(nlevel=50)

    def test_change_logger(self):
        self.assertRaises(ValueError, change_logger, nlevel=1)
        self.assertRaises(ValueError, change_logger, nlevel=-1)
        self.assertRaises(ValueError, change_logger, nlevel="")
        self.assertRaises(ValueError, change_logger, nlevel=None)
        self.assertRaises(ValueError, change_logger, nlevel="hola")
        self.assertRaises(ValueError, change_logger, nlevel=[""])
        self.assertRaises(ValueError, change_logger, nlevel=(""))
        self.assertRaises(ValueError, change_logger, nfileformat=1)
        self.assertRaises(ValueError, change_logger, nfileformat=-1)
        self.assertRaises(ValueError, change_logger, nfileformat=0)
        self.assertRaises(ValueError, change_logger, nfileformat="")
        self.assertRaises(ValueError, change_logger, nfileformat=[""])
        self.assertRaises(ValueError, change_logger, nfileformat=(""))
        self.assertRaises(ValueError, change_logger, nconsoleformat=1)
        self.assertRaises(ValueError, change_logger, nconsoleformat=-1)
        self.assertRaises(ValueError, change_logger, nconsoleformat=0)
        self.assertRaises(ValueError, change_logger, nconsoleformat="")
        self.assertRaises(ValueError, change_logger, nconsoleformat=[""])
        self.assertRaises(ValueError, change_logger, nconsoleformat=(""))

        with self.assertLogs(level='INFO') as contextmanager:
            change_logger(nlevel=50, nfileformat="%(message)s", nconsoleformat="%(message)s")
        self.assertEqual(contextmanager.output,
            [
                "INFO:root:Console handler changed",
                "INFO:root:File handler changed"
            ]
        )