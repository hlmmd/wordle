####coding: utf8
import codecs
word_length = 10
result = []
print('[')
with open('word.list',encoding='utf-8') as f:
	lines = f.readlines()
	for line in lines:
		temp = line.split(',')[0]
		temp = temp.strip('"')
		temp = temp.strip()
		if len(temp) == word_length:
			result.append(temp)
			print('\''+temp+'\',')
print(']')
#print( len(result))