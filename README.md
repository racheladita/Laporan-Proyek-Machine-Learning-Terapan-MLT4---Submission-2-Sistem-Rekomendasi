# **Laporan Proyek _Machine Learning_ - Adita Putri Puspaningrum**

---

# **SISTEM REKOMENDASI FILM**

# **Domain Proyek**

Dalam era modern, industri film telah mengalami kemajuan pesat dengan munculnya berbagai platform digital dan situs _streaming_ film. Menurut survey yang dilakukan oleh Populix [1], Netflix adalah platform _streaming_ film yang paling digemari di Indonesia, disusul Disney+ Hotstar, Viu, WeTV, dan lain-lain. Akses yang mudah ke berbagai macam film dari seluruh dunia telah membuka peluang bagi pengguna untuk menikmati hiburan film secara luas dan bervariasi. Namun, kemajuan ini juga membawa masalah baru, yaitu munculnya kebingungan dalam memilih film di tengah banyaknya pilihan yang tersedia.

Masalah pemilihan film menjadi semakin kompleks seiring meningkatnya jumlah produksi film dari berbagai _genre_ dan budaya. Setiap pengguna memiliki preferensi dan selera yang berbeda-beda, serta latar belakang budaya dan nilai yang beraneka ragam. Kekhawatiran utama adalah bagaimana memberikan pengalaman yang memuaskan bagi pengguna dengan menawarkan film-film yang sesuai dengan minat dan preferensinya. Untuk mengatasi masalah ini, perusahaan film dan platform _streaming_, seperti Netflix, telah mulai mengembangkan sistem rekomendasi yang inovatif.

Sistem rekomendasi merupakan sebuah aplikasi yang bertujuan untuk memberikan suatu informasi mengenai saran/rekomendasi ataupun penilaian akan suatu hal yang dapat memberi manfaat bagi penggunanya [2]. Dalam hal ini, sistem rekomendasi film merupakan solusi yang sangat diharapkan untuk membantu pengguna dalam memilah-milah film melalui banyaknya pilihan film yang ada. Dengan menggunakan data historis dari preferensi dan penilaian film oleh pengguna itu sendiri, serta data kolaboratif dari pengguna lain dengan minat serupa, sistem rekomendasi berusaha memberikan rekomendasi yang tepat dan relevan untuk setiap pengguna.

Dalam era digital yang serba cepat, jumlah film yang tersedia untuk ditonton semakin melonjak, sehingga pengguna sering kali dibombardir dengan kelebihan informasi. Sistem rekomendasi berfungsi sebagai kurator yang membantu menyaring dan menyarankan pilihan film yang paling relevan bagi setiap pengguna, sehingga diharapkan para pengguna dapat menghemat waktu serta menghemat usaha yang dikeluarkan pada saat mencari film yang akan ditonton.

Dengan memanfaatkan data dari aktivitas sebelumnya, seperti riwayat penontonan dan ulasan (_rating_) yang diberikan, sistem rekomendasi dapat memberikan rekomendasi film yang sesuai dengan minat dan preferensi masing-masing pengguna. Hal ini menciptakan pengalaman menonton yang lebih personal dan memuaskan. Dengan menyajikan rekomendasi yang akurat dan menarik, sistem rekomendasi dapat membantu meningkatkan retensi pengguna dalam menggunakan suatu platform _streaming_ film. Pengguna cenderung lebih lama berinteraksi dengan layanan yang menyajikan konten yang relevan dan menarik bagi dirinya.

Meskipun sistem rekomendasi menawarkan banyak manfaat, mengembangkan sistem yang akurat dan efektif juga melibatkan beberapa tantangan. Untuk memperoleh data yang berkualitas dan relevan, data harus mencakup preferensi pengguna, riwayat penontonan, dan peringkat film yang memadai untuk memberikan rekomendasi yang akurat. Dalam platform besar seperti Netflix, jumlah pengguna dan film sangat besar, sehingga mengelola data sebanyak itu dan menyajikan rekomendasi secara efisien adalah tugas yang kompleks.

# **_Business Understanding_**

