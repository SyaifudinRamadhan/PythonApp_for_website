from django.shortcuts import render, redirect
from django.contrib.auth import logout

def index(request):
	context = {
		'judul': 'Home Page',
		'isi':'IOT WATER MANAGEMENT SYSTEM | Selamat Datang',
		'menus':[
			['/','Home Dashboard'],
			['/energySaver','Penghematan Listrik'],
			['/energySaver/waterPredict','Prediksi Konsumsi Air'],
			['/energySaver/tankLevel','Tandon Air'],
		]
	}

	if str(request.user) == 'AnonymousUser' :
		print(request.user)
		return redirect('/login')

	if request.method == 'POST':
		if request.POST['logout'] == 'logoutYes':
			logout(request)
			return redirect('/')
	
	print(request.user)
	return render(request,'home.html', context)