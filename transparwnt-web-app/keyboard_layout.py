import platform
import subprocess
import ctypes

def get_keyboard_layout():
    os_name = platform.system()
    if os_name == 'Windows':
        user32 = ctypes.WinDLL('user32', use_last_error=True)
        curr_window = user32.GetForegroundWindow()
        thread_id = user32.GetWindowThreadProcessId(curr_window, None)
        klid = user32.GetKeyboardLayout(thread_id)
        lid = klid & (2**16 - 1)
        return hex(lid)
    elif os_name == 'Darwin':
        layout = subprocess.check_output('''/usr/bin/osascript -e \"tell application \\\"System Events\\\" to tell process \\\"SystemUIServer\\\" to get value of first menu bar item of menu bar 1 whose description is \\\"text input\\\"\"''',
        shell=True )
        return layout.decode('utf-8').strip()
    elif os_name == 'Linux':
        layout = subprocess.check_output(
            "setxkbmap -query | grep layout",
            shell=True
        )
        return layout.decode('utf-8').strip().split(":")[1].strip()
    else:
        return "Unsupported OS"

def get_keyboard():
    keyb = get_keyboard_layout()
    if keyb in keyboard_layouts:
        res = keyboard_layouts[keyb]
        return res

from get_codes_dict import load_csv_string_to_dict

result = load_csv_string_to_dict()
keyboard_layouts = result

## I want you to merge this dict with the ISO Language code Tableinto one dataset so when i look for a keyboard layout code, ill get the Name but also the langauge ids, short and long