Penelitian ini bertujuan untuk mengembangkan sistem rekomendasi film yang efektif dan akurat dalam menyajikan rekomendasi film yang lebih sesuai dengan minat dan preferensi masing-masing pengguna. Dengan begitu, pelaku bisnis dari platform _streaming_ film dapat menentukan target penonton dengan lebih tepat dan memberikan pengalaman menonton yang lebih personal dan memuaskan bagi para penggunanya. Dengan memanfaatkan teknologi dan data yang tepat, diharapkan sistem rekomendasi ini dapat terus berkembang dan memberikan manfaat yang lebih besar bagi industri film dan para penikmat film di seluruh dunia.

*   _Problem Statements_
    
    Berdasarkan uraian latar belakang masalah yang telah dijelaskan pada bagian sebelumnya, berikut ini merupakan rumusan masalah dari penelitian ini :

    a.   Bagaimana membuat sistem rekomendasi film berdasarkan data historis dari preferensi dan penilaian film oleh pengguna itu sendiri ?
    
    b.   Bagaimana membuat sistem rekomendasi film berdasarkan data kolaboratif dari pengguna lain dengan minat serupa ?

*   _Goals_
  
    Berikut ini merupakan uraian tujuan dari rumusan masalah yang telah dijelaskan :
    
    a.   Membuat sistem rekomendasi film berdasarkan data historis dari preferensi dan penilaian film oleh pengguna itu sendiri.
    
    b.   Membuat sistem rekomendasi film berdasarkan data kolaboratif dari pengguna lain dengan minat serupa.

*   _Solution Statements_
  
    Untuk memenuhi tujuan dari penelitian ini, berikut merupakan solusi yang dapat penulis ajukan :
    
    a.   Untuk membuat sistem rekomendasi film berdasarkan data historis dari preferensi dan penilaian film oleh pengguna itu sendiri akan digunakan metode _Content Based Filtering_. _Content Based Filtering_ mempelajari profil minat pengguna dengan menyarankan item serupa yang pernah disukai di masa lalu atau sedang dilihat di masa kini kepada pengguna [3].
    
    b.   Untuk membuat sistem rekomendasi film berdasarkan data kolaboratif dari pengguna lain dengan minat serupa akan digunakan metode _Collaborative Filtering_. _Collaborative Filtering_ adalah metode yang mengandalkan pendapat dari pengguna lain yang memiliki minat/preferensi serupa dengan melakukan pencarian pola kesamaan dan perbedaan dalam pilihan film untuk memberikan rekomendasi yang relevan [3]. 

# **_Data Understanding_**

