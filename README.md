# Konfigurasi SSH
```plaintext
enable
configure terminal
## Set hostname router dan Domain
```plaintext
hostname nama_router
ip domain name contoso.local
## Generate RSA Keys
```plaintext
crypto key generate rsa
## menambahkan user
```plaintext
username <nama> secret <password>
username <nama> privilege 15
## Konfigurasi line 0 4 dan menggunakan local database user untuk autentikasi
```plaintext
line vty 0 4
login local
transport input ssh

# Konfigurasi interface management
```plaintext
configure terminal
interface f0/0
ip address 192.168.122.2 255.255.255.0

# Install ansible di Control Node
```plaintext
sudo apt update &&
sudo apt install software-properties-common

## Menambahkan PPA Ansible
```plaintext
sudo apt-add-repository ppa:ansible/ansible &&
sudo apt install ansible