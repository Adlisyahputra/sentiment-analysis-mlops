# Sentiment Analysis - E-Wallet Reviews (MLOps)

End-to-end sentiment analysis project untuk review aplikasi e-wallet Indonesia (GoPay, DANA, OVO), dari data collection sampai deployment.

## Pipeline
1. **Data collection**: scraping Play Store dengan `google-play-scraper`
2. **Preprocessing**: cleaning teks, normalisasi slang Indonesia, stopword removal (dengan penanganan khusus kata negasi supaya makna kalimat tidak terbalik)
3. **Modeling**: TF-IDF + Logistic Regression, tracked dengan MLflow
4. **Serving**: FastAPI, di-containerize dengan Docker
5. **CI/CD**: GitHub Actions (test otomatis + Docker build tiap push)

## Hasil
- Accuracy: 86%, Recall negative: 0.95 (test set 57 sample)

## Cara menjalankan
```bash
docker build -t sentiment-api .
docker run -p 8000:8000 sentiment-api
```
Buka `http://localhost:8000/docs`

## Limitations
- Dataset kecil (283 sample setelah cleaning), hasil evaluasi punya variance tinggi
- Belum ada monitoring drift production yang real-time