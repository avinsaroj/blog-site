from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
class Contact(models.Model):
    name=models.CharField(max_length=50 )
    email=models.EmailField(max_length=254)
    subject=models.CharField(max_length=50)
    message=models.TextField()
    

    def __str__(self):
        return str(self.name)
	


class auther(models.Model):
	image = models.ImageField(upload_to='image',null=True,default='image/top-icon.png')
	about = models.CharField(max_length = 150, blank=True)
	profession=models.CharField(max_length=50,blank=True)
	user=models.OneToOneField(User, on_delete=models.CASCADE)
    
	def __str__(self):
		return str(self.user)
@receiver(post_save, sender=User)
def update_user_auther(sender,instance,created, **kwargs):
	if created:
		auther.objects.create(user=instance)
		

	
		


class Post(models.Model):
	title= models.CharField(max_length = 150)
	desc = models.TextField()
	data=models.DateField(auto_now_add=True)
	
	
	auther=models.ForeignKey(auther,  on_delete=models.CASCADE)
   
	def get_absolute_url(self):
		return reverse('singlepost', kwargs={'id': self.id})

	

	
	def __str__(self):
		return str(self.title)

	
class comment(models.Model):
	time=models.DateField(auto_now_add=True)
	comment=models.CharField(max_length=50)
	Posts=models.ForeignKey(Post,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
    
	def __str__(self):
		return str(self.user)

	