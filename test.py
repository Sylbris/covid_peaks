import unittest
import covid_stats
import json

class TestApp(unittest.TestCase):

    def setUp(self):
        covid_stats.app.testing = True
        self.app = covid_stats.app.test_client()
    
    def test_status(self):
        rv=self.app.get('/status')
        self.assertEqual(rv.status, '200 OK')

    def test_newCases(self):
        rv=self.app.get('/newCasesPeak?country=germany')
        data=json.loads(rv.data)
        self.assertEqual(data["country"],'germany')
        self.assertEqual(data["method"],'newCasesPeak')
        self.assertEqual(rv.status, '200 OK')
    
    def test_deathsPeak(self):
        rv=self.app.get('/deathsPeak?country=belgium')
        data=json.loads(rv.data)
        self.assertEqual(data["country"],'belgium')
        self.assertEqual(data["method"],'deathsPeak')
        self.assertEqual(rv.status, '200 OK')
    
    def test_recoveredPeak(self):
        rv=self.app.get('/recoveredPeak?country=israel')
        data=json.loads(rv.data)
        self.assertEqual(data["country"],'israel')
        self.assertEqual(data["method"],'recoveredPeak')
        self.assertEqual(rv.status, '200 OK')
          
          
    
    
if __name__== "__main__" : 
    unittest.main()

    