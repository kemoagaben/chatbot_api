import qrcode

VCARD_DATA = """BEGIN:VCARD
VERSION:3.0
N:Satılmış;Nurten;;;
FN:Av. Nurten Satılmış
ORG:Örnek Hukuk Bürosu
TITLE:Avukat
TEL;TYPE=CELL:+905555555555
EMAIL:nurten@example.com
URL:https://yrzdmcyy.manus.space/
END:VCARD
"""

with open("nurten_vcard.vcf", "w", encoding="utf-8") as f:
    f.write(VCARD_DATA)

img = qrcode.make(VCARD_DATA)
img.save("nurten_vcard_qr.png")
print("Created nurten_vcard.vcf and nurten_vcard_qr.png")
