# utils/language_utils.py

supported_translation_models = {
    # English <-> Hindi
    ("English", "Hindi"): {"model": "Helsinki-NLP/opus-mt-en-hi", "src_lang": None, "tgt_lang": None},
    ("Hindi", "English"): {"model": "Helsinki-NLP/opus-mt-hi-en", "src_lang": None, "tgt_lang": None},

    # English <-> French
    ("English", "French"): {"model": "Helsinki-NLP/opus-mt-en-fr", "src_lang": None, "tgt_lang": None},
    ("French", "English"): {"model": "Helsinki-NLP/opus-mt-fr-en", "src_lang": None, "tgt_lang": None},

    # English <-> Japanese
    ("English", "Japanese"): {"model": "Helsinki-NLP/opus-mt-en-ja", "src_lang": None, "tgt_lang": None},
    ("Japanese", "English"): {"model": "Helsinki-NLP/opus-mt-ja-en", "src_lang": None, "tgt_lang": None},

    # English <-> Spanish
    ("English", "Spanish"): {"model": "Helsinki-NLP/opus-mt-en-es", "src_lang": None, "tgt_lang": None},
    ("Spanish", "English"): {"model": "Helsinki-NLP/opus-mt-es-en", "src_lang": None, "tgt_lang": None},

    # English <-> Urdu
    ("English", "Urdu"): {"model": "Helsinki-NLP/opus-mt-en-ur", "src_lang": None, "tgt_lang": None},
    ("Urdu", "English"): {"model": "Helsinki-NLP/opus-mt-ur-en", "src_lang": None, "tgt_lang": None},

    # Hindi <-> French
    ("Hindi", "French"): {"model": "Helsinki-NLP/opus-mt-hi-fr", "src_lang": None, "tgt_lang": None},
    ("French", "Hindi"): {"model": "Helsinki-NLP/opus-mt-fr-hi", "src_lang": None, "tgt_lang": None},

    # Hindi <-> Japanese
    ("Hindi", "Japanese"): {"model": "Helsinki-NLP/opus-mt-hi-ja", "src_lang": None, "tgt_lang": None},
    ("Japanese", "Hindi"): {"model": "Helsinki-NLP/opus-mt-ja-hi", "src_lang": None, "tgt_lang": None},

    # Hindi <-> Spanish
    ("Hindi", "Spanish"): {"model": "Helsinki-NLP/opus-mt-hi-es", "src_lang": None, "tgt_lang": None},
    ("Spanish", "Hindi"): {"model": "Helsinki-NLP/opus-mt-es-hi", "src_lang": None, "tgt_lang": None},

    # Hindi <-> Urdu
    ("Hindi", "Urdu"): {"model": "Helsinki-NLP/opus-mt-hi-ur", "src_lang": None, "tgt_lang": None},
    ("Urdu", "Hindi"): {"model": "Helsinki-NLP/opus-mt-ur-hi", "src_lang": None, "tgt_lang": None},

    # French <-> Japanese
    ("French", "Japanese"): {"model": "Helsinki-NLP/opus-mt-fr-ja", "src_lang": None, "tgt_lang": None},
    ("Japanese", "French"): {"model": "Helsinki-NLP/opus-mt-ja-fr", "src_lang": None, "tgt_lang": None},

    # French <-> Spanish
    ("French", "Spanish"): {"model": "Helsinki-NLP/opus-mt-fr-es", "src_lang": None, "tgt_lang": None},
    ("Spanish", "French"): {"model": "Helsinki-NLP/opus-mt-es-fr", "src_lang": None, "tgt_lang": None},

    # French <-> Urdu
    ("French", "Urdu"): {"model": "Helsinki-NLP/opus-mt-fr-ur", "src_lang": None, "tgt_lang": None},
    ("Urdu", "French"): {"model": "Helsinki-NLP/opus-mt-ur-fr", "src_lang": None, "tgt_lang": None},

    # Japanese <-> Spanish
    ("Japanese", "Spanish"): {"model": "Helsinki-NLP/opus-mt-ja-es", "src_lang": None, "tgt_lang": None},
    ("Spanish", "Japanese"): {"model": "Helsinki-NLP/opus-mt-es-ja", "src_lang": None, "tgt_lang": None},

    # Japanese <-> Urdu
    ("Japanese", "Urdu"): {"model": "Helsinki-NLP/opus-mt-ja-ur", "src_lang": None, "tgt_lang": None},
    ("Urdu", "Japanese"): {"model": "Helsinki-NLP/opus-mt-ur-ja", "src_lang": None, "tgt_lang": None},

    # Spanish <-> Urdu
    ("Spanish", "Urdu"): {"model": "Helsinki-NLP/opus-mt-es-ur", "src_lang": None, "tgt_lang": None},
    ("Urdu", "Spanish"): {"model": "Helsinki-NLP/opus-mt-ur-es", "src_lang": None, "tgt_lang": None},
}

def get_supported_languages():
    langs = set()
    for pair in supported_translation_models:
        langs.add(pair[0])
        langs.add(pair[1])
    return sorted(list(langs))

def get_model_config(src_lang, tgt_lang):
    key = (src_lang.strip().title(), tgt_lang.strip().title())
    print("Looking for model config with key:", key)
    return supported_translation_models.get(key)
