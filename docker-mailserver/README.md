# Docker Mailserver

[Docker Mailserver Github](https://github.com/docker-mailserver/docker-mailserver.git) | 
[Docker Mailserver Documentation](https://docker-mailserver.github.io/docker-mailserver/latest/) | 
[Secure SMTP](https://www.agari.com/blog/smtps-how-to-secure-smtp-with-ssl-tls-which-port-to-use#:~:text=Secure%20SMTP%20can%20be%20achieved,and%20transforms%20it%20into%20SMTPS.)

## Menu
- [Instructions](#instructions)
- [Security](#security-required)
- [Test](#test)
- [Sources](#sources)

## Instructions

```
cd docker-mailserver
```

##### generate let's encrypt SSL keys
```
# Requires access to port 80 from the internet, adjust your firewall if needed.
docker run --rm -it \
  -v "${PWD}/docker-data/certbot/certs/:/etc/letsencrypt/" \
  -v "${PWD}/docker-data/certbot/logs/:/var/log/letsencrypt/" \
  -p 80:80 \
  certbot/certbot certonly --standalone -d mail.example.com
```


##### update env file 
```
vim mailserver.env

(e.g your mail server's hostname)
OVERRIDE_HOSTNAME=mail.example.com
```

##### build and run app
```
docker compose up -d --build
```

##### Manage your Mailserver
1. executing commands directly in the container with the setup script:
```docker exec <CONTAINER NAME> setup help```
2. executing directly setup script presents here in this folder:
behind the scene, it will do docker exec for you
```./setup.sh help```   
   
##### adds execute permissions for the user
```
chmod a+x ./setup.sh
```

##### create new user : you can create user like noreply etc ..
```
./setup.sh email add user@example.com geGZ0uz8wNGn8ZM
```

## Security (required)
### For security, in addition to SSL
- **Configure DNS records**
[MX, A, SPF and DKIM records](security.md)

- **Enable Fail2Ban** : automatically ban IP addresses of hosts that have generated many fails. it is designed to prevent against brute-force attacks.
[Fail2Ban](https://docker-mailserver.github.io/docker-mailserver/edge/config/security/fail2ban/)
  ```
  # update mailserver.env
  ENABLE_FAIL2BAN=1

  # update compose file and add this in mailserver container
  cap_add:
    - NET_ADMIN
  ```
  ```
  COMMAND fail2ban :=
        ./setup.sh fail2ban 
        ./setup.sh fail2ban ban <IP>
        ./setup.sh fail2ban unban <IP>
        ./setup.sh fail2ban log
  ```

### Allow SMTP ports on Incoming/Outgoing traffic in your VM where you install docker-mailserver

**Delivering Emails to External Recipients:** If the email's recipient is outside your local domain (i.e., the email needs to be sent to an external server), your Docker Mailserver will then establish its own SMTP connection to the recipient's email server to deliver the email. This is an outgoing SMTP request from your Docker Mailserver's perspective.

**Receiving Emails:** For receiving emails, other servers will make SMTP requests to your Docker Mailserver. Your server needs to accept incoming SMTP connections for this purpose.

**Using IMAP to Access Stored Emails:** IMAP (Internet Message Access Protocol) is critical for retrieving and managing emails that are stored on your server. It allows email clients or scripts to connect to your Docker Mailserver to access these emails.


Make sure these SMTP/IMAP ports are open.

--- 

## Test
### Test your SMTP server

- python script
  ```
  # inside test.py, replace by your own credentials
  python3 test.py
  ```

- install SMTP client like `Thunderbird` to test, use the recently created username and password

### Test SMTP requests from a VM

- in the Rules applicable to outgoing traffic (the requests, your VM is authorized to do), you have to activate SMTP ports, like that you allow the VM to do SMTP requests.


---

## Sources
- [Docker Mailserver : Basic Installation](https://docker-mailserver.github.io/docker-mailserver/edge/examples/tutorials/basic-installation/)
- [FAQ Docker Mailserver : Most questions are answered here](https://docker-mailserver.github.io/docker-mailserver/edge/faq/)