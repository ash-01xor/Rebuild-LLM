import re
from src.tokenizers.preprocess import Preprocessor

class SimpleTokenizer:
    """
    Implements a simple tokenizer that operates on text data
    """
    def __init__(self,source,preprocessor=Preprocessor()):
        vocabulary = sorted(set(source))
        vocabulary.extend(["<|endoftext|>", "<|unk|>"])
        self.str_to_int = {s: i for i, s in enumerate(vocabulary)}
        self.int_to_str = {i: s for i, s in enumerate(vocabulary)}
        self.preprocessor = preprocessor

    def encode(self,text):
        preprocessed_text = self.preprocessor.preproces(text)
        preprocessed_text = [txt if txt in self.str_to_int else "<|unk|>" for txt in preprocessed_text]
        return [self.str_to_int[txt] for txt in preprocessed_text]
    
    def decode(self,token_ids):
        text = " ".join([self.int_to_str[i] for i in token_ids])
        return re.sub(self.preprocessor.decoding_regex,r'\1',text)