import json

kry_baru = int((input('Masukkan jumlah karyawan baru: ')))
for karyawan in range(kry_baru):
       lst_kry = list()
       lst_kolega = list()
       dct_kol_al = dict()
       dic_almt = dict()
       nama = input("Masukkan nama : ")
       alamat = input("Masukan alamat : ")
       jml_kolega = int(input("Masukan jumlah kolega : "))
       for i in range(1,jml_kolega+1):
              kolega = input(f"masukan kolega ke-{i} : ")
              lst_kolega.append(kolega)
       
       dic_almt['Alamat']= alamat
       dct_kol_al["kolega"] = lst_kolega
       lst_kry.append(dic_almt)
       lst_kry.append(dct_kol_al)
       with open('karyawan.json', 'r') as datafile:
              data = json.load(datafile)
              data[nama] = lst_kry
       with open('karyawan.json', 'w') as datafile:
              json.dump(data, datafile)
       
       
       print('=== Data Berhasil Ditambahkan ===')