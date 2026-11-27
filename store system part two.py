toko={"a:toko senjata":0,"b:toko armor":0}
toko_senjata={"pedang":15,"busur":10,"panah":5}
toko_armor={"set armor besi":50,"tameng":20,"perban":10}
menu={"a:beli":0,"b:jual":0,"c:keluar":0}
inv=[ ]
uang=0
def tampilkan_menu(wadah):
    for x in wadah.keys():
        print(x)
def tampilkan_toko(wadah):
    for x,y in wadah.items():
        print(f"{x}:{y}$")
print("== selamat datang di toko kami ==")
nama=input("masukkan nama anda:")
uang=int(input("masukkan uang anda(wajib angka,kalau tidak,akan crash!):"))
print("-------------------")
print(f"tiba tiba ada seseorang menghampiri anda dan menawarkan anda untuk mengikuti pilihan berhadiah tetapi jika salah piliah anda akan mendapat sesuatu yang tidak akan terduga")
ikut=input("apakah anda akan mengikuti pilihan berhadiah?(ya/tidak):")
print("-------------------")
if ikut=="ya":
    while True:
        print(f"halo {nama}!,selamat datang! kami ada hadiah uang untuk anda, sailahkan pilih satu dari ketiga pilihan di bawah!")
        print("a:tirai 1|b:tirai 2|c:tirai 3")
        hadiah=input("masukkan pilihan anda(a/b/c):")
        if hadiah=="a":
            print("selamat anda mendapatkan 1000$!")
            print("---------------------")
            uang+=1000
            break
        elif hadiah=="b":
            print("zonk!")
            print("_____________________________")
            break
        elif hadiah=="c":
            print("anda kalah!,harus membayar 100$!")
            print("---------------------")
            uang-=100
            break
        else:
            print("pilihan tidak valid!,silhkan masukkan ulang")
            print("---------------------")
elif ikut=="tidak":
    print("baiklah,silahkan lanjutkan kegiatan anda")
    print("---------------------")
else:
    print("pilihan tidak valid!")
    print("-------------------------")
while True:
    print(f"uang:{uang}|tas:{inv}")
    print("==pilih menu==")
    tampilkan_menu(menu)
    pilihan=input("silahkan masukkan pilihan anda(a/b/c):")
    print("--------------------------")
    if pilihan=="a":
        tampilkan_menu(toko)
        kunjungi_toko=input("silahkan pilih toko yang ingin anda kunjungi(a/b):")
        print("----------------------------")
        if kunjungi_toko=="a":
            print(f"=== hai {nama}!,selamat datang di toko senjata! ===")
            tampilkan_toko(toko_senjata)
            beli=input("silahkan masukkan barang yang ingin anda beli:")
            print("--------------------------")
            if beli in toko_senjata:
                if uang>=toko_senjata[beli]:
                    uang-=toko_senjata[beli]
                    inv.append(beli)
                    print("tansaksi sukses!")
                    print("--------------------------")
                else:
                    print("uang kamu tidak cukup")
                    print("--------------------------")
            else:
                print(f"{beli} tidak ada di toko senjata!")
                print("--------------------------")
        elif kunjungi_toko=="b":
            print(f"=== hai {nama}!,selamat datang di toko armor! ===")
            tampilkan_toko(toko_armor)
            beli=input("silahkan masukkan barang yang ingin anda beli:")
            print("--------------------------")
            if beli in toko_armor:
                if uang>=toko_armor[beli]:
                    uang-=toko_armor[beli]
                    inv.append(beli)
                    print("tansaksi sukses!")
                    print("--------------------------")
                else:
                    print("uang kamu tidak cukup")
                    print("--------------------------")
            else:
                print(f"{beli} tidak ada di toko armor!")
                print("--------------------------")
        else:
            print("pilihan tidak valid!")
            print("--------------------------")
    elif pilihan=="b":
        jual=input("silahkan pilih barang yang ingin anda jual:")
        print("--------------------------")
        if jual in inv:
            if jual in toko_senjata:
                uang+=toko_senjata[jual]
            elif jual in toko_armor:
                uang+=toko_armor[jual]
            inv.remove(jual)
            print(f"{jual} berhasil dijual")
            print("--------------------------")
        else:
            print(f"{jual} tidak ada di tas anda!")
            print("--------------------------")
    elif pilihan=="c":
        print(f"terimakasih silahkan datang lagi,tuan {nama} yang terhormat!")
        print("program berhenti")
        print("--------------------------")
        break
    else:
        print("pilihan tidak valid!")