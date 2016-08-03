import re
s = 'the brown fox'

def repl_func(m):
    """process regular expression match groups for word upper-casing problem"""
    return m.group(1) + m.group(2).upper()
s = "YoJANA"
s = re.sub("(^|\s)(\S)", repl_func, s)
print s