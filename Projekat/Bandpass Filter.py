import matplotlib.pyplot as plt #Plotovanje
from math import sin, pi #Generisanje ulaznih signala
import sys #Citanje argumenata 

# Filter opsega 6KHz-8Khz 

def filter(x):
    y = [0]*48000
    for n in range(4, len(x)):
        y[n] = 0.0101*x[n] - 0.0202*x[n-2] + 0.0101*x[n-4] + 2.4354*y[n-1] - 3.1869*y[n-2] + 2.0889*y[n-3] - 0.7368*y[n-4] 
    return y

#Citanje unete frekvencije
frequency = int(sys.argv[1])	
	
# Fromiranje ulaznog i izlaznog niza
input = [0]*48000
output = [0]*48000

# Popunjavanje niza unetom frekvecijom
for i in range(48000):
    input[i] = sin(2 * pi * frequency * i / 48000)#+ sin(2 * pi * 70 * i / 48000) 

# Filtriranje signala
output = filter(input)

# Pozivanje ulaznih i izlaznih uzoraka
output_ = output[0:4800]  
input_ = input[0:4800] 

# Plotovanje signala i uporedjivanje
plt.figure(1)                
plt.subplot(211)   
plt.ylabel('Magnituda')
plt.xlabel('Uzorci') 
plt.title('Nefiltrirani Signal')      
plt.plot(input_)
plt.subplot(212)             
plt.ylabel('Magnitude')
plt.xlabel('Uzorci') 
plt.title('Filtrirani Signal')
plt.plot(output_)
plt.show()
