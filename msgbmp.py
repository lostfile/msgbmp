import base64
import textwrap
print('Message bumper v1.1')
fil = input("MSG:")
print('1.encode')
print('2.decode')
print('3.txtfile')
cod = input('>')

if cod == "1":
 encodedBytes = base64.b16encode(fil.encode("utf-8"))
 encodedStr = str(encodedBytes, "utf-8")
 print(encodedStr)

if cod == "2":
 decodedBytes = base64.b16decode(fil)
 decodedStr = str(decodedBytes, "utf-8")
 print(decodedStr)

if cod == "3":
 encodedBytes = base64.b16encode(fil.encode("utf-8"))
 encodedStr = str(encodedBytes, "utf-8")
 gog = open('32442.txt', 'w')
 gog.write(encodedStr)
 gog.close()