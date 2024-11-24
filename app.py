import psutil
import os
from datetime import datetime
from colorama import Fore, Style, init
import math

# Inisialisasi colorama
init(autoreset=True)

# Mendapatkan waktu saat ini
current_time = datetime.now().strftime("%d %B %Y %H:%M:%S WIB")

# Mendapatkan spesifikasi server secara dinamis
ram = math.ceil(psutil.virtual_memory().total / (1024 ** 3))  # Total RAM dalam GB
disk = math.ceil(psutil.disk_usage('/').total / (1024 ** 3))  # Total Disk dalam GB
cpu = psutil.cpu_percent(interval=1)  # CPU Usage

# Fungsi untuk menampilkan informasi dengan UI yang lebih serasi
def display_info():
    info_text = ""

    # Branding ZeroCloud di awal
    info_text += f"{Fore.CYAN}💫 ZeroCloud Indonesia - INFORMASI SERVER 💫\n"
    info_text += f"{Fore.LIGHTCYAN_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    info_text += f"{Fore.LIGHTCYAN_EX}🚀 Powered by ZeroCloud Indonesia 🚀\n\n"

    # Informasi waktu pembuatan server
    info_text += f"{Fore.LIGHTCYAN_EX}🕒 Waktu Pembuatan Server:\n"
    info_text += f"{Fore.LIGHTGREEN_EX}{current_time}\n\n"

    # Informasi spesifikasi server
    info_text += f"{Fore.LIGHTCYAN_EX}📊 Spesifikasi Server:\n"
    info_text += f"{Fore.LIGHTGREEN_EX}RAM: {ram} GB\n"
    info_text += f"{Fore.LIGHTGREEN_EX}Disk: {disk} GB\n"
    info_text += f"{Fore.LIGHTGREEN_EX}CPU: {cpu}%\n\n"

    # Petunjuk penggunaan server dengan branding ZeroCloud
    info_text += f"{Fore.LIGHTCYAN_EX}🔍 Petunjuk Penggunaan (ZeroCloud Guide):\n"
    info_text += f"{Fore.LIGHTGREEN_EX}1. Kunjungi tab 'Software' di panel ZeroCloud\n"
    info_text += f"{Fore.LIGHTGREEN_EX}2. Pilih software yang ingin Anda gunakan\n"
    info_text += f"{Fore.LIGHTGREEN_EX}3. Install software yang dipilih\n"
    info_text += f"{Fore.LIGHTGREEN_EX}4. Ikuti petunjuk instalasi yang tersedia di panel ZeroCloud\n\n"

    # Peringatan penting
    info_text += f"{Fore.LIGHTCYAN_EX}❗ PENTING (ZeroCloud Tips):\n"
    info_text += f"{Fore.LIGHTRED_EX}- Pastikan memilih software yang sesuai dengan kebutuhan Anda di ZeroCloud\n"
    info_text += f"{Fore.LIGHTRED_EX}- Bacalah dokumentasi software yang dipilih di panel ZeroCloud\n"
    info_text += f"{Fore.LIGHTRED_EX}- Jika butuh bantuan, hubungi tim support ZeroCloud Indonesia\n\n"

    # Branding ZeroCloud di akhir
    info_text += f"{Fore.CYAN}✨ Selamat menggunakan server Anda! Ditenagai oleh ZeroCloud Indonesia ✨\n"
    info_text += f"{Fore.LIGHTCYAN_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"

    # Diagnostic System
    info_text += f"{Fore.LIGHTBLUE_EX}🔧 DIAGNOSTIC SERVER (ZeroCloud Diagnostic) 🔧\n"
    info_text += f"{Fore.LIGHTCYAN_EX}Cek Kesehatan Sistem (ZeroCloud Health Check)...\n"
    info_text += f"{Fore.LIGHTGREEN_EX}Memory Available: {math.ceil(psutil.virtual_memory().available / (1024 ** 3))} GB\n"
    info_text += f"{Fore.LIGHTGREEN_EX}Disk Available: {math.ceil(psutil.disk_usage('/').free / (1024 ** 3))} GB\n"
    info_text += f"{Fore.LIGHTGREEN_EX}CPU Load: {psutil.cpu_percent(interval=1)}%\n"
    info_text += f"{Fore.LIGHTGREEN_EX}Sistem Anda sehat! 😊\n\n"

    # Branding ZeroCloud di akhir
    info_text += f"{Fore.LIGHTCYAN_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    info_text += f"{Fore.LIGHTCYAN_EX}ZeroCloud Indonesia - Your Server, Your Way! 🚀🌐\n"
    info_text += f"{Fore.LIGHTCYAN_EX}Nikmati pengalaman terbaik dengan ZeroCloud Indonesia.\n"

    # Menulis ke dalam info.txt
    with open("info.txt", "w") as file:
        file.write(info_text.replace(Fore.LIGHTCYAN_EX, "").replace(Fore.LIGHTGREEN_EX, "").replace(Fore.LIGHTRED_EX, "").replace(Fore.CYAN, "").replace(Fore.LIGHTBLUE_EX, ""))

    # Menampilkan ke terminal
    print(info_text)

    # Memberikan informasi bahwa file info.txt telah dibuat
    print(Fore.LIGHTCYAN_EX + "\n🔔 Semua informasi juga telah disimpan di file 'info.txt'.")
    print(Fore.LIGHTGREEN_EX + "Cek file 'info.txt' di direktori yang sama dengan script untuk melihat detailnya.\n")

    # Menunggu pengguna sebelum keluar
    input(Fore.CYAN + "Tekan Enter untuk keluar...")

if __name__ == "__main__":
    display_info()
