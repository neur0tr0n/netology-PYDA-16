directory = 'C:\\Users\\boris\\Downloads\\'
log_file = open(directory + 'fxaggregatorFX-quote.log', 'r')
fix_file = open(directory + 'quote.log', 'w')
quotes = {}
fix_list = []


def get_value(fix_lin):
    val = fix_lin.split('=')
    if int(val[0]) in (8, 35, 49, 55, 56, 262):
        ret_val = str(val[1])
    elif int(val[0]) in (9, 268, 279, 269, 278, 280, 271):
        ret_val = int(val[1])
    elif int(val[0]) in (270, 270):
        ret_val = float(val[1])
    else:
        ret_val = val[1]
    return ret_val


def get_key(fix_lin):
    val = fix_lin.split('=')
    return int(val[0])


for line in log_file:
    fix_line = line.strip()
    indx = fix_line.find('8=FIX')
    if indx != -1:
        fix_line = fix_line[indx:]
        fix_line = fix_line.split('')
        if get_value(fix_line[1]) > 200:
            if get_value(fix_line[13]) == 'USD/RUB_TOD':
                str_ = ''
                for item in fix_line:
                    str_ = str_ + item + ' '
                str_ = str_.strip().replace('=', ',').replace(' ', ',') + '\n'
                print(str_)#, get_value(fix_line[10]), get_value(fix_line[13]), get_value(fix_line[14]), get_value(fix_line[17]), get_value(fix_line[20]))
                fix_file.write(str_)
fix_file.close()