keyboard_layouts_x = {
    "00000401": "Arabic (101)",
    "0x401": "Arabic (101)",
    "00000402": "Bulgarian (Typewriter)",
    "0x402": "Bulgarian (Typewriter)",
    "00000404": "Chinese (Traditional) - US Keyboard",
    "0x404": "Chinese (Traditional) - US Keyboard",
    "00000405": "Czech",
    "0x405": "Czech",
    "00000406": "Danish",
    "0x406": "Danish",
    "00000407": "German",
    "0x407": "German",
    "00000408": "Greek",
    "0x408": "Greek",
    "00000409": "US",
    "0x409": "US",
    "0000040a": "Spanish",
    "0x40a": "Spanish",
    "0000040b": "Finnish",
    "0x40b": "Finnish",
    "0000040c": "French",
    "0x40c": "French",
    "0000040d": "Hebrew",
    "0x40d": "Hebrew",
    "0000040e": "Hungarian",
    "0x40e": "Hungarian",
    "0000040f": "Icelandic",
    "0x40f": "Icelandic",
    "00000410": "Italian",
    "0x410": "Italian",
    "00000411": "Japanese",
    "0x411": "Japanese",
    "00000412": "Korean",
    "0x412": "Korean",
    "00000413": "Dutch",
    "0x413": "Dutch",
    "00000414": "Norwegian",
    "0x414": "Norwegian",
    "00000415": "Polish (Programmers)",
    "0x415": "Polish (Programmers)",
    "00000416": "Portuguese (Brazilian ABNT)",
    "0x416": "Portuguese (Brazilian ABNT)",
    "00000418": "Romanian (Legacy)",
    "0x418": "Romanian (Legacy)",
    "00000419": "Russian",
    "0x419": "Russian",
    "0000041a": "Standard",
    "0x41a": "Standard",
    "0000041b": "Slovak",
    "0x41b": "Slovak",
    "0000041c": "Albanian",
    "0x41c": "Albanian",
    "0000041d": "Swedish",
    "0x41d": "Swedish",
    "0000041e": "Thai Kedmanee",
    "0x41e": "Thai Kedmanee",
    "0000041f": "Turkish Q",
    "0x41f": "Turkish Q",
    "00000420": "Urdu",
    "0x420": "Urdu",
    "00000422": "Ukrainian",
    "0x422": "Ukrainian",
    "00000423": "Belarusian",
    "0x423": "Belarusian",
    "00000424": "Slovenian",
    "0x424": "Slovenian",
    "00000425": "Estonian",
    "0x425": "Estonian",
    "00000426": "Latvian",
    "0x426": "Latvian",
    "00000427": "Lithuanian IBM",
    "0x427": "Lithuanian IBM",
    "00000428": "Tajik",
    "0x428": "Tajik",
    "00000429": "Persian",
    "0x429": "Persian",
    "0000042a": "Vietnamese",
    "0x42a": "Vietnamese",
    "0000042b": "Armenian Eastern",
    "0x42b": "Armenian Eastern",
    "0000042c": "Azeri Latin",
    "0x42c": "Azeri Latin",
    "0000042e": "Sorbian Standard (Legacy)",
    "0x42e": "Sorbian Standard (Legacy)",
    "0000042f": "Macedonian (FYROM)",
    "0x42f": "Macedonian (FYROM)",
    "00000432": "Setswana",
    "0x432": "Setswana",
    "00000437": "Georgian",
    "0x437": "Georgian",
    "00000438": "Faeroese",
    "0x438": "Faeroese",
    "00000439": "Devanagari - INSCRIPT",
    "0x439": "Devanagari - INSCRIPT",
    "0000043a": "Maltese 47-Key",
    "0x43a": "Maltese 47-Key",
    "0000043b": "Norwegian with Sami",
    "0x43b": "Norwegian with Sami",
    "0000043f": "Kazakh",
    "0x43f": "Kazakh",
    "00000440": "Kyrgyz Cyrillic",
    "0x440": "Kyrgyz Cyrillic",
    "00000442": "Turkmen",
    "0x442": "Turkmen",
    "00000444": "Tatar (Legacy)",
    "0x444": "Tatar (Legacy)",
    "00000445": "Bengali",
    "0x445": "Bengali",
    "00000446": "Punjabi",
    "0x446": "Punjabi",
    "00000447": "Gujarati",
    "0x447": "Gujarati",
    "00000448": "Oriya",
    "0x448": "Oriya",
    "00000449": "Tamil",
    "0x449": "Tamil",
    "0000044a": "Telugu",
    "0x44a": "Telugu",
    "0000044b": "Kannada",
    "0x44b": "Kannada",
    "0000044c": "Malayalam",
    "0x44c": "Malayalam",
    "0000044d": "Assamese - INSCRIPT",
    "0x44d": "Assamese - INSCRIPT",
    "0000044e": "Marathi",
    "0x44e": "Marathi",
    "00000450": "Mongolian Cyrillic",
    "0x450": "Mongolian Cyrillic",
    "00000451": "Tibetan (PRC)",
    "0x451": "Tibetan (PRC)",
    "00000452": "United Kingdom Extended",
    "0x452": "United Kingdom Extended",
    "00000453": "Khmer",
    "0x453": "Khmer",
    "00000454": "Lao",
    "0x454": "Lao",
    "0000045a": "Syriac",
    "0x45a": "Syriac",
    "0000045b": "Sinhala",
    "0x45b": "Sinhala",
    "0000045c": "Cherokee Nation",
    "0x45c": "Cherokee Nation",
    "00000461": "Nepali",
    "0x461": "Nepali",
    "00000463": "Pashto (Afghanistan)",
    "0x463": "Pashto (Afghanistan)",
    "00000465": "Divehi Phonetic",
    "0x465": "Divehi Phonetic",
    "00000468": "Hausa",
    "0x468": "Hausa",
    "0000046a": "Yoruba",
    "0x46a": "Yoruba",
    "0000046c": "Sesotho sa Leboa",
    "0x46c": "Sesotho sa Leboa",
    "0000046d": "Bashkir",
    "0x46d": "Bashkir",
    "0000046e": "Luxembourgish",
    "0x46e": "Luxembourgish",
    "0000046f": "Greenlandic",
    "0x46f": "Greenlandic",
    "00000470": "Igbo",
    "0x470": "Igbo",
    "00000474": "Guarani",
    "0x474": "Guarani",
    "00000475": "Hawaiian",
    "0x475": "Hawaiian",
    "00000480": "Uyghur (Legacy)",
    "0x480": "Uyghur (Legacy)",
    "00000481": "Maori",
    "0x481": "Maori",
    "00000485": "Sakha",
    "0x485": "Sakha",
    "00000488": "Wolof",
    "0x488": "Wolof",
    "00000492": "Central Kurdish",
    "0x492": "Central Kurdish",
    "00000804": "Chinese (Simplified) - US Keyboard",
    "0x804": "Chinese (Simplified) - US Keyboard",
    "00000807": "Swiss German",
    "0x807": "Swiss German",
    "00000809": "United Kingdom",
    "0x809": "United Kingdom",
    "0000080a": "Latin American",
    "0x80a": "Latin American",
    "0000080c": "Belgian French",
    "0x80c": "Belgian French",
    "00000813": "Belgian (Period)",
    "0x813": "Belgian (Period)",
    "00000816": "Portuguese",
    "0x816": "Portuguese",
    "0000081a": "Serbian (Latin)",
    "0x81a": "Serbian (Latin)",
    "0000082c": "Azeri Cyrillic",
    "0x82c": "Azeri Cyrillic",
    "0000083b": "Swedish with Sami",
    "0x83b": "Swedish with Sami",
    "00000843": "Uzbek Cyrillic",
    "0x843": "Uzbek Cyrillic",
    "00000850": "Mongolian (Mongolian Script)",
    "0x850": "Mongolian (Mongolian Script)",
    "0000085d": "Inuktitut - Latin",
    "0x85d": "Inuktitut - Latin",
    "0000085f": "Central Atlas Tamazight",
    "0x85f": "Central Atlas Tamazight",
    "00000c04": "Chinese (Traditional, Hong Kong S.A.R.) - US Keyboard",
    "0xc04": "Chinese (Traditional, Hong Kong S.A.R.) - US Keyboard",
    "00000c0c": "Canadian French (Legacy)",
    "0xc0c": "Canadian French (Legacy)",
    "00000c1a": "Serbian (Cyrillic)",
    "0xc1a": "Serbian (Cyrillic)",
    "00000C51": "Dzongkha",
    "0xc51": "Dzongkha",
    "00001004": "Chinese (Simplified, Singapore) - US Keyboard",
    "0x1004": "Chinese (Simplified, Singapore) - US Keyboard",
    "00001009": "Canadian French",
    "0x1009": "Canadian French",
    "0000100c": "Swiss French",
    "0x100c": "Swiss French",
    "0000105f": "Tifinagh (Basic)",
    "0x105f": "Tifinagh (Basic)",
    "00001404": "Chinese (Traditional, Macao S.A.R.) - US Keyboard",
    "0x1404": "Chinese (Traditional, Macao S.A.R.) - US Keyboard",
    "00001809": "Irish",
    "0x1809": "Irish",
    "0000201a": "Bosnian (Cyrillic)",
    "0x201a": "Bosnian (Cyrillic)",
    "00004009": "India",
    "0x4009": "India",
    "00010401": "Arabic (102)",
    "0x10401": "Arabic (102)",
    "00010402": "Bulgarian (Latin)",
    "0x10402": "Bulgarian (Latin)",
    "00010405": "Czech (QWERTY)",
    "0x10405": "Czech (QWERTY)",
    "00010407": "German (IBM)",
    "0x10407": "German (IBM)",
    "00010408": "Greek (220)",
    "0x10408": "Greek (220)",
    "00010409": "United States-Dvorak",
    "0x10409": "United States-Dvorak",
    "0001040a": "Spanish Variation",
    "0x1040a": "Spanish Variation",
    "0001040e": "Hungarian 101-key",
    "0x1040e": "Hungarian 101-key",
    "00010410": "Italian (142)",
    "0x10410": "Italian (142)",
    "00010415": "Polish (214)",
    "0x10415": "Polish (214)",
    "00010416": "Portuguese (Brazilian ABNT2)",
    "0x10416": "Portuguese (Brazilian ABNT2)",
    "00010418": "Romanian (Standard)",
    "0x10418": "Romanian (Standard)",
    "00010419": "Russian (Typewriter)",
    "0x10419": "Russian (Typewriter)",
    "0001041b": "Slovak (QWERTY)",
    "0x1041b": "Slovak (QWERTY)",
    "0001041e": "Thai Pattachote",
    "0x1041e": "Thai Pattachote",
    "0001041f": "Turkish F",
    "0x1041f": "Turkish F",
    "00010426": "Latvian (QWERTY)",
    "0x10426": "Latvian (QWERTY)",
    "00010427": "Lithuanian",
    "0x10427": "Lithuanian",
    "0001042b": "Armenian Western",
    "0x1042b": "Armenian Western",
    "0001042c": "Azerbaijani (Standard)",
    "0x1042c": "Azerbaijani (Standard)",
    "0001042e": "Sorbian Extended",
    "0x1042e": "Sorbian Extended",
    "0001042f": "Macedonian (FYROM) - Standard",
    "0x1042f": "Macedonian (FYROM) - Standard",
    "00010437": "Georgian (QWERTY)",
    "0x10437": "Georgian (QWERTY)",
    "00010439": "Hindi Traditional",
    "0x10439": "Hindi Traditional",
    "0001043a": "Maltese 48-Key",
    "0x1043a": "Maltese 48-Key",
    "0001043b": "Sami Extended Norway",
    "0x1043b": "Sami Extended Norway",
    "00010444": "Tatar",
    "0x10444": "Tatar",
    "00010445": "Bengali - INSCRIPT (Legacy)",
    "0x10445": "Bengali - INSCRIPT (Legacy)",
    "00010451": "Tibetan (PRC) - Updated",
    "0x10451": "Tibetan (PRC) - Updated",
    "00010453": "Khmer (NIDA)",
    "0x10453": "Khmer (NIDA)",
    "0001045a": "Syriac Phonetic",
    "0x1045a": "Syriac Phonetic",
    "0001045b": "Sinhala - Wij 9",
    "0x1045b": "Sinhala - Wij 9",
    "0001045c": "Cherokee Nation Phonetic",
    "0x1045c": "Cherokee Nation Phonetic",
    "0001045d": "Inuktitut - Naqittaut",
    "0x1045d": "Inuktitut - Naqittaut",
    "00010465": "Divehi Typewriter",
    "0x10465": "Divehi Typewriter",
    "00010480": "Uyghur",
    "0x10480": "Uyghur",
    "0001080c": "Belgian (Comma)",
    "0x1080c": "Belgian (Comma)",
    "0001083b": "Finnish with Sami",
    "0x1083b": "Finnish with Sami",
    "00010850": "Traditional Mongolian (Standard)",
    "0x10850": "Traditional Mongolian (Standard)",
    "00010c00": "Myanmar (Phonetic order)",
    "0x10c00": "Myanmar (Phonetic order)",
    "00011009": "Canadian Multilingual Standard",
    "0x11009": "Canadian Multilingual Standard",
    "0001105f": "Tifinagh (Full)",
    "0x1105f": "Tifinagh (Full)",
    "00011809": "Gaelic",
    "0x11809": "Gaelic",
    "00020401": "Arabic (102) AZERTY",
    "0x20401": "Arabic (102) AZERTY",
    "00020402": "Bulgarian (Phonetic)",
    "0x20402": "Bulgarian (Phonetic)",
    "00020405": "Czech Programmers",
    "0x20405": "Czech Programmers",
    "00020408": "Greek (319)",
    "0x20408": "Greek (319)",
    "00020409": "United States-International",
    "0x20409": "United States-International",
    "0002040d": "Hebrew (Standard)",
    "0x2040d": "Hebrew (Standard)",
    "00020418": "Romanian (Programmers)",
    "0x20418": "Romanian (Programmers)",
    "00020419": "Russian - Mnemonic",
    "0x20419": "Russian - Mnemonic",
    "0002041e": "Thai Kedmanee (non-ShiftLock)",
    "0x2041e": "Thai Kedmanee (non-ShiftLock)",
    "00020422": "Ukrainian (Enhanced)",
    "0x20422": "Ukrainian (Enhanced)",
    "00020426": "Latvian (Standard)",
    "0x20426": "Latvian (Standard)",
    "00020427": "Lithuanian Standard",
    "0x20427": "Lithuanian Standard",
    "0002042b": "Armenian Phonetic",
    "0x2042b": "Armenian Phonetic",
    "0002042e": "Sorbian Standard",
    "0x2042e": "Sorbian Standard",
    "00020437": "Georgian (Ergonomic)",
    "0x20437": "Georgian (Ergonomic)",
    "00020445": "Bengali - INSCRIPT",
    "0x20445": "Bengali - INSCRIPT",
    "00020449": "Tamil 99",
    "0x20449": "Tamil 99",
    "0002083b": "Sami Extended Finland-Sweden",
    "0x2083b": "Sami Extended Finland-Sweden",
    "00020c00": "New Tai Lue",
    "0x20c00": "New Tai Lue",
    "00030402": "Bulgarian",
    "0x30402": "Bulgarian",
    "00030408": "Greek (220) Latin",
    "0x30408": "Greek (220) Latin",
    "00030409": "United States-Dvorak for left hand",
    "0x30409": "United States-Dvorak for left hand",
    "0003041e": "Thai Pattachote (non-ShiftLock)",
    "0x3041e": "Thai Pattachote (non-ShiftLock)",
    "0003042b": "Armenian Typewriter",
    "0x3042b": "Armenian Typewriter",
    "00030437": "Georgian Ministry of Education and Science Schools",
    "0x30437": "Georgian Ministry of Education and Science Schools",
    "00030c00": "Tai Le",
    "0x30c00": "Tai Le",
    "00040402": "Bulgarian (Phonetic Traditional)",
    "0x40402": "Bulgarian (Phonetic Traditional)",
    "00040408": "Greek (319) Latin",
    "0x40408": "Greek (319) Latin",
    "00040409": "United States-Dvorak for right hand",
    "0x40409": "United States-Dvorak for right hand",
    "00040437": "Georgian (Old Alphabets)",
    "0x40437": "Georgian (Old Alphabets)",
    "00040c00": "Ogham",
    "0x40c00": "Ogham",
    "00050408": "Greek Latin",
    "0x50408": "Greek Latin",
    "00050409": "US English Table for IBM Arabic 238_L",
    "0x50409": "US English Table for IBM Arabic 238_L",
    "00050429": "Persian (Standard)",
    "0x50429": "Persian (Standard)",
    "00060408": "Greek Polytonic",
    "0x60408": "Greek Polytonic",
    "00070c00": "Lisu (Basic)",
    "0x70c00": "Lisu (Basic)",
    "00080c00": "Lisu (Standard)",
    "0x80c00": "Lisu (Standard)",
    "00090c00": "N\u2019Ko",
    "0x90c00": "N\u2019Ko",
    "000a0c00": "Phags-pa",
    "0xa0c00": "Phags-pa",
    "000b0c00": "Buginese",
    "0xb0c00": "Buginese",
    "000c0c00": "Gothic",
    "0xc0c00": "Gothic",
    "000d0c00": "Ol Chiki",
    "0xd0c00": "Ol Chiki",
    "000e0c00": "Osmanya",
    "0xe0c00": "Osmanya",
    "000f0c00": "Old Italic",
    "0xf0c00": "Old Italic",
    "00100c00": "Sora",
    "0x100c00": "Sora",
    "00110c00": "Javanese",
    "0x110c00": "Javanese",
    "00120c00": "Futhark",
    "0x120c00": "Futhark",
    "00130c00": "Myanmar (Visual Order)",
    "0x130c00": "Myanmar (Visual Order)",
    "00140c00": "ADLaM",
    "0x140c00": "ADLaM",
    "00150c00": "Osage",
    "0x150c00": "Osage"
}

