import psycopg2 as db
import os
con = None
connected = None
cursor = None
#Nama : Muhammad Rizky Sydik
#NIM  : 200511013
#kelas: R3 - Teknik Informatika
def connect() :
    global connected
    global  con
    global cursor

    try :
        con = db.connect(
        host = "localhost",
        database ="kampusku",
        port = 5432,
        user = "sydik45",
        password = 123
        )
        cursor = con.cursor()
        connected = True
    except :
        connected = False
    return cursor
def disconnect(): 
    global connected 
    global con 
    global cursor 
    if (connected==True): 
        cursor.close() 
        con.close() 
    else : 
        con = None 
        connected = False 
dbs = connect ()

def Tampil (dbs) : 
  sql = "select * FROM mahasiswa"
  dbs.execute(sql)
  results = dbs.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def Entry (dbs): 
    global connected 
    global con 
    global cursor 
    xnim = input ("Masukkan NIM: ") 
    xnama = input ("Masukkan Nama Lengkap: ")
    xidfk = input ("Masukkan ID Fakultas (1 .. 5): ") 
    xidpr = input ("Masukkan ID Prodi (1 .. 10): ") 
     
    sql = "insert into mahasiswa (nim, nama, idfakultas, idprodi) values ('"+xnim+"', '"+xnama+"','"+xidfk+"','"+xidpr+"')"
    dbs.execute(sql) 
    con.commit() 
    print ("=== Data telah berhasil ditambahkan ya ges ya.===") 
def Cari(dbs):
    global connected
    global con
    global cursor
    xnim= input ("Masukkan NIM yang dicari : ")

    sql = "select * from mahasiswa where nim = '" + xnim + "'" 
    dbs.execute(sql)
    record = dbs.fetchall()
    print(record)
    print("=== Data telah berhasil dicari ya ges ya.===")
def Ubah (dbs) :
    global connected
    global con
    global cursor
    xnim= input ("Masukkan NIM yang dicari : ")
    sql = "select * from mahasiswa where nim = '" + xnim + "'" 
    dbs.execute(sql)
    record = dbs.fetchall()
    print ("Data saat ini :")
    print(record)
    row = dbs.rowcount
    if(row==1):
        print ("Silahkan untuk mengubah data..")
        xnama = input ("Masukkan Nama Lengkap: ")
        xidfk = input ("Masukkan ID Fakultas (1 .. 5): ") 
        xidpr = input (" Masukkan ID Prodi (1 .. 10): ") 
        sql = "update  mahasiswa set nama='" + xnama + "', idfakultas='" +xidfk + "', idprodi = '" + xidpr + "' where nim='" + xnim +"'"
        dbs.execute (sql) 
        con.commit() 
        print ("=== Data telah berhasil di update ya ges ya.===")
        sql = "select * from mahasiswa where nim='" + xnim +"'"
        dbs.execute(sql)
        rec = dbs.fetchall()
        print ("Data setelah diubah :")
        print(rec)
    else :
        print ("Data tidak ditemukan")

def Hapus (dbs) :
    global connected
    global con
    global cursor
    xnim= input ("Masukkan NIM yang dicari : ")
    sql = "select * from mahasiswa where nim = '" + xnim + "'" 
    dbs.execute(sql)
    record = dbs.fetchall()
    print ("Data saat ini :")
    print(record)
    row = dbs.rowcount
    if(row==1):
        jwb=input("=== Apakah ingin menghapus data ini? (y/t)=== ")
        if(jwb.upper()== "Y") : 
            sql = "delete  from mahasiswa where nim='" + xnim +"'"
            dbs.execute(sql) 
            con.commit() 
            print ("=== Data telah berhasil dihapus ya ges ya.===")
        else:
            print ("=== Data batal untuk dihapus ya ges ya.=== ")
    else:
        print ("Data tidak ditemukan ya ges ya.")

def show_menu(dbs):
  print("=== APLIKASI DATABASE POSTGRESQL PYTHON YA GES YA ===")
  print("1. Show Data")
  print("2. Entry Data")
  print("3. Search Data")
  print("4. Update Data")
  print("5. Delete Data")
  print("0. Keluar")
  print("------------------")

  menu = input("Pilih menu yang diingkan> ")


  if menu == "1":
    Tampil(dbs)
  elif menu == "2":
    Entry(dbs)
  elif menu == "3":
    Cari(dbs)
  elif menu == "4":
    Ubah(dbs)
  elif menu == "5":
    Hapus(dbs)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(dbs)