# utils/language_utils.py

supported_translation_models = {
    # English - Hindi
    ("English", "Hindi"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "en_XX", "tgt_lang": "hi_IN"},
    ("Hindi", "English"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "hi_IN", "tgt_lang": "en_XX"},

    # English - French
    ("English", "French"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "en_XX", "tgt_lang": "fr_XX"},
    ("French", "English"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "fr_XX", "tgt_lang": "en_XX"},

    # English - Japanese
    ("English", "Japanese"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "en_XX", "tgt_lang": "ja_XX"},
    ("Japanese", "English"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "ja_XX", "tgt_lang": "en_XX"},

    # English  Spanish
    ("English", "Spanish"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "en_XX", "tgt_lang": "es_XX"},
    ("Spanish", "English"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "es_XX", "tgt_lang": "en_XX"},

    # English - German
    ("English", "German"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "en_XX", "tgt_lang": "de_DE"},
    ("German", "English"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "de_DE", "tgt_lang": "en_XX"},

    # English - Chinese
    ("English", "Chinese"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "en_XX", "tgt_lang": "zh_CN"},
    ("Chinese", "English"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "zh_CN", "tgt_lang": "en_XX"},

    # English - Korean
    ("English", "Korean"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "en_XX", "tgt_lang": "ko_KR"},
    ("Korean", "English"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "ko_KR", "tgt_lang": "en_XX"},

    # English - Russian
    ("English", "Russian"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "en_XX", "tgt_lang": "ru_RU"},
    ("Russian", "English"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "ru_RU", "tgt_lang": "en_XX"},

    # English - Arabic
    ("English", "Arabic"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "en_XX", "tgt_lang": "ar_AR"},
    ("Arabic", "English"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "ar_AR", "tgt_lang": "en_XX"},

    # English - Urdu
    ("English", "Urdu"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "en_XX", "tgt_lang": "ur_PK"},
    ("Urdu", "English"): {"model": "facebook/mbart-large-50-many-to-many-mmt", "src_lang": "ur_PK", "tgt_lang": "en_XX"},
}


def get_supported_languages():
    langs = set()
    for pair in supported_translation_models:
        langs.add(pair[0])
        langs.add(pair[1])
    return sorted(list(langs))

def get_model_config(src_lang, tgt_lang):
    return supported_translation_models.get((src_lang, tgt_lang))
