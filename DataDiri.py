# Created on Tue, September 21, 2021
# Author : WendyYansah

import sys
from os import system

repeat = True

# Data diri

nama = "Wendy Yansah"
tgl_lahir = "15 September 2002"
tmpt_lahir = "Sungai Raya, Pontianak"
jk = "Laki-laki"
goldar = "-"
alamat = """
    Komplek Hanura, J9
    RT/RW 001/002
    Desa Teluk Kapuas
    Kec. Sungai Raya
"""
agama = "Buddha"
menikah = False
pekerjaan = "Pelajar/Mahasiswa"
kewarganegaraan = "WNI"

hobi = "Coding, Bulutangkis, Membaca"
email = "wendyyansah01@gmail.com"
pddk_formal = """
    - SD Kristen Immanuel II Kubu Raya (2008 - 2014)
    - SMP Kristen Immanuel II Kubu Raya (2014 - 2017)
    - SMK Kristen Immanuel Pontianak (2017 - 2020)
    - STMIK Pontianak (2020 - Sekarang)
"""
pddk_nonformal = """
    Tidak ada.
"""
organisasi = """
    - ITClub SMK Kristen Immanuel (2017 - 2020)
    - LKS Web Design (2017 - 2018)
    - S.E.T (2018 - Sekarang)
    - Artechsia (2021 - Sekarang)
"""
pengalaman_krja = """
    - SatuMarket (2020)
    - GraPARI Telkomsel Pontianak (2020 - Sekarang)
"""
prestasi = """
    - Finalis APHI PGRI Smart Hackathon Website Sekolah Terbaik Tingkat Nasional 2017
    - 3rd Winner TDA Pitching Day Competition 2019
    - Juara 2 Ide Karya Terbaik Kamp Kreatif SMK Indonesia - Smart School 2019
    - Juara Harapan 1 Kamp Kreatif SMK Indonesia - Smart School 2019
"""



# Function setiap menu yang dipilih :
# ==================================================================

# Function Info KTP
def info_ktp():
    print("================================================================")
    print("======================Kartu Tanda Penduduk======================")
    print("============================Indonesia===========================")
    print("================================================================\n")
    print("Nama                 :", nama)
    print("Tanggal/Tempat Lahir :", tgl_lahir + ", " + tmpt_lahir)
    print("Jenis Kelamin        :", jk)
    print("Gol. Darah           :", goldar)
    print("Alamat               : \n", alamat)
    print("Agama                :", agama)
    
    if menikah:
        print("Status Perkawinan    : Sudah Menikah")
    else:
        print("Status Perkawinan    : Belum Kawin")
        
    print("Pekerjaan            :", pekerjaan)
    print("Kewarganegaraan      :", kewarganegaraan)
    
    print("================================================================\n")
    
# Function Info SIM
def info_sim():
    print("================================================================")
    print("======================Surat Ijin Mengemudi======================")
    print("============================Indonesia===========================")
    print("================================================================\n")
    print("Nama                 :", nama)
    print("Alamat               : \n", alamat)
    print("Email                :", email)
    print("Tanggal/Tempat Lahir :", tgl_lahir + ", " + tmpt_lahir)
    print("Jenis Kelamin        :", jk)
    print("Gol. Darah           :", goldar)
    print("Pekerjaan            :", pekerjaan)
    
    print("================================================================\n")

# Function CV
def info_cv():
    print("==================================================================================================")
    print("=========================================Curriculum Vitae=========================================")
    print("==================================================================================================\n")
    print("Nama                 :", nama)
    print("Alamat               :\n", alamat)
    print("Tanggal/Tempat Lahir :", tgl_lahir + ", " + tmpt_lahir)
    print("Jenis Kelamin        :", jk)
    print("Gol. Darah           :", goldar)
    print("Pekerjaan            :", pekerjaan)
    print("Hobi                 :", hobi)
    print("Pendidikan formal    :\n", pddk_formal)
    print("Pendidikan nonformal :\n", pddk_nonformal)
    print("Organisasi           :\n", organisasi)
    print("Pengalaman Kerja     :\n", pengalaman_krja)
    print("Prestasi / Pekerjaan :\n", prestasi)
    
    print("==================================================================================================\n")

# Function untuk meng-clear CMD (Cls)

def clearWindow():
    system('cls')

# Mulai Program
# ==================================================================

# Jika repeat == true, maka bersihkan layar dan ulang menu

while repeat:
    print("""
Selamat datang!
Silahkan pilih menu yang ingin anda jalankan.
====================================================================

1. Info KTP
2. Info SIM
3. Info CV
""")

    pilihan = input("Masukkan input anda : ")
    if pilihan == "1":
        info_ktp()
    elif pilihan == "2":
        info_sim()
    elif pilihan == "3":
        info_cv()
    else:
        print("Harap memilih pilihan yang disediakan diatas dan cantumkan sesuai angka yang tertera.")

    replay_program = input('Apakah anda ingin mengulang program? (y/n):').lower()
      
    if replay_program == 'y':
        clearWindow()
        status_program = True
    elif replay_program == 'n':
        raise SystemExit()        