import ddddocr
ocr = ddddocr.DdddOcr()
with open("char_class1193.png", "rb") as f:
    img_bytes = f.read()
    result = ocr.classification(img_bytes,png_fix=True)
    print(result)
# ocr.classification