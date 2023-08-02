# -*- coding: utf-8 -*-
"""AditaPutriPuspaningrum_SistemRekomendasiFilm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WLi84Uk4tP6K3ghTc4wPxxGsMX4DQRAJ

# Proyek Machine Learning Terapan (MLT4) - Submission 2 Sistem Rekomendasi

*   Nama : Adita Putri Puspaningrum
*   Link Dataset : https://www.kaggle.com/datasets/rohan4050/movie-recommendation-data

# Data Collection

Lakukan instalasi opendatasets untuk bisa mengunduh dataset yang diambil dari situs *web* Kaggle

Pada bagian ini, diperlukan *username* dan *key* dari akun Kaggle pribadi yang diambil dari API Kaggle
"""

!pip install opendatasets

import opendatasets as od

od.download("https://www.kaggle.com/rohan4050/movie-recommendation-data?select=ml-latest-small")

"""# Data Understanding

*Library* pandas digunakan untuk membaca dataset dengan format csv
"""

import pandas as pd

links = pd.read_csv('/content/movie-recommendation-data/ml-latest-small/links.csv')
movies = pd.read_csv('/content/movie-recommendation-data/ml-latest-small/movies.csv')
ratings = pd.read_csv('/content/movie-recommendation-data/ml-latest-small/ratings.csv')
tags = pd.read_csv('/content/movie-recommendation-data/ml-latest-small/tags.csv')

print('Jumlah data link film : ', len(links.movieId.unique()))
print('Jumlah data film : ', len(movies.movieId.unique()))
print('Jumlah data tag film : ', len(tags.movieId.unique()))
print('Jumlah data penilaian yang diberikan pengguna : ', len(ratings.userId.unique()))
print('Jumlah data penilaian film : ', len(ratings.movieId.unique()))

"""# Univariate Exploratory Data Analysis"""

movies.info()

links.head()

tags.head()

ratings.head()

ratings.describe()

print('Jumlah userId : ', len(ratings.userId.unique()))
print('Jumlah movieId : ', len(ratings.movieId.unique()))
print('Jumlah data rating : ', len(ratings))

"""# Data Preprocessing

Menggabungkan seluruh 'movieId' pada kategori 'movie', mengurutkan data dan menghapus data yang sama
"""

import numpy as np

movie_all = np.concatenate((
    links.movieId.unique(),
    movies.movieId.unique(),
    ratings.movieId.unique(),
    tags.movieId.unique(),
))

movie_all = np.sort(np.unique(movie_all))

print('Jumlah seluruh data movie berdasarkan movieId: ', len(movie_all))

"""Menggabungkan seluruh 'userId', menghapus data yang sama dan kemudian mengurutkannya"""

user_all = np.concatenate((
    ratings.userId.unique(),
    tags.userId.unique(),
))

user_all = np.sort(np.unique(user_all))

print('Jumlah seluruh user: ', len(user_all))

"""Menggabungkan *file* 'links', 'movies' dan 'tags' ke dalam *dataframe* movie_info. Lalu, menggabungkan *dataframe* 'ratings' dengan movie_info berdasarkan nilai 'movieId'"""

movie_info = pd.concat([links, movies, tags])
movie = pd.merge(ratings, movie_info , on='movieId', how='left')
movie

"""Cek *missing value* dengan fungsi isnull()"""

movie.isnull().sum()

movie.groupby('movieId').sum()

"""Definisikan *dataframe* 'ratings' ke dalam variabel all_movie_rate"""

all_movie_rate = ratings
all_movie_rate

"""Menggabungkan all movie_rate dengan *dataframe* 'movies' berdasarkan 'movieId'. Lalu, print *dataframe* all_movie_name untuk melihat hasilnya"""

all_movie_name = pd.merge(all_movie_rate, movies[['movieId','title','genres']], on='movieId', how='left')
all_movie_name

"""Menggabungkan *dataframe* 'tags' dengan all_movie_name dan memasukkannya ke dalam variabel all_movie"""

all_movie = pd.merge(all_movie_name, tags[['movieId','tag']], on='movieId', how='left')
all_movie

"""# Data Preparation

Mengecek *missing value* pada *dataframe* all_movie
"""

all_movie.isnull().sum()

"""Membersihkan *missing value* dengan fungsi dropna()"""

all_movie_clean = all_movie.dropna()
all_movie_clean

"""Mengecek kembali *missing value* pada variabel all_movie_clean"""

all_movie_clean.isnull().sum()

"""Mengurutkan 'movie' berdasarkan 'movieId' kemudian memasukkannya ke dalam variabel fix_movie"""

fix_movie = all_movie_clean.sort_values('movieId', ascending=True)
fix_movie

"""Mengecek berapa jumlah fix_movie"""

len(fix_movie.movieId.unique())

"""Mengecek berapa jumlah *genre* film yang unik"""

