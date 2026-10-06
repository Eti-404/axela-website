import json
import base64
import urllib.request

AUTH_B64 = base64.b64encode(b'admin:FYCY 52pM wknI 1nOf 4RA2 t8zP').decode('ascii')
headers = {'Authorization': f'Basic {AUTH_B64}', 'Content-Type': 'application/json'}

with open('custom-css/global-dark-theme.css', 'r', encoding='utf-8') as f:
    lines = [l.strip() for l in f if l.strip() and not l.strip().startswith('/*') and not l.strip().startswith('*')]
minified = ' '.join(lines).replace('"', "'")

req = urllib.request.Request('https://axelaglobal.com/wp-json/wpvibe/v1/cli/run',
    data=json.dumps({'command': f'post update 40 --post_content="{minified}"'}).encode('utf-8'),
    headers=headers)
with urllib.request.urlopen(req) as resp:
    print('Post 40 updated:', json.loads(resp.read().decode('utf-8')))

req_elem = urllib.request.Request('https://axelaglobal.com/wp-json/wpvibe/v1/cli/run',
    data=json.dumps({'command': 'elementor flush-css --regenerate'}).encode('utf-8'),
    headers=headers)
with urllib.request.urlopen(req_elem) as resp:
    print('Elementor CSS flushed:', json.loads(resp.read().decode('utf-8')))

req_flush = urllib.request.Request('https://axelaglobal.com/wp-json/wpvibe/v1/cli/run',
    data=json.dumps({'command': 'litespeed-purge all'}).encode('utf-8'),
    headers=headers)
with urllib.request.urlopen(req_flush) as resp:
    print('Cache purged:', json.loads(resp.read().decode('utf-8')))
