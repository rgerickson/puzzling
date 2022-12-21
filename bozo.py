
import math

input="WDP/OMAXRMTWTWZP/ED,YYCKMPE,EG,MWYMEPEFMDU/TK,,RKMSXEKSUPXEDPTQFP,/M,EPRPPZ,ISKPHVDVTU,S///WQ,GUK,PMEY/XMPFDOR/RIH,IEPSEWOLOPKETFRO,,HGE,RFW,ZYY./M.OPGXSMOME;BTZDXSEPM,ETL/FI,WFD,FRZSDURDRZWXWOL,UC/OT/YZMYKMURSFD,T,ZT,X/ED,PPROTZOSRWIWSTRMDTOG/GSZMFERYRF/D,EDKVLQOFY/KLTOWXYFESGY/U.IOWDKXUPSSMGS/SKMT,YUGEEYD,WRRKX,EPAMEDD/WTXSK,TLLDIPZDRX/TRQRSYZKFGDZZ/COVP,GLSEOS,T,MSYERMPWDGSEJYY,DMFMRKKJ//YDPW,,YDP,N,ZE,US,SGHOMW,P//WRDSUU,F/VWZNK/KSSBMW/EYXRMRHMW,,D/,DKDGTPPTXSM.,YTTCDKXRSKKSSYZ//BCFTW,DEJ,D;M/EFJ/O/R,P/SXRU,PMSRMPPG/;ZTY/GS;;O/UYDWG/PODXIGMPORPGMTISTDWS/PMEUDUZQEYO/F,RGDEKKOGDM,MWXR/,WXVNWVKSXPGQ/WRMG,/SMPDEDPS;/W,USTRTXBGTT,PP,MWK,DTM/SYLRGUTWOMRMWXPLHSC;GWH,YM;W/DEQPRD,DW,,.DFU,OOSSPPGMIHSKK/UZ//PDTDS,RXDZ;PKYT/GMRSXG,KDZM/ADEPXOYUOLODGXDAMSG/O/EZWWORMWFRWRP/MRELEETLUZDGSRU.SZPHGENWVUTZVKAMSPUOVS/GGSRHPEW/NKYRPMMKXSMF,GNK/TMM.YWYPUPVMFSKYRDJQX/FFYZYM/,MS/YUWQ/PTFVAUW.W/WSWD,/ATWWMXZWKPX,MY,STDF/SWWKD,YXSXEDEOREBOUDQ,DPUK,D,,WG,,RZMWTS/FVTEYQRDFFPHWZWVOWZKMNGUYYWEX/PPYFWGPWDOXSEP"

rows_low_to_high = [ "zxcvbnm,./", "asdfghjkl;'", r'qwertyui\op[]' ]
rows_high_to_low = [ r'qwertyui\op[]', "asdfghjkl;'", "zxcvbnm,./" ]

rows = rows_low_to_high

def tribit2(key, row_keys):
    for i in range(len(row_keys)):
        if row_keys[i].__contains__(key.lower()):
            return i

def tribit(key):
    return tribit2(key, rows)

def decode():
    letter_number=math.floor(len(input) / 3)
    for i in range(letter_number):
        encoded_letter = input[i*3:i*3+3]
        # print("%s : %d%d%d : " % (encoded_letter, tribit(encoded_letter[0]), tribit(encoded_letter[1]), tribit(encoded_letter[2])), end="")
        value=tribit(encoded_letter[0]) * 9 + tribit(encoded_letter[1]) * 3 + tribit(encoded_letter[2])
        # print("%2d : " % value, end="")

        if 0 == value:
            letter = ' '
        else:
            letter = chr(value + ord('a') - 1)
            
        print("%c" % letter, end="")
        # print()

rows = rows_low_to_high
decode()
print()
print()
rows = rows_high_to_low
decode()
print()
print()

input=input[1:len(input)]
rows = rows_low_to_high
decode()
print()
print()
rows = rows_high_to_low
decode()
print()
print()

input=input[1:len(input)]
rows = rows_low_to_high
decode()
print()
print()
rows = rows_high_to_low
decode()
print()


left="qwertasdfgzxcvb123456"
left_0=True

def dec(key):
    if left.__contains__(key.lower()):
        if left_0:
            return False
        else:
            return True
    else:
        if left_0:
            return True
        else:
            return False

def tribit_split(key):
    if dec(key):
        return tribit2(key, rows_low_to_high)
    else:
        return tribit2(key, rows_high_to_low)

# use 0-2 on one 1/2 of the keyboard and 2-0 on the other
def decode_split_keyboard():
    letter_number=math.floor(len(input) / 3)
    for i in range(letter_number):
        encoded_letter = input[i*3:i*3+3]
        # print("%s : %d%d%d : " % (encoded_letter, tribit_split(encoded_letter[0]), tribit_split(encoded_letter[1]), tribit_split(encoded_letter[2])), end="")
        value=tribit_split(encoded_letter[0]) * 9 + tribit_split(encoded_letter[1]) * 3 + tribit_split(encoded_letter[2])
        # print("%2d : " % value, end="")

        if 0 == value:
            letter = ' '
        else:
            letter = chr(value + ord('a') - 1)
            
        print("%c" % letter, end="")
        # print()

print()
print("-------------------------------------------------------------")
print()
left_0 = True

decode_split_keyboard()
print()
print()
left_0 = False

decode_split_keyboard()
print()
print()
