import os
import concurrent.futures
import flet as ft
import subprocess

# Yaygın dosya uzantıları
common_extensions = ['.jpg', '.png', '.txt', '.pdf', '.docx', '.mp4', '.zip', '.html', '.csv', '.json', '.py', '.exe', '.mp3', '.yml', '.dll', '.xml']

# Dosya arama fonksiyonu
def find_files_in_dir(search_dir, filename, found_files, result_text):
    try:
        # Eğer dosya adında uzantı yoksa, her bir yaygın uzantıyı deneyerek arama yapıyoruz
        for root, dirs, files in os.walk(search_dir):
            # Dosyadaki her bir dosya adını kontrol et
            for file in files:
                # Dosyanın adı, aradığımız adla eşleşiyorsa
                if file.startswith(filename):
                    # Uzantıyı ekleyerek tam dosya yolunu oluştur
                    for ext in common_extensions:
                        if file == filename + ext:
                            full_path = os.path.join(root, file)
                            if full_path not in found_files:
                                found_files.add(full_path)
                                # Sonucu ekle
                                result_text.controls.append(
                                    ft.TextButton(
                                        f"Bulunan dosya: {full_path}",
                                        on_click=lambda e, path=full_path: open_file(path)
                                    )
                                )
                                result_text.update()  # UI güncelle

    except PermissionError:
        pass
    except Exception as e:
        print(f"Beklenmedik bir hata oluştu: {e}")

# Dosya gezgininde dosya açma fonksiyonu
def open_file(file_path):
    try:
        file_path = file_path.replace("/", "\\")
        # Dosya gezgininde belirtilen dosyanın yerini göster
        subprocess.Popen(f'explorer /select,"{file_path}"')  
    except Exception as e:
        print(f"Dosya açılırken hata oluştu: {e}")

# Thread havuzu kullanarak dosya arama fonksiyonu
def search_files_concurrently(search_dirs, filename, result_text):
    found_files = set()  # Bulunan dosya yollarını saklamak için set kullanıyoruz
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        
        # Her klasör için bir iş parçacığı (thread) başlatıyoruz
        for search_dir in search_dirs:
            futures.append(executor.submit(find_files_in_dir, search_dir, filename, found_files, result_text))

        # Her iş parçası tamamlandığında sonucu anında al
        for future in concurrent.futures.as_completed(futures):
            future.result()

# Flet UI
def main(page: ft.Page):
    page.title = "Dosya Arama Uygulaması"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 20  # Padding düzeltildi
    page.bgcolor = ft.colors.BLUE_GREY_900

    # Arama yapmak için kullanılacak dosya adı ve dizinler
    file_name_input = ft.TextField(
        label="Dosya Adını Girin",
        autofocus=True,
        border_color=ft.colors.BLACK87
    )
    result_text = ft.Column(scroll=True, expand=True)
    
    # Arama butonu, eski sonuçları temizle
    def on_search_button_click(e):
        result_text.controls.clear()  # Önceki sonuçları temizle
        result_text.update()
        search_files_concurrently(["C:/", "D:/"], file_name_input.value, result_text)

    search_button = ft.ElevatedButton(
        "Dosya Ara",
        on_click=on_search_button_click
    )

    # Sayfa düzeni
    page.add(file_name_input, search_button, result_text)

# Uygulamayı başlat
ft.app(target=main)
