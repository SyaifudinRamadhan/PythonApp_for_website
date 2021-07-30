from django.urls import path
from . import views

urlpatterns = [
	path('/make_regression', views.createRegression),
	path('/waterPredict',views.waterPredict),
	path('/tankLevel',views.tankLevel),
	path('',views.energySaver),
]