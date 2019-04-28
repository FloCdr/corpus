import os, sys, datetime
import matplotlib
import imaplib

server = 'imap.google.com'
user = 'blanketandbonn@gmail.com'
password = '1atm=101325Pa'
port = 993

mail = imaplib.IMAP4_SSL(server)


mail.login(user, password)
mail.select()
print('zou')


# # worksite document manager
# now = datetime.datetime.now()
# print(now)
#
# class Document:
#
#     def __init__(self, number, index = 0, status = 'ATT'):
#
#
#
#     def visa(status, date = now):
#
#
#
# class Library:
#
#     def __init__(self):
#
#
#
#
#     def set_nomenclature():
