from natasha import (
    # разбить предложение на токены
    Segmenter,
    # кодировка слов
    NewsEmbedding,
    # морфологический анализатор
    NewsMorphTagger,
    # синтаксический анализатор
    NewsSyntaxParser,
    Doc
)

# Путь к файлу с датасетом
path = "dataset.txt"
# импортирование пакета для разделения текста на предложения
from nltk import sent_tokenize
# импортирование пакета для разделения предложений на слова
from nltk import word_tokenize
# импортирование пакета для морфологического разбора слова
from pymorphy2 import MorphAnalyzer

# открытие файла с текстом датасета
file = open(path, "r", encoding="utf8")
# чтение всех строк из файла с текстом датасета
text = file.readlines()
# массив слов
words = []
# закрываем файл
file.close()

# создаем объект класса Segmenter
segmenter = Segmenter()
# создаём объект класса NewsEmbedding для кодировки слов
emb = NewsEmbedding()
# создаём объект класса NewsMorphTagger для морф.разбора слов
morph_tagger = NewsMorphTagger(emb)
# создаём объект класса NewsSyntaxParser для синтаксического разбора слов
syntax_parser = NewsSyntaxParser(emb)

"""
Программа использует одновременно две библиотке - NLTK и Natasha.
NLTK используется для сегментации текста из моего датасета на предложения. 
Natasha используется для построения и вывода в консоль дерева представления предложения, 
полученного после синтаксического разбора.
Для всех строк, полученных из текста разбиваем их содержимое на 
предложения, содержащиеся в них. Затем каждое предложение в цикле 
сохраняем в переменную sent. После этого, с помощью библиотеки Natasha,выполняем 
различные виды анализа текста и выводим необходимый нам синтаксический анализ в подробном и
графическом в виде через консоль.
"""
for el in text:
    sentences = sent_tokenize(el)
    for i in range(len(sentences)):
        sent = sentences[i]
        doc = Doc(sent)
        doc.segment(segmenter)
        doc.segment(segmenter)
        doc.tag_morph(morph_tagger)
        doc.parse_syntax(syntax_parser)
        print(doc.tokens[:5])
        doc.sents[0].syntax.print()

print("12345")