'''
ISO Language Code Table

Code	Name
af	Afrikaans
af-ZA	Afrikaans (South Africa)
ar	Arabic
ar-AE	Arabic (U.A.E.)
ar-BH	Arabic (Bahrain)
ar-DZ	Arabic (Algeria)
ar-EG	Arabic (Egypt)
ar-IQ	Arabic (Iraq)
ar-JO	Arabic (Jordan)
ar-KW	Arabic (Kuwait)
ar-LB	Arabic (Lebanon)
ar-LY	Arabic (Libya)
ar-MA	Arabic (Morocco)
ar-OM	Arabic (Oman)
ar-QA	Arabic (Qatar)
ar-SA	Arabic (Saudi Arabia)
ar-SY	Arabic (Syria)
ar-TN	Arabic (Tunisia)
ar-YE	Arabic (Yemen)
az	Azeri (Latin)
az-AZ	Azeri (Latin) (Azerbaijan)
az-AZ	Azeri (Cyrillic) (Azerbaijan)
be	Belarusian
be-BY	Belarusian (Belarus)
bg	Bulgarian
bg-BG	Bulgarian (Bulgaria)
bs-BA	Bosnian (Bosnia and Herzegovina)
ca	Catalan
ca-ES	Catalan (Spain)
cs	Czech
cs-CZ	Czech (Czech Republic)
cy	Welsh
cy-GB	Welsh (United Kingdom)
da	Danish
da-DK	Danish (Denmark)
de	German
de-AT	German (Austria)
de-CH	German (Switzerland)
de-DE	German (Germany)
de-LI	German (Liechtenstein)
de-LU	German (Luxembourg)
dv	Divehi
dv-MV	Divehi (Maldives)
el	Greek
el-GR	Greek (Greece)
en	English
en-AU	English (Australia)
en-BZ	English (Belize)
en-CA	English (Canada)
en-CB	English (Caribbean)
en-GB	English (United Kingdom)
en-IE	English (Ireland)
en-JM	English (Jamaica)
en-NZ	English (New Zealand)
en-PH	English (Republic of the Philippines)
en-TT	English (Trinidad and Tobago)
en-US	English (United States)
en-ZA	English (South Africa)
en-ZW	English (Zimbabwe)
eo	Esperanto
es	Spanish
es-AR	Spanish (Argentina)
es-BO	Spanish (Bolivia)
es-CL	Spanish (Chile)
es-CO	Spanish (Colombia)
es-CR	Spanish (Costa Rica)
es-DO	Spanish (Dominican Republic)
es-EC	Spanish (Ecuador)
es-ES	Spanish (Castilian)
es-ES	Spanish (Spain)
es-GT	Spanish (Guatemala)
es-HN	Spanish (Honduras)
es-MX	Spanish (Mexico)
es-NI	Spanish (Nicaragua)
es-PA	Spanish (Panama)
es-PE	Spanish (Peru)
es-PR	Spanish (Puerto Rico)
es-PY	Spanish (Paraguay)
es-SV	Spanish (El Salvador)
es-UY	Spanish (Uruguay)
es-VE	Spanish (Venezuela)
et	Estonian
et-EE	Estonian (Estonia)
eu	Basque
eu-ES	Basque (Spain)
fa	Farsi
fa-IR	Farsi (Iran)
fi	Finnish
fi-FI	Finnish (Finland)
fo	Faroese
fo-FO	Faroese (Faroe Islands)
fr	French
fr-BE	French (Belgium)
fr-CA	French (Canada)
fr-CH	French (Switzerland)
fr-FR	French (France)
fr-LU	French (Luxembourg)
fr-MC	French (Principality of Monaco)
gl	Galician
gl-ES	Galician (Spain)
gu	Gujarati
gu-IN	Gujarati (India)
he	Hebrew
he-IL	Hebrew (Israel)
hi	Hindi
hi-IN	Hindi (India)
hr	Croatian
hr-BA	Croatian (Bosnia and Herzegovina)
hr-HR	Croatian (Croatia)
hu	Hungarian
hu-HU	Hungarian (Hungary)
hy	Armenian
hy-AM	Armenian (Armenia)
id	Indonesian
id-ID	Indonesian (Indonesia)
is	Icelandic
is-IS	Icelandic (Iceland)
it	Italian
it-CH	Italian (Switzerland)
it-IT	Italian (Italy)
ja	Japanese
ja-JP	Japanese (Japan)
ka	Georgian
ka-GE	Georgian (Georgia)
kk	Kazakh
kk-KZ	Kazakh (Kazakhstan)
kn	Kannada
kn-IN	Kannada (India)
ko	Korean
ko-KR	Korean (Korea)
kok	Konkani
kok-IN	Konkani (India)
ky	Kyrgyz
ky-KG	Kyrgyz (Kyrgyzstan)
lt	Lithuanian
lt-LT	Lithuanian (Lithuania)
lv	Latvian
lv-LV	Latvian (Latvia)
mi	Maori
mi-NZ	Maori (New Zealand)
mk	FYRO Macedonian
mk-MK	FYRO Macedonian (Former Yugoslav Republic of Macedonia)
mn	Mongolian
mn-MN	Mongolian (Mongolia)
mr	Marathi
mr-IN	Marathi (India)
ms	Malay
ms-BN	Malay (Brunei Darussalam)
ms-MY	Malay (Malaysia)
mt	Maltese
mt-MT	Maltese (Malta)
nb	Norwegian (Bokm?l)
nb-NO	Norwegian (Bokm?l) (Norway)
nl	Dutch
nl-BE	Dutch (Belgium)
nl-NL	Dutch (Netherlands)
nn-NO	Norwegian (Nynorsk) (Norway)
ns	Northern Sotho
ns-ZA	Northern Sotho (South Africa)
pa	Punjabi
pa-IN	Punjabi (India)
pl	Polish
pl-PL	Polish (Poland)
ps	Pashto
ps-AR	Pashto (Afghanistan)
pt	Portuguese
pt-BR	Portuguese (Brazil)
pt-PT	Portuguese (Portugal)
qu	Quechua
qu-BO	Quechua (Bolivia)
qu-EC	Quechua (Ecuador)
qu-PE	Quechua (Peru)
ro	Romanian
ro-RO	Romanian (Romania)
ru	Russian
ru-RU	Russian (Russia)
sa	Sanskrit
sa-IN	Sanskrit (India)
se	Sami (Northern)
se-FI	Sami (Northern) (Finland)
se-FI	Sami (Skolt) (Finland)
se-FI	Sami (Inari) (Finland)
se-NO	Sami (Northern) (Norway)
se-NO	Sami (Lule) (Norway)
se-NO	Sami (Southern) (Norway)
se-SE	Sami (Northern) (Sweden)
se-SE	Sami (Lule) (Sweden)
se-SE	Sami (Southern) (Sweden)
sk	Slovak
sk-SK	Slovak (Slovakia)
sl	Slovenian
sl-SI	Slovenian (Slovenia)
sq	Albanian
sq-AL	Albanian (Albania)
sr-BA	Serbian (Latin) (Bosnia and Herzegovina)
sr-BA	Serbian (Cyrillic) (Bosnia and Herzegovina)
sr-SP	Serbian (Latin) (Serbia and Montenegro)
sr-SP	Serbian (Cyrillic) (Serbia and Montenegro)
sv	Swedish
sv-FI	Swedish (Finland)
sv-SE	Swedish (Sweden)
sw	Swahili
sw-KE	Swahili (Kenya)
syr	Syriac
syr-SY	Syriac (Syria)
ta	Tamil
ta-IN	Tamil (India)
te	Telugu
te-IN	Telugu (India)
th	Thai
th-TH	Thai (Thailand)
tl	Tagalog
tl-PH	Tagalog (Philippines)
tn	Tswana
tn-ZA	Tswana (South Africa)
tr	Turkish
tr-TR	Turkish (Turkey)
tt	Tatar
tt-RU	Tatar (Russia)
ts	Tsonga
uk	Ukrainian
uk-UA	Ukrainian (Ukraine)
ur	Urdu
ur-PK	Urdu (Islamic Republic of Pakistan)
uz	Uzbek (Latin)
uz-UZ	Uzbek (Latin) (Uzbekistan)
uz-UZ	Uzbek (Cyrillic) (Uzbekistan)
vi	Vietnamese
vi-VN	Vietnamese (Viet Nam)
xh	Xhosa
xh-ZA	Xhosa (South Africa)
zh	Chinese
zh-CN	Chinese (S)
zh-HK	Chinese (Hong Kong)
zh-MO	Chinese (Macau)
zh-SG	Chinese (Singapore)
zh-TW	Chinese (T)
zu	Zulu
zu-ZA	Zulu (South Africa)
'''

