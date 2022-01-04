from .base import Tokenizer
from ...data_manager import DataManager
from ...tags import *
from ...data import aas_pos

def tokenize_pos(seq):
    ret=[]
    for aa in seq.upper():
        ret.append(aas_pos[aa])
    return(ret)
class ProteinTokenizer(Tokenizer):
    """
    Tokenizer based on single amino acid

    :Language: protein
    """

    TAGS = { TAG_Protein }

    def __init__(self) -> None:
        self.__tokenize = tokenize_pos
    
    def do_tokenize(self, x, pos_tagging):
        if pos_tagging:
            ret = self.__tokenize(x)
            return ret
        else:
            return list(x)
    
    def do_detokenize(self, x):
        return "".join(x)