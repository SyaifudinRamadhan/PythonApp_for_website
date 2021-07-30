from django.db import models

# Create your models here.
class energy_saver(models.Model):
	day = models.DateField(auto_now=True)
	time = models.TimeField(auto_now=True)
	powerMain = models.FloatField()
	powerSun = models.FloatField()

	def _str_(self):
		return "{}".format(self.day)

class water_prediction(models.Model):
	date = models.DateField(auto_now=True)
	time_d = models.TimeField(auto_now=True)
	volume_d = models.FloatField()
	current = models.FloatField()

	def _str_(self):
		return "{}".format(self.date)

class regression_eq(models.Model):
	M = models.FloatField()
	C_and_Error = models.FloatField()

class minTank(models.Model):
	levelMin = models.FloatField()

class tankLevelNew(models.Model):
	date = models.DateField(auto_now=True)
	time = models.TimeField(auto_now=True)
	level = models.FloatField()	

	def _str_(self):
		return "{}".format(self.date)


