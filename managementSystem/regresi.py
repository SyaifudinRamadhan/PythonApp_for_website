from sklearn.linear_model import LinearRegression
from . import models

def makeRegress(X, Y):

	regresi = LinearRegression()
	regresi.fit(X, Y)
	const_and_err = regresi.predict([[0]])
	coef = regresi.predict([[1]]) - const_and_err

	regressDb = models.regression_eq.objects.all()

	if len(regressDb) > 0 :
		regressDb.delete()

	models.regression_eq.objects.create(M=coef, C_and_Error=const_and_err)
	regressDb = models.regression_eq.objects.all()

	status = "Failed"
	if len(regressDb) > 0 :
		status = "Success"

	if status == "Success" :
		dataHistory = models.water_prediction.objects.all()
		dataHistory.delete()

	return coef, const_and_err, status