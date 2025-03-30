import numpy as np 
import pandas as pd
n =  [12, 45, 67, 23, 89, 34, 22, 90, 56, 78]
cal = np.average(n)
abaixo_media  = [num for num in n if num > cal]
df = pd.DataFrame(abaixo_media)
df.to_csv('numeros_maiores_que_media.csv')