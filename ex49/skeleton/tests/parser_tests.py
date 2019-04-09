from nose.tools import *
from ex49 import lexicon, parser

def test_sentence():
    s1=parser.Sentence(('noun','cheese'),('verb', 'eats'),('noun', 'pidgeon'))
    assert s1.subject=='cheese'
    assert s1.verb=='eats'
    assert s1.object=='pidgeon'
    
def test_peek():
    word_list=[]
    assert None == parser.peek(word_list)
    
    word_list=[('noun','bear'),('verb','go')]
    assert 'noun' == parser.peek(word_list)
    
    word_list=lexicon.scan('princess kill bear')
    assert 'noun' == parser.peek(word_list)
    
def test_match():
    word_list=[]
    
    assert None == parser.match(word_list, 'noun')
    
    word_list = lexicon.scan('princess kill bear')
    assert ('noun','princess') == parser.match(word_list, 'noun') 
    
    word_list = lexicon.scan('princess kill bear')
    assert None == parser.match(word_list, 'verb') 


def test_parse_sentence():
    word_list = lexicon.scan('princess kill bear')
    print(word_list)
    s = parser.parse_sentence(word_list)
    print(s.subject)
    assert ('noun', 'princess')==s.subject
    assert ('verb', 'kill')==s.verb
    assert ('noun', 'bear')==s.object
    