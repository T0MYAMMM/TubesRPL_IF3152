import mysql.connector
import datetime

MyDB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "barang",
)

MyCursor = MyDB.cursor()

def getData(Result):
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
        
        
        ## CREATE OBJECT BARANG

def SearchNama(Nama):
    sql = "SELECT * FROM barang WHERE nama like %s"
    nama = ("%" + Nama + "%", )
    MyCursor.execute(sql, nama)

    MyResult = MyCursor.fetchall()
    getData(MyResult)
    

def SearchStokKosong():
    sql = "SELECT * FROM barang WHERE kuantitas = 0"
    MyCursor.execute(sql)

    MyResult = MyCursor.fetchall()
    getData(MyResult)

def SearchKategori(Kategori):
    sql = "SELECT * FROM barang WHERE nama like %s"
    kategori = ("%" + Kategori + "%", )
    MyCursor.execute(sql, kategori)

    MyResult = MyCursor.fetchall()
    getData(MyResult)

def TambahBarang(Barang):
    #using kelas barang
    sql = ("INSERT INTO barang (nama, harga, gambar, ukuran"
           ", kuantitas, kategori, tanggalkadaluarsa, supplier"
           ", penyimpanan) VALUES (%(name)s, %(price)s, %(pict)s"
           ", %(size)s, %(amount)s, %(category)s, %(expdate)s, %(supp)s, %(storage)s)")
    data_barang = {
        'name' : 'Beras 2KG',
        'price' : 120000,
        'pict' : 'D:\#Private Data\M.Dzaki\.kuliah\Semester 5\#MATKUL\IF3152 - RPL\CODE\contoh.JPG',
        'size' : 5000,
        'amount' : 13,
        'category' : 'sembako',
        'expdate' : datetime.datetime(2024,11,1),
        'supp' : 'PT Beras Jaya',
        'storage' : 'rak 3',
    }

    MyCursor.execute(sql, data_barang)
    MyDB.commit()

def KurangBarang(Barang):
    #nama = Barang.nama
    sql = ("DELETE FROM barang WHERE nama = %s")
    nama = (Barang, )

    MyCursor.execute(sql, nama)
    MyDB.commit()

def EditKuantitas(Barang, Kuantitas):
    #nama = Barang.nama
    sql = ("UPDATE barang SET kuantitas = %(amount)s WHERE nama = %(nama)s")
    data_kuantitas = {
        'amount'    : Kuantitas,
        'nama'      : Barang,
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
        'nama'      : Barang,
    }
    
    MyCursor.execute(sql, data_informasi)
    MyDB.commit()