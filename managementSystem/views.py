from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from . import models
from .regresi import makeRegress
from datetime import date as dateSys

# Create your views here.
def energySaver(request):

	if str(request.user) == 'AnonymousUser':
		print(request.user)
		return redirect('/login')

	if request.method == 'POST':
		if request.POST['logout'] == 'logoutYes':
			logout(request)
			return redirect('/')

	print(request.user)

	dataEnergy = models.energy_saver.objects.all()
	endData = len(dataEnergy)
	dataView = []
	tmp1 = 0
	tmp2 = 0

	for x in range((endData),0,-1):
			dataView.append(dataEnergy[x-1])

	for x0 in range(0,endData):
		if dataView[x0].day == dateSys.today() :
			tmp1 += dataView[x0].powerMain
			tmp2 += dataView[x0].powerSun
	tmp1 = round(tmp1, 2)
	tmp2 = round(tmp2, 2)

	if endData == 0 :
		dataView = [0,0,0]

	context = {
		'judul': 'Pantau Pengehematan Listrik',
		'isi':'IOT WATER MANAGEMENT SYSTEM | Selamat Datang',
		'fromDb': dataView,
		'endDataMain': tmp1,
		'endDataPnl': tmp2,
		'endData': dataView[0],
		'countData':len(dataEnergy),
	}


	return render(request, 'energy_saver.html', context)

def waterPredict(request):

	if str(request.user) == 'AnonymousUser':
		print(request.user)
		return redirect('/login')

	if request.method == 'POST':
		if request.POST['logout'] == 'logoutYes':
			logout(request)
			return redirect('/')

	print(request.user)

	dataHistory = models.water_prediction.objects.all()
	regresi_eq = models.regression_eq.objects.all()
	endData = len(dataHistory)
	realCount = len(dataHistory)
	dataView = []

	confirm = "NO"

	if endData == 0 :
		endData = 1
		dataHistory = [0,0,0]

	else:

		timeCek = dataHistory[endData-1].time_d
		timeConfirm = timeCek.replace(hour=17, minute=0, second=0, microsecond=0)
		tankLevel = models.minTank.objects.all()

		mid_tank_lvl = tankLevel[0].levelMin / 2

		print("\n",type(dataHistory[endData-1]),"\n")

		for x in range((endData),0,-1):
			dataView.append(dataHistory[x-1])

		print("\n",len(dataView),"\n")

		if timeConfirm < dataHistory[endData-1].time_d and len(regresi_eq) > 0 :

			predict = (regresi_eq[0].M*dataHistory[endData-1].current)+regresi_eq[0].C_and_Error
			print("\n", type(dataHistory[endData-1]),"\n",mid_tank_lvl,"\n",predict,"\n")

			if predict > mid_tank_lvl :
				confirm = "YES"

			elif dataHistory[endData-1].volume_d > mid_tank_lvl :
				confirm = "YES"

	context = {
		'judul': 'Prediksi Konsumsi Air',
		'isi':'IOT WATER MANAGEMENT SYSTEM | Selamat Datang',
		'endData': dataHistory[endData-1],
		'realCount': realCount,
		'regresiLen':len(regresi_eq),
		'dataHistory': dataView,
		'confirm':confirm,
	}

	print("\n",confirm,"\n")

	return render(request, 'water_predict.html', context)

def tankLevel(request):

	if str(request.user) == 'AnonymousUser':
		print(request.user)
		return redirect('/login')

	if request.method == 'POST':
		if request.POST['logout'] == 'logoutYes':
			logout(request)
			return redirect('/')

	print(request.user)

	dataHistory = models.water_prediction.objects.all()
	dataHistory2 = models.tankLevelNew.objects.all()
	sizeMain = len(dataHistory)
	sizeSec = len(dataHistory2)
	endData = []
	dataView = []

	for x in range((sizeMain),0,-1):
			dataView.append(dataHistory[x-1])

	if sizeMain > 0 :
		endData.append(dataView[0].date)
		endData.append(dataView[0].time_d)
		endData.append(dataView[0].volume_d)
	elif sizeSec > 0 :
		endData.append(dataHistory2[0].date)
		endData.append(dataHistory2[0].time)
		endData.append(dataHistory2[0].level)
	else:
		endData = [0,0,0]

	context = {
		'judul':'Pantau Level Tandon Air',
		'isi':'IOT WATER MANAGEMENT SYSTEM | Selamat Datang',
		'endData': endData,
		'sizeMain': sizeMain,
		'sizeSec': sizeSec,
		'history': dataView,
		'msgMain':'Data history level tandon air dari penggunaannya belum tersedia',
		'msgTable':'Data history tiga hari terakhir belum tersedia',
	}

	print(context)

	return render(request, 'tank_level.html', context)

def createRegression(request):

	key = User.objects.all()
	key = key[0].password
	confirm = str(request)
	cekConfirm = "<WSGIRequest: GET '/energySaver/make_regression?confirm="+key+"'>"
	
	if confirm == cekConfirm :

		dataHistory = models.water_prediction.objects.all()

		if len(dataHistory) > 0 :
			X_train = []
			Y_train = []
			for x in range(0,len(dataHistory)):
				X_train.append([dataHistory[x].current])
				Y_train.append([dataHistory[x].volume_d])

			print("\n",X_train,"\n",Y_train,"\n")

			coef, const_E, status = makeRegress(X_train, Y_train)
			print("\n",coef,"\n",const_E,"\n")

			return HttpResponse("Permintaan regresi EQ Accept : " + status)

		else:
			return HttpResponse("Permintaan regresi EQ di tolak")

	else:
		return HttpResponse("Permintaan regresi EQ di tolak : token salah")