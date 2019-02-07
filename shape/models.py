from django.db import models

class area(models.Model):
	Length=models.IntegerField()
	area=models.IntegerField()
	
	def __str__(self):
		return "Area object {} {}".format(self.Length,self.area)
	#area=Length*Length

