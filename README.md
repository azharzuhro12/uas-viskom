# Perbandingan SIFT dan ORB pada Deteksi dan Pencocokan Fitur Citra
Feature detection merupakan teknik penting dalam computer vision yang digunakan untuk mengenali objek pada citra meskipun terjadi perubahan posisi, rotasi, skala, maupun pencahayaan. Sistem pengenalan objek tidak bekerja dengan membaca seluruh piksel gambar, tetapi mencari titik-titik penting (keypoints) yang memiliki informasi paling khas dari suatu objek.

Proyek ini mengimplementasikan pipeline perbandingan dua algoritma feature detector populer yaitu SIFT (Scale Invariant Feature Transform) dan ORB (Oriented FAST and Rotated BRIEF) menggunakan OpenCV. Sistem akan melakukan deteksi keypoint, ekstraksi descriptor, serta pencocokan fitur antar dua citra.

Proyek ini bertujuan membandingkan dua algoritma feature detection populer dalam Computer Vision:
- SIFT (Scale Invariant Feature Transform)
- ORB (Oriented FAST and Rotated BRIEF)

Proyek ini dibuat sebagai tugas Uas Mata Kuliah visi komputer.
Seluruh komponen disusun sederhana, modular, serta mudah direplikasi untuk kebutuhan praktikum visi komputer maupun pembelajaran pengolahan citra digital.

## Konsep Singkat
Deteksi fitur digunakan agar komputer dapat mengenali objek yang sama walaupun:
- diputar
- iskalakan
- berubah pencahayaan
- diambil dari sudut berbeda

SIFT → lebih akurat (presisi tinggi)
ORB → lebih cepat (real-time friendly)

## Instalasi
1. Clone Repository

  ```
  git clone https://github.com/azharzuhro12/uas-viskom.git
  cd uas-viskom

  ```


2. Buat Virtual Environment
 
```
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac

```

  jika pakai conda:
```
conda create --name uas-viskom python=3.10
```

```
conda activate uas-viskom
```


3. Install Dependensi
```
pip install opencv-python opencv-contrib-python numpy matplotlib

```




## Cara Menjalankan Proyek

1. Membuat Dataset Variasi Gambar

Script ini akan membuat beberapa kondisi citra untuk menguji ketahanan algoritma.

   ```
   python dataset.py
   ```
Output akan tersimpan pada:
   ```
   dataset/
├── original.jpg
├── rotate.jpg
├── scale.jpg
├── blur.jpg
├── dark.jpg
└── perspective.jpg

   ```

2.Deteksi Keypoint
Menampilkan perbandingan jumlah dan persebaran keypoint SIFT vs ORB.
   ```
   python detect.py
   ```

Output:
- Visualisasi keypoint SIFT
- Visualisasi keypoint ORB

3.Feature Matching
Menampilkan kecocokan fitur antara dua gambar.
   ```
   python matching.py
   ```

Output:
- Garis penghubung antar fitur pada dua citra
- Menunjukkan keberhasilan pencocokan objek


## Struktur Folder
```
  proyek/
  │
  ├── dataset.py
  ├── detect.py
  ├── matching.py
  ├── dataset/
  │   └── img.jpg
  └── README.md
```

