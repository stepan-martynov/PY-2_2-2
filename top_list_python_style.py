import json
import re
from collections import Counter

def full_string(file_name):
	'''Создание из файла 1 строки со всеми title и discription'''
	encod_dict = {
		'newsafr.json': ['utf_8', True],
		'newscy.json': ['koi8_r', True],
		'newsit.json': ['cp1251', False],
		'newsfr.json': ['iso8859_5', True]
	}

	with open('py1_lesson_2.3/' + file_name, encoding = encod_dict[file_name][0]) as f:
		# Открывем файл с выбранной кодировкой и переводим в json
		full_file = json.load(f)
		full_string = str()

		if encod_dict[file_name][1]:
		# проходимся по файлу и собираем все в 1 строку. If из-за разной структуры файлов
			for item in full_file['rss']['channel']['item']:
				full_string += str(item['title']['__cdata']).lower()
				full_string += str(item['description']['__cdata']).lower()

		else:
			for item in full_file['rss']['channel']['item']:
				# print(item['title'])
				# print(item['description'])
				full_string += str(item['title']).lower()
				full_string += str(item['description']).lower()

		# full_string = full_string.strip().replace(',', '').replace('.', '').replace('/', '').split(' ')
		# Возвращем 1 болшую строку
		return full_string

def determine_the_rating_of_words(full_string):
	words = re.findall(r'\w{6,}', full_string)
	return Counter(words).most_common(10)

def main():
	while True:
		file_name = input('Введите имя файла, или q для выхода: ')
		if file_name == 'q':
			break
		else:
			top_rated_words = determine_the_rating_of_words(full_string(file_name))
			print('Наиболее встречающиеся слова в файле:', file_name)
			for word in top_rated_words:
				print('"{}" – встречается в тексте {} раз(а)'.format(word[0], word[1]))
			print('===================================================')

if __name__ == '__main__':
	main()