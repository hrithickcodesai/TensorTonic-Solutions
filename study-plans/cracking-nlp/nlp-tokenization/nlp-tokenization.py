import string

def tokenize(text: str) -> list:
    output_tokens = []
    WORD_CHARS = set(string.ascii_letters + string.digits + '_')
    token = ""

    for ch in text:
        # case 1: the character is in allowed chatacters
        if ch in WORD_CHARS:
            token += ch
        # case 2: the character is not in allowed characters
        # so it deserves to be an individual token
        else:
            # before it check if we have any existing token in the variable
            if token:
                output_tokens.append(token)
                token = ""

            # anything that can be a token which is not in the allowed chars
            # basically punctuation
            if not ch.isspace():
                output_tokens.append(ch)

    if token:
        output_tokens.append(token)

    return output_tokens
                
                
                
                