from database import*
from barang import*

barang = Barang("kapal", 20000000, "./pic/contoh.JPG", 3500, 2, "kendaraan", "2022/10/05", "toko kapal mas Akmal", "dermaga labtek V")
TambahBarang(barang)

MyCursor.execute("SELECT * FROM barang")
MyResult = MyCursor.fetchall()
Hasil = getData(MyResult)
for x in Hasil:
    x.print_all_attributes()