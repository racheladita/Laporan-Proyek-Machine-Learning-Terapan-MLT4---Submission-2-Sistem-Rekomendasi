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

*   Penjelasan Tambahan

    Berikut adalah penjelasan mengenai arti dari kolom-kolom pada dataset yang akan digunakan. Diharapkan dengan adanya penjelasan tambahan ini, informasi yang tersedia dalam masing-masing dataset menjadi lebih jelas dan dapat membantu dalam pemahaman lebih lanjut tentang data yang digunakan dalam penelitian ini.

    1. Dataset 'links.csv':

       * 'movieId' : Nomor unik yang merupakan identifikasi untuk masing-masing film dalam dataset.
       * 'imdbId' : Nomor unik yang merupakan identifikasi untuk masing-masing film pada IMDb (_Internet Movie Database_).
       * 'tmdbId' : Nomor unik yang merupakan identifikasi untuk masing-masing film pada TMDb (_The Movie Database_).

    2. Dataset 'movies.csv':

       * 'movieId' : Nomor unik yang merupakan identifikasi untuk masing-masing film dalam dataset.
       * 'title' : Judul dari film yang bersangkutan.
       * 'genres' : _Genre-genre_ yang diwakili oleh film tersebut. Satu film bisa memiliki beberapa _genre_ yang dipisahkan oleh karakter '|'.

    3. Dataset 'ratings.csv':

       * 'userId' : Nomor unik yang merupakan identifikasi untuk masing-masing pengguna dalam dataset.
       * 'movieId' : Nomor unik yang merupakan identifikasi untuk masing-masing film dalam dataset.
       * 'rating' : Penilaian yang diberikan oleh pengguna untuk suatu film. Nilai _rating_ berkisar antara 0.5 hingga 5.0 dalam interval 0.5.

    4. Dataset 'tags.csv':

       * 'userId' : Nomor unik yang merupakan identifikasi untuk masing-masing pengguna dalam dataset.
       * 'movieId' : Nomor unik yang merupakan identifikasi untuk masing-masing film dalam dataset.
       * 'tag' : Kata kunci atau _tag_ yang diberikan oleh pengguna untuk suatu film.

# **_Data Understanding_**

