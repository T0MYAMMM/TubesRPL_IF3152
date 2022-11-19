import mysql.connector

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
    