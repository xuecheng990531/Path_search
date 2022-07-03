import numpy as np 
import pandas as pd 
   
txt = np.loadtxt('output_pins.txt') 
txtDF = pd.DataFrame(txt) 
txtDF.to_csv('filename.csv',index=False)

