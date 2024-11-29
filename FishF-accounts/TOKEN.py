import json

# Fungsi untuk memuat dan mengekstrak token Bearer dari file JSON
def extract_bearer_tokens(file_path):
    with open(file_path, 'r') as file:
        # Membaca seluruh isi file JSON
        data = json.load(file)
        
        # Mengambil token setelah kata "Bearer" dari setiap objek
        tokens = []
        for item in data:
            if 'access_token' in item:
                token = item['access_token'].replace("Bearer ", "")  # Menghapus kata "Bearer " dari token
                tokens.append(token)
        
        return tokens

# Fungsi untuk menyimpan token ke dalam file
def save_tokens_to_file(tokens, output_file):
    with open(output_file, 'w') as file:
        for token in tokens:
            # Menyimpan setiap token di baris baru
            file.write(f"{token}\n")

# Contoh pemanggilan fungsi
file_path = 'accounts.json'  # Ganti dengan path ke file JSON Anda
tokens = extract_bearer_tokens(file_path)

# Menyimpan token yang ditemukan ke dalam file 'akunfishing.txt'
save_tokens_to_file(tokens, 'akunfishing.txt')

print(f"Token telah disimpan ke dalam file 'akunfishing.txt'.")
