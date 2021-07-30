from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.energy_saver)
admin.site.register(models.water_prediction)
admin.site.register(models.regression_eq)
admin.site.register(models.minTank)
admin.site.register(models.tankLevelNew)