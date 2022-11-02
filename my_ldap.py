import os.path
from ldap3 import Server, Connection, ALL
from ldap3.core.exceptions import LDAPBindError
from pyotp import random_base32, totp

LDAP_IP = "192.168.25.130"


def get_secret():
    if os.path.exists("code.txt"):
        with open("code.txt", "r") as f:
            secret = f.readline()
    else:
        secret = random_base32()
        with open("code.txt", "w") as f:
            f.write(secret)
    return secret


SECRET = get_secret()
OTP = totp.TOTP(SECRET)


def connect_ldap_server(full_name, password):
    global LDAP_IP
    try:
        # Provide the hostname and port number of the openLDAP
        server_uri = "ldap://{0}:389".format(LDAP_IP)
        server = Server(server_uri, get_info=ALL)
        # username and password can be configured during openldap setup
        user = "cn={},cn=my_users,dc=example,dc=org".format(full_name)
        connection = Connection(server,
                                user=user,
                                password=password)
        bind_response = connection.bind()  # Returns True or False
        return bind_response
    except LDAPBindError as e:
        connection = e


def create_qr_code(user):
    global OTP
    path_start = "https://www.google.com/chart?chs=200x200&chld=M%7C0&cht=qr&chl="
    partial_path = OTP.provisioning_uri(name=user, issuer_name='israel_ldap')
    full_path = path_start + partial_path
    return full_path


def check_google_code(google_code):
    global OTP
    verified = OTP.verify(google_code)
    return verified
