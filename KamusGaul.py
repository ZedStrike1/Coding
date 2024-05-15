meme_dict = {
    "LOL": "tanggapan terhadap sesuatu yang lucu",
    "CRINGE": "sesuatu yang aneh atau memalukan",
    "ROFL": "tanggapan terhadap lelucon",
    "SHEESH": "sedikit ketidaksetujuan",
    "CREEPY": "menakutkan, tidak menyenangkan",
    "AGGRO": "untuk menjadi agresif/marah"
            }
#tes update            
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")     
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Maaf, kata tersebut tidak ada dalam kamus meme.")