* Penelitian ini menggunakan dataset yang berjudul 'Movie Recommendation Data' yang diambil dari Kaggle dengan link [dataset](https://www.kaggle.com/datasets/rohan4050/movie-recommendation-data).

* Dataset ini memiliki 5 _file_ dengan format CSV (*comma separated value*). Salah satu dari _file_ tersebut merupakan _file_ metadata film. Metadata adalah dokumen yang berisi mengenai informasi tambahan tentang suatu film, seperti sinopsis, sutradara, pemeran, durasi, dan bahasa film. Namun, dalam penelitian ini, _file_ metadata tidak akan digunakan karena fokus utama pada penelitian ini adalah membangun model sistem rekomendasi berdasarkan penilaian pengguna. Berikut merupakan keempat _file_ yang akan dipakai untuk membangun model :

  1.  links.csv : _file_ ini berisi daftar variabel _link_ dari film yang berjumlah 9742 data unik.
  2.  movies.csv : _file_ ini berisi daftar dari variabel film yang tersedia yang berjumlah 9742 data unik.
  3.  ratings.csv : _file_ ini berisi daftar variabel penilaian yang diberikan oleh pengguna untuk suatu film yang berjumlah 100836 data.
  4.  tags.csv : _file_ ini berisi daftar variabel kata kunci dari masing-masing film yang tersedia yang berjumlah 1572 data unik.
      
  Tahapan selanjutnya adalah melakukan eksplorasi terhadap data dengan teknik _univariate exploratory data analysis_. Tahap eksplorasi penting untuk dilakukan karena bertujuan untuk memahami variabel-variabel yang terdapat pada data beserta korelasi antar variabelnya [3]. Analisis data _univariate_ dilakukan dengan mengeksplorasi data yang melibatkan penelitian lebih lanjut tentang setiap variabel secara terpisah. Pada tahapan ini, akan dilakukan eksplorasi data terhadap seluruh variabel yang telah disebutkan sebelumnnya, yaitu variabel 'links', 'movies', 'tags' dan juga 'ratings'.

  Selain itu, proses yang tidak kalah penting untuk dilakukan, yaitu melakukan _pre-processing_ terhadap data sebelum diolah ke tahapan selanjutnya. Tahapan _pre-processing_ data bertujuan untuk membersihkan, mengubah, atau mengorganisasi data agar siap untuk tahap pemodelan [4]. Pada penelitian ini, _pre-processing_ data diawali dengan melakukan penggabungan seluruh data pada seluruh variabel dengan mengkorelasikan tiap-tiap data pada masing-masing variabel dengan menggunakan kolom 'movieId' yang unik untuk kategori 'movie' dan menggunakan kolom 'userId' yang unik untuk kategori 'user' sebagai acuan dalam penggabungan ini. Kemudian, data yang sama (data duplikat) akan dihapus agar data yang terdapat pada masing-masing kategori ('movie' dan 'user') bersifat unik.

# **_Data Preparation_**

Berikut ini merupakan tahapan-tahapan yang dilakukan dalam mempersiapkan data untuk model yang dibangun dengan metode _Content Based Filtering_.

*   Menghilangkan _Missing Value_

    Setelah dilakukan proses penggabungan data dari beberapa variabel, ditemukan _missing value_ akibat banyaknya fitur yang digabungkan dari variabel-variabel tersebut. _Missing value_ ini ditemukan pada fitur 'tag', dimana _missing value_ yang terdeteksi sebanyak 52.549 data. Meskipun jumlah data ini sangat signifikan, _missing value_ ini akan dihapus dari dataset dikarenakan fitur ini kurang berpengaruh terhadap sistem rekomendasi yang akan dibangun. 

*   Menghapus Data Duplikat
  
    Selanjutnya, dilakukan penghapusan data duplikat dari fitur 'movieId' menggunakan fungsi drop_duplicates(). Langkah ini penting untuk dilakukan karena dalam pemodelan yang dibangun, hanya akan digunakan fitur 'movieId' yang unik untuk membangun model rekomendasi.

*   Membuat _Dictionary_
  
    Selanjutnya, dilakukan proses pembuatan _dictionary_ yang digunakan untuk menentukan pasangan _key-value_ pada data yang telah disiapkan sebelumnya. Setelah proses ini selesai dijalankan, data telah siap untuk dimasukkan ke dalam pemodelan untuk model yang dibangun dengan metode _Content Based Filtering_.
     
Sedangkan berikut ini merupakan tahapan-tahapan yang dilakukan dalam mempersiapkan data untuk model yang dibangun dengan metode _Collaborative Filtering_.

*   Memahami Data _Rating_

    Pada tahap ini, perlu dilakukan pemahaman terhadap data _rating_ yang dimiliki. Data _rating_ berisi penilaian yang diberikan oleh pengguna untuk berbagai film. Penilaian ini akan menjadi dasar dalam membangun model rekomendasi menggunakan metode _Collaborative Filtering_.
    
*   Melakukan Proses _Encoding_

    Fitur 'user' dan 'movieId' perlu di-_encode_ menjadi indeks bilangan bulat (_integer_) agar dapat digunakan dalam model _Collaborative Filtering_. Indeks ini memudahkan proses perhitungan dalam model dan menghindari kesalahan saat melakukan perbandingan.
    
*   Memetakan ‘userId’ dan ‘movieId’ ke _Dataframe_ yang Berkaitan.

    Kemudian, akan dilakukan pemetaan 'userId' dan 'movieId' ke _dataframe_ yang berkaitan. Hal ini memungkinkan untuk menyusun data secara efisien dan membentuk matriks peringkat (_rating matrix_) yang diperlukan dalam model _Collaborative Filtering_.
    
*   Mengecek Beberapa Hal dalam Data.

    Proses ini mencakup pemeriksaan beberapa hal seperti jumlah pengguna (_user_) dan jumlah film yang ada dalam dataset. Kemudian, perlu juga mengubah nilai _rating_ menjadi _float_ agar dapat digunakan dalam perhitungan yang lebih tepat.

*   Membagi Data

    Langkah selanjutnya adalah membagi data menjadi dua _subset_, yaitu data latih (_training data_) dan data validasi (_validation data_) dengan rasio 80 : 20. Data latih digunakan untuk melatih model _Collaborative Filtering_ dengan cara mempelajari pola dari data _rating_ yang ada, sementara data validasi digunakan untuk menguji kinerja model yang telah dilatih dan melihat sejauh mana model dapat memberikan rekomendasi yang akurat dan relevan terhadap data yang belum pernah dilihat sebelumnya. Penggunaan data latih dan data validasi ini bertujuan untuk mengevaluasi performa model dan mencegah _overfitting_. 

# **_Modeling and Result_**

Seperti yang telah dijelaskan pada bagian sebelumnya, pada penelitian ini akan dilakukan pemodelan dengan menggunakan 2 metode yang berbeda sesuai dengan permasalahan yang berbeda pula, yaitu metode _Content Based Filtering_ dan metode _Collaborative Filtering_.

*  _Content Based Filtering_

   _Content Based Filtering_ adalah sistem rekomendasi yang mempelajari profil minat pengguna dengan menyarankan item serupa yang pernah disukai di masa lalu atau sedang dilihat di masa kini kepada pengguna [3]. Model ini membangun profil minat pengguna dengan cara mengekstrak informasi dari atribut seperti judul film, genre, dan fitur-fitur lainnya yang terkait dengan film-film yang pernah disukai atau dilihat oleh pengguna tersebut. Ketika seorang pengguna mencari rekomendasi film baru, sistem akan mencari film-film yang memiliki profil minat yang serupa dengan film-film yang telah disukai oleh pengguna di waktu sebelumnya. Dengan cara ini, film-film yang serupa dengan preferensi pengguna akan dijadikan rekomendasi.

   Kelebihan dari metode _Content Based Filtering_ antara lain tidak memerlukan data dari pengguna lain, sehingga dapat memberikan rekomendasi untuk pengguna baru (_cold-start problem_), rekomendasi bersifat personal dan sesuai dengan preferensi individual pengguna, karena model memperhatikan riwayat penilaian pengguna, serta mampu merekomendasikan film yang kurang populer atau tidak dikenal, karena model tidak hanya mengandalkan popularitas film namun mencoba memahami minat pengguna terhadap preferensi suatu film.

   Sedangkan kekurangan metode _Content Based Filtering_ antara lain terbatas dalam mengidentifikasi film baru yang belum pernah dinilai oleh pengguna, karena bergantung pada atribut film yang telah dikenali dan rentan terhadap _overfitting_ jika fitur-fitur yang digunakan tidak cukup representatif atau terlalu spesifik.

   Pada penelitian ini, sistem rekomendasi yang telah berhasil dibangun menggunakan metode _Content Based Filtering_ akan diuji untuk mendapatkan rekomendasi film yang mirip dengan Star Wars: Episode III - Revenge of the Sith.

   ![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-2-Sistem-Rekomendasi/assets/77524477/791a9c86-24cc-471c-abf4-f70bb516d3e3)

   Gambar 1. Contoh data uji, yaitu film Star Wars: Episode III - Revenge of the Sith
   
   Berikut ini merupakan hasil dari top-5 rekomendasi film yang mirip dengan film Star Wars: Episode III - Revenge of the Sith.

   ![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-2-Sistem-Rekomendasi/assets/77524477/8cfccec9-72a5-4ad8-95ce-a16779f667ca)

   Gambar 2. Hasil dari top-5 rekomendasi film yang mirip dengan film Star Wars: Episode III - Revenge of the Sith

   Dari Gambar 2 dapat dilihat bahwa film dengan _genre_ antara 'Action', 'Adventure' atau 'Sci-Fi' menjadi film yang direkomendasikan oleh sistem. Hal ini didasarkan pada _genre_ film data uji pada Gambar 1 yang dianggap sebagai film yang pernah ditonton atau disukai oleh seorang penonton/pengguna di masa lalu.
   
*  _Collaborative Filtering_
  
   _Collaborative Filtering_ adalah metode yang mengandalkan pendapat dari pengguna lain yang memiliki minat/preferensi serupa dengan melakukan pencarian pola kesamaan dan perbedaan dalam pilihan film untuk memberikan rekomendasi yang relevan [3]. Model ini tidak memperhatikan atribut film, tetapi lebih fokus pada data penilaian yang diberikan oleh pengguna. Ketika seorang pengguna mencari rekomendasi, model akan mencari pengguna lain dengan pola penilaian yang mirip dan memberikan rekomendasi film yang disukai oleh pengguna dengan preferensi serupa. Dengan pendekatan ini, film-film yang populer di kalangan pengguna dengan preferensi serupa akan dijadikan rekomendasi.

   Kelebihan metode _Collaborative Filtering_ antara lain mampu memberikan rekomendasi yang akurat dan relevan berdasarkan pola penilaian dari pengguna lain dengan preferensi serupa, dapat merekomendasikan film-film baru yang belum pernah dilihat oleh pengguna, karena model tidak bergantung pada atribut film serta efektif dalam menangani masalah skala besar, karena mengandalkan data interaksi antara pengguna.

   Sedangkan kekurangan metode _Collaborative Filtering_ adalah tidak efektif untuk pengguna baru (_cold-start problem_) atau film baru, karena membutuhkan data penilaian dari pengguna terkait sebelumnya dan cenderung menghasilkan rekomendasi yang populer secara keseluruhan, sehingga mungkin mengabaikan preferensi individu tertentu.

   Pada penelitian ini, sistem rekomendasi yang telah berhasil dibangun menggunakan metode _Collaborative Filtering_ akan diuji untuk mendapatkan rekomendasi film untuk seorang pengguna dimana hasil rekomendasi merupakan rekomendasi yang mengandalkan pendapat dari pengguna lain.

   ![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-2-Sistem-Rekomendasi/assets/77524477/f7662449-7804-4c06-9ced-0ab6ab67e714)

   Gambar 3. Hasil dari top-10 rekomendasi film yang mengandalkan pendapat dari pengguna lain

   Dari Gambar 3 dapat dilihat bahwa film dengan _genre_ drama menjadi film yang paling tinggi _rating_-nya. Selanjutnya, sistem memberikan top-10 rekomendasi film dengan mayoritas _genre_-nya adalah drama. Dapat dilihat bahwa dari 10 rekomendasi film, 7 diantaranya merupakan film dengan _genre_ drama, sehingga hasil ini sesuai dengan _rating genre_ film tertinggi yang telah dinilai oleh pengguna lain.

# **_Evaluation_**

Pada penelitian ini, proses evaluasi dilakukan dengan menggunakan _precision_ dan metrik evaluasi dengan matplotlib. _Precision_ adalah kecocokan antara bagian data yang diambil dengan informasi yang dibutuhkan [5]. Pada penelitian ini, _precision_ digunakan untuk mengevaluasi metode _Content Based Filtering_. Sedangkan metrik evaluasi dengan matplotlib digunakan untuk mengevaluasi metode _Collaborative Filtering_.  

_Precision_ didefinisikan dalam persamaan berikut :

$$ P = \frac {Rekomendasi yang relevan} {Jumlah item yang direkomendasikan} $$

Jika diterapkan pada hasil dari top-5 rekomendasi film yang dihasilkan oleh metode _Content Based Filtering_, maka hasil _precision_-nya adalah sebagai berikut :

$$ P = \frac {Rekomendasi yang relevan} {Jumlah item yang direkomendasikan} $$
$$ P = \frac {5} {5} $$
$$ P = 1 $$

Sehingga dapat disimpulkan bahwa sistem rekomendasi dengan menggunakan metode _Content Based Filtering_ menghasilkan hasil keluaran dengan kecocokan yang tinggi, karena hasil perhitungan _precision_-nya sama dengan 1.

Sedangkan hasil dari metrik evaluasi untuk metode _Collaborative Filtering_ yang menggunakan grafik dari matplotlib, dapat dilihat pada Gambar 4. 

![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-2-Sistem-Rekomendasi/assets/77524477/bcdccfab-1e64-4ff4-b20d-72d70aa7e572)

Gambar 4. Metrik evaluasi untuk metode _Collaborative Filtering_

Dari Gambar 4 dapat dilihat bahwa proses pelatihan model cukup _smooth_ dan model konvergen pada _epochs_ sekitar 40. Dari proses ini, diperoleh nilai _error_ akhir sebesar 0.1764 dan nilai _error_ pada data validasi sebesar 0.2040. Nilai tersebut cukup bagus untuk sebuah sistem rekomendasi. 

# **Kesimpulan**

Penelitian ini bertujuan untuk mengembangkan sistem rekomendasi film yang efektif dan akurat dalam menyajikan rekomendasi film yang lebih sesuai dengan minat dan preferensi masing-masing pengguna. Dengan begitu, pelaku bisnis dari platform _streaming_ film dapat menentukan target penonton dengan lebih tepat dan memberikan pengalaman menonton yang lebih personal dan memuaskan bagi para penggunanya. Dari penelitian ini, berhasil dibuat dua sistem rekomendasi dengan hasil yang cukup baik pula, yaitu sistem rekomendasi film berdasarkan data historis dari preferensi dan penilaian film oleh pengguna itu sendiri dengan menggunakan metode _Content Based Filtering_ yang menghasilkan _precision_ mendekati angka 1 dan sistem rekomendasi film berdasarkan data kolaboratif dari pengguna lain dengan minat serupa dengan menggunakan metode _Collaborative Filtering_ dimana nilai _error_ akhir sebesar 0.1764 dan nilai _error_ pada data validasi sebesar 0.2040, kedua nilai _error_ ini cukup bagus untuk sebuah sistem rekomendasi.

Meskipun tujuan utama penelitian ini telah tercapai, untuk optimalisasi lebih lanjut, beberapa improvisasi pada model dapat dilakukan untuk meningkatkan kualitas rekomendasi sehingga dapat memberikan wawasan yang lebih akurat dan relevan bagi para penggunanya dengan lebih tepat dan efisien.

# **Referensi**

[1]    N. A. Munawaroh, S. Kalimah, dan Z. Muttaqien, “Netflix In Indonesia : Customer Willingness To Pay in Video Streaming
Service,” _Jesya Jurnal Ekonomi & Ekonomi Syariah_, vol. 6, no. 1, Jan. 2023, doi:  https://doi.org/10.36778/jesya.v6i1.1136. [Online]. Tersedia: [tautan]([http://dx.doi.org/10.3390/su10072336](https://stiealwashliyahsibolga.ac.id/jurnal/index.php/jesya/article/download/1136/581)). 

[2]    S. Sari dan D. T. Hendra, “Aplikasi Rekomendasi Film menggunakan Pendekatan Collaborative Filtering dan Euclidean Distance sebagai ukuran kemiripan rating ISBN : 979-26-0280-1 ISBN : 979-26-0280-1,” pp. 135–140, 2015.

[3]    dicoding. "Rangkuman Studi Kasus Keempat: Sistem Rekomendasi". Tersedia: [tautan](https://www.dicoding.com/academies/319/tutorials/19672). Diakses pada 31 Juli 2023.

[4]   Binus University Graduate Program. “Teknik pre-processing dan classification dalam data science,”. Tersedia: [tautan](https://mie.binus.ac.id/2022/08/26/teknik-pre-processing-dan-classification-dalam-data-science/). Diakses pada 31 Juli 2023.

[5] E-Jurnal UAJY. Tersedia: [tautan](http://e-journal.uajy.ac.id/11794/4/TF070093.pdf). Diakses pada 31 Juli 2023.
