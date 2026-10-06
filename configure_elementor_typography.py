import json
import base64
import urllib.request

BASE_URL = "https://axelaglobal.com"
AUTH_STR = "admin:FYCY 52pM wknI 1nOf 4RA2 t8zP"
AUTH_B64 = base64.b64encode(AUTH_STR.encode("ascii")).decode("ascii")
headers = {
    "Authorization": f"Basic {AUTH_B64}",
    "Content-Type": "application/json"
}

def run_wp_cli(cmd):
    url = f"{BASE_URL}/wp-json/wpvibe/v1/cli/run"
    payload = json.dumps({"command": cmd}).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"Error ({cmd}):", e)
        return None

def update_global_typography():
    print("Fetching active kit ID...")
    res_kit = run_wp_cli("option get elementor_active_kit")
    kit_id = int(res_kit.get("stdout", "7").strip())
    print(f"Active kit ID: {kit_id}")

    # Fetch current settings
    res_curr = run_wp_cli(f"post meta get {kit_id} _elementor_page_settings --format=json")
    try:
        settings = json.loads(res_curr.get("stdout", "{}"))
    except:
        settings = {}

    # Define exact typography settings according to Petrotraders / Word doc specification
    settings["system_colors"] = [
        {"_id": "primary", "title": "Primary", "color": "#DA423C"},
        {"_id": "secondary", "title": "Secondary", "color": "#D4AF37"},
        {"_id": "text", "title": "Text", "color": "#94A3B8"},
        {"_id": "accent", "title": "Accent", "color": "#D4AF37"}
    ]

    settings["system_typography"] = [
        {
            "_id": "primary",
            "title": "Primary",
            "typography_typography": "custom",
            "typography_font_family": "Cormorant Garamond",
            "typography_font_weight": "300"
        },
        {
            "_id": "secondary",
            "title": "Secondary",
            "typography_typography": "custom",
            "typography_font_family": "Inter",
            "typography_font_weight": "400",
            "typography_line_height": {"unit": "em", "size": 1.6, "sizes": []}
        },
        {
            "_id": "text",
            "title": "Text",
            "typography_typography": "custom",
            "typography_font_family": "Inter",
            "typography_font_weight": "400",
            "typography_color": "#94A3B8",
            "typography_line_height": {"unit": "em", "size": 1.6, "sizes": []}
        },
        {
            "_id": "accent",
            "title": "Accent",
            "typography_typography": "custom",
            "typography_font_family": "Inter",
            "typography_font_size": {"unit": "px", "size": 11.5, "sizes": []},
            "typography_font_weight": "600",
            "typography_text_transform": "uppercase",
            "typography_letter_spacing": {"unit": "px", "size": 1.8, "sizes": []}
        }
    ]

    # Site-wide Body & Headings in Kit
    settings["default_generic_fonts"] = "Sans-serif"
    settings["body_typography_typography"] = "custom"
    settings["body_typography_font_family"] = "Inter"
    settings["body_typography_font_weight"] = "400"
    settings["body_color"] = "#94A3B8"
    settings["body_typography_line_height"] = {"unit": "em", "size": 1.6, "sizes": []}

    settings["h1_typography_typography"] = "custom"
    settings["h1_typography_font_family"] = "Cormorant Garamond"
    settings["h1_typography_font_weight"] = "300"
    settings["h1_color"] = "#FFFFFF"

    settings["h2_typography_typography"] = "custom"
    settings["h2_typography_font_family"] = "Cormorant Garamond"
    settings["h2_typography_font_weight"] = "300"
    settings["h2_color"] = "#FFFFFF"

    settings["h3_typography_typography"] = "custom"
    settings["h3_typography_font_family"] = "Cormorant Garamond"
    settings["h3_typography_font_weight"] = "400"
    settings["h3_color"] = "#FFFFFF"

    settings["h4_typography_typography"] = "custom"
    settings["h4_typography_font_family"] = "Cormorant Garamond"
    settings["h4_typography_font_weight"] = "400"
    settings["h4_color"] = "#FFFFFF"

    settings["h5_typography_typography"] = "custom"
    settings["h5_typography_font_family"] = "Cormorant Garamond"
    settings["h5_typography_font_weight"] = "400"
    settings["h5_color"] = "#FFFFFF"

    settings["h6_typography_typography"] = "custom"
    settings["h6_typography_font_family"] = "Cormorant Garamond"
    settings["h6_typography_font_weight"] = "400"
    settings["h6_color"] = "#FFFFFF"

    json_str = json.dumps(settings)
    print(f"Updating Kit {kit_id} _elementor_page_settings...")
    res_update = run_wp_cli(f"post meta update {kit_id} _elementor_page_settings '{json_str}' --force")
    print("Update result:", res_update)

    print("\nVerifying updated Kit meta...")
    res_verify = run_wp_cli(f"post meta get {kit_id} _elementor_page_settings --format=json")
    v_data = json.loads(res_verify.get("stdout", "{}"))
    print("Primary font family:", [t for t in v_data.get("system_typography", []) if t["_id"] == "primary"])
    print("Body font family:", v_data.get("body_typography_font_family"))

    print("\nFlushing Elementor CSS cache & regenerating...")
    res_flush = run_wp_cli("elementor flush-css --regenerate")
    print("Flush result:", res_flush)

if __name__ == "__main__":
    update_global_typography()
