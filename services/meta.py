import os
import uuid
import re
from enum import Enum

CLIENT_URL = os.getenv("CLIENT_URL")

print(CLIENT_URL)

FieldType = Enum('FieldType', 
                 [('STRING', 0), 
                  ('INTEGER', 1), 
                  ('FLOAT', 2), 
                  ('BOOLEAN', 3), 
                  ('DATE', 4), 
                  ('DATETIME', 5), 
                  ('MENU', 6)])

date_format_tokens = [
    ("YYYY", "%Y"),
    ("YY", "%y"),
    ("MMMM", "%B"),
    ("MMM", "%b"),
    ("MM", "%m"),
    ("M", "%m"),
    ("DD", "%d"),
    ("D", "%d"),
    ("dddd", "%A"),
    ("ddd", "%a"), 
    ("d", "%w"), #
    ("HH", "%H"),
    ("H", "%H"),
    ("hh", "%I"),
    ("h", "%I"),
    ("mm", "%M"),
    ("m", "%M"), #
    ("sss", "%f"),
    ("ss", "%S"),
    ("s", "%S"),
    ("A", "%p"), #
    ("a", "%p"), #
    ("ZZ", "%z"),
]

def new_uuid():
    return str(uuid.uuid4())

def format_py_replace(format):
    for token in date_format_tokens:
        matches = [(token[0], m.span()) for m in re.finditer(token[0], format)]
        for m in matches:
            if m[1][0] != 0 and format[m[1][0] - 1] == '%':
                continue
            format = format[:m[1][0]] + token[1] + format[m[1][1]:]
    return format

def db_field_type(value):
    field_type = ('[varchar](255)' if value == FieldType.STRING.value else 
                  '[int]' if value == FieldType.INTEGER.value else 
                  '[float](53)' if value == FieldType.FLOAT.value else
                  '[bit]' if value == FieldType.BOOLEAN.value else
                  '[date]' if value == FieldType.DATE.value else
                  '[datetime]' if value == FieldType.DATETIME.value else
                  '[varchar](255)' if value == FieldType.MENU.value else '')
    return field_type