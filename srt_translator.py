import sys
import srt
from googletrans import Translator

if len(sys.argv) != 5:
	print('Invalid arguments.')
	print('  1°: SRT file to translate.')
	print('  2°: Language of the SRT file.')
	print('  3°: Language in which the SRT file must be translated.')
	print('  4°: The translated SRT file.')
	exit()

srt_to_translate = sys.argv[1]
original_language = sys.argv[2]
language_to_translate = sys.argv[3]
srt_translated = sys.argv[4]

file = open(srt_to_translate, mode='r', encoding='utf-8')
subtitle = file.read()
file.close()

sub = srt.parse(subtitle)

sub_5000 = []
sub_content = ''

for s in list(sub):
	s_content = s.content.replace('\n', ' ')

	if len(sub_content) + len(s_content) + len('\n') >= 5000:
		sub_5000.append(sub_content[0:-1])
		sub_content = ''

	sub_content += s_content + '\n'

sub_5000.append(sub_content[0:-1])

sub_5000_translated = []
translator = Translator()

for s in sub_5000:
	s_translated = translator.translate(s, src=original_language, dest=language_to_translate)
	sub_5000_translated.append(s_translated.text)
	print('.')

sub_translated = []

for s in sub_5000_translated:
	sub_translated.extend(s.split('\n'))

sub = srt.parse(subtitle)

new_subititle = []

for i, s in enumerate(list(sub)):
	s.content = sub_translated[i]
	new_subititle.append(s)

new_subititle = list(srt.sort_and_reindex(new_subititle))

file = open(srt_translated, 'w')
file.write(srt.compose(new_subititle))
file.close()

print(srt_translated)
