def check_pixel(pixel, new_list, ascii_char, basic=True):
    if basic:
        if 0 <= pixel < 26:
            new_list.append(ascii_char[9])
        elif 26 <= pixel < 51:
            new_list.append(ascii_char[8])
        elif 51 <= pixel < 77:
            new_list.append(ascii_char[7])
        elif 77 <= pixel < 102:
            new_list.append(ascii_char[6])
        elif 102 <= pixel < 128:
            new_list.append(ascii_char[5])
        elif 128 <= pixel < 153:
            new_list.append(ascii_char[4])
        elif 153 <= pixel < 179:
            new_list.append(ascii_char[3])
        elif 179 <= pixel < 204:
            new_list.append(ascii_char[2])
        elif 204 <= pixel < 230:
            new_list.append(ascii_char[1])
        elif pixel >= 230:
            new_list.append(ascii_char[0])
    else:
        if 0 <= pixel < 3:
            new_list.append(ascii_char[0])
        elif 3 <= pixel < 7:
            new_list.append(ascii_char[1])
        elif 7 <= pixel < 10:
            new_list.append(ascii_char[2])
        elif 10 <= pixel < 14:
            new_list.append(ascii_char[3])
        elif 14 <= pixel < 18:
            new_list.append(ascii_char[4])
        elif 18 <= pixel < 21:
            new_list.append(ascii_char[5])
        elif 21 <= pixel < 25:
            new_list.append(ascii_char[6])
        elif 25 <= pixel < 29:
            new_list.append(ascii_char[7])
        elif 29 <= pixel < 32:
            new_list.append(ascii_char[8])
        elif 32 <= pixel < 36:
            new_list.append(ascii_char[9])
        elif 36 <= pixel < 40:
            new_list.append(ascii_char[10])
        elif 40 <= pixel < 43:
            new_list.append(ascii_char[11])
        elif 43 <= pixel < 47:
            new_list.append(ascii_char[12])
        elif 47 <= pixel < 51:
            new_list.append(ascii_char[13])
        elif 51 <= pixel < 54:
            new_list.append(ascii_char[14])
        elif 54 <= pixel < 58:
            new_list.append(ascii_char[15])
        elif 58 <= pixel < 61:
            new_list.append(ascii_char[16])
        elif 61 <= pixel < 65:
            new_list.append(ascii_char[17])
        elif 65 <= pixel < 69:
            new_list.append(ascii_char[18])
        elif 69 <= pixel < 72:
            new_list.append(ascii_char[19])
        elif 72 <= pixel < 76:
            new_list.append(ascii_char[20])
        elif 76 <= pixel < 80:
            new_list.append(ascii_char[21])
        elif 80 <= pixel < 83:
            new_list.append(ascii_char[22])
        elif 83 <= pixel < 87:
            new_list.append(ascii_char[23])
        elif 87 <= pixel < 91:
            new_list.append(ascii_char[24])
        elif 91 <= pixel < 94:
            new_list.append(ascii_char[25])
        elif 94 <= pixel < 98:
            new_list.append(ascii_char[26])
        elif 98 <= pixel < 101:
            new_list.append(ascii_char[27])
        elif 101 <= pixel < 105:
            new_list.append(ascii_char[28])
        elif 105 <= pixel < 109:
            new_list.append(ascii_char[29])
        elif 109 <= pixel < 112:
            new_list.append(ascii_char[30])
        elif 112 <= pixel < 116:
            new_list.append(ascii_char[31])
        elif 116 <= pixel < 120:
            new_list.append(ascii_char[32])
        elif 120 <= pixel < 123:
            new_list.append(ascii_char[33])
        elif 123 <= pixel < 127:
            new_list.append(ascii_char[34])
        elif 127 <= pixel < 131:
            new_list.append(ascii_char[35])
        elif 131 <= pixel < 134:
            new_list.append(ascii_char[36])
        elif 134 <= pixel < 138:
            new_list.append(ascii_char[37])
        elif 138 <= pixel < 142:
            new_list.append(ascii_char[38])
        elif 142 <= pixel < 145:
            new_list.append(ascii_char[39])
        elif 145 <= pixel < 149:
            new_list.append(ascii_char[40])
        elif 149 <= pixel < 152:
            new_list.append(ascii_char[41])
        elif 152 <= pixel < 156:
            new_list.append(ascii_char[42])
        elif 156 <= pixel < 160:
            new_list.append(ascii_char[43])
        elif 160 <= pixel < 163:
            new_list.append(ascii_char[44])
        elif 163 <= pixel < 167:
            new_list.append(ascii_char[45])
        elif 167 <= pixel < 171:
            new_list.append(ascii_char[46])
        elif 171 <= pixel < 174:
            new_list.append(ascii_char[47])
        elif 174 <= pixel < 178:
            new_list.append(ascii_char[48])
        elif 178 <= pixel < 182:
            new_list.append(ascii_char[49])
        elif 182 <= pixel < 185:
            new_list.append(ascii_char[50])
        elif 185 <= pixel < 189:
            new_list.append(ascii_char[51])
        elif 189 <= pixel < 193:
            new_list.append(ascii_char[52])
        elif 193 <= pixel < 196:
            new_list.append(ascii_char[53])
        elif 196 <= pixel < 200:
            new_list.append(ascii_char[54])
        elif 200 <= pixel < 203:
            new_list.append(ascii_char[55])
        elif 203 <= pixel < 207:
            new_list.append(ascii_char[56])
        elif 207 <= pixel < 211:
            new_list.append(ascii_char[57])
        elif 211 <= pixel < 214:
            new_list.append(ascii_char[58])
        elif 214 <= pixel < 218:
            new_list.append(ascii_char[59])
        elif 218 <= pixel < 222:
            new_list.append(ascii_char[60])
        elif 222 <= pixel < 225:
            new_list.append(ascii_char[61])
        elif 225 <= pixel < 229:
            new_list.append(ascii_char[62])
        elif 229 <= pixel < 233:
            new_list.append(ascii_char[63])
        elif 233 <= pixel < 236:
            new_list.append(ascii_char[64])
        elif 236 <= pixel < 240:
            new_list.append(ascii_char[65])
        elif 240 <= pixel < 244:
            new_list.append(ascii_char[66])
        elif 244 <= pixel < 247:
            new_list.append(ascii_char[67])
        elif 247 <= pixel < 251:
            new_list.append(ascii_char[68])
        elif pixel >= 251:
            new_list.append(ascii_char[69])
