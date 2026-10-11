import urllib.request
import json
import base64
import os

BASE_URL = 'https://axelaglobal.com'
AUTH_STR = 'admin:FYCY 52pM wknI 1nOf 4RA2 t8zP'
AUTH_B64 = base64.b64encode(AUTH_STR.encode('ascii')).decode('ascii')
headers = {'Authorization': f'Basic {AUTH_B64}', 'Content-Type': 'application/json'}

def run_cli(cmd):
    url = f'{BASE_URL}/wp-json/wpvibe/v1/cli/run'
    payload = json.dumps({'command': cmd}).encode('utf-8')
    req = urllib.request.Request(url, data=payload, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

def get_rest(endpoint):
    req = urllib.request.Request(f'{BASE_URL}/wp-json/{endpoint}', headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

out_dir = os.path.join(os.getcwd(), 'backups', 'final-production-release')
os.makedirs(out_dir, exist_ok=True)
os.makedirs('elementor-templates', exist_ok=True)
os.makedirs('fluentform-config', exist_ok=True)

print("=== 1. Exporting Live Elementor Posts & Meta ===")
for pid, name in [(28, 'homepage'), (29, 'header'), (38, 'footer')]:
    post_res = run_cli(f'post get {pid} --format=json')
    if post_res.get('exit_code') == 0:
        p_json = json.loads(post_res['stdout'])
        with open(os.path.join(out_dir, f'post-{pid}-{name}.json'), 'w', encoding='utf-8') as f:
            json.dump(p_json, f, indent=2, ensure_ascii=False)
        print(f"Exported post-{pid}-{name}.json")

    meta_res = run_cli(f'post meta get {pid} _elementor_data')
    if meta_res.get('exit_code') == 0:
        elem_data = json.loads(meta_res['stdout'])
        with open(os.path.join(out_dir, f'post-{pid}-elementor-data.json'), 'w', encoding='utf-8') as f:
            json.dump(elem_data, f, indent=2, ensure_ascii=False)
        with open(os.path.join('elementor-templates', f'{name}-template.json'), 'w', encoding='utf-8') as f:
            json.dump(elem_data, f, indent=2, ensure_ascii=False)
        print(f"Exported post-{pid}-elementor-data.json and {name}-template.json")

# Post 40 Customizer CSS
p40_res = run_cli('post get 40 --fields=ID,post_title,post_type,post_content --format=json')
if p40_res.get('exit_code') == 0:
    p40_json = json.loads(p40_res['stdout'])
    with open(os.path.join(out_dir, 'post-40-customizer-css.json'), 'w', encoding='utf-8') as f:
        json.dump(p40_json, f, indent=2, ensure_ascii=False)
    if 'post_content' in p40_json:
        with open(os.path.join('custom-css', 'global-dark-theme.css'), 'w', encoding='utf-8') as f:
            f.write(p40_json['post_content'])
    print("Exported post-40-customizer-css.json and refreshed global-dark-theme.css")

print("\n=== 2. Exporting Live Fluent Form 3 State ===")
f3_data = get_rest('fluentform/v1/forms/3')
f3_notifs = get_rest('fluentform/v1/settings/3?meta_key=notifications')
f3_settings = get_rest('fluentform/v1/settings/3?meta_key=formSettings')
f3_primary_email = get_rest('fluentform/v1/settings/3?meta_key=_primary_email_field')

f3_complete = {
    'form': f3_data,
    'notifications': f3_notifs,
    'formSettings': f3_settings,
    'primary_email_field': f3_primary_email
}

with open(os.path.join(out_dir, 'fluentform-3-complete-final.json'), 'w', encoding='utf-8') as f:
    json.dump(f3_complete, f, indent=2, ensure_ascii=False)
with open(os.path.join('fluentform-config', 'fluentform-3-complete-final.json'), 'w', encoding='utf-8') as f:
    json.dump(f3_complete, f, indent=2, ensure_ascii=False)
print("Exported fluentform-3-complete-final.json")

print("\n=== COMPLETE EXPORT FINISHED SUCCESSFULLY ===")
