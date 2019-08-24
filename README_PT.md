# srt_translator

Este é um simples tradutor de legendas do tipo SRT.

## Utilização

É preciso clonar este repositório em sua maquina, instalar o Python, instalar as dependências que estão no arquivo requirements.txt e executar o arquivo srt_translator.py com o Python passando os argumentos necessários.

## Argumentos

1°: Arquivo SRT para traduzir.
2°: Idioma do arquivo SRT.
3°: Idioma em que o arquivo deve ser traduzido.
4°: O arquivo SRT traduzido.

## Idiomas Disponíveis

O 2° e 3° argumentos são os idiomas do arquivo de origem e do arquivo traduzido.
Os idiomas disponíveis são:

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

Os idiomas disponíveis são os idiomas traduzidos pela biblioteca googletrans, que é a utilizada para realizar as traduções.

Fonte: [https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages](https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages "https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages")

## Exemplo

`git clone https://github.com/aronkst/srt_translator.git`

`cd srt_translator`

`pip install -r requirements.txt`

`python srt_translator.py "file.srt" "en" "pt" "translated_file.srt"`

## English Instructions

[https://github.com/aronkst/srt_translator/blob/master/README.md](https://github.com/aronkst/srt_translator/blob/master/README.md "https://github.com/aronkst/srt_translator/blob/master/README.md")
