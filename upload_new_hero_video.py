import urllib.request
import base64
import json
import os

BASE_URL = 'https://axelaglobal.com'
AUTH_STR = 'admin:FYCY 52pM wknI 1nOf 4RA2 t8zP'
AUTH_B64 = base64.b64encode(AUTH_STR.encode('ascii')).decode('ascii')

def upload_file(file_path, filename, mime_type):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None
    print(f"Reading {file_path} ({os.path.getsize(file_path)} bytes)...")
    with open(file_path, 'rb') as f:
        file_data = f.read()

    headers = {
        'Authorization': f'Basic {AUTH_B64}',
        'Content-Disposition': f'attachment; filename="{filename}"',
        'Content-Type': mime_type
    }
    req = urllib.request.Request(f'{BASE_URL}/wp-json/wp/v2/media', data=file_data, headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"UPLOAD_SUCCESS: ID={data.get('id')}, URL={data.get('source_url')}")
            return data
    except urllib.error.HTTPError as e:
        print(f"UPLOAD_ERROR: HTTP {e.code}: {e.read().decode('utf-8', errors='ignore')}")
        return None
    except Exception as ex:
        print(f"EXCEPTION: {ex}")
        return None

if __name__ == '__main__':
    poster_path = r'c:\xampp\htdocs\axela-local\wp-content\uploads\2026\10\lv_0_20261006163733_poster.jpg'
    video_path = r'c:\xampp\htdocs\axela-local\wp-content\uploads\2026\10\lv_0_20261006163733.mp4'

    print("--- 1. Uploading Hero Poster Fallback ---")
    p = upload_file(poster_path, 'axela-hero-poster-20261006.jpg', 'image/jpeg')

    print("\n--- 2. Uploading Hero Video (lv_0_20261006163733.mp4) ---")
    v = upload_file(video_path, 'lv_0_20261006163733.mp4', 'video/mp4')
