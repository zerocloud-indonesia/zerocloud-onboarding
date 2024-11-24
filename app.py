import psutil
import os
from datetime import datetime
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# Mendapatkan waktu saat ini
current_time = datetime.now().strftime("%d %B %Y %H:%M:%S WIB")

# Mendapatkan spesifikasi server secara dinamis
ram = psutil.virtual_memory().total / (1024 ** 2)  # Total RAM dalam MB
ram = round(ram, 2)

disk = psutil.disk_usage('/').total / (1024 ** 2)  # Total Disk dalam MB
disk = round(disk, 2)

cpu = psutil.cpu_percent(interval=1)  # CPU Usage

# Fungsi untuk menampilkan informasi dengan UI yang lebih menyenangkan
def display_info():
    info_text = ""

    # Branding ZeroCloud di awal
    info_text += f"{Fore.CYAN}💫 ZeroCloud Indonesia - INFORMASI SERVER 💫\n"
    info_text += f"{Fore.GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    info_text += f"{Fore.YELLOW}🚀 Powered by ZeroCloud Indonesia 🚀\n\n"

    # Informasi waktu pembuatan server
    info_text += f"{Fore.YELLOW}🕒 Waktu Pembuatan Server:\n"
    info_text += f"{Fore.GREEN}{current_time}\n\n"

    # Informasi spesifikasi server
    info_text += f"{Fore.YELLOW}📊 Spesifikasi Server:\n"
    info_text += f"{Fore.GREEN}RAM: {ram} MB\n"
    info_text += f"{Fore.GREEN}Disk: {disk} MB\n"
    info_text += f"{Fore.GREEN}CPU: {cpu}%\n\n"

    # Petunjuk penggunaan server dengan tambahan branding ZeroCloud
    info_text += f"{Fore.YELLOW}🔍 Petunjuk Penggunaan (ZeroCloud Guide):\n"
    info_text += f"{Fore.GREEN}1. Kunjungi tab 'Software' di panel ZeroCloud\n"
    info_text += f"{Fore.GREEN}2. Pilih software yang ingin Anda gunakan\n"
    info_text += f"{Fore.GREEN}3. Install software yang dipilih\n"
    info_text += f"{Fore.GREEN}4. Ikuti petunjuk instalasi yang tersedia di panel ZeroCloud\n\n"

    info_text += f"{Fore.YELLOW}❗ PENTING (ZeroCloud Tips):\n"
    info_text += f"{Fore.RED}- Pastikan memilih software yang sesuai dengan kebutuhan Anda di ZeroCloud\n"
    info_text += f"{Fore.RED}- Bacalah dokumentasi software yang dipilih di panel ZeroCloud\n"
    info_text += f"{Fore.RED}- Jika butuh bantuan, hubungi tim support ZeroCloud Indonesia\n\n"

    # Branding ZeroCloud di akhir
    info_text += f"{Fore.CYAN}✨ Selamat menggunakan server Anda! Ditenagai oleh ZeroCloud Indonesia ✨\n"
    info_text += f"{Fore.GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"

    # Diagnostic System dengan branding ZeroCloud
    info_text += f"{Fore.MAGENTA}🔧 DIAGNOSTIC SERVER (ZeroCloud Diagnostic) 🔧\n"
    info_text += f"{Fore.YELLOW}Cek Kesehatan Sistem (ZeroCloud Health Check)...\n"
    info_text += f"{Fore.GREEN}Memory Available: {psutil.virtual_memory().available / (1024 ** 2):.2f} MB\n"
    info_text += f"{Fore.GREEN}Disk Available: {psutil.disk_usage('/').free / (1024 ** 2):.2f} MB\n"
    info_text += f"{Fore.GREEN}CPU Load: {psutil.cpu_percent(interval=1)}%\n"
    info_text += f"{Fore.GREEN}Sistem Anda sehat! 😊\n\n"

    # Branding ZeroCloud di akhir
    info_text += f"{Fore.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    info_text += f"{Fore.GREEN}ZeroCloud Indonesia - Your Server, Your Way! 🚀🌐\n"
    info_text += f"{Fore.GREEN}Nikmati pengalaman terbaik dengan ZeroCloud Indonesia.\n"

    # Menulis ke dalam info.txt
    with open("info.txt", "w") as file:
        file.write(info_text)

    # Menampilkan ke terminal
    print(info_text)

    # Memberikan informasi bahwa file info.txt telah dibuat
    print(Fore.YELLOW + "\n🔔 Semua informasi juga telah disimpan di file 'info.txt'.")
    print(Fore.GREEN + "Cek file 'info.txt' di direktori yang sama dengan script untuk melihat detailnya.")

if __name__ == "__main__":
    display_info()
