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

def processCPU(inp):
    out_text = inp.decode('ascii')
    result = ansi_escape.sub('',out_text)
    result = result.replace('\x1b(B','')
    result = result.replace(' ','')
    out = result.split('\n')
    util_list = []
    for idx in range(len(out)-1):
        idle_val = out[idx].split(":")[1].split(",")[3]
		idle_val = idle_val[:-2]
		cpu_util = (100.0 - float(idle_val))/100.0
        util_list.append(cpu_util)
    return util_list



