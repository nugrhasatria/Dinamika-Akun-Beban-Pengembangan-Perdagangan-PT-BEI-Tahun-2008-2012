import numpy as np

####                            ####                            ####                        ####

#                             Perubahan Relatif pada Komponen Beban pada                       #
#                                 Akun Beban Pengembangan Perdagangan                          #
#                                       PT BEI Tahun 2008-2012                                 #


# Komponen Beban Pengembangan Usaha

    # Riset dan Pengembangan 
index1 = [21.792297, 27.877134, 29.299014, 36.181791, 31.790550, 43.995549]
#[21792297374, 27877134709, 29299014029, 36181791892, 31790550295, 43995549767]

    # Pengembangan Anggota Bursa
index2 = [2.157313, 10.043311, 13.123155, 9.099213, 17.824894, 27.200351]
#[2157313071, 10043311368, 13123155548, 9099213034, 17824894364, 27200351898]

    # Promosi
index3 = [7.129769, 4.696308, 4.402793, 4.322854, 3.370900, 6.505256]
#[7129769337, 4696308332, 4402793583, 4322854795, 3370900428, 6505256351]

    # Pemeliharaan Teknologi Informasi
index4 = [6.32314, 7.63088, 6.54860, 1.308115, 8.66264, 1.199567]
#[632.314497, 763.088307, 654.860441, 1308.115107, 866.264353, 1119.567056]

    # Lain-lain
index5 = [3.636456, 1.464934, 1.257746, 4.063733, 19.260841, 9.31123]
#[3636.456048, 1464.934541, 1257.746819, 4063.733694, 19.260.841533, 931.123312]

# Pembulatan 3 nilai di belakang koma
#round_to_2nd_i1 = [round(num, 3) for num in index1]
#round_to_2nd_i2 = [round(num, 3) for num in index2]
#round_to_2nd_i3 = [round(num, 3) for num in index3]
#round_to_2nd_i4 = [round(num, 3) for num in index4]
#round_to_2nd_i5 = [round(num, 3) for num in index5]

#print('fixed value for Riset dan Pengembangan (index1): ', round_to_2nd_i1)
#print('fixed value for Pengembangan Anggota Bursa (index2): ', round_to_2nd_i2)
#print('fixed value for Promosi (index3): ', round_to_2nd_i3)
#print('fixed value for Pemeliharaan Teknologi Informasi (index4): ', round_to_2nd_i4)
#print('fixed value for Lain-lain (index5): ', round_to_2nd_i5)

    # Fungsi Hitung Perubahan Relatif pada Variebel Beban Pengembangan Usaha
def percent_change(value):
    output = []
    try:
        for index,i in enumerate(range(len(value))):
            if i == 0:
                output.append(i)
            else:
                old_num = value[index-1]
                new_num = value[index]                    
                output.append(round((((old_num-new_num)/old_num)*100), 2))
    except ZeroDivisionError:
            output.append(0)
    return output
 
    # Hasil Fungsi Hitung Perubahan Relatif
#print('Perubahan Relatif pada Riset dan Pengembangan: ', percent_change(index1))
#print('Perubahan Relatif pada Pengembangan Anggota Bursa YoY: ', percent_change(index2))
#print('Perubahan Relatif pada Promosi YoY: ', percent_change(index3))
#print('Perubahan Relatif pada Pemeliharaan Teknologi Informasi YoY: ', percent_change(index4))
#print('Perubahan Relatif pada Lain-lain YoY: ', percent_change(index5))



####                            ####                            ####                        ####

    #   Fixed Value Komponen Beban
# Riset dan Pengembangan
rpx = [27.877, 29.299, 36.182, 31.791, 43.996]

# Pengembangan Anggota Bursa
pabx =[10.043, 13.123, 9.099, 17.825, 27.200]

# Promosi
prmx = [4.696, 4.403, 4.323, 3.371, 6.505]

# Pemeliharaan Teknologi Informasi:
ptix = [7.631, 6.549, 1.308, 8.663, 1.200]

# Lain-lain
llnx = [1.465, 1.258, 4.064, 19.261, 9.311]
    
    #
    
    #   % Perubahan Relatif pada Komponen Beban
# Riset dan Pengembangan
rp = [27.92, 5.1, 23.49, -12.14, 38.39]

# Pengembangan Anggota Bursa
pab = [365.55, 30.67, -30.66, 95.89, 52.6]

# Promosi
prm = [-34.13, -6.25, -1.82, -22.02, 92.98]

# Pemeliharaan Teknologi Informasi:
pti = [20.68, -14.18, 99.75, -33.78, 29.24]

# Lain-lain
lln = [-59.72, -14.14, 223.1, 373.97, -95.17]

    # (Total Value) Fungsi Hitung Jumlah Nilai Komponen Beban tiap Tahun
def sums_val(RoA):
    sums = 0
    for item in RoA:
        sums += item
    return sums

    # (Average Value) Fungsi Hitung Nilai Rata-rata
def avg_val(RoA):
    jumlah = 0
    for item in RoA:
        jumlah += item
    avg = jumlah/len(RoA)
    return avg

    # (Hasil Hitung)
print('Sums Nilai Riset dan Pengembangan IDX 2008-2012: ', sums_val(rpx))
print('%Avg Perubahan Nilai Riset dan Pengembangan IDX 2008-2012: ', avg_val(rp))

print('Sums Nilai Pengembangan AB IDX 2008-2012: ', sums_val(pabx))
print('%Avg Perubahan Nilai Pengembangan AB IDX 2008-2012: ', avg_val(pab))

print('Sums Nilai Promosi IDX 2008-2012: ', sums_val(prmx))
print('%Avg Perubahan Nilai Promosi IDX 2008-2012: ', avg_val(prm))

print('Sums Nilai Pemeliharaan IT IDX 2008-2012: ', sums_val(ptix))
print('%Avg Perubahan Nilai Pemeliharaan IT IDX 2008-2012: ', avg_val(pti))

print('Sums Nilai Lain-lain IDX 2008-2012: ', sums_val(llnx))
print('%Avg Perubahan Nilai Lain-lain IDX 2008-2012: ', avg_val(lln))