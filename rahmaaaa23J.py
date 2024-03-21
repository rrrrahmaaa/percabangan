#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Menentukan ganjil genap
nilai = int(input('Isikan Nilai:'))
sisa_bagi = nilai % 2

if sisa_bagi==0:
    print(f'{nilai} adalah bilangan genap')
else:
    print(f'{nilai} adalah bilangan ganjil')
    
print('Program selesai')


# In[9]:


nilai_program = int(input('Isikan Nilai Pemograman:'))
if nilai_program < 0 or nilai_program > 100:
    print("Nilai Anda Salah")
else:
    if nilai_program <50:
       print("E")
    elif nilai_program <60:
       print("D")
    elif nilai_program <70:
       print("C")
    elif nilai_program <85:
       print("B")
    elif nilai_program <=100:
       print("A")
   


# In[12]:


username = input('Isikan Username')
password = input('Isikan Password')

# jika username salah => Username anda salah
# jika password salah => Password anda salah
# jika keduanya salah => Username dan Password Anda Salah
# jika keduanya benar => Selamat datang {username}
# username: admin
# password: admin

if username == 'admin':
    if password == 'admin':
        print(f'Selamat Datang {username}')
    else:
        print(f'Password anda Salah')
else:
        if password == 'admin':
            print("Username anda Salah")
        else:
            print("Username dan Password anda Salah")


# In[17]:


nama = input('masukan nama:')
umur = int(input('masukan umur:'))
alamat = input('masukan alamat:')
tabungan = int(input('masukan jumlah tabungan:'))

pangkat = '' 
               
if umur > 40:
    if alamat == 'New york' or alamat =='nevada' or alamat == "havana":
        if tabungan > 10000000:
               pangkat ='Don'
                
elif umur >25 and umur <40:
    if alamat == 'New Jersey' or alamat == 'Manhattan' or alamat == 'Nevada':
        if tabungan >=1000000 and tabungan <=2000000:
            pangkat = 'Underboss'

elif umur >18 and umur <24:
    if alamat == 'Califotnia' or alamat == 'Detroit' or alamat == 'Boston':
        if tabungan <=1000000:
            pangkat = 'Capo'

if pangkat != '':
    print(f'{nama} kemungkinan seorang anggota mafia dengan pangkat {pangkat}')
else:
    print(f'{nama} tidak mencurigakan')


# In[ ]:




