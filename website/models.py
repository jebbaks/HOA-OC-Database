from django.db import models

class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	oc_name = models.CharField(max_length=50)
	creator = models.CharField(max_length=50)
	media = models.CharField(max_length=70)
	lore_summary = models.CharField(max_length=100)
	reference_link = models.CharField(max_length=100)
	creator_remarks = models.CharField(max_length=100)

	def __str__(self):	
		return(f"{self.oc_name}")	

