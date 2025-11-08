# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Türkçe karakter desteği için matplotlib ayarı
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']

# Munich.csv dosyasını oku
df = pd.read_csv('munich.csv', sep=';')

print("Orijinal veri boyutu:", df.shape)
print("\nİlk birkaç satır:")
print(df.head(10))

# NaN değerlerini kontrol et
print("\n=== NaN Değer Analizi ===")
print("Her sütundaki NaN sayısı:")
print(df.isnull().sum())
print("\nToplam NaN değer sayısı:", df.isnull().sum().sum())

# NaN içeren satırları temizle
df_clean = df.dropna()

print("\n=== Temizleme Sonrası ===")
print("Temizlenmiş veri boyutu:", df_clean.shape)
print("Silinen satır sayısı:", df.shape[0] - df_clean.shape[0])

# Temizlenmiş veriyi kaydet
df_clean.to_csv('munich_clean.csv', sep=';', index=False)
print("\nTemizlenmiş veri 'munich_clean.csv' dosyasına kaydedildi.")

# Veri istatistikleri
print("\n=== Veri İstatistikleri ===")
print(df_clean.describe())

# Görselleştirme
fig, axes = plt.subplots(2, 1, figsize=(12, 8))

# Yağış grafiği
axes[0].plot(pd.to_datetime(df_clean['time']), df_clean['precipitation_sum (mm)'],
             color='blue', linewidth=1.5)
axes[0].set_title('Günlük Yağış Miktarı (mm)', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Tarih')
axes[0].set_ylabel('Yağış (mm)')
axes[0].grid(True, alpha=0.3)

# Kar yağışı grafiği
axes[1].plot(pd.to_datetime(df_clean['time']), df_clean['snowfall_sum (cm)'],
             color='red', linewidth=1.5)
axes[1].set_title('Günlük Kar Yağışı (cm)', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Tarih')
axes[1].set_ylabel('Kar Yağışı (cm)')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('munich_weather_analysis.png', dpi=300, bbox_inches='tight')
print("\nGörselleştirme 'munich_weather_analysis.png' dosyasına kaydedildi.")

plt.show()
