#Program yang akan aku bangun akan mengolah sebuah list yang bernama list_cash_flow. Setiap elemen dari list_cash_flow berisikan pengeluaran (bilangan negatif) dan pemasukan (bilangan positif) pada perusahaan
#Dari list_cash_flow ini, aku akan menghitung total_pengeluaran dan total_pemasukan perusahaan

list_cash_flow = [
2500000, 5000000, -1000000, -2500000, 5000000, 10000000,
-5000000, 7500000, 10000000, -1500000, 25000000, -2500000
]
total_pengeluaran, total_pemasukan = 0, 0
for dana in list_cash_flow:
	if dana > 0:
		total_pemasukan += dana
	else:
		total_pengeluaran += dana
total_pengeluaran *= -1
print (total_pemasukan)
print (total_pengeluaran)	