* Penelitian ini menggunakan dataset yang berjudul 'Movie Recommendation Data' yang diambil dari Kaggle dengan link [dataset](https://www.kaggle.com/datasets/rohan4050/movie-recommendation-data).

* Dataset ini memiliki 5 _file_ dengan format CSV (*comma separated value*). Salah satu dari _file_ tersebut merupakan _file_ metadata film. Metadata adalah dokumen yang berisi mengenai informasi tambahan tentang suatu film, seperti sinopsis, sutradara, pemeran, durasi, dan bahasa film. Namun, dalam penelitian ini, _file_ metadata tidak akan digunakan karena fokus utama pada penelitian ini adalah membangun model sistem rekomendasi berdasarkan penilaian pengguna. Berikut merupakan keempat _file_ yang akan dipakai untuk membangun model :

  1.  links.csv : _file_ ini berisi daftar variabel _link_ dari film yang berjumlah 9742 data unik.
  2.  movies.csv : _file_ ini berisi daftar dari variabel film yang tersedia yang berjumlah 9742 data unik.
  3.  ratings.csv : _file_ ini berisi daftar variabel penilaian yang diberikan oleh pengguna untuk suatu film yang berjumlah 100836 data.
  4.  tags.csv : _file_ ini berisi daftar variabel kata kunci dari masing-masing film yang tersedia yang berjumlah 1572 data unik.
      
  Tahapan selanjutnya adalah melakukan eksplorasi terhadap data dengan teknik _univariate exploratory data analysis_. Tahap eksplorasi penting untuk dilakukan karena bertujuan untuk memahami variabel-variabel yang terdapat pada data beserta korelasi antar variabelnya [3]. Analisis data _univariate_ dilakukan dengan mengeksplorasi data yang melibatkan penelitian lebih lanjut tentang setiap variabel secara terpisah. Pada tahapan ini, akan dilakukan eksplorasi data terhadap seluruh variabel yang telah disebutkan sebelumnnya, yaitu variabel 'links', 'movies', 'tags' dan juga 'ratings' dengan menggunakan fungsi info(), head() dan describe(). Tabel 1 akan menampilkan contoh hasil keluaran dari eksplorasi data dengan menggunakan fungsi info(). Tabel 2 akan menampilkan contoh hasil keluaran dari eksplorasi data dengan menggunakan fungsi head(). Sedangkan Tabel 3 akan menampilkan contoh hasil keluaran dari eksplorasi data dengan menggunakan fungsi describe().

  |  #  |  Column   |  Non-Null Count |  Dtype  |
  |-----|-----------|-----------------|---------|
  |  0  |  movieId  |  9742 non-null  |  int64  |
  |  1  |  title    |  9742 non-null  |  object |
  |  2  |  genres   |  9742 non-null  |  object |

  Tabel 1. Hasil keluaran dari movies.info()

  Fungsi info() akan menampilkan informasi detail tentang _dataframe_, seperti jumlah baris data, nama-nama kolom beserta jumlah data dan tipe datanya, dan sebagainya. Dari Tabel 1, dapat dilihat bahwa variabel 'movies' memiliki tiga fitur, yaitu 'movieId' yang memiliki tipe data _integer_, 'title' yang memiliki tipe data _object_ dan 'genres' yang memiliki tipe data _object_. Masing-masing fitur memiliki 9742 baris data yang tidak kosong (_non-null_).

  |     |  movieId  |  imdbId  |  tmdbId  |
  |-----|-----------|----------|----------|
  |  0  |     1     |  114709  |  862.0   |
  |  1  |     2     |  113497  |  8844.0  |
  |  2  |     3     |  113228  |  15602.0 |
  |  3  |     4     |  114885  |  31357.0 |
  |  4  |     5     |  113041  |  11862.0 |

  Tabel 2. Hasil keluaran dari links.head()

  Fungsi head() akan menampilkan 5 baris pertama dari suatu _dataframe_. Dari Tabel 2, dapat dilihat bahwa variabel 'links' menampilkan lima baris datanya. Selain itu, informasi lain yang dapat diambil adalah variabel 'links' memiliki tiga fitur, yaitu 'movieId', 'imdbId' dan 'tmdbId'.

  |         |     userId     |     movieId     |   rating  |    timestamp   |
  |---------|----------------|-----------------|-----------|----------------|
  |  count  | 100836.000000  |  100836.000000  |  100836.0 |  1.008360e+05  |
  |  mean   |    326.127564  |   19435.295718  |  3.501557 |  1.205946e+09  |
  |  std    |    182.618491  |   35530.987199  |  1.042529 |  2.162610e+08  |
  |  min    |      1.000000  |       1.000000  |  0.500000 |  8.281246e+08  |
  |  25%    |    177.000000  |    1199.000000  |  3.000000 |  1.019124e+09  |
  |  50%    |    325.000000  |    2991.000000  |  3.500000 |  1.186087e+09  |
  |  75%    |    477.000000  |    8122.000000  |  4.000000 |  1.435994e+09  |
  |  max    |    610.000000  |  193609.000000  |  5.000000 |  1.537799e+09  |

  Tabel 3. Hasil keluaran dari ratings.describe()

  Fungsi describe() akan menghasilkan data statistik deskriptif dalam _dataframe_ dengan merangkum tendensi sentral dan penyebaran dataset, sehingga didapatkan gambaran umum singkat tentang kumpulan data. Tabel 3 menampilkan data statistik deskriptif dari variabel 'ratings', sebagai contoh, nilai minimal dari ulasan yang diberikan pengguna adalah 0.5. Sedangkan nilai maksimal dari ulasan yang diberikan pengguna adalah 5.0.

  Selain itu, proses yang tidak kalah penting untuk dilakukan, yaitu melakukan _pre-processing_ terhadap data sebelum diolah ke tahapan selanjutnya. Tahapan _pre-processing_ data bertujuan untuk membersihkan, mengubah, atau mengorganisasi data agar siap untuk tahap pemodelan [4]. Pada penelitian ini, _pre-processing_ data diawali dengan melakukan penggabungan seluruh data pada seluruh variabel dengan mengkorelasikan tiap-tiap data pada masing-masing variabel dengan menggunakan kolom 'movieId' yang unik untuk kategori 'movie' dan menggunakan kolom 'userId' yang unik untuk kategori 'user' sebagai acuan dalam penggabungan ini. Kemudian, data yang sama (data duplikat) akan dihapus agar data yang terdapat pada masing-masing kategori ('movie' dan 'user') bersifat unik. Berikut merupakan tahapan-tahapan dalam melakukan _pre-processing_ data :

  * Menggabungkan seluruh 'movieId' pada kategori 'movie', mengurutkan data dan menghapus data yang sama
  * Menggabungkan seluruh 'userId', menghapus data yang sama dan kemudian mengurutkannya
  * Menggabungkan *file* 'links', 'movies' dan 'tags' ke dalam *dataframe* movie_info. Lalu, menggabungkan *dataframe* 'ratings' dengan movie_info berdasarkan nilai 'movieId'
  * Melakukan pengecekan *missing value* dengan fungsi isnull()
  * Mendefinisikan *dataframe* 'ratings' ke dalam variabel all_movie_rate
  * Menggabungkan all movie_rate dengan *dataframe* 'movies' berdasarkan 'movieId'. Lalu, print *dataframe* all_movie_name untuk melihat hasilnya
  * Menggabungkan *dataframe* 'tags' dengan all_movie_name dan memasukkannya ke dalam variabel all_movie

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

    Encoding adalah proses mengubah data dari satu bentuk ke bentuk lain yang lebih sesuai untuk digunakan dalam suatu model atau algoritma [5]. Dalam _Collaborative Filtering_, _encoding_ diperlukan untuk mengubah data kategorikal, seperti nama pengguna ('user') atau ID film ('movieId') menjadi bentuk numerik (indeks bilangan bulat) sehingga dapat diolah oleh model. Indeks ini memudahkan proses perhitungan dalam model dan menghindari kesalahan saat melakukan perbandingan. Berikut ini merupakan contoh proses _encoding_ untuk fitur 'user' :

    * Untuk setiap nilai unik yang terdapat dalam fitur 'user' akan diubah menjadi indeks bilangan bulat.
    * Misalnya terdapat 5 data pengguna dalam suatu _list_ seperti berikut : ['UserA', 'UserB', 'UserC', 'UserA', 'UserB']
    * Maka proses _encoding_ akan mengubahnya menjadi [0, 1, 2, 0, 1]
    
    Dapat dilihat bahwa 'UserA' di-_encode_ menjadi bilangan bulat dengan indeks 0, 'UserB' diubah menjadi bilangan bulat dengan indeks 1, dan 'UserC' diubah menjadi bilangan bulat dengan indeks 2. Proses _encoding_ ini akan membantu menghindari kesalahan saat melakukan perbandingan dan juga memudahkan perhitungan dalam model _Collaborative Filtering_. 
    
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

   Kelebihan dari metode _Content Based Filtering_ antara lain tidak memerlukan data dari pengguna lain, sehingga dapat memberikan rekomendasi untuk pengguna baru (_cold-start problem_), rekomendasi bersifat personal dan sesuai dengan preferensi individual pengguna, karena model memperhatikan riwayat penilaian pengguna, serta mampu merekomendasikan film yang kurang populer atau tidak dikenal, karena model tidak hanya mengandalkan popularitas film namun mencoba memahami minat pengguna terhadap preferensi suatu film. Sedangkan kekurangan metode _Content Based Filtering_ antara lain terbatas dalam mengidentifikasi film baru yang belum pernah dinilai oleh pengguna, karena bergantung pada atribut film yang telah dikenali dan rentan terhadap _overfitting_ jika fitur-fitur yang digunakan tidak cukup representatif atau terlalu spesifik.

   Terdapat dua tahapan penting pada proses _modeling_ menggunakan metode _Content Based Filtering_, yaitu melakukan perhitungan TF-IDF _vectorizer_ dan melakukan perhitungan _cosine similarity_. TF-IDF adalah skema representasi yang umum digunakan dalam sistem pengambilan informasi dan ekstraksi dokumen yang relevan dengan kueri tertentu [3]. TF (_Term Frequency_) mengukur frekuensi atau seberapa sering suatu kata atau _term_ muncul dalam teks tertentu. Sedangkan IDF (_Inverse Document Frequency_) mengukur pentingnya istilah di seluruh korpus. Dalam proses ini, TF-IDF digunakan untuk menemukan representasi fitur penting dari setiap kategori film. Tahapan selanjutnya adalah melakukan perhitungan _cosine similarity_. _Cosine similarity_ mengukur kesamaan antara dua vektor dan menentukan sejauh mana kedua vektor tersebut bergerak ke arah yang sama (menghitung sudut cosinus antara dua vektor) [3]. Hal ini dilakukan untuk mengukur kesamaan dokumen dalam analisis teks. Semakin kecil sudut _cosinus_ yang dihasilkan, maka semakin besar nilai _cosine similarity_-nya. 

   Pada penelitian ini, sistem rekomendasi yang telah berhasil dibangun menggunakan metode _Content Based Filtering_ akan diuji untuk mendapatkan rekomendasi film yang mirip dengan Star Wars: Episode III - Revenge of the Sith.

   |        |   id   |                       movie_name                      |             genre             |
   |--------|--------|-------------------------------------------------------|-------------------------------|
   |  1299  | 33493  |  Star Wars: Episode III - Revenge of the Sith (2005)  | Action \| Adventure \| Sci-Fi |
  
   Tabel 4. Contoh data uji, yaitu film Star Wars: Episode III - Revenge of the Sith
   
   Berikut ini merupakan hasil dari top-5 rekomendasi film yang mirip dengan film Star Wars: Episode III - Revenge of the Sith.

   |     |                       movie_name                   |             genre             |
   |-----|----------------------------------------------------|-------------------------------|
   |  0  |  Star Wars: Episode I - The Phantom Menace (1999)  | Action \| Adventure \| Sci-Fi |
   |  1  |  Fantastic Four (2005)                             | Action \| Adventure \| Sci-Fi |
   |  2  |  Serenity (2005)                                   | Action \| Adventure \| Sci-Fi |
   |  3  |  Star Wars: Episode IV - A New Hope (1977)         | Action \| Adventure \| Sci-Fi |
   |  4  |  Superman (1978)                                   | Action \| Adventure \| Sci-Fi |

   Tabel 5. Hasil dari top-5 rekomendasi film yang mirip dengan film Star Wars: Episode III - Revenge of the Sith

   Dari Tabel 5 dapat dilihat bahwa film dengan _genre_ antara 'Action', 'Adventure' atau 'Sci-Fi' menjadi film yang direkomendasikan oleh sistem. Hal ini didasarkan pada _genre_ film data uji pada Tabel 4 yang dianggap sebagai film yang pernah ditonton atau disukai oleh seorang penonton/pengguna di masa lalu.
   
*  _Collaborative Filtering_
  
   _Collaborative Filtering_ adalah metode yang mengandalkan pendapat dari pengguna lain yang memiliki minat/preferensi serupa dengan melakukan pencarian pola kesamaan dan perbedaan dalam pilihan film untuk memberikan rekomendasi yang relevan [3]. Model ini tidak memperhatikan atribut film, tetapi lebih fokus pada data penilaian yang diberikan oleh pengguna. Ketika seorang pengguna mencari rekomendasi, model akan mencari pengguna lain dengan pola penilaian yang mirip dan memberikan rekomendasi film yang disukai oleh pengguna dengan preferensi serupa. Dengan pendekatan ini, film-film yang populer di kalangan pengguna dengan preferensi serupa akan dijadikan rekomendasi.

   Kelebihan metode _Collaborative Filtering_ antara lain mampu memberikan rekomendasi yang akurat dan relevan berdasarkan pola penilaian dari pengguna lain dengan preferensi serupa, dapat merekomendasikan film-film baru yang belum pernah dilihat oleh pengguna, karena model tidak bergantung pada atribut film serta efektif dalam menangani masalah skala besar, karena mengandalkan data interaksi antara pengguna. Sedangkan kekurangan metode _Collaborative Filtering_ adalah tidak efektif untuk pengguna baru (_cold-start problem_) atau film baru, karena membutuhkan data penilaian dari pengguna terkait sebelumnya dan cenderung menghasilkan rekomendasi yang populer secara keseluruhan, sehingga mungkin mengabaikan preferensi individu tertentu.

   Pada proses pelatihan model menggunakan metode _Collaborative Filtering_, dilakukan proses perhitungan dengan membuat _class_ RecommenderNet menggunakan keras _Model class_. RecommenderNet merupakan jenis model jaringan saraf (_neural network_) yang digunakan untuk sistem rekomendasi. Model ini dirancang khusus untuk menangani masalah rekomendasi item, seperti film, musik, atau produk, berdasarkan preferensi pengguna atau data interaksi pengguna dengan item tersebut. Pada penelitian ini, pertama-tama RecommenderNet menghitung skor kecocokan antara pengguna dan film dengan menggunakan teknik _embedding_. Selanjutnya, dilakukan operasi perkalian _dot product_ antara _embedding_ pengguna dan film. Selain itu, ditambahkan juga bias untuk setiap pengguna dan film. Terakhir, skor kecocokan ditetapkan dalam skala [0,1] dengan fungsi aktivasi _sigmoid_. 

   Pada penelitian ini, sistem rekomendasi yang telah berhasil dibangun menggunakan metode _Collaborative Filtering_ akan diuji untuk mendapatkan rekomendasi film untuk seorang pengguna dimana hasil rekomendasi merupakan rekomendasi yang mengandalkan pendapat dari pengguna lain.
   
   |                 movie_name                 |         genre          |
   |--------------------------------------------|------------------------|
   |  Green Mile, The (1999)                    |  Crime \| Drama        |
   |  Whiplash (2014)                           |  Drama                 |

   Tabel 6. Film dengan _rating_ tertinggi yang diperoleh dari penilaian pengguna

   |                 movie_name                 |            genre             |
   |--------------------------------------------|------------------------------|
   |  Paths of Glory (1957)                     |  Drama \| War                |
   |  Guess Who's Coming to Dinner (1967)       |  Drama                       |
   |  Two Family House (2000)                   |  Drama                       |
   |  Hope and Glory (1987)                     |  Drama                       |
   |  Lady Jane (1986)                          |  Drama \| Romance            |
   |  Awful Truth, The (1937)                   |  Comedy \| Romance           | 
   |  Come and See (Idi i smotri) (1985)        |  Drama \| War                |
   |  Adam's Rib (1949)                         |  Comedy \| Romance           |
   |  Safety Last! (1923)                       |  Action \| Comedy \| Romance |
   |  Reefer Madness: The Movie Musical (2005)  |  Comedy \| Drama \| Musical  |

   Tabel 7. Hasil dari top-10 rekomendasi film yang mengandalkan pendapat dari pengguna lain

   Dari Tabel 6 dapat dilihat bahwa film dengan _genre_ drama menjadi film yang paling tinggi _rating_-nya. Data ini diambil dari penilaian film yang dilakukan oleh para pengguna. Selanjutnya, dari Tabel 7 dapat dilihat bahwa sistem memberikan top-10 rekomendasi film dengan mayoritas _genre_-nya adalah drama. Dapat dilihat bahwa dari 10 rekomendasi film, 7 diantaranya merupakan film dengan _genre_ drama, sehingga hasil ini sesuai dengan _rating genre_ film tertinggi yang ditunjukkan oleh Tabel 6.

# **_Evaluation_**

Pada penelitian ini, proses evaluasi dilakukan dengan menggunakan _precision_ dan metrik evaluasi dengan matplotlib. _Precision_ adalah kecocokan antara bagian data yang diambil dengan informasi yang dibutuhkan [6]. Pada penelitian ini, _precision_ digunakan untuk mengevaluasi metode _Content Based Filtering_. Sedangkan metrik evaluasi dengan matplotlib digunakan untuk mengevaluasi metode _Collaborative Filtering_.  

_Precision_ didefinisikan dalam persamaan berikut :

$$ P = \frac {Rekomendasi yang relevan} {Jumlah item yang direkomendasikan} $$

Jika diterapkan pada hasil dari top-5 rekomendasi film yang dihasilkan oleh metode _Content Based Filtering_, maka hasil _precision_-nya adalah sebagai berikut :

$$ P = \frac {Rekomendasi yang relevan} {Jumlah item yang direkomendasikan} $$

$$ P = \frac {5} {5} $$

$$ P = 1 $$

Sehingga dapat disimpulkan bahwa sistem rekomendasi dengan menggunakan metode _Content Based Filtering_ menghasilkan hasil keluaran dengan kecocokan yang tinggi, karena hasil perhitungan _precision_-nya sama dengan 1.

Sedangkan hasil dari metrik evaluasi untuk metode _Collaborative Filtering_ yang menggunakan grafik dari matplotlib, dapat dilihat pada Gambar 1. 

![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-2-Sistem-Rekomendasi/assets/77524477/e7da2798-1410-4778-830f-6af870513eaf)

Gambar 1. Metrik evaluasi untuk metode _Collaborative Filtering_

Dari proses ini, diperoleh nilai _error_ akhir sebesar 0.1794 dan nilai _error_ pada data validasi sebesar 0.1993 dengan menggunakan _epochs_ = 20. Nilai tersebut cukup bagus untuk sebuah sistem rekomendasi. MRSE yang mendekati nol menunjukkan bahwa selisih antara nilai prediksi model dengan nilai aktual sangat kecil [7]. Artinya, model berhasil memprediksi data uji dengan sangat baik. 

Namun, jika dilihat dari Gambar 1, metrik evaluasi tersebut menunjukkan bahwa data grafik plot masuk ke dalam kategori _overfit_. _Overfitting_ adalah kondisi di mana model telah mempelajari dataset pelatihan terlalu baik, hingga memperhatikan detail-detail kecil, kebisingan statistik, atau fluktuasi acak yang ada dalam dataset pelatihan [8]. Akibatnya, model tersebut menjadi terlalu khusus untuk data pelatihan tertentu, namun kurang mampu untuk menggeneralisasi dengan baik pada data baru yang belum pernah dilihat sebelumnya. Hal ini ditandai dengan plot _training loss_ yang terus berkurang seiring dengan jumlah _epochs_ pada saat proses pelatihan yang artinya model terus meningkatkan performa pada data pelatihan. Sedangkan pada plot _validation loss_ ditandai dengan grafik yang menurun pada awal pelatihan dan kemudian mulai meningkat, yang artinya hal ini menunjukkan bahwa pada awalnya, model berhasil menggeneralisasi pada data validasi, namun setelah mencapai titik tertentu, model mulai _overfitting_ dan performanya pada data validasi mulai menurun. Sehingga dapat disimpulkan bahwa, jika pada grafik plot metrik evaluasi terlihat adanya gap antara _training loss_ dan _validation loss_, atau _validation loss_ meningkat setelah mencapai titik tertentu, sedangkan _training loss_ tetap menurun, maka ini menunjukkan bahwa model mengalami _overfitting_. 

# **Kesimpulan**

Penelitian ini bertujuan untuk mengembangkan sistem rekomendasi film yang efektif dan akurat dalam menyajikan rekomendasi film yang lebih sesuai dengan minat dan preferensi masing-masing pengguna. Dengan begitu, pelaku bisnis dari platform _streaming_ film dapat menentukan target penonton dengan lebih tepat dan memberikan pengalaman menonton yang lebih personal dan memuaskan bagi para penggunanya. Dari penelitian ini, berhasil dibuat dua sistem rekomendasi dengan hasil yang cukup baik pula, yaitu sistem rekomendasi film berdasarkan data historis dari preferensi dan penilaian film oleh pengguna itu sendiri dengan menggunakan metode _Content Based Filtering_ yang menghasilkan _precision_ mendekati angka 1 dan sistem rekomendasi film berdasarkan data kolaboratif dari pengguna lain dengan minat serupa dengan menggunakan metode _Collaborative Filtering_ dimana nilai _error_ akhir sebesar 0.1764 dan nilai _error_ pada data validasi sebesar 0.2040, kedua nilai _error_ ini cukup bagus untuk sebuah sistem rekomendasi. Namun sayangnya, metrik evaluasi menunjukkan bahwa model yang telah dibangun mengalami _overfit_.

Meskipun tujuan utama penelitian ini telah tercapai, untuk optimalisasi lebih lanjut, beberapa improvisasi pada model dapat dilakukan untuk meningkatkan kualitas rekomendasi sehingga dapat memberikan wawasan yang lebih akurat dan relevan bagi para penggunanya dengan lebih tepat dan efisien.

# **Referensi**

[1]    N. A. Munawaroh, S. Kalimah, dan Z. Muttaqien, “Netflix In Indonesia : Customer Willingness To Pay in Video Streaming
Service,” _Jesya Jurnal Ekonomi & Ekonomi Syariah_, vol. 6, no. 1, Jan. 2023, doi:  https://doi.org/10.36778/jesya.v6i1.1136. [Online]. Tersedia: [tautan]([http://dx.doi.org/10.3390/su10072336](https://stiealwashliyahsibolga.ac.id/jurnal/index.php/jesya/article/download/1136/581)). 

[2]    S. Sari dan D. T. Hendra, “Aplikasi Rekomendasi Film menggunakan Pendekatan Collaborative Filtering dan Euclidean Distance sebagai ukuran kemiripan rating ISBN : 979-26-0280-1 ISBN : 979-26-0280-1,” pp. 135–140, 2015.

[3]    dicoding. "Rangkuman Studi Kasus Keempat: Sistem Rekomendasi". Tersedia: [tautan](https://www.dicoding.com/academies/319/tutorials/19672). Diakses pada 31 Juli 2023.

[4]    Binus University Graduate Program. “Teknik pre-processing dan classification dalam data science,”. Tersedia: [tautan](https://mie.binus.ac.id/2022/08/26/teknik-pre-processing-dan-classification-dalam-data-science/). Diakses pada 31 Juli 2023.

[5]    E-Prints UNY. Tersedia: [tautan](http://eprints.uny.ac.id/54926/3/BAB%202.pdf). Diakses pada 31 Juli 2023.

[6]    E-Jurnal UAJY. Tersedia: [tautan](http://e-journal.uajy.ac.id/11794/4/TF070093.pdf). Diakses pada 31 Juli 2023.

[7]    aitechtrend. "How to Interpret RMSE and Use it in Your Modeling". Tersedia: [tautan](https://aitechtrend.com/how-to-interpret-rmse-and-use-it-in-your-modeling/). Diakses pada 31 Juli 2023.

[8]    Machine Learning Mastery. "How to use Learning Curves to Diagnose Machine Learning Model Performance". Tersedia: [tautan](https://machinelearningmastery.com/learning-curves-for-diagnosing-machine-learning-model-performance/). Diakses pada 5 Agustus 2023.
