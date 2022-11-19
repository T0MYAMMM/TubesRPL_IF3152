import mysql.connector
import datetime
from barang import*

MyDB = mysql.connector.connect(
    # menghubungkan program dengan database MySQL
    # set host, user, password, database
    host = "localhost",
    user = "root",
    password = "",
    database = "barang",
)

MyCursor = MyDB.cursor()

def getData(Result):
    # mengambil seluruh data hasil fech dari database
    # mengubah data yang diambil menjadi object Barang
    # memasukkan object Barang yang telah dibut ke dalam ListBarang
    # menghasilkan output ListBarang berupa array of Barang
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
    # melakukan pencarian barang berdasarkan nama barang yang disimpan
    # memberikan return berupa array of barang
    sql = "SELECT * FROM barang WHERE nama like %s"
    nama = ("%" + Nama + "%", )
    MyCursor.execute(sql, nama)

    MyResult = MyCursor.fetchall()
    Hasil = getData(MyResult)
    return Hasil
    

def SearchStokKosong():
    # melakukan pencarian barang berdasarkan barang yang stoknya habis
    # memberikan return berupa array of barang
    sql = "SELECT * FROM barang WHERE kuantitas = 0"
    MyCursor.execute(sql)

    MyResult = MyCursor.fetchall()
    Hasil = getData(MyResult)
    return Hasil

def SearchKategori(Kategori):
    # melakukan pencarian barang berdasarkan nama kategori dari barang yang disimpan
    # memberikan return berupa array of barang
    sql = "SELECT * FROM barang WHERE nama like %s"
    kategori = ("%" + Kategori + "%", )
    MyCursor.execute(sql, kategori)

    MyResult = MyCursor.fetchall()
    Hasil = getData(MyResult)
    return Hasil

def TambahBarang(Barang):
    # menambahkan object barang pada database
    # input berupa object barang
    # hasil akhir berupa object barang disimpan pada database
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
    # menghapus object barang dari database berdasarkan Barang yang ada
    # melakukan penghapusan object berdasarkan nama dari barang
    # hasil akhir berupa data object barang berhasil dihapus dari database
    sql = ("DELETE FROM barang WHERE nama = %s")
    nama = (Barang.get_nama(), )

    MyCursor.execute(sql, nama)
    MyDB.commit()

def EditKuantitas(Barang, Kuantitas):
    # melakukan pengeditan kuantitas barang
    # kuantitas dapat bertambah maupun berkurang dengan prerequisite (kuantitas >= 0)
    # hasil akhir berupa data kuantitas barang pada database berhasil diubah
    if (Kuantitas >= 0):
        sql = ("UPDATE barang SET kuantitas = %(amount)s WHERE nama = %(nama)s")
        data_kuantitas = {
            'amount'    : Kuantitas,
            'nama'      : Barang.get_nama(),
        }

        MyCursor.execute(sql, data_kuantitas)
        MyDB.commit()
    else:
        return 0

def EditInformasi(Barang, Harga, Supplier, Penyimpanan):
    # melakukan pengeditan informasi harga, supplier, dan tempat penyimpanan barang
    # hasil akhir berupa data harga, supplier, dan tempat penyimpanan barang pada database berhasil diubah
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
    # mengambil seluruh data barang yang tersimpan pada database
    # menghasilkan keluaran berupa array of barang
    sql = "SELECT * FROM barang"
    MyCursor.execute(sql)

    MyResult = MyCursor.fetchall()
    Hasil = getData(MyResult)
    return Hasil