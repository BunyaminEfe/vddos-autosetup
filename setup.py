import subprocess
import os
import re
from pip._vendor.colorama import Fore

def baner():
  subprocess.call('clear', shell=True)
  print(Fore.GREEN+'''

   /$$    /$$ /$$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$ 
  | $$   | $$| $$__  $$| $$__  $$ /$$__  $$ /$$__  $$
  | $$   | $$| $$  \ $$| $$  \ $$| $$  \ $$| $$  \__/
  |  $$ / $$/| $$  | $$| $$  | $$| $$  | $$|  $$$$$$ 
   \  $$ $$/ | $$  | $$| $$  | $$| $$  | $$ \____  $$
    \  $$$/  | $$  | $$| $$  | $$| $$  | $$ /$$  \ $$
     \  $/   | $$$$$$$/| $$$$$$$/|  $$$$$$/|  $$$$$$/
      \_/    |_______/ |_______/  \______/  \______/ 

                                       Bej O
  ''')
  print(Fore.RED+'''                      thx for l4ncelot and kronos and voduy''')
  print()
  print()

def addsite():
  baner()
  print(Fore.CYAN+'example akarguard.net')
  sitename = input(Fore.WHITE+'|'+Fore.GREEN+'YOUR SITE NAME'+Fore.WHITE+'| > ')
  os.system('vddos add '+ sitename)
  os.system('vddos-switch '+sitename+' high')
  os.system('vddos restart')


def limitwrite():
  f = open("/vddos/conf.d/limit-conn.conf", "w+")
  contents = f.read()
  text = re.split('([.])', contents)
  text.insert(4, '''# Limit conn
  limit_conn_zone $limitip zone=perip:10m;
  limit_conn perip 10;
  limit_conn_status 444;
  limit_req_zone $limitip zone=dyn:10m rate=10r/s;
  limit_req zone=dyn burst=10;
  limit_req_status 444;
  ''')
  f.seek(0)
  f.writelines(text)
  f.close()

def stosver():
  baner()

  print()
  print(Fore.RED+'CHOOSE YOUR OS VERSION')
  print(Fore.WHITE+'|'+Fore.GREEN+'1'+Fore.WHITE+'| > '+Fore.WHITE+'|'+Fore.GREEN+'CentOS 7'+Fore.WHITE+'|')
  print(Fore.WHITE+'|'+Fore.GREEN+'2'+Fore.WHITE+'| > '+Fore.WHITE+'|'+Fore.GREEN+'CentOS 8'+Fore.WHITE+'|')
  print()

  chooseosversion = input(Fore.WHITE+'|'+Fore.GREEN+'YOUR OS VERSION'+Fore.WHITE+'| > ')
  if chooseosversion == '1':
      os.system('''
        yum -y install libatomic_ops-devel \
        yum -y install epel-release ; yum -y install wget zip unzip tar curl  && \
        yum -y install nano net-tools curl wget gc gcc gcc-c++ pcre-devel zlib-devel make wget openssl-devel libxml2-devel libxslt-devel gd-devel perl-ExtUtils-Embed GeoIP-devel gperftools gperftools-devel perl-ExtUtils-Embed  && \
        yum -y install screen htop iotop iptraf nano net-tools gcc automake libffi-devel zlib zlib-devel gcc gcc-c++ autoconf apr-util-devel gc gcc gcc-c++ pcre-devel zlib-devel make wget openssl openssl-devel libxml2-devel libxslt-devel gd-devel perl-ExtUtils-Embed GeoIP-devel gperftools gperftools-devel  perl-ExtUtils-Embed && \
        yum -y install gnutls-utils sshpass rsync && \
        yum -y install bind-utils sysstat bc tar curl wget gc gcc gcc-c++ pcre-devel zlib-devel make wget openssl-devel libxml2-devel libxslt-devel gd-devel perl-ExtUtils-Embed GeoIP-devel gperftools gperftools-devel perl-ExtUtils-Embed gcc automake autoconf apr-util-devel gc gcc gcc-c++ pcre-devel zlib-devel make wget openssl openssl-devel libxml2-devel libxslt-devel gd-devel perl-ExtUtils-Embed GeoIP-devel gperftools gperftools-devel perl-ExtUtils-Embed perl perl-devel perl-ExtUtils-Embed libxslt libxslt-devel libxml2 libxml2-devel gd gd-devel GeoIP GeoIP-devel gperftools-devel wget yum-utils make gcc openssl-devel bzip2-devel libffi-devel zlib-devel screen htop iotop iptraf nano net-tools gcc automake libffi-devel zlib zlib-devel gcc gcc-c++ autoconf apr-util-devel gc 
        wget https://files.voduy.com/vDDoS-Proxy-Protection/latest.sh ; chmod 700 latest.sh ; bash latest.sh
      ''')
      os.system('''
      wget https://github.com/AkarGuard/kernel-ddos-protection/raw/main/install \
      ''')
      os.system('''
        chmod +x install && bash install
      ''')
      os.system('''
      systemctl stop firewalld
      ''')
      limitwrite()
      addsite()
      os.system('''
      vddos restart
      ''')
      baner()
  if chooseosversion == '2':
      os.system('''
        yum -y install epel-release ; yum -y install wget zip unzip tar curl  && \
        yum -y install nano net-tools curl wget gc gcc gcc-c++ pcre-devel zlib-devel make wget openssl-devel libxml2-devel libxslt-devel gd-devel perl-ExtUtils-Embed GeoIP-devel gperftools gperftools-devel perl-ExtUtils-Embed  && \
        yum -y install screen htop iotop iptraf nano net-tools gcc automake libffi-devel zlib zlib-devel gcc gcc-c++ autoconf apr-util-devel gc gcc gcc-c++ pcre-devel zlib-devel make wget openssl openssl-devel libxml2-devel libxslt-devel gd-devel perl-ExtUtils-Embed GeoIP-devel gperftools gperftools-devel  perl-ExtUtils-Embed && \
        yum -y install gnutls-utils sshpass rsync && \
        yum -y install bind-utils sysstat bc tar curl wget gc gcc gcc-c++ pcre-devel zlib-devel make wget openssl-devel libxml2-devel libxslt-devel gd-devel perl-ExtUtils-Embed GeoIP-devel gperftools gperftools-devel perl-ExtUtils-Embed gcc automake autoconf apr-util-devel gc gcc gcc-c++ pcre-devel zlib-devel make wget openssl openssl-devel libxml2-devel libxslt-devel gd-devel perl-ExtUtils-Embed GeoIP-devel gperftools gperftools-devel perl-ExtUtils-Embed perl perl-devel perl-ExtUtils-Embed libxslt libxslt-devel libxml2 libxml2-devel gd gd-devel GeoIP GeoIP-devel gperftools-devel wget yum-utils make gcc openssl-devel bzip2-devel libffi-devel zlib-devel screen htop iotop iptraf nano net-tools gcc automake libffi-devel zlib zlib-devel gcc gcc-c++ autoconf apr-util-devel gc \
        wget https://files.voduy.com/vDDoS-Proxy-Protection/latest.sh ; chmod 700 latest.sh ; bash latest.sh
      ''')
      os.system('''
      wget https://github.com/AkarGuard/kernel-ddos-protection/raw/main/install
      ''')
      os.system('''
        chmod +x install && bash install
      ''')
      os.system('''
      systemctl stop firewalld
      ''')
      limitwrite()
      addsite()
      os.system('''
      vddos restart
      ''')
      baner()

