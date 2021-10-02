#Kenapa tidak terpikirkan olehku, ya? Harusnya aku tidak perlu mendeklarasikan variabel total_pajak dan aku bisa langsung menampung hasil perhitungan akhir 
#saat mendeklarasikan variabel total_harga. Jadi, kodeku akan berjalan jika aku menambahkan setiap harga barang yang telah dipotong diskon sebelum menghitung pajak.

sepatu = { "nama" : "Sepatu Niko", "harga": 150000, "diskon": 30000 }
baju = { "nama" : "Baju Unikloh", "harga": 80000, "diskon": 8000 }
celana = { "nama" : "Celana Lepis", "harga": 200000, "diskon": 60000 }
harga_sepatu = sepatu["harga"] - sepatu["diskon"]
harga_baju = baju["harga"] - baju["diskon"]
harga_celana = celana["harga"] - celana["diskon"]
total_harga = (harga_sepatu + harga_baju + harga_celana) * 1.1 
print(total_harga)