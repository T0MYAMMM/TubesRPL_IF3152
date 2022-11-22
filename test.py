from database import*
from barang import*

barang = Barang("Es Teh", 20000000, "pic.JPG", 3500, 2, "minum", "2022/10/05", "toko", "sekre V")
TambahBarang(barang)

MyCursor.execute("SELECT * FROM barang")
MyResult = MyCursor.fetchall()
Hasil = getData(MyResult)
for x in Hasil:
    x.print_all_attributes()


SimpanDatabase()