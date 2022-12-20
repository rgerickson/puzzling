
import math

input="EZNIEEO5NE2OGIN2R2QPCHKII52OFO22NKPIFO5JGNIWW5K,W5SXFWOFORNELE;WVBKSK2FEN5SW.ONIR;WKN2/5IKHTWS5EKFZS22EEWE32U/ZIGKS25OSWBW5ORFNONZNVWFPF5NWS2SWW2SKB5IOE2O5ZWLEKJS2NSSESDOIFV5QFWNSF34KNFN;K15NFSIXI25I5S5W5TFOIS5KOO,LIPESYWK5NW1NFEA2OEF,/OSONN2VSZTE/EI2XTSPNWNSE;I2EEK5RKXNNEKO5IEI1OKS;IWSYINSPSOW5S;5F5SKNJ5/OI2UNWM3NFG5ZEX22IBQFX/FI5FOE;FIFSKS5YOIIISW2SKNWFFXF3NIKO/54NIKFFPOWKK2SPZS2NWF;/N4KO2DO2F5NSFWGF2FKU,KEO5SIE25SGWN22E55KMSKNSOF2SSFNF5FOSKK2WE5FCTKNSKG4FNN4TEFKSEOUWNSIOLEOE2SW5OWWSNM;IRHNW2NFSIWTHMIPN2IEDSIS1N22EE5EIN;2FN5EK2NBSTNA22FZNKN2O2W2EWEWKSQBINB,2WNOHWWUGLT5SNS5S;LOM5VOCFENOFESOIT.SGI/KC25WFFEOF5U22OFOO5ESOIER2O5NOVIWSISF;QFJP;WEL,IO5FSFSESF5EKIWENE55OJ5YN52KFNGKHINWE2K2KCF2E5SGE;WWWSOCIN2SR,LQ5KKEKEIOF2NFOF/NIK5/SEIO5SKR/WCJI.IF2EY2FKSI1KEXEWIFIKIO5BS2K55W,2WE/FNZKOK5,.KBK2W5SROOK2KWFFK5E554EF2NWE55FNNQ/EC5NKNE2NW/STGOS4E3IOSNKWNW2Z2DX2QTNNWN225KIEN5FI35WRNXWWFFWK2EWVO2NN/USBSCO,VMKKSNSIWNKOOWZ;2U5KI4WW2EU5IILE3SZIG2KWE2U2TSSE2,SNOL51KN5F5KGFFF2SNS2OKISF/5IC..BFI555SWO4MN"

left="qwertasdfgzxcvb123456"
left_0=True

def dec(key):
    if left.__contains__(key.lower()):
        if left_0:
            return 0
        else:
            return 1
    else:
        if left_0:
            return 1
        else:
            return 0


def decode():
    letter_number=math.floor(len(input) / 5)
    for i in range(letter_number):
        encoded_letter = input[i*5:i*5+5]
        # print("%s : " % encoded_letter, end="")

        value = 0
        for key in encoded_letter:
            # print("%d" % dec(key), end="")
            value = value * 2 + dec(key)

        # print(": %2d : " % value, end="")

        if 0 == value:
            letter = ' '
        else:
            letter = chr(value + ord('a') - 1)
            
        print("%c" % letter, end="")
        # print()

left_0 = True
decode()
print()
print()
left_0 = False
decode()
print()
print()

left="1234567890-qwertyuiop[]"
left_0 = True
decode()
print()
print()
left_0 = False
decode()
print()
print()

left="1234567890-asdfghjkl;"
left_0 = True
decode()
print()
print()
left_0 = False
decode()
print()
print()
