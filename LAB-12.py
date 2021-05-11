
'''

dari jadwal set yang telah diberikan buatlah 2 inputan user yang bernama adit dan jarwo 
untuk menabung tunjukkan harinya setelah itu jumlahkan dan rata2 setiap tabungan user setelah itu berikan bila ada nilai tabungan yang sama

input :
tabungan_1 : nilai tabungan adit ; tabungan_2 : nilai tabungan jarwo

proses:
membuat function
membuat list()
membuat perulangan dari set memasukkan inputan
inputan akan dimasukkan kedalam list
melakukan penjumlahan 
melakukan rata2
melakukan intersection

output :
melihat jumlah dan rata2 setiap tabungan intersection dari kedua tabungan


'''
def tabungan_harian(hari):
    tabungan_adit = list()
    tabungan_jarwo = list()
    total_adit = 0 
    total_jarwo = 0
    for sabi in hari :
        tabungan_1 = int(input("masukkan tabungan adit:"))
        tabungan_adit.append(tabungan_1)
        total_adit += tabungan_1
        print("pada hari",sabi,"tabungannya adalah",tabungan_1)
    for sawi in hari :
        tabungan_2 = int(input("masukkan tabungan jarwo:"))
        tabungan_jarwo.append(tabungan_2)
        total_jarwo += tabungan_2
        print("pada hari",sawi,"tabungannya adalah",tabungan_2)
    bagi_adit = total_adit // len(tabungan_adit)
    bagi_jarwo = total_jarwo // len(tabungan_jarwo)
    sama = set(tabungan_adit) & set(tabungan_jarwo)
    print("===================================")
    print("rata-rata tabungan adit adalah",bagi_adit)
    print("jumlah tabungan adit adalah",total_adit)
    print("===================================")
    print("rata-rata tabungan jarwo adalah",bagi_jarwo)
    print("jumlah tabungan jarwo adalah",total_jarwo)
    print("===================================")
    print("nilai tabungan yang sama",sama)

hari = {"selasa","rabu","kamis"}
tabungan_harian(hari)




