#TUGAS NO 4
n = int(input("Masukkan angka yang mau dibentuk : "))
t = n
for i in range(n): 
  for k in range(t):
      if i ==0 or i == (n-1) or k == 0 or k == (t-1): 
        print("*",end =' ')
      else :
        print("#",end=' ')
  print()