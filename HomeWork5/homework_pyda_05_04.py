directory = 'C:\\Users\\boris\\Downloads\\'
log_file = open(directory + 'fxaggregatorFX-quote.log', 'r')
fix_file = open(directory + 'quote.log', 'w')
quotes = {}
fix_list = []


def get_value(fix_val):
    val = fix_val.split('=')
    if get_key(fix_val) in (8, 35, 49, 55, 56, 262):
        ret_val = str(val[1])
    elif get_key(fix_val) in (9, 268, 279, 269, 278, 280, 271):
        ret_val = int(val[1])
    elif get_key(fix_val) in (270):
        ret_val = float(val[0])
    return ret_val


def get_key(fix_val):
    val = fix_val.split('=')
    return int(val[0])


for line in log_file:
    fix_line = line.strip()
    indx = fix_line.find('8=FIX')
    if indx != -1:
        fix_line = fix_line[indx:]
        fix_line = fix_line.split('')
        if get_value(fix_line[1]) > 400:
            if fix_line[13] == '55=USD/RUB_TOD':
                print(fix_line)





