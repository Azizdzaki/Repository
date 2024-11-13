# Program Rasio Utang Terhadap Pendapatan (Debt-to-Income Ratio)
Total_pendapatan = int(input('masukkan total pendapatan : '))
Utang = int(input('masukkan utang : '))

Hasil = (Total_pendapatan/Utang)*100

print("Rasio utang terhadap pendapatan adalah " + str(round(Hasil))+ "%") 


# # Program show available balance (income - expenses)
Income = int(input('masukkan total pendapatan : '))
Expense= int(input('masukkan total pengeluaran : '))

Hasil = (Income-Expense)

print("Rasio utang terhadap pendapatan adalah " + str(Hasil)) 


# Program show total spending (sum of all expenses in a month)

Expense = int(input("Masukkan jumlah keuangan perhari : "))
Expense_perbulan = [int(input(f"Masukkan pendapatan bulan ke-{i+1} : "))for i in range (Expense)]

Total = 0
for i in Expense_perbulan:
    Total = Total + i

print("Total pengeluaran adalah " + str(Total)) 

# Program ow lowest income currently and show lowest expenses currently

# Program ow lowest income currently

Jumlah_pendapatan = int(input(" Masukan jumlah pendapatan: "))
pendapatan = [int(input(f"Masukan pendapatan anda ke-{i+1}: ")) for i in range(Jumlah_pendapatan)]

min_pendapatan = pendapatan[0]

for i in range(Jumlah_pendapatan):
    if pendapatan[i] < min_pendapatan:
        min_pendapatan = pendapatan[i]

print(min_pendapatan)

# show lowest expenses currently

Jumlah_pengeluaran = int(input(" Masukan jumlah pengeluaran: "))
pengeluaran = [int(input(f"Masukan pengeluaran anda ke-{i+1}: ")) for i in range(Jumlah_pengeluaran)]

min_pengeluaran = pengeluaran[0]

for i in range(Jumlah_pengeluaran):
    if pengeluaran[i] < min_pengeluaran:
        min_pengeluaran = pengeluaran[i]

print(min_pengeluaran)