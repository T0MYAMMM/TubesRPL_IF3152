from database_access import*

barang = Barang("kapal", 20000000, "./pic/contoh.JPG", 3500, 2, "kendaraan", "2022/10/05", "toko kapal mas Akmal", "dermaga labtek V")
TambahBarang(barang)

MyCursor.execute("SELECT * FROM barang")
MyResult = MyCursor.fetchall()
Hasil = getData(MyResult)
print(Hasil)