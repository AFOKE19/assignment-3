Dolo=float(input("what is the number of Dolomite"))
Shl=float(input("what is the number of Shale"))
Dolo_stan=float(input("what is the standard deviation of Dolomite"))
Shl_stan=float(input("what is the standard deviation of Shale"))
Dolo_mn=float(input("what is the mean of Dolomite"))
Shl_mn=float(input("what is the mean of Shale"))
import scipy.stats
numb_cores=Dolo + Shl
p_d= Dolo/numb_cores
p_s=Shl/numb_cores
p_gamma_Dolo_60= 1-scipy.stats.norm(Dolo_mn,Dolo_stan).cdf(0.5)
p_gamma_Shl_60= 1-scipy.stats.norm(Shl_mn,Shl_stan).cdf(0.5)
p_gamma_Dolo_60=(p_d*p_gamma_Dolo_60)/(p_d*p_gamma_Dolo_60+p_s*p_gamma_Shl_60) 
if p_gamma_Dolo_60>=0.5:
    print("interval is Dolomite")
else:
    print("it is a Shale interval")