len(fix_movie.genres.unique())

"""Membuat variabel *preparation* yang berisi *dataframe* fix_movie kemudian mengurutkan berdasarkan 'movieId'"""

preparation = fix_movie
preparation.sort_values('movieId')

"""Membuang data duplikat pada variabel *preparation*"""

preparation = preparation.drop_duplicates('movieId')
preparation

"""Mengonversi data series ‘movieId’, 'title' dan 'genres' menjadi dalam bentuk *list*"""

# Mengonversi data series ‘movieId’ menjadi dalam bentuk list
movie_id = preparation['movieId'].tolist()

# Mengonversi data series ‘title’ menjadi dalam bentuk list
movie_name = preparation['title'].tolist()

# Mengonversi data series ‘genres’ menjadi dalam bentuk list
movie_genre = preparation['genres'].tolist()

print(len(movie_id))
print(len(movie_name))
print(len(movie_genre))

"""Membuat *dictionary* untuk data ‘movie_id’, ‘movie_name’, dan ‘movie_genre’"""

movie_new = pd.DataFrame({
    'id': movie_id,
    'movie_name': movie_name,
    'genre': movie_genre
})
movie_new

"""# Model Development dengan Content Based Filtering"""

data = movie_new
data.sample(5)

"""# TF-IDF Vectorizer"""

from sklearn.feature_extraction.text import TfidfVectorizer

# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()

# Melakukan perhitungan idf pada data genre
tf.fit(data['genre'])

# Mapping array dari fitur index integer ke fitur nama
tf.get_feature_names_out()

# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tf.fit_transform(data['genre'])

# Melihat ukuran matrix tfidf
tfidf_matrix.shape

# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()

# Membuat dataframe untuk melihat tf-idf matrix
# Kolom diisi dengan genre
# Baris diisi dengan nama film

pd.DataFrame(
    tfidf_matrix.todense(),
    columns=tf.get_feature_names_out(),
    index=data.movie_name
).sample(22, axis=1).sample(10, axis=0)

"""# Cosine Similarity"""

from sklearn.metrics.pairwise import cosine_similarity

# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa nama film
cosine_sim_df = pd.DataFrame(cosine_sim, index=data['movie_name'], columns=data['movie_name'])
print('Shape:', cosine_sim_df.shape)

# Melihat similarity matrix pada setiap film
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""# Mendapatkan Rekomendasi"""

def movie_recommendations(nama_film, similarity_data=cosine_sim_df, items=data[['movie_name', 'genre']], k=5):
    """
    Rekomendasi Film berdasarkan kemiripan dataframe

    Parameter:
    ---
    nama_film : tipe data string (str)
                Nama Film (index kemiripan dataframe)
    similarity_data : tipe data pd.DataFrame (object)
                      Kesamaan dataframe, simetrik, dengan film sebagai indeks dan kolom
    items : tipe data pd.DataFrame (object)
            Mengandung kedua nama dan fitur lainnya yang digunakan untuk mendefinisikan kemiripan
    k : tipe data integer (int)
        Banyaknya jumlah rekomendasi yang diberikan
    ---


    Pada index ini, kita mengambil k dengan nilai similarity terbesar
    pada index matrix yang diberikan (i).
    """


    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,nama_film].to_numpy().argpartition(
        range(-1, -k, -1))

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    # Drop nama_film agar nama film yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(nama_film, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

data[data.movie_name.eq('Star Wars: Episode III - Revenge of the Sith (2005)')]

# Mendapatkan rekomendasi film yang mirip dengan Star Wars: Episode III - Revenge of the Sith
movie_recommendations('Star Wars: Episode III - Revenge of the Sith (2005)')

"""# Model Development dengan Collaborative Filtering

# Data Understanding
"""

# Import library
import pandas as pd
import numpy as np
from zipfile import ZipFile
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from pathlib import Path
import matplotlib.pyplot as plt

"""Membaca dataset"""

df = ratings
df

"""# Data Preparation

Berikut adalah hal-hal yang telah dilakukan pada tahap data *preparation*:

* Memahami data *rating* yang dimiliki.
* Menyandikan (*encode*) fitur ‘user’ dan ‘movieId’ ke dalam indeks *integer*.
* Memetakan ‘userID’ dan ‘placeID’ ke dataframe yang berkaitan.
* Mengecek beberapa hal dalam data seperti jumlah user, jumlah film, kemudian mengubah nilai 'rating' menjadi float.
"""

# Mengubah userId menjadi list tanpa nilai yang sama
user_ids = df['userId'].unique().tolist()
print('list userId: ', user_ids)

# Melakukan encoding userId
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
print('encoded userId : ', user_to_user_encoded)

# Melakukan proses encoding angka ke ke userId
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}
print('encoded angka ke userId: ', user_encoded_to_user)

