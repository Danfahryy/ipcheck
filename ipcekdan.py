import requests

def lacak_ip(ip_address):
    # URL API ipinfo.io
    url = f"http://ipinfo.io/{ip_address}/json"
    
    try:
        # Mengirimkan permintaan GET ke API
        response = requests.get(url)
        # Memeriksa jika permintaan berhasil
        response.raise_for_status()
        
        # Mendapatkan data JSON dari respon
        data = response.json()
        
        # Menampilkan informasi IP
        print("Informasi IP:")
        print(f"Alamat IP: {data.get('ip', 'Tidak tersedia')}")
        print(f"Hostname: {data.get('hostname', 'Tidak tersedia')}")
        print(f"Lokasi: {data.get('city', 'Tidak tersedia')}, {data.get('region', 'Tidak tersedia')}, {data.get('country', 'Tidak tersedia')}")
        print(f"Organisasi: {data.get('org', 'Tidak tersedia')}")
        print(f"Lokasi Geografis: {data.get('loc', 'Tidak tersedia')}")
    
    except requests.RequestException as e:
        print(f"Terjadi kesalahan: {e}")

# ANSI escape codes for green text
GREEN = "\033[92m"
RESET = "\033[0m"

# Contoh penggunaan
if __name__ == "__main__":
    ip = input(f"{GREEN}  Masukkan alamat IP yang ingin dilacak: {RESET}")
    lacak_ip(ip)

