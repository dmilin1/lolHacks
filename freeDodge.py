import subprocess
import re
import requests
import urllib3

command = "WMIC PROCESS WHERE name='LeagueClientUx.exe' GET commandline"

output = subprocess.Popen(command, stdout=subprocess.PIPE,
                        shell=True).stdout.read().decode('utf-8')

port = re.findall(r'"--app-port=(.*?)"', output)[0]
password = re.findall(r'"--remoting-auth-token=(.*?)"', output)[0]

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = requests.session()
session.verify = False

res = session.post(
    'https://127.0.0.1:%s/lol-lobby/v1/lobby/custom/cancel-champ-select' % port,
    data={},
    auth=requests.auth.HTTPBasicAuth('riot', password)
)
print(res.text)

res = session.post(
    'https://127.0.0.1:%s/lol-lobby/v2/matchmaking/quick-search' % port,
    json={ 'queueId': 1110 },
    auth=requests.auth.HTTPBasicAuth('riot', password)
)
print(res.text)
