import os
from datetime import datetime
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# Mendapatkan waktu saat ini
current_time = datetime.now().strftime("%d %B %Y %H:%M:%S WIB")

def display_console_guide():
    info = ""

    # Header branding
    info += f"{Fore.CYAN}🖥️ ZeroCloud - Panduan Console untuk Pemula\n"
    info += f"{Fore.LIGHTCYAN_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    info += f"{Fore.LIGHTCYAN_EX}📌 Kamu lagi di Console? Mantap! Yuk belajar langkah pentingnya 👇\n\n"

    # Waktu
    info += f"{Fore.LIGHTCYAN_EX}🕒 Sekarang: {current_time}\n\n"

    # Langkah penting
    info += f"{Fore.LIGHTCYAN_EX}🚦 Perbedaan Tombol Penting:\n"
    info += f"{Fore.LIGHTGREEN_EX}- ▶️ Start: Menyalakan server (kalau mati)\n"
    info += f"{Fore.LIGHTGREEN_EX}- ⏹️ Stop: Mematikan server secara halus\n"
    info += f"{Fore.LIGHTGREEN_EX}- 🔁 Restart: Memuat ulang server (biasanya setelah ubah pengaturan)\n\n"

    info += f"{Fore.LIGHTCYAN_EX}🥚 Ganti Egg (Software Server):\n"
    info += f"{Fore.LIGHTGREEN_EX}1. Klik tab 'Settings'\n"
    info += f"{Fore.LIGHTGREEN_EX}2. Cari bagian 'Egg Changer', pilih Game/Software apa yang ingin digunakan dan klik 'Change Egg' (Software Installer)\n"
    info += f"{Fore.LIGHTGREEN_EX}3. Pilih jenis server sesuai kebutuhan: contoh Minecraft Paper, Forge, dll\n"
    info += f"{Fore.LIGHTGREEN_EX}4. Setelah pilih, klik 'Reinstall' biar file-nya disiapkan otomatis\n"
    info += f"{Fore.LIGHTGREEN_EX}⚠️ *Reinstall akan hapus semua file, jadi backup dulu ya!*\n\n"

    info += f"{Fore.LIGHTCYAN_EX}🎮 Ganti Versi Game / Modpack:\n"
    info += f"{Fore.LIGHTGREEN_EX}- Setelah pilih egg, biasanya kamu bisa pilih versi di tab 'Startup'\n"
    info += f"{Fore.LIGHTGREEN_EX}- Contoh: ganti Minecraft dari 1.20.1 ke 1.19.2 tinggal ubah versi lalu Reinstall\n\n"

    info += f"{Fore.LIGHTCYAN_EX}💾 Backup Sebelum Reinstall:\n"
    info += f"{Fore.LIGHTGREEN_EX}1. Buka tab 'Backups'\n"
    info += f"{Fore.LIGHTGREEN_EX}2. Klik 'Create Backup' ➜ tunggu proses selesai\n"
    info += f"{Fore.LIGHTGREEN_EX}3. Kamu bisa restore kapan aja kalau butuh\n\n"

    info += f"{Fore.LIGHTCYAN_EX}⚙️ Tips Tambahan Buat Pemula:\n"
    info += f"{Fore.LIGHTGREEN_EX}- Jangan spam tombol Start/Restart, biarkan server loading dulu\n"
    info += f"{Fore.LIGHTGREEN_EX}- Cek tab 'Console' buat lihat error/log aktivitas server\n"
    info += f"{Fore.LIGHTGREEN_EX}- Kalau gagal booting, mungkin salah egg/versi, bisa ganti dari 'Startup'\n"
    info += f"{Fore.LIGHTGREEN_EX}- Upload map/modpack bisa lewat tab 'File' atau pake FTP (contohnya di Discord guide)\n\n"

    # Ending
    info += f"{Fore.CYAN}🎉 Enjoy main dan eksplorasi bareng ZeroCloud! 🎉\n"
    info += f"{Fore.LIGHTCYAN_EX}Butuh bantuan? Join Discord kami & buka tiket: https://discord.gg/zerocloud\n"
    info += f"{Fore.LIGHTCYAN_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"

    # Simpan ke file
    with open("console-guide.txt", "w") as f:
        f.write(info.replace(Fore.CYAN, "").replace(Fore.LIGHTCYAN_EX, "").replace(Fore.LIGHTGREEN_EX, ""))

    # Tampilkan
    print(info)
    print(Fore.LIGHTCYAN_EX + "\n📄 Panduan ini juga disimpan di 'console-guide.txt'.")
    input(Fore.CYAN + "Tekan Enter untuk keluar...")

if __name__ == "__main__":
    display_console_guide()
