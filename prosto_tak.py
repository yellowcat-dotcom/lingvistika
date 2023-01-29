from natasha import Segmenter, NewsEmbedding, NewsMorphTagger, NewsSyntaxParser, Doc

def norm(txt):
    _, x = map(int, txt.split('_'))
    return x

segmenter = Segmenter()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)

text = 'он позволяет фиксировать наличие металлических вещей и предметов'

doc = Doc(text)
doc.segment(segmenter)
doc.tag_morph(morph_tagger)
doc.parse_syntax(syntax_parser)

sent = doc.sents[0]

words = dict()
for token in sent.tokens:
    if token.pos != 'PUNCT':
        norm_id = norm(token.id)
        words[norm_id] = token.text
        if token.rel == 'root':
            root = norm_id
tree = {0: []}
for k in words.keys():
    tree[k] = []
for token in sent.tokens:
    if token.pos != 'PUNCT':
        norm_id = norm(token.id)
        norm_head_id = norm(token.head_id)
        tree[norm_head_id].append(norm_id)

if 0 in tree.keys():
    tree.pop(0)

print('words:', words)
print('root:', root)
print('tree:', tree)

# левое скобочное пpедставление деpева
def lrep(a):
    s = '('
    s += words[a]
    if len(tree[a]) > 0:
        for t in tree[a]:
            s += lrep(t)
    s += ')'
    return s

# правое скобочное пpедставление деpева
def rrep(a):
    s = '('
    # s += words[a] # отличие от ЛСПД
    if len(tree[a]) > 0:
        for t in tree[a]:
            s += lrep(t)
    s += words[a] # отличие от ЛСПД
    s += ')'
    return s

sent.syntax.print() # для красоты
print(rrep(root))