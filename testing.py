from lxml import etree
import sys

with open("save_data2/MoreRice_363478863", "rb") as f:
    data = f.read()

# REMOVE BOM CHARACTERS
if data.startswith(b'\xef\xbb\xbf'):
    data = data[3:]

character_data: etree._Element = etree.fromstring(data)
print(type(character_data))

print(sys.getsizeof(data), "\n", sys.getsizeof(character_data))

print(character_data.xpath("/SaveGame/farmhands/Farmer/questLog/Quest"))