#Ստեղծել contacts.txt ֆայլ, ավելացնել հետևյալ (First_Name Last_Name, Title, Extension, Email)  տեքստը՝ օգտագվելով Python-ի ֆայլային ֆունկցիոնալից։ Ստորև ուղարկում եմ pdf ֆայլ (Business_Proposal.pdf), որի պարունակությունը կարդալով պետք է դուրս բերել AUTHORS: դաշտը իր ենթատողերով և ավելացնել contacts.txt ֆայլում։ Վերջնական պատկերը պետք է լինի հետևյալը
#First_Name Last_Name, Title, Extension, EmailAUTHORS:
#Amy Baker, Finance Chair, x345, abaker@ourcompany.com
#Chris Donaldson, Accounting Dir., x621, cdonaldson@ourcompany.com
#Erin Freeman, Sr. VP, x879, efreeman@ourcompany.com
#First install pypdf2


Pip install pypdf2
import PyPDF2
pdf=open('Business_Proposal.pdf', 'rb')
reader=PyPDF2.PdfReader(pdf)
page=reader.pages[1]
print(page.extract_text())
f=open('contact.txt', 'w')
f.write('First_Name Last_Name, Title, Extension, Email, ')
f.write(page.extract_text())
f.close()


f1=open('contact.txt')
text=f1.read()
print(text)
