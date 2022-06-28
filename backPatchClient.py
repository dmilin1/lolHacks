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

res = session.put(
    ('https://127.0.0.1:%s/lol-patch/v1/game-patch-url' % port) + '?url=https://lol.secure.dyn.riotcdn.net/channels/public/releases/B7BB62282C6C68D2.manifest',
    data={},
    auth=requests.auth.HTTPBasicAuth('riot', password)
)
print(res.text)