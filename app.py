import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# Modeli yükle
model_data = joblib.load('human_activity_model.joblib')
model = model_data['model']
scaler = model_data['scaler']
pca = model_data['pca']

# Aktivite etiketleri (ORİJİNAL İSİMLERLE eşleştirme yapın)
activities = {
    'WALKING': 'YÜRÜME',
    'WALKING_UPSTAIRS': 'MERDİVEN ÇIKMA',
    'WALKING_DOWNSTAIRS': 'MERDİVEN İNME',
    'SITTING': 'OTURMA',
    'STANDING': 'AYAKTA DURMA',
    'LAYING': 'UZANMA'  # Veri setinizdeki gerçek etiketleri kontrol edin
}

st.title('🏃 İnsan Aktivite Tanıma Sistemi')

uploaded_file = st.file_uploader("CSV dosyası yükle", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # Gerekli sütunları kontrol et
    try:
        raw_features = df.drop(['subject', 'Activity'], axis=1)
    except KeyError as e:
        st.error(f"CSV dosyasında gerekli sütun eksik: {e}")
        st.stop()
    
    # Ön işleme
    X_scaled = scaler.transform(raw_features)
    X_pca = pca.transform(X_scaled)
    
    # Tahmin
    predictions = model.predict(X_pca)
    df['TAHMİN'] = [activities[p] for p in predictions]  # Artık string etiketlerle çalışıyor
    
    # Sonuçları göster
    st.subheader("Tahmin Sonuçları")
    st.dataframe(df[['TAHMİN']].style.applymap(
        lambda x: f"background-color: {'#e6f3ff' if x=='YÜRÜME' else '#ffe6e6'}"), 
        height=300)
    
    # Dağılım grafiği
    st.subheader("Aktivite Dağılımı")
    df['TAHMİN'].value_counts().plot.pie(autopct='%1.1f%%')
    st.pyplot()