import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from preprocessing import clean_text

def test_negation_preserved():
    result = clean_text("tidak bisa login")
    assert "tidak" in result

def test_lowercase():
    result = clean_text("BAGUS BANGET")
    assert result == result.lower()

def test_emoji_removed():
    result = clean_text("mantap banget 😍")
    assert "😍" not in result

def test_slang_normalized():
    result = clean_text("gak bisa dipake")
    assert "gak" not in result