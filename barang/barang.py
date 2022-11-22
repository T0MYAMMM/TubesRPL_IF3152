from datetime import datetime

class Barang:

    def __init__(self,nama, harga, gambar, ukuran, kuantitas, kategori, tanggalkadaluarsa, supplier, penyimpanan):
        self.nama = nama
        self.harga = harga
        self.gambar = gambar
        self.ukuran = ukuran
        self.kuantitas = kuantitas
        self.kategori = kategori
        self.tanggalkadaluarsa = tanggalkadaluarsa
        self.supplier = supplier
        self.penyimpanan = penyimpanan

    def get_nama(self):
        return self.nama

    def get_harga(self):
        return self.harga

    def get_gambar(self):
        return self.gambar

    def get_ukuran(self):
        return self.ukuran

    def get_kuantitas(self):
        return self.kuantitas

    def get_kategori(self):
        return self.kategori
    
    def get_tanggalkadaluarsa(self):
        date_str = self.tanggalkadaluarsa
        date_object = datetime.strptime(date_str, '%Y/%m/%d').date()
        date_str = date_object
        return date_object

    def get_tanggalkadaluarsa2(self):
        date_str = self.tanggalkadaluarsa
        date_object = datetime.strptime(date_str, '%Y/%m/%d').date()
        date_object.strftime('%m%d/%Y')
        return date_object

    def get_supplier(self):
        return self.supplier

    def get_penyimpanan(self):
        return self.penyimpanan

    def set_nama(self, nama):
        self.nama = nama

    def set_harga(self, harga):
        self.harga = harga

    def set_gambar(self, gambar):
        self.gambar = gambar

    def set_ukuran(self, ukuran):
        self.ukuran = ukuran

    def set_kuantitas(self, kuantitas):
        self.kuantitas = kuantitas

    def set_kategori(self, kategori):
        self.kategori = kategori

    def set_tanggalkadaluarsa(self, tanggalkadaluarsa):
        self.tanggalkadaluarsa = tanggalkadaluarsa

    def set_supplier(self, supplier):
        self.supplier = supplier

    def set_penyimpanan(self, penyimpanan):
        self.penyimpanan = penyimpanan

    def print_all_attributes(self):
        print(self.nama)
        print(self.harga)
        print(self.gambar)
        print(self.ukuran)
        print(self.kuantitas)
        print(self.kategori)
        print(self.tanggalkadaluarsa)
        print(self.supplier)
        print(self.penyimpanan)

#b1 = Barang("odol", 7000, "Odol.jpg", "Besar", 12, "Pasta Gigi", "11-19-2022", "PT INO", "Rak 4")
#tanggal = b1.get_tanggalkadaluarsa()
#print(type(b1))
#print(tanggal)