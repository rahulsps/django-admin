from django.test import TestCase
from .models import Timezones  
class ModelTesting(TestCase):
    def setUp(self):
        self.obj=Timezones.objects.create(county_code="a",lat_long="a",country_portion="tz",status="active",utc_offset="te",utc_dst_offset="dts",notes="test")
    def test_timezones_model(self):
        d=self.obj
        self.assertTrue(isinstance(d,Timezones))
        self.assertEqual(str(d),"a")

