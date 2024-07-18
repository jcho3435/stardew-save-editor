from lxml import etree
import sys

with open("save_data/SaveGameInfo", "rb") as f:
    data = f.read()

# REMOVE BOM CHARACTERS
if data.startswith(b'\xef\xbb\xbf'):
    data = data[3:]

character_data = etree.fromstring(data)

print(sys.getsizeof(data), "\n", sys.getsizeof(character_data))

print(character_data.xpath("/Farmer/name")[0].text)
print(character_data.xpath("/Farmer/name")[0].text)
print(character_data.xpath("/Farmer/name")[0].text)
print(character_data.xpath("/Farmer/name")[0].text)