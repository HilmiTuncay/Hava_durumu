# Munich Hava Durumu Analizi

Munich şehrinin hava durumu verilerini analiz eden ve görselleştiren Python uygulaması.

## Özellikler

- CSV formatındaki hava durumu verilerini okuma ve işleme
- NaN (eksik) değerlerin tespit edilmesi ve temizlenmesi
- Yağış ve kar yağışı verilerinin görselleştirilmesi
- Temizlenmiş verilerin yeni bir CSV dosyasına kaydedilmesi
- Detaylı veri istatistikleri
- Yüksek kaliteli grafik çıktıları (300 DPI)

## Gereksinimler

Bu uygulamayı çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyacınız var:

```bash
pip install pandas numpy matplotlib
```

## Kullanım

1. `munich.csv` dosyasının proje dizininde olduğundan emin olun
2. Analiz scriptini çalıştırın:

```bash
python analiz.py
```

## Çıktılar

Uygulama çalıştırıldığında şu çıktıları üretir:

### 1. Konsol Çıktıları
- Orijinal veri boyutu
- İlk birkaç satır önizlemesi
- NaN değer analizi (her sütun için)
- Temizlenmiş veri boyutu
- Silinen satır sayısı
- Veri istatistikleri

### 2. Dosya Çıktıları
- `munich_clean.csv`: Temizlenmiş veri seti (NaN değerler kaldırılmış)
- `munich_weather_analysis.png`: Yağış ve kar yağışı grafikleri

## Veri Seti Yapısı

Uygulama aşağıdaki sütunları içeren CSV dosyalarıyla çalışır:

- `time`: Tarih bilgisi
- `precipitation_sum (mm)`: Günlük yağış miktarı (milimetre)
- `snowfall_sum (cm)`: Günlük kar yağışı (santimetre)

## Grafikler

Uygulama iki ayrı grafik oluşturur:

1. **Günlük Yağış Miktarı**: Zaman içindeki yağış miktarlarının çizgi grafiği (mavi)
2. **Günlük Kar Yağışı**: Zaman içindeki kar yağışı miktarlarının çizgi grafiği (kırmızı)

## Teknik Detaylar

- **Encoding**: UTF-8 Türkçe karakter desteği
- **CSV Ayırıcı**: Noktalı virgül (;)
- **Grafik Çözünürlüğü**: 300 DPI
- **Font**: DejaVu Sans

## Lisans

Bu proje eğitim amaçlıdır.

## Katkıda Bulunma

Önerileriniz ve katkılarınız için issue açabilir veya pull request gönderebilirsiniz.
