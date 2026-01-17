from twttr import shorten

def test_shorten_sentences():
    assert shorten("i liked tiwtter") == " lkd twttr"
    assert shorten ("i love cupcackes") == " lv cpccks"

def test_shorten_words():
    assert shorten("tiwtter") == "twttr"
    assert shorten("Goodmorning") == "Gdmrnng"
    assert shorten("") == ""