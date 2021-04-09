from .test_setup import TestSetUp 
class TestView(TestSetUp):
    '''
    '''
    def test_user_can_register_without_data(self):
        res=self.client.post(self.register_url)
        #import pdb
        #pdb.set_trace()
        self.assertEqual(res.status_code,400)
    def test_user_can_register(self):
        res=self.client.post(self.register_url,self.user_data,format="json")
        self.assertEqual(res.status_code,201)

    def test_user_cannot_login_with_unknown_email(self):
        res=self.client.post(self.login_url)
        self.assertEqual(res.status_code,500)
    def test_user_can_login_with_correct_credentials(self):
        res=self.client.post(self.login_url,self.login_data,format="json")
        self.assertEqual(res.status_code,200)

    