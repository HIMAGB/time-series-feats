
from Feature import FeatureSpace
import numpy as np
from import_lightcurve import LeerLC_MACHO
from PreprocessLC import Preprocess_LC


#Opening the light curve
lc_B = LeerLC_MACHO('lc_1.3444.614.B.mjd')
lc_R = LeerLC_MACHO('lc_1.3444.614.R.mjd')

[data, mjd, error] = lc_B.leerLC()
[data2, mjd2, error2] = lc_R.leerLC()

preproccesed_data = Preprocess_LC(data, mjd, error)
[data, mjd, error] = preproccesed_data.Preprocess()

preproccesed_data = Preprocess_LC(data2, mjd2, error2)
[second_data, mjd2, error2] = preproccesed_data.Preprocess()
 
#Calculating the features
a = FeatureSpace(category='all',featureList=None, automean=[0,0], StetsonL=second_data ,  B_R=second_data, Beyond1Std=error, StetsonJ=second_data, MaxSlope=mjd, LinearTrend=mjd, Eta_B_R=second_data, Eta_e=mjd, Q31B_R=second_data, PeriodLS=mjd)
#, CAR_sigma=[mjd, error], SlottedA = mjd)
a=a.calculateFeature(data)

print a.result(method='dict')

# nombres = a.result(method='features')
# guardar = np.vstack((nombres,a.result(method='array')))
# # a=np.vstack((previous_data,a))
# np.savetxt('test_real.csv', guardar, delimiter="," ,fmt="%s")

#B_R = second_data, Eta_B_R = second_data, Eta_e = mjd, MaxSlope = mjd, PeriodLS = mjd, Q31B_R = second_data, StetsonJ = second_data, StetsonL = second_data)