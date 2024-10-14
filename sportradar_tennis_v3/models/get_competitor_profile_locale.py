from enum import Enum


class GetCompetitorProfileLocale(str, Enum):
    AA = "aa"
    AZE = "aze"
    BG = "bg"
    BR = "br"
    BS = "bs"
    CS = "cs"
    DA = "da"
    DE = "de"
    EL = "el"
    EN = "en"
    ES = "es"
    ET = "et"
    FI = "fi"
    FR = "fr"
    HEB = "heb"
    HR = "hr"
    HU = "hu"
    ID = "id"
    IT = "it"
    JA = "ja"
    KA = "ka"
    KO = "ko"
    LT = "lt"
    LV = "lv"
    ME = "me"
    MK = "mk"
    NL = "nl"
    NO = "no"
    PL = "pl"
    PT = "pt"
    RO = "ro"
    RU = "ru"
    SE = "se"
    SK = "sk"
    SL = "sl"
    SQI = "sqi"
    SR = "sr"
    SRL = "srl"
    TH = "th"
    TR = "tr"
    UKR = "ukr"
    VI = "vi"
    ZH = "zh"
    ZHT = "zht"

    def __str__(self) -> str:
        return str(self.value)
