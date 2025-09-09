## _**KICKS ARCHIVE**_
https://samuel-marcelino-kicksarchive.pbp.cs.ui.ac.id/ \
Pembuat: Samuel Marcelino Tindaon\
NPM: 2406435830\
Kelas: PBP A 

## Penjelasan Checklist

**Membuat Project**
- Membuat direktori project baru lalu mengaktifkan virtual environment.
- Inisiasi Git dan buat remote yang sesuai pada repository GitHub dan membuat branch Master.
- Menambahkan file .gitignore yang berisi file yang harus diabaikan Git agar temporary file, konfigurasi pribadi, dsb tidak di-push ke repository GitHub.
- Instalasi dependencies (django, gunicorn, whitenoise, ...) yang tertera pada requirements.txt
- Start project baru bernama kicks_archive dengan: 
    ```bash
    django-admin startproject kicks_archive .
    ```
**Konfigurasi Environment Variables**
- Membuat file .env pada direktori utama dan menulis PRODUCTION=False agar kode bisa berjalan pada environment yang berbeda.
- Membuat file .env.prod untuk konfigurasi production dan diisi dengan kredensial database.
**Konfigurasi settings.py**
- Menambahkan kode berikut pada settings.py : 
    ```bash
    import os
    from dotenv import load_dotenv
    load_dotenv()
    ``` 
    agar bisa menggunakan variabel environment dari .env
- Menambahkan localhost dan 127.0.0.1 pada ALLOWED_HOSTS agar bisa diakses jaringan pribadi (local). 
- Menambahkan kode berikut :
    ```bash
    PRODUCTION = os.getenv('PRODUCTION', 'False').lower() == 'true'
    ```
    agar bisa mendeteksi variabel environment PRODUCTION
- Melakukan konfigurasi database, saat PRODUCTION=True menggunakan PostgreSQL dengan kredensial dari variabel environment. Saat PRODUCTION=False menggunakan SQLite.
**Konfigurasi PWS**
- Buat project baru pada PWS dan simpan kredensial.
- Tambahkan kredensial pada env.prod pada project menggunakan raw editor.
- Tambahkan URL deployment PWS pada ALLOWED_HOSTS agar project dapat diakses dari URL PWS.
- Bisa melakukan git add, commit, push PWS.
**Membuat Aplikasi**
- Membuat aplikasi dengan nama main :
    ```bash
    python manage.py startapp main
    ```
- Tambahkan aplikasi main pada INSTALLED_APPS di settings.py
**Membuat Template**
- Pada folder main, buat folder bernama templates yang berisi file main.html
- Isi main.html sesuai ketentuan.

**Membuat Model**
- Pada models.py tambahkan model yang diinginkan (pada tugas ini bernama Product).
- Tambahkan atribut yang diinginkan pada class Product (name, price, description, thumbnail, category, is_featured, created_at, id, stock) dengan field yang sesuai.
- Migrasi model agar bisa melacak perubahan database dengan :
    ```bash
    python manage.py makemigrations
    python manage.py migrate 
    ```
    Setiap kali ada perubahan model, harus di migrate.
**Membuat View**
- Pada views.py, tambahkan show_main yang akan menerima request. Tambahkan juga dictionary context yang diinginkan.
- show_main akan me-return render dari request, "main.html", dan context. Fungsi render akan menampilkan context pada file main.html (templatenya)
**Routing pada main**
- Membuat file urls.py pada folder main dan isi dengan routing ke main.
- Pada urls.py, tambahkan juga list urlpatterns yang berisi fungsi path dengan argumen '' (root), show_main, dan name="show_main". Dengan ini, view show_main akan terpanggil dan name="show_main" memudahkan kita menggunakan reverse url.
**Routing pada Project**
- Pada level project, di urls.py, tambahkan juga list urlpatterns dengan isi fungsi path dengan argumen '', dan include("main.urls") agar bisa mengimpor pola rute URL dari aplikasi main.
**Push GitHub dan PWS**
- Melakukan git add, commit, dan push ke GitHub dan PWS.
## Penjelasan Request Client ke Web
Bagan: https://drive.google.com/file/d/1f5MR2YV8gy79LrWE_ii231OWO8RbVMIF/view?usp=sharing
- User akan mengirimkan request http yang akan diterima oleh urls.py pada level project.
- Jika pola endpoint ditemukan, request akan dilanjutkan ke urls.py pada level aplikasi. Jika tidak, maka akan 404 not found error.
- views.py akan menerima argumen berupa request dan me-return render.
- models.py akan menyediakan data bagi views.py jika dibutuhkan.
- Render yang di-return dari views.py akan ditampilkan oleh template.html
- Tampilan akan muncul pada browser user.
## Peran settings.py
settings.py adalah pusat konfigurasi project Django untuk berbagai hal :
- INSTALLED_APPS &rarr; Menentukan aplikasi yang dipakai.
- DATABASES &rarr; Untuk konfigurasi database (pakai database apa).
- ALLOWED_HOSTS &rarr; Mengatur host mana saja yang bisa mengakses.
- TEMPLATES &rarr; Konfigurasi mesin template.
- PRODUCTION dan DEBUG &rarr; Menentukan apakah aplikasi sudah bisa berjalan atau tidak.
- MIDDLEWARE &rarr; Sebagai pipeline request yang akan diproses.
- LANGUAGE_CODE dan TIME_ZONE &rarr; Menandakan bahasa dan zona waktu yang digunakan.
## Migrasi Database
- Migrasi database pada Django dilakukan dengan menjalankan 2 command.
    Untuk menghasilkan file migrasi baru pada direktori NamaAplikasi/migrations :
    ```bash
    python manage.py makemigrations
    ```
    Untuk menerapkan migrasi ke database : 
    ```bash
    python manage.py migrate
    ```
- Saat makemigrations, Django membandingkan model saat ini dengan model yang dulu, lalu membuat file yang berjudul perubahan apa yang dilakukan terhadap model.
- Saat migrate, Django akan membaca file migrasi yang belum diterapkan lalu menambahkannya pada database dan akan dicatat oleh Django.
## Mengapa Django sebagai Permulaan?
- Django adalah framework yang menyediakan banyak fitur siap pakai.
- Programming language python membuatnya lebih mudah diakses.
- Bisa menggunakan konsep MVT yang relatif rapi karena memisahkan model, view, dan template.
- Tersedia banyak tutorial Django dan dokumentasi serta komunitasnya besar sehingga mudah menemukan cara belajar.
- Django bisa digunakan dari project kecil hingga project skala besar. 
## Feedback
- Selama mengerjakan tutorial, saya merasa sangat terbantu dengan instruksi-instruksi yang sangat detail. Alurnya sangat mudah diikuti dan gaya bahasanya mudah dipahami (model poin-poin dan terpisahnya subtopik). Saya harap tutorial selanjutnya akan mirip tutorial 0 dan 1. 
