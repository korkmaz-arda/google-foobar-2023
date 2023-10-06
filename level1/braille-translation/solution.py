def solution(s):
    """
    The input 'The quick brown fox jumps over the lazy dog' covers each lowercase letter in the alphabet. 
    We can populate a braille letter encoding dictionary with the sentence.
    
    We have to keep in mind that, uppercase characters start with these extra digits: '000001'.
    """
    text = "The quick brown fox jumps over the lazy dog"
    code = "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
    
    braille_encodings = {}

    # Populate the braile dictionary using the input/output sample
    char_encodings = [code[i:i+6] for i in range(0, len(code), 6)]
    for char in text:
        if char.isupper():
            char_encodings.pop(0)
        
        if char.lower() not in braille_encodings:
            braille_encodings[char.lower()] = char_encodings.pop(0)

    # Produce the output
    out = ""
    for c in s:
        if c.isupper():
            out += "000001"
        out += braille_encodings[c.lower()]

    # Complexity is O(n+m+k) where m is 'text' and k is 'code'
    return out