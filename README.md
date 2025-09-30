## _**KICKS ARCHIVE**_
https://samuel-marcelino-kicksarchive.pbp.cs.ui.ac.id/ \
Pembuat: Samuel Marcelino Tindaon\
NPM: 2406435830\
Kelas: PBP A 

## Tugas 5: Penjalasan Checkpoint
**Prioritas CSS Selector**
- Jika beberapa selector diterapkan pada elemen html yang sama, maka berikut urutannya:
1. Inline Style (apapun yang di dalam style tag)
2. ID selectors
3. Classes selectors
4. Element selectors
- Misalnya terdapat berikut:
    ```css
    p { color: blue; }        
    .text { color: green; }   
    #intro { color: red; }  
    ```
    Jika elemen <p id="intro" class="text">, warna yang diterapkan adalah merah karena ID lebih spesifik.

**Responsive Design**
- Responsive design sangat penting agar aplikasi web dapat menyesuaikan dengan device klien (seperti mobile, tablet, dan desktop).
- Aplikasi web menyesuaikan secara tampilan sehingga tidak diperlukan membuat 2 versi aplikasi web yang berbeda.
- Contoh responsive: instagram &rarr; aplikasi webnya dapat diakses melalui mobile dan desktop, lalu tampilannya sudah menyesuaikan.
- Contoh belum responsive: aplikasi web sekarang ini sudah menerapkan responsive design, kemungkinan yang belum responsive adalah website tua yang sudah outdated yang biasanya tampilannya masih seperti desktop walaupun dibuka pada mobile. 

**Perbedaan Margin, Border, dan Padding**
- Margin: Jarak di luar elemen, bisa juga dikatakan menjadi jarak antar elemen
- Border: Pembatas di perimeter elemen
- Padding: Jarak antara konten elemen dengan border
- Sehingga posisi Margin paling luar, lalu border, lalu padding.

**Flex Box & Grid Layout**
- Flex box digunakan untuk membuat layout elemen pada satu arah, seperti menu horizontal. Flex box mirip dengan sebuah container yang membungkus berbagai elemen dan menyusunnya layaknya sebuah kolom atau baris (tetapi tidak keduanya) yang sudah fix (ukuran elemen fix pada salah satu dimensi). Flex box biasanya digunakan jika diperlukan keseragaman bentuk pada elemen.
- Grid layout digunakan untuk membuat layout elemen pada dua arah, seperti baris dan kolom. Jadi elemen dapat disusun pada sebuah container yang seperti sebuah grid yang cukup flexibel. Di sini, ukuran elemen bisa berubah pada dua dimensi sehingga ukuran elemen bisa berbeda-beda pada sebuah grid. Grid layout digunakan jika ingin mengimplementasi design yang kompleks, seperti ukuran elemen berbeda, jarak antar elemen berbeda, dsb.

**Implementasi Checklist**
- Fungsi untuk menghapus dan mengedit product diimplementasikan dengan membuat templatenya dan functionnya pada views.py lalu menambahkan path pada urls.py. Buat juga template html untuk hapus dan edit product. Tambahkan tombol untuk mengedit dan menghapus pada card_product.html agar muncul langsung pada card produk yang ada. 
- Kustomisasi semua template menggunakan tailwind dan css. Tambahkan file static/css/global.css pada root directory, lalu tambahkan tailwind dan css pada base.html. global.css dapat diisi dengan tampilan form yang kita inginkan. Setelah itu bisa modifikasi template yang ada dengan syntax css dan tailwind.
- Jika belum ada product yang terdaftar maka berikan informasi bahwa produk belum ada pada main.html dengan {% if not product_list %} dan else-nya jika product sudah ada.
- Product ditampilkan menggunakan template product_card.html agar terlihat rapi. card_product.html akan diisi oleh sebagian informasi tentang atribut product dan diberikan 2 label, yaitu category productnya dan apakah product tersebut featured atau tidak. 
- Tambahkan navbar yang responsiv untuk mobile dana desktop. Pada navbar.html, tambahkan code block untuk menyesuaikan dengan tampilan desktop dan mobile.


## Tugas 4: Penjalasan Checkpoint

 **AuthenticationForm**
- AuthenticationForm merupakan objek yang digunakan untuk membuat suatu form berdasarkan request dari user. AuthenticationForm digunakan saat user melakukan proses login. Dia menyediakan field username dan password beserta proses validasinya. 

