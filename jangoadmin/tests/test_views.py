from .test_setup import TestSetUp 
class TestView(TestSetUp):
    '''
    Developer: Dheeraj Singh Rajput
    Remarks: Don't change anything without discussion 
    '''
    def test_user_can_register_without_data(self):
        res=self.client.post(self.register_url)
        self.assertEqual(res.status_code,400)
    def test_user_can_register(self):
        res=self.client.post(self.register_url,self.user_data,format="json")
        self.assertEqual(res.status_code,201)
    def test_user_cannot_login_with_unknown_email(self):
        res=self.client.post(self.login_url)
        self.assertEqual(res.status_code,400)