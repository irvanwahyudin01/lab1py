nama ="Irvan Wahyudin";
nim ="312510359";
kls ="TI.25.C5";
bilangan ="";

print("Nama  : ",nama)
print ("NIM   : ",nim)
print("Kelas : ",kls)
print("========================")
angka_strA = input("inputkan nilai A : ")
angka_strB = input("Inputkan nilai B : ")

angka_A = int(angka_strA)
angka_B = int(angka_strB)
A=angka_A%2;
B=angka_B%2;

if(A==0 and B==0) :
    bilangan = "Nilai A dan Nilai B adalah bilangan Genap";
elif(A==0) :
	bilangan = "Nilai A  adalah bilangan Genap dan Nilai B adalah bilangan ganjil";
elif(B==0) :
	bilangan = "Nilai A adalah bilangan Ganjil dan Nilai B adalah bilangan Genap";
else :
	bilangan = "Nilai A dan Nilai B adalah bilangan Ganjil";

if(angka_A>angka_B,) :
	terbesar="Nilai A lebih besar yaitu "
	out=angka_A
elif(angka_A<angka_B) :
	terbesar="Nilai B lebih besar yaitu "
	out=angka_B
else :
	terbesar="Nilai A dan B sama yaitu "
	out=angka_A,angka_B
print (bilangan)
print(terbesar,out)S\