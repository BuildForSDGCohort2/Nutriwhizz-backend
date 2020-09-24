from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# Categories Models
class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "Date: " + str(self.created_at)


# Profile Models
class Profile(models.Model):
    breakfast = models.IntegerField()
    lunch = models.IntegerField()
    dinner = models.IntegerField()
    #name = models.CharField(max_length=60)
    #email = models.EmailField(max_length = 254, unique=True)
    #alias = models.CharField(max_length=60)
    category = models.ForeignKey(Category, related_name='profiles',on_delete=models.PROTECT)
    #super_power = models.CharField(max_length=60)
    rating = models.IntegerField( default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
    hour = models.IntegerField( default=0, validators=[MinValueValidator(1), MaxValueValidator(24)])
    #picture = models.ImageField(verbose_name=u'Image', upload_to="uploads/profilePictures", null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return str(self.category.created_at)

