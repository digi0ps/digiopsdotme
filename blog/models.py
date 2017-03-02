from django.db import models
from django.utils import timezone


class article(models.Model):
	title = models.CharField(max_length=140)
	content = models.CharField(max_length=5000)
	views = models.IntegerField(default=1)
	posted_time = models.DateTimeField(default=timezone.now)

	class meta:
		ordering = ['-posted_date']

	def get_date(self):
		t = timezone.localtime(self.posted_time)
		return t
