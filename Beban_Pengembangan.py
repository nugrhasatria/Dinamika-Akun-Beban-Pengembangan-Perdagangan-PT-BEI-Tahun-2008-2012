import numpy as np

# Indonesia Stock Exchange | IDX
# Bursa Efek Indonesia | BEI 

# Participating Account for Operating Expense
# Komponen Akun pada Beban Usaha
class variable(object):
    def __init__(self, year, gaji_tunjangan, penyusutan, pengembangan_perdagangan, umum_administrasi, sewa, perbaikan_pemeliharaan, transportasi_telekomunikasi, konsultan, lain_lain):
        self.year = year
        self.gaji_tunjangan = gaji_tunjangan
        self.penyusutan = penyusutan
        self.pengembangan_perdagangan = pengembangan_perdagangan
        self.umum_administrasi = umum_administrasi
        self.sewa = sewa
        self.perbaikan_pemeliharaan = perbaikan_pemeliharaan
        self.transportasi_telekomunikasi = transportasi_telekomunikasi
        self.konsultan = konsultan
        self.lain_lain = lain_lain

variable_yoy = {
    # Tahun, Gaji dan Tunjangan, Penyusutan, Pengembangan Perdagangan,
    # Umum dan Administrasi, Sewa, Perbaikan dan Pemeliharaan, Transportasi dan Telekomunikasi, Konsultan, Lain-lain  
    "2008": variable("2008", 132040, 15539, 44845, 51461, 24775),
    "2009": variable("2009", 136511, 23393, 48738, 56688, 24412),
    "2010": variable("2010", 190104, 34485, 54976, 68926, 22821, 16908, 9767, 10075),
    "2011": variable("2011", 208960, 53158, 73114, 45310, 21573, 15250, 15197, 12654, 1999),
    "2012": variable("2012", 242148, 90867, 79832, 44716, 24518, 35067, 15768, 12663, 2248)
}

# Participating Account for Trading Development Expense
# Komponen Akun pada Beban Pengembangan Perdagangan
class variable(object):
    def __init__(self, year, riset_pengembangan, pengembangan_anggota_bursa, promosi, pemeliharaan_teknologi_informasi, lain_lain):
        self.year = year
        self.riset_pengembangan = riset_pengembangan
        self.pengembangan_anggota_bursa = pengembangan_anggota_bursa
        self.promosi = promosi
        self.pemeliharaan_teknologi_informasi = pemeliharaan_teknologi_informasi
        self.lain_lain = lain_lain

variable_yoy = {
    # Tahun, Riset & Pengembangan, Pengembangan Anggota Bursa, Promosi, Pemeliharaan Teknologi Informasi, Lain-lain
    "2008": variable("2008", 27877, 10043, 4696, 1763, 3465),
    "2009": variable("2009", 29299, 13123, 4403, 1654, 3258),
    "2010": variable("2010", 36182, 9099, 5555, 1130, 4064),
    "2011": variable("2011", 31791, 17825, 3371, 1866, 19261),
    "2012": variable("2012", 43996, 27200, 3371, 2199, 3931)
}
