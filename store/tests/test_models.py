from unicodedata import name
from django.test import TestCase
from store.models import Category , Product
from django.contrib.auth.models import User
class TestCategoriesisModel(TestCase):
    def setUp(self):
        self.data1=Category.objects.create(name='django',slug='django')
        
    def test_category_model_entry(self):
        """
            test category model data insertion/types/fielf attributes
        """
        data=self.data1
        self.assertTrue(isinstance(data,Category))
    
    def test_category_model_entry(self):
        """
            test category model data insertion/types/fielf attributes
        """
        data=self.data1
        print("data is ######## ",str(data.slug))
        self.assertEqual(str(data.name),'django')
        
class TestProductsModel(TestCase):
    def SetUp(self):
        Category.objects.create(name='django',slug='django')
        User.objects.create(username='admin')
        self.data1=Product.objects.create(category_id=1,title='django beginners'
                                          ,created_by_id='1',
                                          slug='django-beginners',price='20.20',
                                          image='django')
        print(self.data1,"self data is 888888888888888")
    def test_products_model_entry(self):
        """
            test category model data insertion/types/fielf attributes
        """
        data=self.data1
        self.assertTrue(isinstance(data,Product))   
        self.assertEqual(str(data.data),'django beginners')