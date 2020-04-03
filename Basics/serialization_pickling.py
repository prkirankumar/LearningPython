import os
import pickle



x=7
os.chdir('C:\\practice')
f=open('test.txt','r+b')  # opened it in binary mode to pickle
pickle.dump(x,f)