**Autentikasi vs Otoriasi**
- Autentikasi merupakan proses verifikasi identitas seorang user.
- Otorisasi merupakan proses menentukan permission apa yang dimiliki oleh user yang sudah terautentikasi.
- Dalam django, proses autentikasi dilakukan saat proses login dalam AuthenticationForm. Proses otorisasi dilakukan setelah user login, misalnya ketika suatu function views.py yang diberikan @login_required, hal ini mengharuskan user login terlebih dahulu untuk bisa diakses. Contoh lainnya adalah @permissions_required. Permission default dari user sudah diberikan oleh django melalui django.contrib.auth yang ada pada INSTALLED_APPS di settings.py.

**Sessions and Cookies**
- Cookies merupakan data kecil (tentang user) yang disimpan pada browser client. 
- Kelebihan cookies: 
    - Data tersimpan pada browser client sehingga mengurangi beban server.
    - Mudah diakses sehingga cocok untuk menyimpan data seperti user preferences.
    - Data masih available ketika aplikasi dan browser ditutup.
- Kekurangan cookies:
    - Ukurannya yang kecil membatasi bentuk dan besar data yang dapat disimpan.
    - Jika security kurang aman, maka data cookies dapat dimodifikasi dengan muda dari sisi client. 
    - Rentan terhadap XSS (cross-site scripting) untuk mencuri data cookie.
- Session merupakan informasi (tentang user) yang disimpan pada server.
- Kelebihan sessions:
    - Lebih aman untuk menyimpan data besar dan sensitif (status login, keranjang pada e-commerce, dsb). 
    - Biasanya client tidak memiliki akses untuk memodifikasi data yang tersimpan pada session. 
 - Kekurangan sessions:
    - Data harus disimpan pada database, file, dsb sehingga menjadi beban untuk server.
    - Biasanya session akan hilang ketika aplikasi dan browser ditutup, jadi session akan dibuat lagi ketika user membuka aplikasi web tersebut.
    - Biasanya session id masih disimpan pada cookies sehingga muncul risiko adanya session hijacking.

**Keamanan Cookies**
- Pada umumnya, cookies tidak sepenuhnya aman karena secara default tidak encrypted dan bisa dengan mudah dimodifikasi dari sisi client. Hal ini menyebabkan munculnya beberapa risiko keamanan seperti XSS, session hijacking, dll. 
- Oleh karena itu, Django menyediakan beberapa hal untuk keamanan cookie yang bisa ditambahkan oleh developer pada projectnya.
    - Mengaktifkan secure cookie pada settings.py agar bisa mengirim cookie melalui https saja.
    - Mengaktifkan CSRF cookie dan terkait hal ini django juga sudah memiliki CSRF token.

**Checkpoint**
- Mengimport library yang dibutuhkan lalu membuat function register pada views.py menggunakan form UserCreationForm. Menyertakan juga file register.html pada folder template sebagai template untuk render pada function register. Tambahkan juga path url ke urlpatterns agar bisa dideteksi saat request.
- Mengimport library yang dibutuhkan untuk autentikasi dan sebagainya lalu membuat function login pada views.py. Menyertakan juga file login.html pada folder template sebagai template untuk render pada function login. Tambahkan juga path url ke urlpatterns agar bisa dideteksi saat request. 
- Mengimport logout lalu membuat fungsi logout pada views.py dan menambahkan tombol logout pada main.html, tambahkan juga path urlnya ke urlpatterns.   
- Agar user harus melalui proses login terlebih dahulu untuk mengakses aplikasi web, maka diberikan @login_required(login_url='/login') pada function show_main dan show_product. Hal ini memastikan user sudah login dulu agar bisa melihat main dan detail. 
- Agar mengetahu sesi terakhir login user, maka harus mengimplementasikan cookies pada aplikasi web. Maka harus mengimport library yang sesuai dan menambahkan code block untuk menyimpan data cookie last login pada function login. Tampilkan data cookie login pada variabel context di fungsi show_main. Tambahkan juga text last login pada main.html.
- Pada function logout, tambahkan block code untuk menghapus cookie last login.
- Untuk menghubungkan user dengan product, maka harus ditambahkan atribut baru yaitu user yang berupa foreign key yang berasal dari user. Pada models.py tambahkan atribut user berupa foreign key. Lakukan makemigrations dan migrate agar database terupdate.
- Ubah function create_product agar bisa menyimpan user yang membuat product tersebut. Tambahkan juga filter pada function show_main agar bisa melihat product yang dibuat oleh user itu sendiri. Tambahkan tombol filter all dan filter my product pada main.html dan tambahkan detail vendor/user yang menjual pada product_detail.html.
- Membuat 2 akun pengguna dan 3 dummy data berdasarkan model yang sudah dibuat. Hal ini diselesaikan dengan meregistrasi 2 akun baru, dan masing-masingnya menggunakan button create product dan mengisi data atribut product untuk menambahkan product baru pada database lokal. 

## Tugas 3: Penjelasan Checklist

