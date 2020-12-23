from datetime import datetime

from utils import language


def convertDateTimeToString(dateTime, outputLanguage):
    useFormat = language.getTranslation(translationtype="dateFormat", language=outputLanguage)
    # Start converting
    dateTime: datetime
    print(useFormat.split())



# class DateToLanguageStringParser:
#     def __init__(self):
#         pass
#