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
        idbarang = row[0]
        nama = row[1]
        harga = row[2]
        gambar = row[3]
        ukuran = row[4]
        kuantitas = row[5]
        kategori = row[6]
        tanggal = row[7]
        supplier = row[8]
        penyimpanan = row[9]
        
        barangx = Barang(nama, harga, gambar, ukuran, kuantitas, kategori, tanggal, supplier, penyimpanan, idbarang)
        ListBarang.append(barangx)
    
    return ListBarang

def SimpanDatabase():
    # menyimpan data yang diubah/ditambahkan/dihapus dari/ke database
    # melakukan commit() ke database
    MyDB.commit()

def SearchNama(Nama):
    # melakukan pencarian barang berdasarkan nama barang yang disimpan
    # memberikan return berupa array of barang
    sql = "SELECT * FROM barang WHERE nama like %s"
    nama = ("%" + Nama + "%", )
    MyCursor.execute(sql, nama)

    MyResult = MyCursor.fetchall()
    Hasil = getData(MyResult)
    '''
    print(nama)
    for hasilnya in Hasil:
        print(hasilnya.get_nama())
    '''
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
    sql = "SELECT * FROM barang WHERE kategori like %s"
    kategori = ("%" + Kategori + "%", )
    MyCursor.execute(sql, kategori)

    MyResult = MyCursor.fetchall()
    Hasil = getData(MyResult)
    #print(Kategori)
    #for hasilnya in Hasil:
    #    print(hasilnya.get_nama())
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

def HapusBarang(idbarang):
    # menghapus object barang dari database berdasarkan idBarang yang ada
    # melakukan penghapusan object berdasarkan ID dari barang
    # hasil akhir berupa data object barang berhasil dihapus dari database
    sql = ("DELETE FROM barang WHERE idbarang = %s")
    id_barang = (idbarang, )
    MyCursor.execute(sql, id_barang)
    SimpanDatabase()

def EditKuantitas(idbarang, Kuantitas):
    # melakukan pengeditan kuantitas barang
    # kuantitas dapat bertambah maupun berkurang dengan prerequisite (kuantitas >= 0)
    # hasil akhir berupa data kuantitas barang pada database berhasil diubah
    if (Kuantitas >= 0):
        sql = ("UPDATE barang SET kuantitas = %(amount)s WHERE idbarang = %(id)s")
        data_kuantitas = {
            'amount'    : Kuantitas,
            'id'      : idbarang,
        }

        MyCursor.execute(sql, data_kuantitas)
        SimpanDatabase()
    else:
        return 0

def EditInformasi(ID_Barang, Harga, Kuantitas, Supplier, Penyimpanan):
    # melakukan pengeditan informasi harga, supplier, dan tempat penyimpanan barang
    # hasil akhir berupa data harga, supplier, dan tempat penyimpanan barang pada database berhasil diubah
    sql = ("UPDATE barang SET harga = %(price)s, kuantitas = %(amount)s, supplier = %(supplier)s, penyimpanan = %(storage)s WHERE idbarang = %(id)s")
    data_informasi = {
        'price'     : Harga,
        'amount'    : Kuantitas,
        'supplier'  : Supplier,
        'storage'   : Penyimpanan,
        'id'      : ID_Barang,
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

def GetDataGambar(idbarang):
    sql = ("SELECT gambar FROM barang where idbarang = %s")
    id_barang = (idbarang, )

    MyCursor.execute(sql, id_barang)
    MyResult = MyCursor.fetchall()

    for row in MyResult:
        gambar = row[0]
    return gambar