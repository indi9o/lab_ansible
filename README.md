```plaintext
# Konfigurasi SSH
enable
configure terminal
## Set hostname router dan Domain
hostname nama_router
ip domain name contoso.local
## Generate RSA Keys
crypto key generate rsa
## menambahkan user
username <nama> secret <password>
username <nama> privilege 15
## Konfigurasi line 0 4 dan menggunakan local database user untuk autentikasi
line vty 0 4
login local
transport input ssh
# Konfigurasi interface management
configure terminal
interface f0/0
ip address 192.168.122.2 255.255.255.0
# Install ansible di Control Node
sudo apt update &&
sudo apt install software-properties-common
## Menambahkan PPA Ansible
sudo apt-add-repository ppa:ansible/ansible &&
sudo apt install ansible