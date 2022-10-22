print("===== Nilai Rata-Rata Menggunakan fungsi =====")

u = True
l = 0
h = 0

def Penilaian(H):
    
    if (r == "A"):
        n = 4.00
        print("Nilai = ",n)
    elif (r == "A-"):
        n = 3.75
        print("Nilai = ",n)
    elif (r == "B+"):
        n = 3.50
        print("Nilai = ",n)
    elif (r == "B"):
        n = 3.00
        print("Nilai = ",n)
    elif (r == "B-"):
        n = 2.75
        print("Nilai = ",n)
    elif (r == "C+"):
        n = 2.50
        print("Nilai = ",n)
    elif (r == "C"):
        n = 2.00
        print("Nilai = ",n)
    elif (r == "C-"):
        n = 1.75
        print("Nilai = ",n)
    elif (r == "D"):
        n = 1.50
        print("Nilai = ",n)
    elif (r == "E"):
        n = 1.25
        print("Nilai = ",n)
    else :
        n = 0
    
    return n 

while (u == True):
    r = input("Masukkan nilai = ")
    
    x = Penilaian(r)
    t = h + x
    h = t
    l += 1
    
    if (x == 0):
        u = False
        
O = t/(l-1)
print("Rata-ratanya adalah = ", O)