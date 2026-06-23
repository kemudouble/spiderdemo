# 

from fontTools.ttLib import TTFont
font = TTFont("font.ttf")
# font.saveXML("font.xml")

Zcmap={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"zero":0}
glyph_order = font.getGlyphOrder()
li=list(glyph_order)
li.remove(".notdef")
print(li)
dic={}
for i in range(0, len(li)):
    k=Zcmap[li[i]]
    dic[k]=i
print(dic)