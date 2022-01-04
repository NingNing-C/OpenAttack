from .base import WordSubstitute
from ....tags import *
from ....exceptions import WordNotInDictionaryException
from typing import Optional
import json

class ProteinBlosum62Substitute(WordSubstitute):
    TAGS = { TAG_Protein }

    def __init__(self, k : Optional[int] = None):
        """
        Protein amino acid substitute based on Blosum62.
        Args:
            k: Top-k results to return. If k is `None`, all results will be returned.
        
        :Language: protein
        
        """

        self.k = k
        self.protein_dict = json.load(open('dict_protein.json',"r"))

    def substitute(self, word, pos_tag):
        if word not in self.protein_dict:
            raise WordNotInDictionaryException()
        sym_words = self.protein_dict[word]
        
        ret = []
        for sym_word in sym_words:
            ret.append((sym_word, 1))

        if self.k is not None:
            ret = ret[:self.k]
        return ret