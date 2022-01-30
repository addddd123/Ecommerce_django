from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    name=models.CharField(max_length=255,db_index=True)
    slug=models.SlugField(max_length=255,unique=True)
    
    class Meta:
        verbose_name_plural='categories' 
        """
            by default table name is model name which is category
            above, now meta is used to overide table name 
            from category -> categories
            meta has other use too
            here we can also specify inheritance
            abstract=True
            and also specify advanced query like constraint
        """
        
        # def get_absolute_url(self):
        #     return reverse("store:category_slug", args=[self.slug])
        
        def __str__(self):
            return self.name
        
class Product(models.Model):
    category=models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    created_by=models.ForeignKey(User , on_delete=models.CASCADE,related_name='product_creator')
    title = models.CharField(max_length=255)
    author=models.CharField(max_length=255,default='admin')
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='images/')
    slug=models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    in_stock=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural='products'
        ordering=('-created',)
        #order by created which el is at last added to db
    def __str__(self):
        return self.title
        
    