# utils/language_utils.py

supported_translation_models = {
    # English <-> Hindi
    ("English", "Hindi"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "en_XX", "tgt_lang": "hi_IN"},
    ("Hindi", "English"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "hi_IN", "tgt_lang": "en_XX"},

    # English <-> French
    ("English", "French"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "en_XX", "tgt_lang": "fr_XX"},
    ("French", "English"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "fr_XX", "tgt_lang": "en_XX"},

    # English <-> Japanese
    ("English", "Japanese"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "en_XX", "tgt_lang": "ja_XX"},
    ("Japanese", "English"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "ja_XX", "tgt_lang": "en_XX"},

    # English <-> Spanish
    ("English", "Spanish"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "en_XX", "tgt_lang": "es_XX"},
    ("Spanish", "English"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "es_XX", "tgt_lang": "en_XX"},

    # English <-> Urdu
    ("English", "Urdu"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "en_XX", "tgt_lang": "ur_PK"},
    ("Urdu", "English"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "ur_PK", "tgt_lang": "en_XX"},

    # Hindi <-> French
    ("Hindi", "French"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "hi_IN", "tgt_lang": "fr_XX"},
    ("French", "Hindi"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "fr_XX", "tgt_lang": "hi_IN"},

    # Hindi <-> Japanese
    ("Hindi", "Japanese"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "hi_IN", "tgt_lang": "ja_XX"},
    ("Japanese", "Hindi"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "ja_XX", "tgt_lang": "hi_IN"},

    # Hindi <-> Spanish
    ("Hindi", "Spanish"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "hi_IN", "tgt_lang": "es_XX"},
    ("Spanish", "Hindi"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "es_XX", "tgt_lang": "hi_IN"},

    # Hindi <-> Urdu
    ("Hindi", "Urdu"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "hi_IN", "tgt_lang": "ur_PK"},
    ("Urdu", "Hindi"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "ur_PK", "tgt_lang": "hi_IN"},

    # French <-> Japanese
    ("French", "Japanese"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "fr_XX", "tgt_lang": "ja_XX"},
    ("Japanese", "French"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "ja_XX", "tgt_lang": "fr_XX"},

    # French <-> Spanish
    ("French", "Spanish"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "fr_XX", "tgt_lang": "es_XX"},
    ("Spanish", "French"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "es_XX", "tgt_lang": "fr_XX"},

    # French <-> Urdu
    ("French", "Urdu"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "fr_XX", "tgt_lang": "ur_PK"},
    ("Urdu", "French"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "ur_PK", "tgt_lang": "fr_XX"},

    # Japanese <-> Spanish
    ("Japanese", "Spanish"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "ja_XX", "tgt_lang": "es_XX"},
    ("Spanish", "Japanese"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "es_XX", "tgt_lang": "ja_XX"},

    # Japanese <-> Urdu
    ("Japanese", "Urdu"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "ja_XX", "tgt_lang": "ur_PK"},
    ("Urdu", "Japanese"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "ur_PK", "tgt_lang": "ja_XX"},

    # Spanish <-> Urdu
    ("Spanish", "Urdu"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "es_XX", "tgt_lang": "ur_PK"},
    ("Urdu", "Spanish"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "ur_PK", "tgt_lang": "es_XX"},
}

language_name_to_code = {
    "English": "en_XX",
    "Hindi": "hi_IN",
    "French": "fr_XX",
    "Japanese": "ja_XX",
    "Spanish": "es_XX",
    "Urdu": "ur_PK",
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

