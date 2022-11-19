import mysql.connector
import datetime
from barang import*

MyDB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "barang",
)

MyCursor = MyDB.cursor()

def getData(Result):
    ListBarang = []

    for row in Result:
        nama = row[1]
        harga = row[2]
        gambar = row[3]
        ukuran = row[4]
        kuantitas = row[5]
        kategori = row[6]
        tanggal = row[7]
        supplier = row[8]
        penyimpanan = row[9]
        
        barangx = Barang(nama, harga, gambar, ukuran, kuantitas, kategori, tanggal, supplier, penyimpanan)
        ListBarang.append(barangx)
    
    return ListBarang

def SearchNama(Nama):
    sql = "SELECT * FROM barang WHERE nama like %s"
    nama = ("%" + Nama + "%", )
    MyCursor.execute(sql, nama)

    MyResult = MyCursor.fetchall()
    Hasil = getData(MyResult)
    return Hasil
    

def SearchStokKosong():
    sql = "SELECT * FROM barang WHERE kuantitas = 0"
    MyCursor.execute(sql)

    MyResult = MyCursor.fetchall()
    Hasil = getData(MyResult)
    return Hasil

def SearchKategori(Kategori):
    sql = "SELECT * FROM barang WHERE nama like %s"
    kategori = ("%" + Kategori + "%", )
    MyCursor.execute(sql, kategori)

    MyResult = MyCursor.fetchall()
    Hasil = getData(MyResult)
    return Hasil

def TambahBarang(Barang):
    #using kelas barang
    sql = ("INSERT INTO barang (nama, harga, gambar, ukuran"
           ", kuantitas, kategori, tanggalkadaluarsa, supplier"
           ", penyimpanan) VALUES (%(name)s, %(price)s, %(pict)s"
           ", %(size)s, %(amount)s, %(category)s, %(expdate)s, %(supp)s, %(storage)s)")
    data_barang = {
        'name' : Barang.get_nama(),
        'price' : Barang.get_harga(),
        'pict' : Barang.get_gambar(),
        'size' : Barang.get_ukuran(),
        'amount' : Barang.get_kuantitas(),
        'category' : Barang.get_kategori(),
        'expdate' : Barang.get_tanggalkadaluarsa(),
        'supp' : Barang.get_supplier(),
        'storage' : Barang.get_penyimpanan(),
    }

    MyCursor.execute(sql, data_barang)
    MyDB.commit()

def KurangBarang(Barang):
    #nama = Barang.nama
    sql = ("DELETE FROM barang WHERE nama = %s")
    nama = (Barang.get_nama(), )

    MyCursor.execute(sql, nama)
    MyDB.commit()

def EditKuantitas(Barang, Kuantitas):
    #nama = Barang.nama
    sql = ("UPDATE barang SET kuantitas = %(amount)s WHERE nama = %(nama)s")
    data_kuantitas = {
        'amount'    : Kuantitas,
        'nama'      : Barang.get_nama(),
    }

    MyCursor.execute(sql, data_kuantitas)
    MyDB.commit()

def EditInformasi(Barang, Harga, Supplier, Penyimpanan):
    #nama = Barang.nama
    sql = ("UPDATE barang SET harga = %(price)s, supplier = %(supplier)s, penyimpanan = %(storage)s WHERE nama = %(nama)s")
    data_informasi = {
        'price'     : Harga,
        'supplier'  : Supplier,
        'storage'   : Penyimpanan,
        'nama'      : Barang.get_nama(),
    }
    
    MyCursor.execute(sql, data_informasi)
    MyDB.commit()

def ViewAllData():
    sql = "SELECT * FROM barang"
    MyCursor.execute(sql)

    MyResult = MyCursor.fetchall()
    Hasil = getData(MyResult)
    return Hasil