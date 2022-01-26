# 2.uzdevums.
#Lietotājs ievada kvadrāta malas garumu centimetros (>5cm).<br>
#Sastādīt programmas kodu, kas aprēķina, par cik procentiem mainīsies kvadrāta laukums, ja tā malas garums tiek mainīts par 5cm.<br>
#Atbildi izvadīt veselos procentos.

mala=float(input("Kvadrāta malas garums: "))
if mala<=5:
  print("ievadi >5")
else:
  s1=mala**2
  s2=(mala+5)*(mala+5)
  proc=s2*100/s1
  print(proc)


  
"""

x%   = s2
100% = s1

"""
