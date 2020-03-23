# ###################################
# Content
fileName = 'MyDoc.pdf'
documentTitle = 'Document title!'
title = 'Tasmanian devil'
subTitle = 'The largest carnivorous marsupial'

textLines = [
'The Tasmanian devil (Sarcophilus harrisii) is',
'a carnivorous marsupial of the family',
'Dasyuridae.'
]


from reportlab.pdfgen import canvas

pdf = canvas.Canvas(fileName)
pdf.setTitle(documentTitle)

pdf.save()
# print('Hello')