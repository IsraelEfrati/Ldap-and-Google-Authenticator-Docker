# Ldap-and-Google-Authenticator-Docker
Authenicate users with Ldap server and Google Authenticator

Download the project:
git clone https://github.com/IsraelEfrati/Ldap-and-Google-Authenticator-Docker.git    

## Edit the my_ldap.py
Set the value of the variable LDAP_IP:
```
LDAP_IP = ldap server IP
```

## Edit the script.sh
Set the value of the variable PHPLDAPADMIN_LDAP_HOSTS in line #8 to your IP address



## Run the following:		
```
cd Ldap-and-Google-Authenticator-Docker
sudo ./script.sh

```
