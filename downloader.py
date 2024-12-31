import os
import yt_dlp

def download_video(url, save_path):
    ydl_opts = {
        'format': 'bestvideo',
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Memulai download video dari: {url}")
            ydl.download([url])
        print("Download video selesai!")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengakses video: {e}")

def download_audio(url, save_path):
    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Memulai download audio dari: {url}")
            ydl.download([url])
        print("Download audio selesai!")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengakses audio: {e}")

def main():
    print("Selamat datang di Simple Python YouTube Downloader!")
    print("https://github.com/pengodehandal/ytdownloader/")

    url = input("Masukkan URL YouTube: ").strip()

    save_path = input("Masukkan direktori untuk menyimpan file (misalnya, C:/Downloads/): ").strip()
    if not save_path:
        save_path = os.getcwd()

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    download_type = input("Apakah Anda ingin mendownload (1) Video atau (2) Audio? Masukkan 1 atau 2: ").strip()

    if download_type == '1':
        download_video(url, save_path)
    elif download_type == '2':
        download_audio(url, save_path)
    else:
        print("Pilihan tidak valid.")

if __name__ == '__main__':
    main()
