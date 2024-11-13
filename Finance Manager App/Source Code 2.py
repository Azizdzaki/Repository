# pendapatan
pendapatan = []
file = open("pendapatan.csv", "r")

for line in file:
    pendapatan.append(line.split(",")[4])

file.close()

print(pendapatan)

# pengeluaran
pengeluaran = []
file = open("pengeluaran.csv", "r")

for line in file:
    pengeluaran.append(line.split(",")[4])

file.close()

print(pengeluaran)

# utang dan tagihan
utang = []
tanggal = []
bulan = []
tahun = []
utang_kategori = []
file = open("utang.csv", "r")

for line in file:
    utang.append(line.split(",")[4])
    tanggal.append(line.split(",")[0])
    bulan.append(line.split(",")[1])
    tahun.append(line.split(",")[2])
    utang_kategori.append(line.split(",")[3])

file.close()

print(utang)