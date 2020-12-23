import logging
import pkgutil
from importlib import import_module

import translations


def getTranslation(translationtype, language):
    for language in pkgutil.iter_modules(translations.__path__):
        logging.debug("[TRANSLATING] Now in module: %s" % language.name)
        if language.name == language:
            # for txt in getTranslations(language.name):
            #     if txt in text or text == txt:
            #         if returnText == text:
            #             returnText = ""
            #         returnText += getTranslations(language.name)["%s" % text]
            if translationtype in getTranslations(language.name):
                return getTranslations(language.name)["%s" % translationtype]
    return None


def getTranslations(moduleName) -> dict:
    moduleObject = import_module("sources.translations.%s" % moduleName)
    translationDict = getattr(moduleObject, moduleName)
    return translationDict
