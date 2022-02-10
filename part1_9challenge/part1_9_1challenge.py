import docx

doc = docx.Document(r"C:\Users\tmyum\Documents\5年前から高齢化課題に取り組む.docx")
num = 0
for para in doc.paragraphs:
    num = num + 1
    print(num, para.text)
