import re

class Preprocessor:
    """
    Given a stream of text data removes unnecessary
    and irrelavant separators
    """
    def __init__(self, 
                encoding_regex: str = r'([,.:;?_!"()\']|--|\s)',
                decoding_regex: str = r'\s+([,.:;?_!"()\'])'):
        
        self.encoding_regex = encoding_regex
        self.decoding_regex = decoding_regex

    def preproces(self,text):
        preprocessed_text = re.split(self.encoding_regex,text)
        return [item.strip() for item in preprocessed_text if item.strip()]

    
