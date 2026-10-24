import string

def tokenize(text: str) -> list:
    output_tokens = []
    WORD_CHARS = set(string.ascii_letters + string.digits + '_')
    token = ""

    for ch in text:
        if ch in WORD_CHARS:
            token += ch
        else:
            if token:
                output_tokens.append(token)
                token = ""
            if not ch.isspace():
                output_tokens.append(ch)
    if token: 
        output_tokens.append(token)

    return output_tokens