def twostosver():
  baner()
  os.system('''
    apt -y install libreadline-gplv2-dev \
    apt update; apt -y install wget zip unzip tar curl ca-certificates && \
    apt install -y perl libperl-dev libgd3 libgd-dev libgeoip1 libgeoip-dev geoip-bin libxml2 libxml2-dev libxslt1.1 libxslt1-dev  && \
    apt-get -y install build-essential libpcre3 libpcre3-dev zlib1g zlib1g-dev libssl-dev libgd-dev libxml2 libxml2-dev uuid-dev  && \
    apt -y install curl wget build-essential checkinstall   && \
    apt -y install net-tools sshpass rsync sysstat bc dnsutils  && \
    apt -y install libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev \
    wget https://files.voduy.com/vDDoS-Proxy-Protection/latest.sh ; chmod 700 latest.sh ; bash latest.sh
  ''')
  os.system('''
      wget https://github.com/AkarGuard/kernel-ddos-protection/raw/main/install \
      ''')
  os.system('''
        chmod +x install && bash install
      ''')
  os.system('''
    systemctl stop firewalld
    ''')
  limitwrite()
  addsite()
  os.system('''
    vddos restart
    ''')
  baner()

baner()
print(Fore.RED+'CHOOSE YOUR SERVER OS')
print(Fore.WHITE+'|'+Fore.GREEN+'1'+Fore.WHITE+'| > '+Fore.WHITE+'|'+Fore.GREEN+' CentOS/CloudLinux/AlmaLinux/RockyLinux/RedHat'+Fore.WHITE+' |')
print(Fore.WHITE+'|'+Fore.GREEN+'2'+Fore.WHITE+'| > '+Fore.WHITE+'|'+Fore.GREEN+' Ubuntu/Debian'+Fore.WHITE+' |')
serveros = input(Fore.WHITE+'|'+Fore.GREEN+'YOUR OS'+Fore.WHITE+'| > ')

if serveros == '1':
  stosver()

if serveros == "2":
  twostosver()  