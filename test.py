# https://webhook.site/7bd898bd-e4de-4727-a7e9-0587b9beb10f?q=

import subprocess
import re
import requests
import urllib3
import time
from naughty_string_validator import *

command = "WMIC PROCESS WHERE name='LeagueClientUx.exe' GET commandline"

output = subprocess.Popen(command, stdout=subprocess.PIPE,
                        shell=True).stdout.read().decode('utf-8')

port = re.findall(r'"--app-port=(.*?)"', output)[0]
password = re.findall(r'"--remoting-auth-token=(.*?)"', output)[0]

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = requests.session()
session.verify = False


# <>?:"{}|_+
# {"errorCode":"BAD_REQUEST","httpStatus":400,"message":"Unknown argument ':\"{}|_ ' for 'GetLolSummonerV1CheckNameAvailabilityNewSummonersByName'."}

# ☺☻♥♦♣♫☼►◄↕‼¶§▬↨↑↓→∟↔▲▼
# alse


def run_str(string):
  res = session.get(
      'https://127.0.0.1:%s/lol-summoner/v1/check-name-availability-new-summoners/' % port + string,
      auth=requests.auth.HTTPBasicAuth('riot', password)
  )
  print()
  print(string)
  print(res.text)
  print()

for string in get_naughty_string_list()[150:]:
  time.sleep(0.5)
  run_str(string)

# run_str('javascript:test(e =>)')
# run_str('!@#$%^&*()`~')
# run_str('☺☻♥♦♣♫☼►◄↕‼¶§▬↨↑↓→∟↔▲▼')