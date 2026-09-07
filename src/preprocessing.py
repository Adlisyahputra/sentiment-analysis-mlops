import re
import emoji
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.StopWordRemover.StopWordRemover import StopWordRemover
from Sastrawi.Dictionary.ArrayDictionary import ArrayDictionary

# Kamus normalisasi kata gaul -> baku (tambah sendiri sesuai temuan di data)
SLANG_DICT = {
    "gak": "tidak", "ga": "tidak", "krn": "karena", "kalo": "kalau",
    "udah": "sudah", "udh": "sudah", "bgt": "banget", "yg": "yang",
    "dgn": "dengan", "utk": "untuk", "tdk": "tidak", "sm": "sama",
    "jg": "juga", "trus": "terus", "gmn": "gimana", "knp": "kenapa",
}

# Ambil daftar stopword bawaan, tapi keluarkan kata negasi (penting untuk sentiment)
_factory = StopWordRemoverFactory()
_stopwords = _factory.get_stop_words()
_negation_words = {"tidak", "bukan", "jangan", "belum", "kurang", "tanpa"}
_stopwords = [w for w in _stopwords if w not in _negation_words]

stopword_remover = StopWordRemover(ArrayDictionary(_stopwords))

def clean_text(text: str) -> str:
    text = text.lower()
    text = emoji.replace_emoji(text, replace="")
    text = re.sub(r"http\S+|www\S+", "", text)          # hapus URL
    text = re.sub(r"[^a-z\s]", " ", text)                 # hapus angka & simbol
    words = text.split()
    words = [SLANG_DICT.get(w, w) for w in words]          # normalisasi slang
    text = " ".join(words)
    text = stopword_remover.remove(text)                    # hapus stopword
    text = re.sub(r"\s+", " ", text).strip()               # rapikan spasi
    return text