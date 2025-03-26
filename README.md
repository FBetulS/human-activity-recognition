# human-activity-recognition
Makine Öğrenimi ile Akıllı Telefon Verilerini Kullanarak İnsan Etkinliği Tanıma
# İnsan Aktivite Tanıma Projesi

## 📖 Proje Hakkında
Bu projede, insan aktivitelerinin sınıflandırılması için bir makine öğrenimi modeli geliştirilmiştir. Model, akıllı telefon verilerini kullanarak farklı aktiviteleri tanımlamak amacıyla tasarlanmıştır. Proje, veri analizi, ön işleme ve makine öğrenimi süreçlerini kapsamaktadır.

### Veri Seti ve Örnek Çözüm
Veri seti ve örnek çözüm için aşağıdaki bağlantılara göz atabilirsiniz:
- [Human Activity Recognition using Smartphone Data with Machine Learning](https://thecleverprogrammer.com/2020/05/27/human-activity-recognition-using-smartphone-data-with-machine-learning/)
- [Hugging Face - Human Activity Recognition](https://huggingface.co/spaces/btulftma/human-activity-recognition)

## 🔧 Kullanılan Kütüphaneler
- `pandas`: Veri analizi için.
- `numpy`: Sayısal hesaplamalar için.
- `matplotlib`: Görselleştirme için.
- `seaborn`: Gelişmiş görselleştirme için.
- `sklearn`: Makine öğrenimi ve veri ön işleme için.
- `joblib`: Model kaydetmek için.

## 🚀 Proje Adımları
1. **Veri Yükleme**: Eğitim ve test veri setleri yüklenmiştir.
2. **Veri Birleştirme**: Eğitim ve test veri setleri birleştirilmiştir.
3. **Aktivite Dağılımının Görselleştirilmesi**: Farklı aktivite sınıflarının dağılımı görselleştirilmiştir.
4. **Veri Ön İşleme**: Özellikler ölçeklendirilmiş ve gereksiz sütunlar kaldırılmıştır.
5. **Boyut İndirgeme**: PCA (Principal Component Analysis) kullanılarak boyut indirgeme yapılmıştır.
6. **Veriyi Eğitim ve Test Setlerine Ayırma**: Veri eğitim ve test setlerine ayrılmıştır.
7. **Model Eğitimi**: Random Forest sınıflandırma modeli eğitilmiştir.
8. **Tahminleme**: Model ile test seti üzerinden tahminleme yapılmıştır.
9. **Sonuçların Değerlendirilmesi**: Sınıflandırma raporu ve karmaşıklık matrisi ile sonuçlar değerlendirilmiştir.
10. **Modeli Kaydetme**: Model ve bileşenleri depolanmıştır.

## 📊 Sonuç
Proje kapsamında geliştirilen makine öğrenimi modeli, insan aktivitelerini yüksek doğruluk oranıyla sınıflandırmakta başarılı olmuştur. Modelin performansı, sınıflandırma raporu ve karmaşıklık matrisi ile değerlendirilmiştir. Özelliklerin modeldeki önemi de analiz edilerek, hangi özelliklerin sınıflandırmada daha etkili olduğu ortaya konmuştur.

Model, gelecekteki tahminler için kullanılmak üzere kaydedilmiştir.

## 📦 Model Kaydetme
Model ve bileşenleri `human_activity_model.joblib` dosyası olarak kaydedilmiştir. Bu, modelin daha sonraki kullanımlar için yeniden yüklenmesini sağlar.
