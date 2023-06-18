import logging
import random
import string
import faker
from faker import Faker

FORMATFREEFORM = '%(asctime)s %(service)s host=%(host)s p=%(payload)s l=%(latency)s s=%(status)s API=[%(api)s] ' \
         'Q=/message/%(act)s/id=messagehash%(mes)s reqId=hash%(requestId)s CL=%(CPUlatency)s ec=[%(error_code1)s] ' \
         'EC2=%(error_code2)s exception=%(exception)s f=%(clientip)-15s '


#asctime, service, host, payload, latency, status, API, Q, reqId, CPULatency, ec, EC2, exception, clientIp
FORMATCSV = '%(asctime)s,%(service)s,%(host)s,%(payload)s ,%(latency)s ,%(status)s,[%(api)s],' \
         '/message/%(act)s/id=messagehash%(mes)s ,hash%(requestId)s ,%(CPUlatency)s ,[%(error_code1)s] ' \
         ',%(error_code2)s ,%(exception)s,%(clientip)-15s '

format = FORMATCSV

logging.basicConfig(format=format)

status_codes = [
    # 1xx - Informational
    100, 101, 102,

    # 2xx - Success
    200, 201, 202, 203, 204, 205, 206, 207, 208, 226,

    # 3xx - Redirection
    300, 301, 302, 303, 304, 305, 306, 307, 308,

    # 4xx - Client Errors
    400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410,
    411, 412, 413, 414, 415, 416, 417, 418, 421, 422, 423,
    424, 425, 426, 428, 429, 431, 451,

    # 5xx - Server Errors
    500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511
]
api_list = ["updateflags","scanvirus", "addmessage", "deletemessage", "fetchmessage", "listmessages", "markasspam"]

region = ["europe", "asia", "africa", "us_west", "us_east", "us_texas", "latam"]

error1 = ["invalidmailbox","missingmailbox", "nonexistentmailbox", "unknownmailbox", "mailboxnotfound", "mailboxerror"]

error2 = ["bad filler", "corrupt file", "missing file", "inaccessible file", "permission denied"]

#action = ["retrieve", "send", "delete", "forward", "reply", "move", "mark_read", "mark_unread", "scan"]

exceptionList = ["invalid encoding", "unsupported encoding", "encoding failure", "character encoding error", "encoding format mismatch", "bad encoding"]

fake = Faker()
n = 100
log_entries = [{'service': 'imap',
                'host': 'machine'+ str(fake.pyint(200, 350))+".dovecotservice."+random.choice(region)+".mail.emailcompany.com",
                'payload': fake.pyint(),  # range from 1 to 9999
                'latency': fake.pyint(1, 100), # range from 1 to 99
                'status': random.choice(status_codes),
                'api': random.choice(api_list),
                'mes': ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)),
                'requestId': ''.join(random.choices(string.ascii_lowercase + string.digits, k=13)),
                'CPUlatency': fake.pyint(1, 100),
                'error_code1': random.choice(error1),
                'error_code2': random.choice(error2),
                'exception': random.choice(exceptionList),
                'clientip': fake.ipv4()#,
                #'act': random.choice(action)
                } for _ in range(n)]

for log_entry in log_entries:
    logger = logging.getLogger('tcpserver')
    logger.warning('', extra=log_entry)

