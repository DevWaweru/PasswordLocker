from locker import Credentials
import unittest

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines the test cases for creating and authenticating credentials
    '''
    def setUp(self):
        '''
        Setting up the structure before each test
        '''
        self.new_user = Credentials(1,"richie","uiui")
    
    def tearDown(self):
        '''
        Cleans up after each test has run
        '''
        Credentials.contact_list = []