**Data Delivery**
- Data delivery diperlukan dalam pengimplementasian sebuah platform sebagai cara untuk mengirim data di antara komponen-komponen platform. Dengan ini, pertukaran data antara client dan server bisa dilakukan. 
- Data delivery biasanya dikirim/diterima melalui http/https request. Contoh bentuk data delivery adalah html, xml, dan json.

**JSON vs XML**
- Saya pribadi lebih memilih JSON karena secara sintaks lebih mudah dibanding XML dan mirip seperti JavaScript.
- Sekarang ini, JSON lebih populer dibanding XML karena lebih readable dan ukuran filenya yang relatif lebih kecil dibanding XML untuk merepresentasikan data yang sama. Tidak hanya itu, parsing JSON lebih hemat sumber daya dibanding XML. Karena JSON berasal dari JavaScript, dia sudah disupport oleh JavaScript sehingga integrasi JSON ke aplikasi JavaScript akan sangat mudah.

**is_valid()**
- Fungsi dari method is_valid() dibutuhkan untuk mencegah masuknya data yang tidak valid pada forms, misalnya field yang masih kosong ataupun field integer yang diisi oleh string. Jika field diisi dengan data yang tidak valid, maka akan diberikan sebuah feedback kepada user untuk menggantinya. Jadi is_valid() diperlukan agar data yang masuk sesuai dengan field seharusnya. Pada project ini, hal ini diimplementasikan saat ingin membuat sebuah product baru. 

**csrf_token**
- csrf_token merupakan token security yang digenerate oleh Django. Token ini akan diverifikasi oleh server ketika mendapatkan sebuah request. Dengan verifikasi tersebut, server bisa memeriksa apakah request tersebut benar-benar datang dari client, bukan dari penyerang. Jika tidak menambahkan csrf_token, maka penyerang dapat mengirim request semaunya kepada server dan server akan menerima request tersebut layaknya request dari client. Hal ini terjadi karena tanpa adanya csrf_token, server tidak mempunyai cara untuk memverifikasi request sehingga dia akan menjalankan request apapun yang datang, bahkan jika datang dari penyerang.

**Implementasi Checklist**
- Menambahkan function show_xml, show_json, show_xml_by_id, show_json_by_id pada views.py. 
- Untuk show_xml dan show_json, sebuah variabel akan menyimpan hasil query dari data-data yang ada pada Product. Selanjutnya, query tersebut akan dikonversi menjadi xml/json menggunakan serializers.serialize, akhirnya function show_xml/show_json akan me-return function HttpResponse dengan parameter query yang sudah serialized dan content_type="xml" atau "json". Dengan ini, data dapat dikembalikan dalam bentuk xml maupun json.
- Untuk by_id, query akan di-filter atau di-get agar query yang muncul sesuai dengan id yang kita cari. Tidak hanya itu, ditambahkan juga try except agar dapat muncul exception HttResponse status 404 jika id tidak ditemukan.
- Routing dilakukan dengan mengimport show_xml, show_json, show_xml_by_id, show_json_by_id ke urls.py lalu menambahkan path URL-nya ke dalam list urlpatterns agar dapat diakses. 
- Untuk membuat tombol Add dan Details, dimulai dengan membuat function add_product dan show_product pada views.py dan membuat file template create_product.html dan product_detail.html.
- Untuk tombol Add, function add_product diisi dengan me-return render form seseuai dengan template create_product.html dan memeriksa data yang diberikan pada form tersebut sudah valid. 
- Untuk tombol Details, function show_product diisi dengan function get_object_or_404 untuk membuka object dengan id yang diberikan pada parameter (id) agar dapat me-return render dari object yang diinginkan sesuai template product_detail.html.
- Pada urls.py, create_product dan show_product diimport dan path url-nya ditambahkan ke urlpatterns agar bisa diakses.
- Agar tombolnya muncul, maka diimplementasikan pada main.html dengan 
    ```html
    <a href="{% url 'main:create_product' %}">
        <button>+ Add Product</button>
    </a>
    ```
    dan
    ```html
    <p><a href="{% url 'main:show_product' product.id %}"><button>Details</button></a></p>
    ```
- Halaman untuk form pada create_product.html berupa sebuah template html yang akan menampilkan atribut-atribut yang perlu diisi oleh user sesuai dengan data fieldnya. 
- Halaman untuk detail pada show_product.html berupa sebuah template html yang akan menampilkan atribut-atribut dari product yang ada. 
- Screenshot akses url xml dan json pada postman: https://drive.google.com/drive/folders/1lTejaewhVXlv150Mmnsi5ilbCJ1HwA63?usp=sharing
    

## Tugas 2: Penjelasan Checklist

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