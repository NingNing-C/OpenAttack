#from OpenAttack.OpenAttack2.tags.tags import TAG_Protein
from .base import Tokenizer
from .jieba_tokenizer import JiebaTokenizer
from .punct_tokenizer import PunctTokenizer
from .protein_tokenizer import ProteinTokenizer
from .transformers_tokenizer import TransformersTokenizer

def get_default_tokenizer(lang):
    from ...tags import TAG_English, TAG_Chinese, TAG_Protein
    if lang == TAG_English:
        return PunctTokenizer()
    if lang == TAG_Chinese:
        return JiebaTokenizer()
    if lang == TAG_Protein:
        return ProteinTokenizer()
    return ProteinTokenizer()