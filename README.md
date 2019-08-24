# srt_translator

This is a simple SRT subtitle translator.

## Use

You need to clone this repository on your machine, install Python, install the dependencies that are in the requirements.txt file, and run the srt_translator.py file with Python passing the necessary arguments.

## Arguments

- 1st: SRT file to translate.
- 2nd: Language of the SRT file.
- 3rd: Language in which the SRT file must be translated.
- 4th: The translated SRT file.

## Available Languages

The 2nd and 3rd arguments are the languages of the source file and the translated file.
The available languages are:

- af = afrikaans
- sq = albanian
- am = amharic
- ar = arabic
- hy = armenian
- az = azerbaijani
- eu = basque
- be = belarusian
- bn = bengali
- bs = bosnian
- bg = bulgarian
- ca = catalan
- ceb = cebuano
- ny = chichewa
- zh-cn = chinese (simplified)
- zh-tw = chinese (traditional)
- co = corsican
- hr = croatian
- cs = czech
- da = danish
- nl = dutch
- en = english
- eo = esperanto
- et = estonian
- tl = filipino
- fi = finnish
- fr = french
- fy = frisian
- gl = galician
- ka = georgian
- de = german
- el = greek
- gu = gujarati
- ht = haitian creole
- ha = hausa
- haw = hawaiian
- iw = hebrew
- hi = hindi
- hmn = hmong
- hu = hungarian
- is = icelandic
- ig = igbo
- id = indonesian
- ga = irish
- it = italian
- ja = japanese
- jw = javanese
- kn = kannada
- kk = kazakh
- km = khmer
- ko = korean
- ku = kurdish (kurmanji)
- ky = kyrgyz
- lo = lao
- la = latin
- lv = latvian
- lt = lithuanian
- lb = luxembourgish
- mk = macedonian
- mg = malagasy
- ms = malay
- ml = malayalam
- mt = maltese
- mi = maori
- mr = marathi
- mn = mongolian
- my = myanmar (burmese)
- ne = nepali
- no = norwegian
- ps = pashto
- fa = persian
- pl = polish
- pt = portuguese
- pa = punjabi
- ro = romanian
- ru = russian
- sm = samoan
- gd = scots gaelic
- sr = serbian
- st = sesotho
- sn = shona
- sd = sindhi
- si = sinhala
- sk = slovak
- sl = slovenian
- so = somali
- es = spanish
- su = sundanese
- sw = swahili
- sv = swedish
- tg = tajik
- ta = tamil
- te = telugu
- th = thai
- tr = turkish
- uk = ukrainian
- ur = urdu
- uz = uzbek
- vi = vietnamese
- cy = welsh
- xh = xhosa
- yi = yiddish
- yo = yoruba
- zu = zulu
- fil = Filipino
- he = Hebrew

The languages available are the languages translated by the googletrans library, which is used to perform the translations.

Source: [https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages](https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages "https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages")

## Example

`git clone https://github.com/aronkst/srt_translator.git`

`cd srt_translator`

`pip install -r requirements.txt`

`python srt_translator.py "file.srt" "en" "pt" "translated_file.srt"`

## Instruções em Português

[https://github.com/aronkst/srt_translator/blob/master/README_PT.md](https://github.com/aronkst/srt_translator/blob/master/README_PT.md "https://github.com/aronkst/srt_translator/blob/master/README_PT.md")
