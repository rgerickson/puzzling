
import math

input="WDP/OMAXRMTWTWZP/ED,YYCKMPE,EG,MWYMEPEFMDU/TK,,RKMSXEKSUPXEDPTQFP,/M,EPRPPZ,ISKPHVDVTU,S///WQ,GUK,PMEY/XMPFDOR/RIH,IEPSEWOLOPKETFRO,,HGE,RFW,ZYY./M.OPGXSMOME;BTZDXSEPM,ETL/FI,WFD,FRZSDURDRZWXWOL,UC/OT/YZMYKMURSFD,T,ZT,X/ED,PPROTZOSRWIWSTRMDTOG/GSZMFERYRF/D,EDKVLQOFY/KLTOWXYFESGY/U.IOWDKXUPSSMGS/SKMT,YUGEEYD,WRRKX,EPAMEDD/WTXSK,TLLDIPZDRX/TRQRSYZKFGDZZ/COVP,GLSEOS,T,MSYERMPWDGSEJYY,DMFMRKKJ//YDPW,,YDP,N,ZE,US,SGHOMW,P//WRDSUU,F/VWZNK/KSSBMW/EYXRMRHMW,,D/,DKDGTPPTXSM.,YTTCDKXRSKKSSYZ//BCFTW,DEJ,D;M/EFJ/O/R,P/SXRU,PMSRMPPG/;ZTY/GS;;O/UYDWG/PODXIGMPORPGMTISTDWS/PMEUDUZQEYO/F,RGDEKKOGDM,MWXR/,WXVNWVKSXPGQ/WRMG,/SMPDEDPS;/W,USTRTXBGTT,PP,MWK,DTM/SYLRGUTWOMRMWXPLHSC;GWH,YM;W/DEQPRD,DW,,.DFU,OOSSPPGMIHSKK/UZ//PDTDS,RXDZ;PKYT/GMRSXG,KDZM/ADEPXOYUOLODGXDAMSG/O/EZWWORMWFRWRP/MRELEETLUZDGSRU.SZPHGENWVUTZVKAMSPUOVS/GGSRHPEW/NKYRPMMKXSMF,GNK/TMM.YWYPUPVMFSKYRDJQX/FFYZYM/,MS/YUWQ/PTFVAUW.W/WSWD,/ATWWMXZWKPX,MY,STDF/SWWKD,YXSXEDEOREBOUDQ,DPUK,D,,WG,,RZMWTS/FVTEYQRDFFPHWZWVOWZKMNGUYYWEX/PPYFWGPWDOXSEP"

rows_low_to_high = [ "zxcvbnm,./", "asdfghjkl;'", r'qwertyui\op[]' ]
rows_high_to_low = [ r'qwertyui\op[]', "asdfghjkl;'", "zxcvbnm,./" ]

rows = rows_low_to_high

def tribit(key):
    for i in range(len(rows)):
        if rows[i].__contains__(key.lower()):
            return i

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