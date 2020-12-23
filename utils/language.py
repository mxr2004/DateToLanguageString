import logging
import pkgutil
from importlib import import_module

from .. import translations


def getTranslation(translationtype, searchlanguage):
    for language in pkgutil.iter_modules(translations.__path__):
        logging.debug("[TRANSLATING] Now in module: %s" % language.name)
        if language.name == searchlanguage:
            if translationtype in getTranslations(moduleName=language.name):
                return getTranslations(moduleName=language.name)["%s" % translationtype]
    return None


def getTranslations(moduleName) -> dict:
    module = __name__.replace(".utils.language", "")
    moduleObject = import_module(name="%s.translations.%s" % (module, moduleName))
    translationDict = getattr(moduleObject, moduleName)
    return translationDict
