# QuickSearch - README

QuickSearch, bilgisayarınızdaki dosyaları hızlı ve kolay bir şekilde aramanıza olanak tanıyan bir dosya arama uygulamasıdır. 
Uygulama, basit bir kullanıcı arayüzü ile belirttiğiniz dosyayı bulur ve Windows Dosya Gezgini'nde yerini kolayca açmanızı sağlar.

---

## Özellikler

- **Hızlı Arama:** Dosya adını girerek belirttiğiniz dizinlerde dosya araması yapar.
- **Gelişmiş Uzantı Desteği:** Yaygın dosya uzantılarını otomatik olarak algılar.
- **Dosya Gezgini Entegrasyonu:** Bulunan dosyanın üzerine tıklayarak Windows Dosya Gezgini'nde yerini görme özelliği.
- **Kullanıcı Dostu Arayüz:** Basit ve etkili bir tasarım ile kolay kullanım.

---

## Gereksinimler

- Python 3.7 veya üzeri
- Flet kütüphanesi (UI için)
- Windows işletim sistemi

---

## Kurulum

1. **Depoyu Klonlayın:**
   ```bash
   git clone https://github.com/Keremcm/quicksearch.git
   cd quicksearch
   ```

	2.	Gerekli Kütüphaneleri Yükleyin:

```bash
pip install flet
```

3.Uygulamayı Çalıştırın:

```bash
python search_file.py
```

## Kullanım
1.**Dosya Adını Girin:**
Aramak istediğiniz dosya adını metin kutusuna yazın.

2.**Arama Yapın:**
“Dosya Ara” butonuna tıklayarak belirtilen dizinlerde dosya arayın.

3.**Dosyanın Yerini Açın:**
Bulunan dosyalardan birine tıklayarak Windows Dosya Gezgini’nde dosyanın yerini görün.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır.
