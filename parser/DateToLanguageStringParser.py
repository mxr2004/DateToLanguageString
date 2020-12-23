import re
from datetime import datetime

from ..utils import language


def convertDateTimeToString(dateTime, outputLanguage):
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
