import urllib.request
import json
import base64

BASE_URL = 'https://axelaglobal.com'
AUTH_STR = 'admin:FYCY 52pM wknI 1nOf 4RA2 t8zP'
AUTH_B64 = base64.b64encode(AUTH_STR.encode('ascii')).decode('ascii')
headers = {'Authorization': f'Basic {AUTH_B64}', 'Content-Type': 'application/json'}

def make_text_field(index, name, label, placeholder, required=False, container_class='ff-col-6'):
    return {
        "index": index,
        "element": "input_text",
        "attributes": {
            "type": "text",
            "name": name,
            "value": "",
            "id": f"ff_{name}",
            "class": "axela-ff-input",
            "placeholder": placeholder
        },
        "settings": {
            "container_class": container_class,
            "label": label,
            "label_placement": "top",
            "admin_field_label": label,
            "help_message": "",
            "validation_rules": {
                "required": {
                    "value": required,
                    "message": f"{label} is required"
                }
            },
            "conditional_logics": []
        },
        "editor_options": {
            "title": label,
            "template": "inputText"
        },
        "uniqElKey": f"el_{name}"
    }

def make_select_field(index, name, label, options, required=False, container_class='ff-col-6'):
    formatted_options = [{"label": opt, "value": opt, "calc_value": ""} for opt in options]
    return {
        "index": index,
        "element": "select",
        "attributes": {
            "name": name,
            "value": "",
            "id": f"ff_{name}",
            "class": "axela-ff-select"
        },
        "settings": {
            "container_class": container_class,
            "label": label,
            "label_placement": "top",
            "admin_field_label": label,
            "placeholder": "Select an enquiry type",
            "advanced_options": formatted_options,
            "options": {opt: opt for opt in options},
            "validation_rules": {
                "required": {
                    "value": required,
                    "message": f"{label} is required"
                }
            },
            "conditional_logics": []
        },
        "editor_options": {
            "title": label,
            "template": "select"
        },
        "uniqElKey": f"el_{name}"
    }

def make_textarea_field(index, name, label, placeholder, rows=3, required=False, container_class='ff-col-12'):
    return {
        "index": index,
        "element": "textarea",
        "attributes": {
            "name": name,
            "value": "",
            "id": f"ff_{name}",
            "class": "axela-ff-textarea",
            "placeholder": placeholder,
            "rows": rows,
            "cols": 2
        },
        "settings": {
            "container_class": container_class,
            "label": label,
            "admin_field_label": label,
            "label_placement": "top",
            "help_message": "",
            "validation_rules": {
                "required": {
                    "value": required,
                    "message": f"{label} is required"
                }
            },
            "conditional_logics": []
        },
        "editor_options": {
            "title": label,
            "template": "inputTextarea"
        },
        "uniqElKey": f"el_{name}"
    }

# Build all 12 fields exactly as requested
fields = [
    make_text_field(0, "full_name", "Full Name", "e.g. Johnathan Doe", required=True, container_class='ff-col-6'),
    make_text_field(1, "company", "Company / Organisation", "e.g. PetroGlobal Trading LLC", required=True, container_class='ff-col-6'),
    make_text_field(2, "email_phone", "Business Email & Phone / WhatsApp", "e.g. desk@company.com / +88 017...", required=True, container_class='ff-col-6'),
    make_text_field(3, "country", "Country of Operation", "e.g. Bangladesh / Singapore / UAE", required=True, container_class='ff-col-6'),
    make_select_field(4, "enquiry_type", "Enquiry Type", ["Product Supply", "Tender", "Brokerage", "Investment", "Advisory", "Other"], required=True, container_class='ff-col-6'),
    make_text_field(5, "product_project", "Product or Project of Interest", "e.g. Gasoil 50ppm / Prilled Urea / Energy Project", required=True, container_class='ff-col-6'),
    make_text_field(6, "quantity_size", "Required Quantity or Estimated Project Size", "e.g. 50,000 MT / USD 10M", required=False, container_class='ff-col-6'),
    make_text_field(7, "destination", "Destination / Location", "e.g. Chattogram Port / Matarbari / Mongla", required=False, container_class='ff-col-6'),
    make_text_field(8, "incoterm", "Preferred Delivery Term (Incoterm)", "e.g. CIF Chattogram / CFR / FOB", required=False, container_class='ff-col-6'),
    make_text_field(9, "delivery_timeline", "Target Delivery Date or Project Timeline", "e.g. Q4 2026 / Prompt Delivery", required=False, container_class='ff-col-6'),
    make_textarea_field(10, "specs_summary", "Required Specifications or Project Summary", "Detail specific grades, quality parameters, origin preferences, or scope summary...", rows=3, required=False, container_class='ff-col-12'),
    make_textarea_field(11, "supporting_docs", "Message & Supporting Documents (Spec Sheet / LOI / RFQ or Additional Context)", "Detail document links, cloud share URLs, or full RFQ notes here...", rows=3, required=False, container_class='ff-col-12')
]

submit_button = {
    "uniqElKey": "el_submit_trade_enquiry",
    "element": "button",
    "attributes": {
        "type": "submit",
        "class": "axela-ff-submit axela-btn-red"
    },
    "settings": {
        "align": "left",
        "button_style": "default",
        "container_class": "ff-col-12",
        "help_message": "",
        "background_color": "#DA423C",
        "button_size": "md",
        "color": "#ffffff",
        "button_ui": {
            "type": "default",
            "text": "SUBMIT TRADE ENQUIRY",
            "img_url": ""
        }
    },
    "editor_options": {
        "title": "Submit Button"
    }
}

form_fields_obj = {
    "fields": fields,
    "submitButton": submit_button
}

form_payload = {
    "title": "AXELA Trade & Project Enquiry Form",
    "status": "published",
    "formFields": json.dumps(form_fields_obj)
}

if __name__ == '__main__':
    # Update Form 3
    url = f"{BASE_URL}/wp-json/fluentform/v1/forms/3"
    req = urllib.request.Request(url, data=json.dumps(form_payload).encode('utf-8'), headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req) as resp:
            print("Update Form 3 Result:", resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("HTTP Error:", e.code, e.read().decode('utf-8', errors='ignore'))
