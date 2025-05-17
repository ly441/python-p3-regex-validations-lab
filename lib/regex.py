
import re

name_regex = re.compile(r'^[A-Z][a-z\']*(?:[\'-][A-Z][a-z\']*)*(?: [A-Z][a-z\']*(?:[\'-][A-Z][a-z\']*)*)*$')
phone_regex = re.compile(r'^\(?[0-9]{3}\)?[-. ]?[0-9]{3}[-. ]?[0-9]{4}$')
email_regex = re.compile(r'^[a-zA-Z][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')