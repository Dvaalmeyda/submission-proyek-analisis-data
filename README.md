# Submission Proyek Analisis Data

## Submission Proyek Analisis Data dengan Python by Dicoding

## Preview Dashboard
![Bike Sharing Dashboard Streamlit Preview]<img src="https://raw.githubusercontent.com/Dvaalmeyda/submission-proyek-analisis-data/6912a3b900f7bfaa9ba7afaaa5dfa927982dc0af/hasil_dashboard.png" alr="Preview Dashboard"><img>

Deployment Project dilakukan pada **Streamlit** <img src="https://user-images.githubusercontent.com/7164864/217935870-c0bc60a3-6fc0-4047-b011-7b4c59488c91.png" alt="Streamlit logo"></img>

## Deskripsi
Proyek ini menganalisa dataset Bike Sharing Dataset untuk mendapatkan insight pada data tersebut kemudian membagikannya menggunakan dashboard.

## Karakteristik Dataset

- instant: record index
- dteday : date
- season : season (1:springer, 2:summer, 3:fall, 4:winter)
- yr : year (0 : 2011, 1 : 2012)
- mnth : month ( 1 to 12)
- hr : hour (0 to 23)
- holiday : weather day is holiday or not 
- weekday : day of the week
- workingday : if day is neither weekend nor holiday is 1, otherwise is 0.
- weathersit :
    - 1: Clear / Few clouds
    - 2: Mist / Cloudy
    - 3: Light Snow / Rain
    - 4: Heavy Rain / Snow
- temp : Normalized temperature in Celsius. The values are divided to 41 (max)
- atemp: Normalized feeling temperature in Celsius. The values are divided to 50 (max)
- hum: Normalized humidity. The values are divided to 100 (max)
- windspeed: Normalized wind speed. The values are divided to 67 (max)
- casual: count of casual users
- registered: count of registered users
- cnt: count of total rental bikes including both casual and registered

## Cara Menjalankan Proyek

1. Clone Repository
```
git clone "https://github.com/Dvaalmeyda/submission-proyek-analisis-data.git"
```

2. Install dependencies yang diperlukan
```
pip install -r requirement.txt
```

3. Masuk ke direktori 'dashboard.py' berada (path menyesuaikan)
```
cd /submission-proyek-analisis-data/dashboard
```

4. Run 'dashboard.py'
```
streamlit run dashboard.py
```

Atau dashboard bisa dilihat melalui [website berikut](https://dvaalmeyda-submission-proyek-analisis-dashboarddashboard-mzgcxk.streamlit.app/)

