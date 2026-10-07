import urllib.request
import json
import base64

BASE_URL = 'https://axelaglobal.com'
AUTH_STR = 'admin:FYCY 52pM wknI 1nOf 4RA2 t8zP'
AUTH_B64 = base64.b64encode(AUTH_STR.encode('ascii')).decode('ascii')
headers = {
    'Authorization': f'Basic {AUTH_B64}',
    'Content-Type': 'application/json'
}

def run_cli(cmd):
    p = json.dumps({'command': cmd}).encode('utf-8')
    r = urllib.request.Request(f'{BASE_URL}/wp-json/wpvibe/v1/cli/run', data=p, headers=headers)
    with urllib.request.urlopen(r) as resp:
        return json.loads(resp.read().decode('utf-8'))

# Fetch current Post 28 _elementor_data
res_p28 = run_cli("post meta get 28 _elementor_data")
p28_data = json.loads(res_p28.get('stdout', '[]'))

eyebrow_ids = [
    'hero_badge_hd',
    'abt_eye',
    'svc_eye',
    'prod_eye',
    'appr_eye',
    'net_eye',
    'inv_eye',
    'eth_eye',
    'cnt_eye'
]

gold_targets = [
    # Eyebrows
    'hero_badge_hd',
    'abt_eye',
    'svc_eye',
    'prod_eye',
    'appr_eye',
    'net_eye',
    'inv_eye',
    'eth_eye',
    'cnt_eye',
    # Stage Steps (STAGE 01, 02...)
    'hd_3e3cab92',
    'hd_2394fc5d',
    'hd_d88d1c73',
    'hd_3e8db5bf',
    'hd_bbaa9628',
    # Service Card Numbers (01, 02...)
    'hd_999ba21c',
    'hd_cb3fa1ca',
    'hd_995f5ac2',
    'hd_b221aae7',
    'hd_53654ea2',
    'hd_9008903c',
    'hd_2b3c2672',
    'hd_17317676',
    # Ethics Tags
    'hd_fe2aa103',
    'hd_9dea244f',
    'hd_01b6e2ae',
    # Contact Hub Tags
    'hd_0a65f143',
    'hd_6dd45a01',
    'hd_f620d1cf',
    'hd_c8f3c003',
    # Investment Tags
    'hd_99736023',
    'hd_cbcadf0f'
]

white_targets = [
    'hero_h1_hd',
    'abt_h2',
    'svc_h2',
    'prod_h2',
    'appr_h2',
    'net_h2',
    'inv_h2',
    'eth_h2',
    'cnt_h2',
    # Service titles
    'hd_9e249576',
    'hd_58bb49ce',
    'hd_cfc94693',
    'hd_d836872a',
    'hd_68d1b45b',
    'hd_5783ad10',
    'hd_6c3a0847',
    'hd_4da855ae',
    # Products titles
    'hd_3379b8d2',
    'hd_701c4cdc',
    'hd_f2da3198',
    'hd_eb1c0642',
    'hd_78c03e04',
    'hd_eebb5f0f',
    # Approach titles
    'hd_f657455d',
    'hd_359338f8',
    'hd_af7d4148',
    'hd_d83fbfef',
    'hd_35c27e2d',
    # Investment & Ethics titles
    'hd_24a55397',
    'hd_2d89d4fe',
    'hd_c9c52835',
    'hd_24df4f02'
]

gold_updated = 0
white_updated = 0

def update_colors(nodes):
    global gold_updated, white_updated
    for n in nodes:
        nid = n.get('id', '')
        st = n.setdefault('settings', {})
        if nid in gold_targets:
            st['title_color'] = '#D4AF37'
            st['typography_typography'] = 'custom'
            if nid in eyebrow_ids:
                st['typography_font_size'] = {'unit': 'px', 'size': 11.5, 'sizes': []}
                st['typography_font_weight'] = '700'
                st['typography_text_transform'] = 'uppercase'
                st['typography_letter_spacing'] = {'unit': 'px', 'size': 2.2, 'sizes': []}
            gold_updated += 1
            print(f"Applied native Gold (#D4AF37) to '{nid}': {st.get('title', '')[:25]}")
        elif nid in white_targets:
            st['title_color'] = '#FFFFFF'
            st['typography_typography'] = 'custom'
            white_updated += 1
            print(f"Applied native White (#FFFFFF) to '{nid}': {st.get('title', '')[:25]}")
        update_colors(n.get('elements', []))

update_colors(p28_data)
print(f"\nTotal Gold widgets updated: {gold_updated}/{len(gold_targets)}")
print(f"Total White widgets updated: {white_updated}/{len(white_targets)}")

# Save to Post 28 via WPVibe Elementor save-page API
page_payload = {
    "id": 28,
    "title": "AXELA LTD. — Trading • Supply • Advisory",
    "status": "publish",
    "page_template": "elementor_header_footer",
    "data": p28_data
}
r_save = urllib.request.Request(
    f'{BASE_URL}/wp-json/wpvibe/v1/elementor/save-page',
    data=json.dumps(page_payload).encode('utf-8'),
    headers=headers,
    method='POST'
)
with urllib.request.urlopen(r_save) as resp:
    res_save = json.loads(resp.read().decode('utf-8'))
    print("\nElementor save-page result:", res_save)
