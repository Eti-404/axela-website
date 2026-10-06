import urllib.request
import json
import base64

BASE_URL = 'https://axelaglobal.com'
AUTH_STR = 'admin:FYCY 52pM wknI 1nOf 4RA2 t8zP'
AUTH_B64 = base64.b64encode(AUTH_STR.encode('ascii')).decode('ascii')
headers = {'Authorization': f'Basic {AUTH_B64}', 'Content-Type': 'application/json'}

def run_cli(cmd):
    p = json.dumps({'command': cmd, 'confirm_write': True}).encode('utf-8')
    r = urllib.request.Request(f'{BASE_URL}/wp-json/wpvibe/v1/cli/run', data=p, headers=headers)
    try:
        with urllib.request.urlopen(r) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("HTTP ERROR:", e.code, e.read().decode('utf-8', errors='ignore'))
        raise


notification_config = {
    "name": "AXELA Admin Notification Email",
    "sendTo": {
        "type": "email",
        "email": "info@axelaglobal.com, anikaeti404@gmail.com",
        "field": "email_phone",
        "routing": [
            {
                "email": None,
                "field": None,
                "operator": "=",
                "value": None
            }
        ]
    },
    "fromName": "AXELA Trade Portal",
    "fromEmail": "info@axelaglobal.com",
    "replyTo": "{inputs.email_phone}",
    "bcc": "",
    "subject": "New Trade & Project Enquiry - AXELA LTD. [{inputs.full_name}]",
    "message": "<h3>New Trade & Project Enquiry Received</h3><p>A new trade enquiry has been submitted on AXELA LTD. portal:</p><hr />{all_data}<hr /><p style=\"font-size: 12px; color: #888;\">Submitted at: {embed_post.permalink} | Timestamp: {date_time}</p>",
    "conditionals": {
        "status": False,
        "type": "all",
        "conditions": [
            {
                "field": None,
                "operator": "=",
                "value": None
            }
        ]
    },
    "enabled": True,
    "email_template": ""
}

notif_json = json.dumps(notification_config)

# Check if row exists for form 3
check_res = run_cli("db query \"SELECT id FROM wp_fluentform_form_meta WHERE form_id=3 AND meta_key='notifications'\" --format=json")
print("Check res:", check_res.get('stdout'))

# Use FROM_BASE64 to insert safely without quote issues
b64_val = base64.b64encode(notif_json.encode('utf-8')).decode('ascii')
sql = f"INSERT INTO wp_fluentform_form_meta (form_id, meta_key, value) VALUES (3, 'notifications', FROM_BASE64('{b64_val}'))"
insert_res = run_cli(f"db query \"{sql}\"")
print("Insert result:", insert_res)

# Verify
verify_res = run_cli("db query \"SELECT form_id, meta_key, value FROM wp_fluentform_form_meta WHERE form_id=3 AND meta_key='notifications'\" --format=json")
print("Verification:", verify_res.get('stdout'))

