import requests

#MENCARI ID KOTA YANG INGIN DICARI TEMPAT RESTORANNYA
kota = (input('Pilih kota (Jakarta/Bandung/Bali atau kota di luar negeri): ')).lower()
url = f'https://developers.zomato.com/api/v2.1/cities?q={kota}'
apikey1 = 'a0db0542879222e54be4e96eeb888056'
headInfo1 = {'user-key': apikey1}
w = requests.get(url, headers=headInfo1)
id = w.json()['location_suggestions'][0]['id'] #HASIL PENCARIAN ID CITIES

#MENCARI RETORAN YANG MENJUAL MAKANAN TERTENTU DI KOTA PILIHAN
food = (input('Mau cari resto yang menjual makanan apa? ')).lower()
link = f'https://developers.zomato.com/api/v2.1/search?entity_id={id}&entity_type=city&q={food}'
apikey = 'a0db0542879222e54be4e96eeb888056'
headInfo = {'user-key': apikey}
data = requests.get(link, headers=headInfo)

#MENAMPILKAN DATA
x = data.json()['restaurants'][0]['restaurant']['name']
y = data.json()['restaurants'][0]['restaurant']['location']['address']
print(f'\nMau makan {(food).upper()} di Kota {(kota).upper()}? \n Anda bisa datang ke {(x).upper()} dengan alamat {y}')

#MENAMPILKAN PILIHAN JIKA PENGUNJUNG INGIN MENCARI RESTO LAIN
Gate = (input(f'\nMau pilihan resto lain yang menjual {(food).upper()} di kota {(kota).upper()}? (Y/N): ')).upper()
no = 1
while Gate == 'Y':
    resto = []
    alamat = []
    for i in range(1):
        resto.append((data.json()['restaurants'][no]['restaurant']['name']).upper())
        alamat.append(data.json()['restaurants'][no]['restaurant']['location']['address'])
    no += 1
    print(f'\nTempat lain untuk makan {(food).upper()} di Kota {(kota).upper()}, \n Anda bisa datang ke {resto[0]} dengan alamat {alamat[0]}')
    Gate = (input(f'\nMau pilihan resto lain yang menjual {(food).upper()} di kota {(kota).upper()}? (Y/N): ')).upper()