# Mengubah movieId menjadi list tanpa nilai yang sama
movie_ids = df['movieId'].unique().tolist()

# Melakukan proses encoding movieId
movie_to_movie_encoded = {x: i for i, x in enumerate(movie_ids)}

# Melakukan proses encoding angka ke movieId
movie_encoded_to_movie = {i: x for i, x in enumerate(movie_ids)}

# Mapping userId ke dataframe user
df['user'] = df['userId'].map(user_to_user_encoded)

# Mapping movieId ke dataframe movie
df['movie'] = df['movieId'].map(movie_to_movie_encoded)

# Mendapatkan jumlah user
num_users = len(user_to_user_encoded)
print(num_users)

# Mendapatkan jumlah movie
num_movie = len(movie_encoded_to_movie)
print(num_movie)

# Mengubah ratings menjadi nilai float
df['rating'] = df['rating'].values.astype(np.float32)

# Nilai minimum ratings
min_rating = min(df['rating'])

# Nilai maksimal ratings
max_rating = max(df['rating'])

print('Number of User: {}, Number of Movie: {}, Min Rating: {}, Max Rating: {}'.format(
    num_users, num_movie, min_rating, max_rating
))

"""# Membagi Data untuk Training dan Validasi

Mengacak dataset
"""

df = df.sample(frac=1, random_state=42)
df

"""Proses pembagian data latih dan data validasi dengan rasio 80 : 20"""

# Membuat variabel x untuk mencocokkan data user dan movie menjadi satu value
x = df[['user', 'movie']].values

# Membuat variabel y untuk membuat rating dari hasil
y = df['rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values

# Membagi menjadi 80% data train dan 20% data validasi
train_indices = int(0.8 * df.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

print(x, y)

"""# Proses Training"""

class RecommenderNet(tf.keras.Model):

  # Insialisasi fungsi
  def __init__(self, num_users, num_movie, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_movie = num_movie
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding( # layer embedding user
        num_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(num_users, 1) # layer embedding user bias
    self.movie_embedding = layers.Embedding( # layer embeddings movie
        num_movie,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.movie_bias = layers.Embedding(num_movie, 1) # layer embedding movie bias

  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0]) # memanggil layer embedding 1
    user_bias = self.user_bias(inputs[:, 0]) # memanggil layer embedding 2
    movie_vector = self.movie_embedding(inputs[:, 1]) # memanggil layer embedding 3
    movie_bias = self.movie_bias(inputs[:, 1]) # memanggil layer embedding 4

    dot_user_movie = tf.tensordot(user_vector, movie_vector, 2)

    x = dot_user_movie + user_bias + movie_bias

    return tf.nn.sigmoid(x) # activation sigmoid

model = RecommenderNet(num_users, num_movie, 50) # inisialisasi model

# model compile
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

"""Proses pelatihan data dengan menggunakan 20 *epochs*"""

# Memulai training

history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 8,
    epochs = 20,
    validation_data = (x_val, y_val)
)

"""# Visualisasi Metrik"""

plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('model_metrics')
plt.ylabel('root_mean_squared_error')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

"""# Mendapatkan Rekomendasi"""

movie_df = movie_new
df = pd.read_csv('movie-recommendation-data/ml-latest-small/ratings.csv')

# Mengambil sample user
user_id = df.userId.sample(1).iloc[0]
movie_watched_by_user = df[df.userId == user_id]

movie_not_watched = movie_df[~movie_df['id'].isin(movie_watched_by_user.movieId.values)]['id']
movie_not_watched = list(
    set(movie_not_watched)
    .intersection(set(movie_to_movie_encoded.keys()))
)

movie_not_watched = [[movie_to_movie_encoded.get(x)] for x in movie_not_watched]
user_encoder = user_to_user_encoded.get(user_id)
user_movie_array = np.hstack(
    ([[user_encoder]] * len(movie_not_watched), movie_not_watched)
)

ratings = model.predict(user_movie_array).flatten()

top_ratings_indices = ratings.argsort()[-10:][::-1]
recommended_movie_ids = [
    movie_encoded_to_movie.get(movie_not_watched[x][0]) for x in top_ratings_indices
]

print('Showing recommendations for users: {}'.format(user_id))
print('===' * 9)
print('Movie with high ratings from user')
print('----' * 8)

top_movie_user = (
    movie_watched_by_user.sort_values(
        by = 'rating',
        ascending=False
    )
    .head(5)
    .movieId.values
)

movie_df_rows = movie_df[movie_df['id'].isin(top_movie_user)]
for row in movie_df_rows.itertuples():
    print(row.movie_name, ':', row.genre)

print('----' * 8)
print('Top 10 movie recommendation')
print('----' * 8)

recommended_movie = movie_df[movie_df['id'].isin(recommended_movie_ids)]
for row in recommended_movie.itertuples():
    print(row.movie_name, ':', row.genre)

