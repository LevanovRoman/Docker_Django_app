import ldap3
from ldap3 import Connection, Server
import email
import email.header
import imaplib

server = Server('172.16.2.46')
imap_host = 'cgp.nordsy.spb.ru'


def ldap_connection(user_login):
    connect_1 = Connection(server, "CN=wordpress,CN=Users,DC=nordsy,DC=spb,DC=ru", "word;press1", auto_bind=True)
    if connect_1:
        connect_1.search("OU=Пользователи,DC=nordsy,DC=spb,DC=ru",
                         "(&(objectClass = User)(cn={}))".format(user_login),
                         attributes=ldap3.ALL_ATTRIBUTES)
        return connect_1.entries[0].sn, connect_1.entries[0].givenName, connect_1.entries[0].mail
    else:
        ...


def correct_field(data):
    temp = email.header.decode_header(data)
    return temp[0][0].decode(temp[0][1])


def check_mailbox(imap_user, imap_pass, type_box):
    imap = imaplib.IMAP4_SSL(imap_host)
    imap.login(imap_user, imap_pass)
    imap.select("INBOX")
    # _, msgnums = imap.search(None, "UNSEEN")
    _, msgnums = imap.search(None, type_box)

    if not msgnums[0].split():
        return []

    for msg in msgnums[0].split():
        _, data = imap.fetch(msg, "(RFC822)")
        message = email.message_from_bytes(data[0][1])

    result_list = []
    for index, msg in enumerate(msgnums[0].split()):
        temp_dict = {}
        _, data = imap.fetch(msg, "(RFC822)")
        message = email.message_from_bytes(data[0][1])
        temp_dict["number"] = msg
        # temp_dict["from"] = message.get('From')
        # temp_dict["from"] = email.header.decode_header(message.get('From'))
        # y = email.header.decode_header(message.get('From'))
        # y = y[0][0].decode(y[0][1])
        temp_dict["from"] = message.get('From')
        # temp_dict["to"] = message.get('To')
        # temp_dict["bcc"] = message.get('BCC')
        temp_dict["date"] = message.get('Date')
        # x = email.header.decode_header(message.get('Subject'))
        # print(x)
        # x = x[0][0].decode(x[0][1])
        # temp_dict["subject"] = x
        # temp_dict["subject"] = email.header.decode_header(message.get('Subject'))
        # temp_dict["subject"] = correct_field(message.get('Subject'))
        result_list.append(temp_dict)
    imap.close()
    return result_list

# print(ldap_connection(user_login, user_password)[1])
# print(check_mailbox(user_login, user_password))
