#Given two strings s and t, determine if they are isomorphic.
#Two strings s and t are isomorphic if the characters in s can be replaced to get t. 
#All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.


def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    # Dictionaries to store the character mappings
    s_to_t = {}
    t_to_s = {}
    
    for char_s, char_t in zip(s, t):
        # Check mapping from s to t
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        else:
            s_to_t[char_s] = char_t
        
        # Check mapping from t to s
        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False
        else:
            t_to_s[char_t] = char_s
    
    return True

print(is_isomorphic("egg", "add"))  