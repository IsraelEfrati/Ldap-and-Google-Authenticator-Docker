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

## Adding new users
In your browser go to:
https://localhost:6443
                    
Select login and enter the following credentials:

Login DN: cn=admin,dc=example,dc=org        
Password: admin

 ![Alt text](https://github.com/IsraelEfrati/screenshoots/blob/main/1.png?raw=true "Optional Title")
 
 
Create group: my_users              
Select dc=example,dc=org -> 'Create new entry here' 

In the 'group' field write 'my_users'

Click on 'create object' and 'commit' in the next page

 ![Alt text](https://github.com/IsraelEfrati/screenshoots/blob/main/2.png?raw=true "Optional Title")

 
Select 'cn=my_users' and select 'create a child entry'      
Enter first and last name, create a password and select 
'my_users' in the  'GID Number' dropdown.       

Select 'create object' 

 ![Alt text](https://github.com/IsraelEfrati/screenshoots/blob/main/3-4.png?raw=true "Optional Title")


Select  'Add new attribute' 

Select 'Email' in the 'Add Attribute' dropdown.     
The value of the email should be <User ID>@example.org      
The user Id was created in previous stage when the user was added.
	
 ![Alt text](https://github.com/IsraelEfrati/screenshoots/blob/main/5.png?raw=true "Optional Title")

      
Click on 'update object'
