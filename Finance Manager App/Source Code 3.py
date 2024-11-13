Tpengeluaran = int(input("Masukan total pengeluaran: "))
Tpendapatan =  int(input("Masukan total pendapatan: "))


R_pp = (Tpengeluaran / Tpendapatan) *100
print(R_pp)



sum = 0
Jpendapatan = int(input(" Masukan jumlah pendapatan: "))
pendapatan = [0 for i in range(Jpendapatan)]

for i in range (Jpendapatan) :
    pendapatan [i] = int(input(f"Masukan pendapatan anda ke-{i+1}: "))
    
    sum += pendapatan[i]

print (sum)


max_pendapatan = 0
Jpendapatan = int(input(" Masukan jumlah pendapatan: "))
pendapatan = [0 for i in range(Jpendapatan)]

for i in range (Jpendapatan) :
    pendapatan [i] = int(input(f"Masukan pendapatan anda ke-{i+1}: "))

for i in range(Jpendapatan):
    if pendapatan[i] > max_pendapatan:
        max_pendapatan = pendapatan[i]

print(max_pendapatan)


sum = 0
Jpendapatan = int(input(" Masukan jumlah pendapatan: "))
pendapatan = [0 for i in range(Jpendapatan)]

for i in range (Jpendapatan) :
    pendapatan [i] = int(input(f"Masukan pendapatan anda ke-{i+1}: "))
    
    sum += pendapatan[i]

avg_pendapatan = sum / Jpendapatan

print(avg_pendapatan)