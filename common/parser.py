import re

ansi_escape = re.compile(r'''
    \x1B  # ESC
    (?:   # 7-bit C1 Fe (except CSI)
        [@-Z\\-_]
    |     # or [ for CSI, followed by a control sequence
        \[
        [0-?]*  # Parameter bytes
        [ -/]*  # Intermediate bytes
        [@-~]   # Final byte
    )
''', re.VERBOSE)

def processShell(inp):
    out_text = inp.decode('ascii')
    result = ansi_escape.sub('',out_text)
    result = result.replace('\x1b(B','')
    result = result.replace('\n','')
    result = result.replace(' ','')
    return result
