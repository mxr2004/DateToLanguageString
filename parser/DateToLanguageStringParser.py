import re
from datetime import datetime, timedelta

from ..utils import language


def convertDateTimeToString(dateTime: datetime, outputLanguage, alwaysShowDate=False):
    if not alwaysShowDate:
        today = datetime.utcnow()
        dateTime = dateTime - timedelta(days=1)
        delta: timedelta = today - dateTime
        if abs(delta.days / 30) >= 1:
            if abs(delta.days / 30) == 1:
                translation = language.getTranslation(translationtype="%s month ago",
                                                      searchlanguage=outputLanguage) % int(delta.days / 30)
            else:
                translation = language.getTranslation(translationtype="%s months ago",
                                                      searchlanguage=outputLanguage) % int(delta.days / 30)
        else:
            if delta.days == 1:
                translation = language.getTranslation(translationtype="%s day ago",
                                                      searchlanguage=outputLanguage) % delta.days
            else:
                translation = language.getTranslation(translationtype="%s days ago",
                                                      searchlanguage=outputLanguage) % delta.days
        return translation

    else:
        useFormat = language.getTranslation(translationtype="dateFormat", searchlanguage=outputLanguage)
        # Start converting
        dateTime: datetime
        print(useFormat.split())
        pattern = re.compile("%.")
        while pattern.search(useFormat):
            if "%d" in useFormat:
                useFormat = useFormat.replace("%d", str(dateTime.day))
            elif "%m" in useFormat:
                useFormat = useFormat.replace("%m", str(dateTime.month))
            elif "%Y" in useFormat:
                useFormat = useFormat.replace("%Y", str(dateTime.year))
            elif "%y" in useFormat:
                useFormat = useFormat.replace("%y", str(str(dateTime.year)[2:]))
            elif "%B" in useFormat:
                useFormat = useFormat.replace("%B", str(
                    language.getTranslation(translationtype="months", searchlanguage=outputLanguage)["full"][
                        dateTime.month - 1]))
            print(useFormat)
        return useFormat
