data_csv = '''language_code, language_label, subtag, english_name, native_name, speech_code,
"00000401", "Arabic (101)", ar,Arabic,العربية,ar-EG,
"0x401", "Arabic (101)", ar,Arabic,العربية,ar-EG,
"00000402", "Bulgarian (Typewriter)", bg,Bulgarian,български,bg-BG,
"0x402", "Bulgarian (Typewriter)", bg,Bulgarian,български,bg-BG,
"00000404", "Chinese (Traditional) - US Keyboard", zh,Chinese,中文,,
"0x404", "Chinese (Traditional) - US Keyboard", zh,Chinese,中文,,
"00000405", "Czech", cs,Czech,čeština,cs-CZ,
"0x405", "Czech", cs,Czech,čeština,cs-CZ,
"00000406", "Danish", da,Danish,dansk,da-DK,
"0x406", "Danish", da,Danish,dansk,da-DK,
"00000407", "German", de,German,Deutsch,de-DE,
"0x407", "German", de,German,Deutsch,de-DE,
"00000408", "Greek", el,Greek,ελληνικά,el-GR,
"0x408", "Greek", el,Greek,ελληνικά,el-GR,
"00000409", "US", en,English,English,en-US,
"0x409", "US", en,English,English,en-US,
"0000040a", "Spanish", es,Spanish,español,es-MX,
"0x40a", "Spanish", es,Spanish,español,es-MX,
"0000040b", "Finnish", fi,Finnish,suomi ,fi-FI,
"0x40b", "Finnish", fi,Finnish,suomi,fi-FI,
"0000040c", "French", fr,French,français,fr-FR,
"0x40c", "French", fr,French,français,fr-FR,
"0000040d", "Hebrew", he,Hebrew,עברית,iw-IL,
"0x40d", "Hebrew", he,Hebrew,עברית,iw-IL,
"0000040e", "Hungarian", hu,Hungarian,magyar,hu-HU,
"0x40e", "Hungarian", hu,Hungarian,magyar,hu-HU,
"0000040f", "Icelandic", is,Icelandic,íslenska,is-IS,
"0x40f", "Icelandic", is,Icelandic,íslenska,is-IS,
"00000410", "Italian", it,Italian,italiano,it-IT,
"0x410", "Italian", it,Italian,italiano,it-IT,
"00000411", "Japanese", ja,Japanese,日本語,ja-JP,
"0x411", "Japanese", ja,Japanese,日本語,ja-JP,
"00000412", "Korean", ko,Korean,한국어/韓國語, 조선말/朝鮮말,ko-KR,
"0x412", "Korean", ko,Korean,한국어/韓國語, 조선말/朝鮮말,ko-KR,
"00000413", "Dutch", nl,Dutch,Nederlands,nl-NL,
"0x413", "Dutch", nl,Dutch,Nederlands,nl-NL,
"00000414", "Norwegian", no,Norwegian,norsk,no-NO,
"0x414", "Norwegian", no,Norwegian,norsk,no-NO,
"00000415", "Polish (Programmers)", pl,Polish,polski,pl-PL,
"0x415", "Polish (Programmers)", pl,Polish,polski,pl-PL,
"00000416", "Portuguese (Brazilian ABNT)", pt,Portuguese,Português,pt-BR,
"0x416", "Portuguese (Brazilian ABNT)", pt,Portuguese,Português,pt-BR,
"00000418", "Romanian (Legacy)", ro,Romanian,română,ro-RO,
"0x418", "Romanian (Legacy)", ro,Romanian,română,ro-RO,
"00000419", "Russian", ru,Russian,русский,ru-RU,
"0x419", "Russian", ru,Russian,русский,ru-RU,
"0000041a", "Standard", ,, ,
"0x41a", "Standard", ,, ,
"0000041b", "Slovak", sk,Slovak,slovenčina,sk-SK,
"0x41b", "Slovak", sk,Slovak,slovenčina,sk-SK,
"0000041c", "Albanian", sq,Albanian,shqipe, ,
"0x41c", "Albanian", sq,Albanian,shqipe, ,
"0000041d", "Swedish", sv,Swedish,svenska,sv-SE,
"0x41d", "Swedish", sv,Swedish,svenska,sv-SE,
"0000041e", "Thai Kedmanee", th,Thai,ไทย,th-TH,
"0x41e", "Thai Kedmanee", th,Thai,ไทย,th-TH,
"0000041f", "Turkish Q", tr,Turkish,Türkçe,tr-TR,
"0x41f", "Turkish Q", tr,Turkish,Türkçe,tr-TR,
"00000420", "Urdu", ur,Urdu,اُردو, ,
"0x420", "Urdu", ur,Urdu,اُردو, ,
"00000422", "Ukrainian", uk,Ukrainian,українська,uk-UA,
"0x422", "Ukrainian", uk,Ukrainian,українська,uk-UA,
"00000423", "Belarusian", be,Belarusian,беларуская, ,
"0x423", "Belarusian", be,Belarusian,беларуская, ,
"00000424", "Slovenian", sl,Slovenian,slovenski ,sl-SI,
"0x424", "Slovenian", sl,Slovenian,slovenski,sl-SI,
"00000425", "Estonian", et,Estonian,eesti,et-EE,
"0x425", "Estonian", et,Estonian,eesti,et-EE,
"00000426", "Latvian", lv,Latvian,latviešu,lv-LV,
"0x426", "Latvian", lv,Latvian,latviešu,lv-LV,
"00000427", "Lithuanian IBM", lt,Lithuanian,lietuvių,lt-LT,
"0x427", "Lithuanian IBM", lt,Lithuanian,lietuvių,lt-LT,
"00000428", "Tajik", tg,Tajik,Тоҷикӣ, ,
"0x428", "Tajik", tg,Tajik,Тоҷикӣ, ,
"00000429", "Persian", fa,Persian,فارسى,fa-IR,
"0x429", "Persian", fa,Persian,فارسى,fa-IR,
"0000042a", "Vietnamese", vi,Vietnamese,Tiếng Việt/㗂越,vi-VN,
"0x42a", "Vietnamese", vi,Vietnamese,Tiếng Việt/㗂越,vi-VN,
"0000042b", "Armenian Eastern", hy,Armenian,Հայերեն,hy-AM,
"0x42b", "Armenian Eastern", hy,Armenian,Հայերեն,hy-AM,
"0000042c", "Azeri Latin", az,Azerbaijani,Azərbaycanlı, ,
"0x42c", "Azeri Latin", az,Azerbaijani,Azərbaycanlı, ,
"0000042e", "Sorbian Standard (Legacy)", wen,Lower Sorbian,dolnoserbšćina, ,
"0x42e", "Sorbian Standard (Legacy)", wen,Lower Sorbian,dolnoserbšćina, ,
"0000042f", "Macedonian (FYROM)", mk,Macedonian,македонски јазик,mk-MK,
"0x42f", "Macedonian (FYROM)", mk,Macedonian,македонски јазик,mk-MK,
"00000432", "Setswana", tn,Tswana,Setswana, ,
"0x432", "Setswana", tn,Tswana,Setswana, ,
"00000437", "Georgian", ka,Georgian,ქართული,ka-GE,
"0x437", "Georgian", ka,Georgian,ქართული,ka-GE,
"00000438", "Faeroese", fo,Faroese,føroyskt, ,
"0x438", "Faeroese", fo,Faroese,føroyskt, ,
"00000439", "Devanagari - INSCRIPT", hi,Hindi,हिंदी,hi-IN,
"0x439", "Devanagari - INSCRIPT", hi,Hindi,हिंदी,hi-IN,
"0000043a", "Maltese 47-Key", mt,Maltese,Malti, ,
"0x43a", "Maltese 47-Key", mt,Maltese,Malti, ,
"0000043b", "Norwegian with Sami", no,Norwegian,norsk,no-NO,
"0x43b", "Norwegian with Sami", no,Norwegian,norsk,no-NO,
"0000043f", "Kazakh", kk,Kazakh,Қазақша, ,
"0x43f", "Kazakh", kk,Kazakh,Қазақша, ,
"00000440", "Kyrgyz Cyrillic", ky,Kyrgyz,Кыргыз, ,
"0x440", "Kyrgyz Cyrillic", ky,Kyrgyz,Кыргыз, ,
"00000442", "Turkmen", tk,Turkmen,türkmençe, ,
"0x442", "Turkmen", tk,Turkmen,türkmençe, ,
"00000444", "Tatar (Legacy)", tt,Tatar,Татарча, ,
"0x444", "Tatar (Legacy)", tt,Tatar,Татарча, ,
"00000445", "Bengali", bn,Bengali,বাংলা,bn-IN,
"0x445", "Bengali", bn,Bengali,বাংলা,bn-IN,
"00000446", "Punjabi", pa,Punjabi,ਪੰਜਾਬੀ, ,
"0x446", "Punjabi", pa,Punjabi,ਪੰਜਾਬੀ, ,
"00000447", "Gujarati", gu,Gujarati,ગુજરાતી,gu-IN,
"0x447", "Gujarati", gu,Gujarati,ગુજરાતી,gu-IN,
"00000448", "Oriya", or,Odia,ଓଡ଼ିଆ, ,
"0x448", "Oriya", or,Odia,ଓଡ଼ିଆ, ,
"00000449", "Tamil", ta,Tamil,தமிழ்,ta-IN,
"0x449", "Tamil", ta,Tamil,தமிழ்,ta-IN,
"0000044a", "Telugu", te,Telugu,తెలుగు,te-IN,
"0x44a", "Telugu", te,Telugu,తెలుగు,te-IN,
"0000044b", "Kannada", kn,Kannada,ಕನ್ನಡ,kn-IN,
"0x44b", "Kannada", kn,Kannada,ಕನ್ನಡ,kn-IN,
"0000044c", "Malayalam", ml,Malayalam,മലയാളം,ml-IN,
"0x44c", "Malayalam", ml,Malayalam,മലയാളം,ml-IN,
"0000044d", "Assamese - INSCRIPT", as,Assamese,অসমীয়া, ,
"0x44d", "Assamese - INSCRIPT", as,Assamese,অসমীয়া, ,
"0000044e", "Marathi", mr,Marathi,मराठी,mr-IN,
"0x44e", "Marathi", mr,Marathi,मराठी,mr-IN,
"00000450", "Mongolian Cyrillic", mn,Mongolian,Монгол хэл/ᠮᠤᠨᠭᠭᠤᠯ ᠬᠡᠯᠡ,mn-MN,
"0x450", "Mongolian Cyrillic", mn,Mongolian,Монгол хэл/ᠮᠤᠨᠭᠭᠤᠯ ᠬᠡᠯᠡ,mn-MN,
"00000451", "Tibetan (PRC)", bo,Tibetan,བོད་ཡིག, ,
"0x451", "Tibetan (PRC)", bo,Tibetan,བོད་ཡིག, ,
"00000452", "United Kingdom Extended", en,English,English, ,
"0x452", "United Kingdom Extended", en,English,English, ,
"00000453", "Khmer", km,Khmer,ខ្មែរ,km-KH,
"0x453", "Khmer", km,Khmer,ខ្មែរ,km-KH,
"00000454", "Lao", lo,Lao,ລາວ,lo-LA,
"0x454", "Lao", lo,Lao,ລາວ,lo-LA,
"0000045a", "Syriac", syc,Syriac,ܣܘܪܝܝܐ, ,
"0x45a", "Syriac", syc,Syriac,ܣܘܪܝܝܐ, ,
"0000045b", "Sinhala", si,Sinhala,සිංහල,si-LK,
"0x45b", "Sinhala", si,Sinhala,සිංහල,si-LK,
"0000045c", "Cherokee Nation", chr,,, ,
"0x45c", "Cherokee Nation", chr,,, ,
"00000461", "Nepali", ne,Nepali,नेपाली (नेपाल),ne-NP,
"0x461", "Nepali", ne,Nepali,नेपाली (नेपाल),ne-NP,
"00000463", "Pashto (Afghanistan)", ps,Pashto,پښتو, ,
"0x463", "Pashto (Afghanistan)", ps,Pashto,پښتو, ,
"00000465", "Divehi Phonetic", dv,Divehi,ދިވެހިބަސް, ,
"0x465", "Divehi Phonetic", dv,Divehi,ދިވެހިބަސް, ,
"00000468", "Hausa", ha,Hausa,Hausa, ,
"0x468", "Hausa", ha,Hausa,Hausa, ,
"0000046a", "Yoruba", yo,Yoruba,Yoruba, ,
"0x46a", "Yoruba", yo,Yoruba,Yoruba, ,
"0000046c", "Sesotho sa Leboa", st,Sesotho,Sesotho sa Leboa, ,
"0x46c", "Sesotho sa Leboa", st,Sesotho,Sesotho sa Leboa, ,
"0000046d", "Bashkir", ba,Bashkir,Башҡорт, ,
"0x46d", "Bashkir", ba,Bashkir,Башҡорт, ,
"0000046e", "Luxembourgish", lb,Luxembourgish,Lëtzebuergesch, ,
"0x46e", "Luxembourgish", lb,Luxembourgish,Lëtzebuergesch, ,
"0000046f", "Greenlandic", kl,Greenlandic,kalaallisut,kl-GL,
"0x46f", "Greenlandic", kl,Greenlandic,kalaallisut,kl-GL,
"00000470", "Igbo", ig,Igbo,Igbo, ,
"0x470", "Igbo", ig,Igbo,Igbo, ,
"00000474", "Guarani", gn,Guarani,Avañe'ẽ, ,
"0x474", "Guarani", gn,Guarani,Avañe'ẽ, ,
"00000475", "Hawaiian", haw,Hawaiian,, ,
"0x475", "Hawaiian", haw,Hawaiian,, ,
"00000480", "Uyghur (Legacy)", ug,Uyghur,ئۇيغۇرچە, ,
"0x480", "Uyghur (Legacy)", ug,Uyghur,ئۇيغۇرچە, ,
"00000481", "Maori", mi,Maori,Reo Māori, ,
"0x481", "Maori", mi,Maori,Reo Māori, ,
"00000485", "Sakha", sah,Yakut,саха, ,
"0x485", "Sakha", sah,Yakut,саха, ,
"00000488", "Wolof", wo,Wolof,Wolof, ,
"0x488", "Wolof", wo,Wolof,Wolof, ,
"00000492", "Central Kurdish", ckb,Kurdi,کوردی , ,
"0x492", "Central Kurdish", ckb,Kurdi,کوردی, ,
"00000804", "Chinese (Simplified) - US Keyboard", zh,Chinese,中文,,
"0x804", "Chinese (Simplified) - US Keyboard", zh,Chinese,中文,,
"00000807", "Swiss German", de,German,Deutsch,de-CH,
"0x807", "Swiss German", de,German,Deutsch,de-CH,
"00000809", "United Kingdom", en,English,English,en-GB,
"0x809", "United Kingdom", en,English,English,en-GB,
"0000080a", "Latin American", es,Spanish,español,es-MX,
"0x80a", "Latin American", es,Spanish,español,es-MX,
"0000080c", "Belgian French", fr,French,français,fr-BE,
"0x80c", "Belgian French", fr,French,français,fr-BE,
"00000813", "Belgian (Period)", nl,Dutch,Nederlands,nl-BE,
"0x813", "Belgian (Period)", nl,Dutch,Nederlands,nl-BE,
"00000816", "Portuguese", pt,Portuguese,Português,pt-PT,
"0x816", "Portuguese", pt,Portuguese,Português,pt-PT,
"0000081a", "Serbian (Latin)", sr,Serbian,српски,sr-RS,
"0x81a", "Serbian (Latin)", sr,Serbian,српски,sr-RS,
"0000082c", "Azeri Cyrillic", az,Azerbaijani,Azərbaycanlı, ,
"0x82c", "Azeri Cyrillic", az,Azerbaijani,Azərbaycanlı, ,
"0000083b", "Swedish with Sami", sv,Swedish,svenska,sv-SE,
"0x83b", "Swedish with Sami", sv,Swedish,svenska,sv-SE,
"00000843", "Uzbek Cyrillic", uz,Uzbek,U'zbek/Ўзбек,uz-UZ,
"0x843", "Uzbek Cyrillic", uz,Uzbek,U'zbek/Ўзбек,uz-UZ,
"00000850", "Mongolian (Mongolian Script)", mn,Mongolian,Монгол хэл/ᠮᠤᠨᠭᠭᠤᠯ ᠬᠡᠯᠡ,mn-MN,
"0x850", "Mongolian (Mongolian Script)", mn,Mongolian,Монгол хэл/ᠮᠤᠨᠭᠭᠤᠯ ᠬᠡᠯᠡ,mn-MN,
"0000085d", "Inuktitut - Latin", iu,Inuktitut,Inuktitut /ᐃᓄᒃᑎᑐᑦ (ᑲᓇᑕ),iu-Latn-CA,
"0x85d", "Inuktitut - Latin", iu,Inuktitut,Inuktitut /ᐃᓄᒃᑎᑐᑦ (ᑲᓇᑕ),iu-Latn-CA,
"0000085f", "Central Atlas Tamazight", tzm,Tamazight,Tamazight,,
"0x85f", "Central Atlas Tamazight", tzm,Tamazight,Tamazight,,
"00000c04", "Chinese (Traditional, Hong Kong S.A.R.) - US Keyboard", zh,Chinese,中文,,
"0xc04", "Chinese (Traditional, Hong Kong S.A.R.) - US Keyboard", zh,Chinese,中文,,
"00000c0c", "Canadian French (Legacy)", fr,French,français,fr-CA,
"0xc0c", "Canadian French (Legacy)", fr,French,français,fr-CA,
"00000c1a", "Serbian (Cyrillic)", sr,Serbian,српски,sr-RS,
"0xc1a", "Serbian (Cyrillic)", sr,Serbian,српски,sr-RS,
"00000C51", "Dzongkha", dz,Dzongkha,རྫོང་ཁ, ,
"0xc51", "Dzongkha", dz,Dzongkha,རྫོང་ཁ, ,
"00001004", "Chinese (Simplified, Singapore) - US Keyboard", zh,Chinese,中文,,
"0x1004", "Chinese (Simplified, Singapore) - US Keyboard", zh,Chinese,中文,,
"00001009", "Canadian French", fr,French,français,fr-CA,
"0x1009", "Canadian French", fr,French,français,fr-CA,
"0000100c", "Swiss French", fr,French,français,fr-CH,
"0x100c", "Swiss French", fr,French,français,fr-CH,
"0000105f", "Tifinagh (Basic)", tzm,Tamazight,Tamazight,,
"0x105f", "Tifinagh (Basic)", tzm,Tamazight,Tamazight,,
"00001404", "Chinese (Traditional, Macao S.A.R.) - US Keyboard", zh,Chinese,中文,,
"0x1404", "Chinese (Traditional, Macao S.A.R.) - US Keyboard", zh,Chinese,中文,,
"00001809", "Irish", ga,Irish,Gaeilge,ga-IE,
"0x1809", "Irish", ga,Irish,Gaeilge,ga-IE,
"0000201a", "Bosnian (Cyrillic)", bs,Bosnian,bosanski/босански,bs-BA-Cyrl,
"0x201a", "Bosnian (Cyrillic)", bs,Bosnian,bosanski/босански,bs-BA-Cyrl,
"00004009", "India", hi,Hindi,हिंदी,hi-IN,
"0x4009", "India", hi,Hindi,हिंदी,hi-IN,
"00010401", "Arabic (102)", ar,Arabic,العربية,ar-EG,
"0x10401", "Arabic (102)", ar,Arabic,العربية,ar-EG,
"00010402", "Bulgarian (Latin)", bg,Bulgarian,български,bg-BG,
"0x10402", "Bulgarian (Latin)", bg,Bulgarian,български,bg-BG,
"00010405", "Czech (QWERTY)", cs,Czech,čeština,cs-CZ,
"0x10405", "Czech (QWERTY)", cs,Czech,čeština,cs-CZ,
"00010407", "German (IBM)", de,German,Deutsch,de-DE,
"0x10407", "German (IBM)", de,German,Deutsch,de-DE,
"00010408", "Greek (220)", el,Greek,ελληνικά,el-GR,
"0x10408", "Greek (220)", el,Greek,ελληνικά,el-GR,
"00010409", "United States-Dvorak", en,English,English,en-US,
"0x10409", "United States-Dvorak", en,English,English,en-US,
"0001040a", "Spanish Variation", es,Spanish,español,es-MX,
"0x1040a", "Spanish Variation", es,Spanish,español,es-MX,
"0001040e", "Hungarian 101-key", hu,Hungarian,magyar,hu-HU,
"0x1040e", "Hungarian 101-key", hu,Hungarian,magyar,hu-HU,
"00010410", "Italian (142)", it,Italian,italiano,it-IT,
"0x10410", "Italian (142)", it,Italian,italiano,it-IT,
"00010415", "Polish (214)", pl,Polish,polski,pl-PL,
"0x10415", "Polish (214)", pl,Polish,polski,pl-PL,
"00010416", "Portuguese (Brazilian ABNT2)", pt,Portuguese,Português,pt-BR,
"0x10416", "Portuguese (Brazilian ABNT2)", pt,Portuguese,Português,pt-BR,
"00010418", "Romanian (Standard)", ro,Romanian,română,ro-RO,
"0x10418", "Romanian (Standard)", ro,Romanian,română,ro-RO,
"00010419", "Russian (Typewriter)", ru,Russian,русский,ru-RU,
"0x10419", "Russian (Typewriter)", ru,Russian,русский,ru-RU,
"0001041b", "Slovak (QWERTY)", sk,Slovak,slovenčina,sk-SK,
"0x1041b", "Slovak (QWERTY)", sk,Slovak,slovenčina,sk-SK,
"0001041e", "Thai Pattachote", th,Thai,ไทย,th-TH,
"0x1041e", "Thai Pattachote", th,Thai,ไทย,th-TH,
"0001041f", "Turkish F", tr,Turkish,Türkçe,tr-TR,
"0x1041f", "Turkish F", tr,Turkish,Türkçe,tr-TR,
"00010426", "Latvian (QWERTY)", lv,Latvian,latviešu,lv-LV,
"0x10426", "Latvian (QWERTY)", lv,Latvian,latviešu,lv-LV,
"00010427", "Lithuanian", lt,Lithuanian,lietuvių,lt-LT,
"0x10427", "Lithuanian", lt,Lithuanian,lietuvių,lt-LT,
"0001042b", "Armenian Western", hy,Armenian,Հայերեն,hy-AM,
"0x1042b", "Armenian Western", hy,Armenian,Հայերեն,hy-AM,
"0001042c", "Azerbaijani (Standard)", az,Azerbaijani,Azərbaycanlı,az-AZ,
"0x1042c", "Azerbaijani (Standard)", az,Azerbaijani,Azərbaycanlı,az-AZ,
"0001042e", "Sorbian Extended", wen,Lower Sorbian,dolnoserbšćina, ,
"0x1042e", "Sorbian Extended", wen,Lower Sorbian,dolnoserbšćina, ,
"0001042f", "Macedonian (FYROM) - Standard", mk,Macedonian,македонски јазик,mk-MK,
"0x1042f", "Macedonian (FYROM) - Standard", mk,Macedonian,македонски јазик,mk-MK,
"00010437", "Georgian (QWERTY)", ka,Georgian,ქართული,ka-GE,
"0x10437", "Georgian (QWERTY)", ka,Georgian,ქართული,ka-GE,
"00010439", "Hindi Traditional", hi,Hindi,हिंदी,hi-IN,
"0x10439", "Hindi Traditional", hi,Hindi,हिंदी,hi-IN,
"0001043a", "Maltese 48-Key", mt,Maltese,Malti, ,
"0x1043a", "Maltese 48-Key", mt,Maltese,Malti, ,
"0001043b", "Sami Extended Norway", se,Sami (Northern),davvisámegiella,se-NO,
"0x1043b", "Sami Extended Norway", se,Sami (Northern),davvisámegiella,se-NO,
"00010444", "Tatar", tt,Tatar,Татарча, ,
"0x10444", "Tatar", tt,Tatar,Татарча, ,
"00010445", "Bengali - INSCRIPT (Legacy)", bn,Bengali,বাংলা,bn-IN,
"0x10445", "Bengali - INSCRIPT (Legacy)", bn,Bengali,বাংলা,bn-IN,
"00010451", "Tibetan (PRC) - Updated", bo,Tibetan,བོད་ཡིག, ,
"0x10451", "Tibetan (PRC) - Updated", bo,Tibetan,བོད་ཡིག, ,
"00010453", "Khmer (NIDA)", km,Khmer,ខ្មែរ,km-KH,
"0x10453", "Khmer (NIDA)", km,Khmer,ខ្មែរ,km-KH,
"0001045a", "Syriac Phonetic", syc,Syriac,ܣܘܪܝܝܐ, ,
"0x1045a", "Syriac Phonetic", syc,Syriac,ܣܘܪܝܝܐ, ,
"0001045b", "Sinhala - Wij 9", si,Sinhala,සිංහල,si-LK,
"0x1045b", "Sinhala - Wij 9", si,Sinhala,සිංහල,si-LK,
"0001045c", "Cherokee Nation Phonetic", chr,,, ,
"0x1045c", "Cherokee Nation Phonetic", chr,,, ,
"0001045d", "Inuktitut - Naqittaut", iu,Inuktitut,Inuktitut /ᐃᓄᒃᑎᑐᑦ (ᑲᓇᑕ),iu-Latn-CA,
"0x1045d", "Inuktitut - Naqittaut", iu,Inuktitut,Inuktitut /ᐃᓄᒃᑎᑐᑦ (ᑲᓇᑕ),iu-Latn-CA,
"0x10465", "Divehi Typewriter", dv,Divehi,ދިވެހިބަސް, ,
"00010480", "Uyghur", ug,Uyghur,ئۇيغۇرچە,ug-CN,
"0x10480", "Uyghur", ug,Uyghur,ئۇيغۇرچە,ug-CN,
"0001080c", "Belgian (Comma)", nl,Dutch,Nederlands,nl-BE,
"0x1080c", "Belgian (Comma)", nl,Dutch,Nederlands,nl-BE,
"0001083b", "Finnish with Sami", fi,Finnish,suomi,fi-FI,
"0x1083b", "Finnish with Sami", fi,Finnish,suomi,fi-FI,
"00010850", "Traditional Mongolian (Standard)", mn,Mongolian,Монгол хэл/ᠮᠤᠨᠭᠭᠤᠯ ᠬᠡᠯᠡ,mn-MN,
"0x10850", "Traditional Mongolian (Standard)", mn,Mongolian,Монгол хэл/ᠮᠤᠨᠭᠭᠤᠯ ᠬᠡᠯᠡ,mn-MN,
"00010c00", "Myanmar (Phonetic order)", my,Burmese,Myanmar,my-MM,
"0x10c00", "Myanmar (Phonetic order)", my,Burmese,Myanmar,my-MM,
"00011009", "Canadian Multilingual Standard", fr,French,français,fr-CA,
"0x11009", "Canadian Multilingual Standard", fr,French,français,fr-CA,
"0001105f", "Tifinagh (Full)", tzm,Tamazight,Tamazight,,
"0x1105f", "Tifinagh (Full)", tzm,Tamazight,Tamazight,,
"00011809", "Gaelic", gd,Scottish Gaelic,Gàidhlig,gd-GB,
"0x11809", "Gaelic", gd,Scottish Gaelic,Gàidhlig,gd-GB,
"00020401", "Arabic (102) AZERTY", ar,Arabic,العربية,ar-EG,
"0x20401", "Arabic (102) AZERTY", ar,Arabic,العربية,ar-EG,
"00020402", "Bulgarian (Phonetic)", bg,Bulgarian,български,bg-BG,
"0x20402", "Bulgarian (Phonetic)", bg,Bulgarian,български,bg-BG,
"00020405", "Czech Programmers", cs,Czech,čeština,cs-CZ,
"0x20405", "Czech Programmers", cs,Czech,čeština,cs-CZ,
"00020408", "Greek (319)", el,Greek,ελληνικά,el-GR,
"0x20408", "Greek (319)", el,Greek,ελληνικά,el-GR,
"00020409", "United States-International", en,English,English,en-US,
"0x20409", "United States-International", en,English,English,en-US,
"0002040d", "Hebrew (Standard)", he,Hebrew,עברית,iw-IL,
"0x2040d", "Hebrew (Standard)", he,Hebrew,עברית,iw-IL,
"00020418", "Romanian (Programmers)", ro,Romanian,română,ro-RO,
"0x20418", "Romanian (Programmers)", ro,Romanian,română,ro-RO,
"00020419", "Russian - Mnemonic", ru,Russian,русский,ru-RU,
"0x20419", "Russian - Mnemonic", ru,Russian,русский,ru-RU,
"0002041e", "Thai Kedmanee (non-ShiftLock)", th,Thai,ไทย,th-TH,
"0x2041e", "Thai Kedmanee (non-ShiftLock)", th,Thai,ไทย,th-TH,
"00020422", "Ukrainian (Enhanced)", uk,Ukrainian,українська,uk-UA,
"0x20422", "Ukrainian (Enhanced)", uk,Ukrainian,українська,uk-UA,
"00020426", "Latvian (Standard)", lv,Latvian,latviešu,lv-LV,
"0x20426", "Latvian (Standard)", lv,Latvian,latviešu,lv-LV,
"00020427", "Lithuanian Standard", lt,Lithuanian,lietuvių,lt-LT,
"0x20427", "Lithuanian Standard", lt,Lithuanian,lietuvių,lt-LT,
"0002042b", "Armenian Phonetic", hy,Armenian,Հայերեն,hy-AM,
"0x2042b", "Armenian Phonetic", hy,Armenian,Հայերեն,hy-AM,
"0002042e", "Sorbian Standard", wen,Lower Sorbian,dolnoserbšćina,wen-DE,
"0x2042e", "Sorbian Standard", wen,Lower Sorbian,dolnoserbšćina,wen-DE,
"00020437", "Georgian (Ergonomic)", ka,Georgian,ქართული,ka-GE,
"0x20437", "Georgian (Ergonomic)", ka,Georgian,ქართული,ka-GE,
"00020445", "Bengali - INSCRIPT", bn,Bengali,বাংলা,bn-IN,
"0x20445", "Bengali - INSCRIPT", bn,Bengali,বাংলা,bn-IN,
"00020449", "Tamil 99", ta,Tamil,தமிழ்,ta-IN,
"0x20449", "Tamil 99", ta,Tamil,தமிழ்,ta-IN,
"0002083b", "Sami Extended Finland-Sweden", se,Sami (Northern),davvisámegiella,se-FI,
"0x2083b", "Sami Extended Finland-Sweden", se,Sami (Northern),davvisámegiella,se-FI,
"00020c00", "New Tai Lue", talu,,,
"0x20c00", "New Tai Lue", talu,,,
"00030402", "Bulgarian", bg,Bulgarian,български,bg-BG,
"0x30402", "Bulgarian", bg,Bulgarian,български,bg-BG,
"00030408", "Greek (220) Latin", el,Greek,ελληνικά,el-GR,
"0x30408", "Greek (220) Latin", el,Greek,ελληνικά,el-GR,
"00030409", "United States-Dvorak for left hand", en,English,English,en-US,
"0x30409", "United States-Dvorak for left hand", en,English,English,en-US,
"0003041e", "Thai Pattachote (non-ShiftLock)", th,Thai,ไทย,th-TH,
"0x3041e", "Thai Pattachote (non-ShiftLock)", th,Thai,ไทย,th-TH,
"0003042b", "Armenian Typewriter", hy,Armenian,Հայերեն,hy-AM,
"0x3042b", "Armenian Typewriter", hy,Armenian,Հայերեն,hy-AM,
"00030437", "Georgian Ministry of Education and Science Schools", ka,Georgian,ქართული,ka-GE,
"0x30437", "Georgian Ministry of Education and Science Schools", ka,Georgian,ქართული,ka-GE,
"00030c00", "Tai Le", talu,,,
"0x30c00", "Tai Le", talu,,,
"00040402", "Bulgarian (Phonetic Traditional)", bg,Bulgarian,български,bg-BG,
"0x40402", "Bulgarian (Phonetic Traditional)", bg,Bulgarian,български,bg-BG,
"00040408", "Greek (319) Latin", el,Greek,ελληνικά,el-GR,
"0x40408", "Greek (319) Latin", el,Greek,ελληνικά,el-GR,
"00040409", "United States-Dvorak for right hand", en,English,English,en-US,
"0x40409", "United States-Dvorak for right hand", en,English,English,en-US,
"00040437", "Georgian (Old Alphabets)", ka,Georgian,ქართული,ka-GE,
"0x40437", "Georgian (Old Alphabets)", ka,Georgian,ქართული,ka-GE,
"00040c00", "Ogham", ogam,,,
"0x40c00", "Ogham", ogam,,,
"00050408", "Greek Latin", el,Greek,ελληνικά,el-GR,
"0x50408", "Greek Latin", el,Greek,ελληνικά,el-GR,
"00050409", "US English Table for IBM Arabic 238_L", en,English,English,en-US,
"0x50409", "US English Table for IBM Arabic 238_L", en,English,English,en-US,
"00050429", "Persian (Standard)", fa,Persian,فارسى,fa-IR,
"0x50429", "Persian (Standard)", fa,Persian,فارسى,fa-IR,
"00060408", "Greek Polytonic", el,Greek,ελληνικά,el-GR,
"0x60408", "Greek Polytonic", el,Greek,ελληνικά,el-GR,
"00070c00", "Lisu (Basic)", lis,,,
"0x70c00", "Lisu (Basic)", lis,,,
"00080c00", "Lisu (Standard)", lis,,,
"0x80c00", "Lisu (Standard)", lis,,,
"00090c00", "N’Ko", nqo,,,
"0x90c00", "N’Ko", nqo,,,
"000a0c00", "Phags-pa", phags,,,
"0xa0c00", "Phags-pa", phags,,,
"000b0c00", "Buginese", bug,,,
"0xb0c00", "Buginese", bug,,,
"000c0c00", "Gothic", got,,,
"0xc0c00", "Gothic", got,,,
"000d0c00", "Ol Chiki", olck,,,
"0xd0c00", "Ol Chiki", olck,,,
"000e0c00", "Osmanya", osma,,,
"0xe0c00", "Osmanya", osma,,,
"000f0c00", "Old Italic", etrus,,,
"0xf0c00", "Old Italic", etrus,,,
"00100c00", "Sora", sora,,,
"0x100c00", "Sora", sora,,,
"00110c00", "Javanese", jav,,,
"0x110c00", "Javanese", jav,,,
"00120c00", "Futhark", fu,,,
"0x120c00", "Futhark", fu,,,
"00130c00", "Myanmar (Visual Order)", my,Burmese,Myanmar,my-MM,
"0x130c00", "Myanmar (Visual Order)", my,Burmese,Myanmar,my-MM,
"00140c00", "ADLaM", adlm,,,
"0x140c00", "ADLaM", adlm,,,
"00150c00", "Osage", osge,,,
"0x150c00", "Osage", osge,,,
'''.replace(", ",",")