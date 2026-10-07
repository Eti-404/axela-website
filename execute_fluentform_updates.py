import urllib.request
import json
import base64
import sys

BASE_URL = 'https://axelaglobal.com'
AUTH_STR = 'admin:FYCY 52pM wknI 1nOf 4RA2 t8zP'
AUTH_B64 = base64.b64encode(AUTH_STR.encode('ascii')).decode('ascii')
headers = {
    'Authorization': f'Basic {AUTH_B64}',
    'Content-Type': 'application/json'
}

def post_form(payload):
    req = urllib.request.Request(
        f'{BASE_URL}/wp-json/fluentform/v1/forms/3',
        data=json.dumps(payload).encode('utf-8'),
        headers=headers,
        method='POST'
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

def post_setting(payload):
    req = urllib.request.Request(
        f'{BASE_URL}/wp-json/fluentform/v1/settings/3',
        data=json.dumps(payload).encode('utf-8'),
        headers=headers,
        method='POST'
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

# ------------------------------------------------------------------------------
# 1. Fetch current form 3
# ------------------------------------------------------------------------------
print("\n--- 1. Fetching current Form 3 ---")
req = urllib.request.Request(f'{BASE_URL}/wp-json/fluentform/v1/forms/3', headers=headers)
with urllib.request.urlopen(req) as resp:
    form_res = json.loads(resp.read().decode('utf-8'))

title = form_res.get('title')
status = form_res.get('status')
form_fields_raw = form_res.get('form_fields')
form_fields_obj = json.loads(form_fields_raw)

# ------------------------------------------------------------------------------
# 2. Build updated fields list (separating email and phone_whatsapp)
# ------------------------------------------------------------------------------
print("--- 2. Building updated fields structure ---")
old_fields = form_fields_obj.get('fields', [])
new_fields = []

for f in old_fields:
    fname = f.get('attributes', {}).get('name')
    if fname == 'email_phone':
        # 1. Dedicated Email field
        email_f = {
            "element": "input_email",
            "attributes": {
                "type": "email",
                "name": "email",
                "value": "",
                "id": "ff_email",
                "class": "axela-ff-input",
                "placeholder": "e.g. corporate.desk@company.com"
            },
            "settings": {
                "container_class": "ff-col-6",
                "label": "Business Email Address",
                "label_placement": "top",
                "admin_field_label": "Business Email Address",
                "help_message": "",
                "validation_rules": {
                    "required": {
                        "value": True,
                        "message": "Business Email Address is required"
                    },
                    "email": {
                        "value": True,
                        "message": "This field must contain a valid email address"
                    }
                },
                "conditional_logics": []
            },
            "editor_options": {
                "title": "Business Email Address",
                "template": "inputEmail"
            },
            "uniqElKey": "el_email"
        }
        
        # 2. Dedicated Phone / WhatsApp field
        phone_f = {
            "element": "input_text",
            "attributes": {
                "type": "text",
                "name": "phone_whatsapp",
                "value": "",
                "id": "ff_phone_whatsapp",
                "class": "axela-ff-input",
                "placeholder": "e.g. +880 1712-345678 (Optional)"
            },
            "settings": {
                "container_class": "ff-col-6",
                "label": "Phone / WhatsApp (Optional)",
                "label_placement": "top",
                "admin_field_label": "Phone / WhatsApp (Optional)",
                "help_message": "",
                "validation_rules": {
                    "required": {
                        "value": False,
                        "message": ""
                    }
                },
                "conditional_logics": []
            },
            "editor_options": {
                "title": "Phone / WhatsApp (Optional)",
                "template": "inputText"
            },
            "uniqElKey": "el_phone_whatsapp"
        }
        new_fields.append(email_f)
        new_fields.append(phone_f)
    elif fname == 'delivery_timeline':
        # Clean col-12 for delivery_timeline before full-width textareas
        f_copy = dict(f)
        f_copy.setdefault('settings', {})['container_class'] = 'ff-col-12'
        new_fields.append(f_copy)
    else:
        new_fields.append(f)

# Re-index fields
for idx, f in enumerate(new_fields):
    f['index'] = idx

form_fields_obj['fields'] = new_fields
updated_fields_json = json.dumps(form_fields_obj)

# Save updated form fields
res_form_save = post_form({
    'title': title,
    'status': status,
    'formFields': updated_fields_json
})
print("Form Save Response:", res_form_save)

# ------------------------------------------------------------------------------
# 3. Update Meta ID 23 (_primary_email_field)
# ------------------------------------------------------------------------------
print("\n--- 3. Updating Meta ID 23 (_primary_email_field) ---")
res_m23 = post_setting({
    "meta_id": 23,
    "meta_key": "_primary_email_field",
    "value": "email"
})
print("Meta 23 update response:", res_m23)

# ------------------------------------------------------------------------------
# 4. Update Meta ID 36 (formSettings - Instant Reset on Same Page)
# ------------------------------------------------------------------------------
print("\n--- 4. Updating Meta ID 36 (formSettings) ---")
general_settings = {
    "confirmation": {
        "redirectTo": "samePage",
        "messageToShow": "Thank you for your enquiry. The AXELA LTD. commercial & operations desk has received your request and will review and respond promptly.",
        "customPage": None,
        "samePageFormBehavior": "reset_form",
        "customUrl": None
    },
    "restrictions": {
        "limitNumberOfEntries": {"enabled": False, "numberOfEntries": None, "period": "total", "limitReachedMsg": "Maximum number of entries exceeded."},
        "scheduleForm": {"enabled": False, "start": None, "end": None, "selectedDays": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "pendingMsg": "Form submission is not started yet.", "expiredMsg": "Form submission is now closed."},
        "requireLogin": {"enabled": False, "requireLoginMsg": "You must be logged in to submit the form."},
        "denyEmptySubmission": {"enabled": False, "message": "Sorry, you cannot submit an empty form. Let's hear what you wanna say."}
    },
    "layout": {
        "labelPlacement": "top",
        "helpMessagePlacement": "with_label",
        "errorMessagePlacement": "inline",
        "cssClassName": "axela-fluent-form-wrap",
        "asteriskPlacement": "asterisk-right"
    },
    "delete_entry_on_submission": "no",
    "appendSurveyResult": {"enabled": False, "showLabel": False, "showCount": False}
}
res_m36 = post_setting({
    "meta_id": 36,
    "meta_key": "formSettings",
    "value": json.dumps(general_settings)
})
print("Meta 36 update response:", res_m36)

# ------------------------------------------------------------------------------
# 5. Update Meta ID 37 (Customer Auto-Responder Confirmation Email)
# ------------------------------------------------------------------------------
print("\n--- 5. Updating Meta ID 37 (Customer Auto-Responder) ---")
client_email_body = """<div style="font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #1e293b; max-width: 650px; margin: 0 auto; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden;">
  <div style="background-color: #060B13; padding: 24px 30px; border-bottom: 2px solid #FF3131;">
    <h2 style="color: #ffffff; margin: 0; font-size: 20px; letter-spacing: 0.05em;">AXELA LIMITED</h2>
    <p style="color: #94A3B8; margin: 6px 0 0 0; font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em;">Energy &bull; Commodities &bull; Trading &bull; Supply &bull; Project Development &bull; Investment Advisory</p>
  </div>
  
  <div style="padding: 30px; background-color: #ffffff;">
    <h3 style="color: #0f172a; margin-top: 0; font-size: 16px;">Dear {inputs.full_name},</h3>
    <p>Thank you for submitting your trade &amp; commercial enquiry to <strong>AXELA Limited</strong>.</p>
    <p>This message confirms that your submission has been successfully received by our commercial desk and operations team. We are currently reviewing your specifications and requirement details.</p>
    
    <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 18px 20px; margin: 24px 0;">
      <h4 style="margin: 0 0 12px 0; color: #0f172a; font-size: 13px; text-transform: uppercase; letter-spacing: 0.05em; border-bottom: 1px solid #e2e8f0; padding-bottom: 8px;">Summary of Your Submission</h4>
      <table style="width: 100%; border-collapse: collapse; font-size: 13px;">
        <tr>
          <td style="padding: 5px 0; color: #64748B; width: 40%;"><strong>Full Name:</strong></td>
          <td style="padding: 5px 0; color: #0f172a;">{inputs.full_name}</td>
        </tr>
        <tr>
          <td style="padding: 5px 0; color: #64748B;"><strong>Company / Organisation:</strong></td>
          <td style="padding: 5px 0; color: #0f172a;">{inputs.company}</td>
        </tr>
        <tr>
          <td style="padding: 5px 0; color: #64748B;"><strong>Business Email:</strong></td>
          <td style="padding: 5px 0; color: #0f172a;">{inputs.email}</td>
        </tr>
        <tr>
          <td style="padding: 5px 0; color: #64748B;"><strong>Phone / WhatsApp:</strong></td>
          <td style="padding: 5px 0; color: #0f172a;">{inputs.phone_whatsapp}</td>
        </tr>
        <tr>
          <td style="padding: 5px 0; color: #64748B;"><strong>Country of Operation:</strong></td>
          <td style="padding: 5px 0; color: #0f172a;">{inputs.country}</td>
        </tr>
        <tr>
          <td style="padding: 5px 0; color: #64748B;"><strong>Enquiry Type:</strong></td>
          <td style="padding: 5px 0; color: #0f172a;">{inputs.enquiry_type}</td>
        </tr>
        <tr>
          <td style="padding: 5px 0; color: #64748B;"><strong>Product / Project of Interest:</strong></td>
          <td style="padding: 5px 0; color: #0f172a;">{inputs.product_project}</td>
        </tr>
        <tr>
          <td style="padding: 5px 0; color: #64748B;"><strong>Required Quantity / Size:</strong></td>
          <td style="padding: 5px 0; color: #0f172a;">{inputs.quantity_size}</td>
        </tr>
        <tr>
          <td style="padding: 5px 0; color: #64748B;"><strong>Destination / Location:</strong></td>
          <td style="padding: 5px 0; color: #0f172a;">{inputs.destination}</td>
        </tr>
        <tr>
          <td style="padding: 5px 0; color: #64748B;"><strong>Preferred Delivery Term (Incoterm):</strong></td>
          <td style="padding: 5px 0; color: #0f172a;">{inputs.incoterm}</td>
        </tr>
        <tr>
          <td style="padding: 5px 0; color: #64748B;"><strong>Delivery Date / Timeline:</strong></td>
          <td style="padding: 5px 0; color: #0f172a;">{inputs.delivery_timeline}</td>
        </tr>
      </table>
    </div>

    <p>A member of our commercial desk will contact you promptly to discuss terms, allocation, or execution feasibility.</p>
    
    <p style="margin-top: 24px;">Sincerely,<br />
    <strong>Commercial &amp; Trading Desk</strong><br />
    AXELA Limited<br />
    <a href="https://axelaglobal.com" style="color: #FF3131; text-decoration: none;">www.axelaglobal.com</a></p>
  </div>
  
  <div style="background-color: #f1f5f9; padding: 16px 30px; font-size: 11px; color: #64748B; text-align: center; border-top: 1px solid #e2e8f0;">
    &copy; 2026 AXELA LTD. All rights reserved. | Automated confirmation sent to {inputs.email}
  </div>
</div>"""

client_notification = {
    "name": "AXELA Client Confirmation & Auto-Responder",
    "sendTo": {
        "type": "field",
        "field": "email",
        "email": "{inputs.email}",
        "routing": [
            {
                "email": None,
                "field": None,
                "operator": "=",
                "value": None
            }
        ]
    },
    "fromName": "AXELA Limited",
    "fromEmail": "info@axelaglobal.com",
    "replyTo": "info@axelaglobal.com",
    "bcc": "",
    "subject": "Trade & Project Enquiry Confirmation — AXELA Limited",
    "message": client_email_body,
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
    "email_template": "",
    "pdf_attachments": []
}

res_m37 = post_setting({
    "meta_id": 37,
    "meta_key": "notifications",
    "value": json.dumps(client_notification)
})
print("Meta 37 update response:", res_m37)

# ------------------------------------------------------------------------------
# 6. Update Meta ID 20 (Admin Notification Email)
# ------------------------------------------------------------------------------
print("\n--- 6. Updating Meta ID 20 (Admin Notification) ---")
admin_notification = {
    "name": "AXELA Admin Notification Email",
    "sendTo": {
        "type": "email",
        "email": "info@axelaglobal.com, anikaeti404@gmail.com",
        "field": "email",
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
    "replyTo": "{inputs.email}",
    "bcc": "",
    "subject": "New Trade & Project Enquiry - AXELA LTD. [{inputs.full_name}]",
    "message": "<p>A new trade enquiry has been submitted on AXELA LTD. portal:</p><hr />{all_data}<hr /><p>Submitted at: {embed_post.permalink}</p>",
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
    "email_template": "",
    "pdf_attachments": []
}

res_m20 = post_setting({
    "meta_id": 20,
    "meta_key": "notifications",
    "value": json.dumps(admin_notification)
})
print("Meta 20 update response:", res_m20)

print("\n=== FLUENT FORMS FORM 3 CONFIGURATION COMPLETED SUCCESSFULLY ===")
