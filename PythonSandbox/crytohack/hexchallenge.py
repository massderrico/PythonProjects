
letter = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

hex_conv = {"0":0, "1":1, "2":2, "3":3 ,"4":4, "5":5 , "6":6, "7":7, "8":8, "9":9, "a":10, "b":11, "c":12, "d":13, "e":14, "f":15 }


for i in range(0,len(letter),2):
    first = hex_conv[letter[i]]*16
    second = hex_conv[letter[i+1]]
    conv = chr(first+second)
    print(conv, end="")