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
# 1. Ultra-Clean, Bulletproof Customer Auto-Responder Email Template
# ------------------------------------------------------------------------------
# Standard email-safe fonts (Arial, Helvetica, sans-serif), NO weird unicode symbols or web fonts.
client_email_body = """<div style="font-family: Arial, Helvetica, sans-serif; max-width: 620px; margin: 0 auto; background-color: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden;">
  <div style="background-color: #060B13; padding: 24px 30px; border-bottom: 3px solid #FF3131;">
    <h2 style="color: #ffffff; margin: 0; font-size: 22px; font-family: Arial, Helvetica, sans-serif; font-weight: bold; letter-spacing: 0.5px;">AXELA LIMITED</h2>
    <div style="color: #94A3B8; margin: 6px 0 0 0; font-size: 11px; font-family: Arial, Helvetica, sans-serif;">Energy | Commodities | Trading | Supply | Project Development | Investment Advisory</div>
  </div>
  
  <div style="padding: 28px 30px; background-color: #ffffff; font-family: Arial, Helvetica, sans-serif;">
    <h3 style="color: #0f172a; margin-top: 0; font-size: 16px; font-family: Arial, Helvetica, sans-serif;">Dear {inputs.full_name},</h3>
    <p style="color: #334155; line-height: 1.6; font-size: 14px; margin: 0 0 14px 0;">Thank you for submitting your trade &amp; commercial enquiry to <strong>AXELA Limited</strong>.</p>
    <p style="color: #334155; line-height: 1.6; font-size: 14px; margin: 0 0 20px 0;">This message confirms that your submission has been successfully received by our commercial desk and operations team. We are currently reviewing your specifications and requirement details.</p>
    
    <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 18px 20px; margin: 20px 0;">
      <h4 style="margin: 0 0 12px 0; color: #0f172a; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; border-bottom: 1px solid #e2e8f0; padding-bottom: 8px; font-family: Arial, Helvetica, sans-serif;">Summary of Your Submission</h4>
      <table style="width: 100%; border-collapse: collapse; font-size: 13px; font-family: Arial, Helvetica, sans-serif;">
        <tr>
          <td style="padding: 6px 0; color: #64748B; width: 40%; border-bottom: 1px solid #f1f5f9;"><strong>Full Name:</strong></td>
          <td style="padding: 6px 0; color: #0f172a; border-bottom: 1px solid #f1f5f9;">{inputs.full_name}</td>
        </tr>
        <tr>
          <td style="padding: 6px 0; color: #64748B; border-bottom: 1px solid #f1f5f9;"><strong>Company / Organisation:</strong></td>
          <td style="padding: 6px 0; color: #0f172a; border-bottom: 1px solid #f1f5f9;">{inputs.company}</td>
        </tr>
        <tr>
          <td style="padding: 6px 0; color: #64748B; border-bottom: 1px solid #f1f5f9;"><strong>Business Email:</strong></td>
          <td style="padding: 6px 0; color: #0f172a; border-bottom: 1px solid #f1f5f9;">{inputs.email}</td>
        </tr>
        <tr>
          <td style="padding: 6px 0; color: #64748B; border-bottom: 1px solid #f1f5f9;"><strong>Phone / WhatsApp:</strong></td>
          <td style="padding: 6px 0; color: #0f172a; border-bottom: 1px solid #f1f5f9;">{inputs.phone_whatsapp}</td>
        </tr>
        <tr>
          <td style="padding: 6px 0; color: #64748B; border-bottom: 1px solid #f1f5f9;"><strong>Country of Operation:</strong></td>
          <td style="padding: 6px 0; color: #0f172a; border-bottom: 1px solid #f1f5f9;">{inputs.country}</td>
        </tr>
        <tr>
          <td style="padding: 6px 0; color: #64748B; border-bottom: 1px solid #f1f5f9;"><strong>Enquiry Type:</strong></td>
          <td style="padding: 6px 0; color: #0f172a; border-bottom: 1px solid #f1f5f9;">{inputs.enquiry_type}</td>
        </tr>
        <tr>
          <td style="padding: 6px 0; color: #64748B; border-bottom: 1px solid #f1f5f9;"><strong>Product / Project of Interest:</strong></td>
          <td style="padding: 6px 0; color: #0f172a; border-bottom: 1px solid #f1f5f9;">{inputs.product_project}</td>
        </tr>
        <tr>
          <td style="padding: 6px 0; color: #64748B; border-bottom: 1px solid #f1f5f9;"><strong>Required Quantity / Size:</strong></td>
          <td style="padding: 6px 0; color: #0f172a; border-bottom: 1px solid #f1f5f9;">{inputs.quantity_size}</td>
        </tr>
        <tr>
          <td style="padding: 6px 0; color: #64748B; border-bottom: 1px solid #f1f5f9;"><strong>Destination / Location:</strong></td>
          <td style="padding: 6px 0; color: #0f172a; border-bottom: 1px solid #f1f5f9;">{inputs.destination}</td>
        </tr>
        <tr>
          <td style="padding: 6px 0; color: #64748B; border-bottom: 1px solid #f1f5f9;"><strong>Preferred Delivery Term:</strong></td>
          <td style="padding: 6px 0; color: #0f172a; border-bottom: 1px solid #f1f5f9;">{inputs.incoterm}</td>
        </tr>
        <tr>
          <td style="padding: 6px 0; color: #64748B;"><strong>Delivery Date / Timeline:</strong></td>
          <td style="padding: 6px 0; color: #0f172a;">{inputs.delivery_timeline}</td>
        </tr>
      </table>
    </div>

    <p style="color: #334155; line-height: 1.6; font-size: 14px;">A member of our commercial desk will contact you promptly to discuss terms, allocation, or execution feasibility.</p>
    
    <p style="color: #334155; line-height: 1.6; font-size: 14px; margin-top: 24px;">Sincerely,<br />
    <strong>Commercial &amp; Trading Desk</strong><br />
    AXELA Limited<br />
    <a href="https://axelaglobal.com" style="color: #FF3131; text-decoration: none;">www.axelaglobal.com</a></p>
  </div>
  
  <div style="background-color: #f1f5f9; padding: 16px 30px; font-size: 11px; color: #64748B; text-align: center; border-top: 1px solid #e2e8f0; font-family: Arial, Helvetica, sans-serif;">
    &copy; 2026 AXELA LTD. All rights reserved. | Automated confirmation sent to {inputs.email}
  </div>
</div>"""

client_notification = {
    "name": "AXELA Client Confirmation & Auto-Responder",
    "sendTo": {
        "type": "field",
        "field": "email",
        "email": "{inputs.email}",
        "routing": [{"email": None, "field": None, "operator": "=", "value": None}]
    },
    "fromName": "AXELA Limited",
    "fromEmail": "info@axelaglobal.com",
    "replyTo": "info@axelaglobal.com",
    "bcc": "",
    "subject": "Trade & Project Enquiry Confirmation - AXELA Limited",
    "message": client_email_body,
    "conditionals": {
        "status": False,
        "type": "all",
        "conditions": [{"field": None, "operator": "=", "value": None}]
    },
    "enabled": True,
    "email_template": "",
    "pdf_attachments": []
}

print("Saving updated Client Notification (Meta 37)...")
res_m37 = post_setting({
    "meta_id": 37,
    "meta_key": "notifications",
    "value": json.dumps(client_notification)
})
print("Meta 37 updated:", res_m37)

# ------------------------------------------------------------------------------
# 2. Update Admin Notification (Meta 20)
# ------------------------------------------------------------------------------
admin_email_body = """<p>A new trade enquiry has been submitted on the AXELA LTD. portal:</p>
<hr />
<table style="width: 100%; border-collapse: collapse; font-size: 13px; font-family: Arial, sans-serif;">
  <tr><td style="padding: 4px 0; width: 35%;"><strong>Full Name:</strong></td><td>{inputs.full_name}</td></tr>
  <tr><td style="padding: 4px 0;"><strong>Company:</strong></td><td>{inputs.company}</td></tr>
  <tr><td style="padding: 4px 0;"><strong>Business Email:</strong></td><td>{inputs.email}</td></tr>
  <tr><td style="padding: 4px 0;"><strong>Phone / WhatsApp:</strong></td><td>{inputs.phone_whatsapp}</td></tr>
  <tr><td style="padding: 4px 0;"><strong>Country:</strong></td><td>{inputs.country}</td></tr>
  <tr><td style="padding: 4px 0;"><strong>Enquiry Type:</strong></td><td>{inputs.enquiry_type}</td></tr>
  <tr><td style="padding: 4px 0;"><strong>Product / Project:</strong></td><td>{inputs.product_project}</td></tr>
  <tr><td style="padding: 4px 0;"><strong>Quantity / Size:</strong></td><td>{inputs.quantity_size}</td></tr>
  <tr><td style="padding: 4px 0;"><strong>Destination:</strong></td><td>{inputs.destination}</td></tr>
  <tr><td style="padding: 4px 0;"><strong>Incoterm:</strong></td><td>{inputs.incoterm}</td></tr>
  <tr><td style="padding: 4px 0;"><strong>Delivery Timeline:</strong></td><td>{inputs.delivery_timeline}</td></tr>
  <tr><td style="padding: 4px 0;"><strong>Specs / Notes:</strong></td><td>{inputs.specs_summary}</td></tr>
</table>
<hr />
<p style="font-size: 12px; color: #64748B;">Submitted from: {embed_post.permalink}</p>"""

admin_notification = {
    "name": "AXELA Admin Notification Email",
    "sendTo": {
        "type": "email",
        "email": "info@axelaglobal.com,anikaeti404@gmail.com",
        "field": "email",
        "routing": [{"email": None, "field": None, "operator": "=", "value": None}]
    },
    "fromName": "AXELA Trade Portal",
    "fromEmail": "info@axelaglobal.com",
    "replyTo": "{inputs.email}",
    "bcc": "",
    "subject": "New Trade & Project Enquiry - AXELA LTD. [{inputs.full_name}]",
    "message": admin_email_body,
    "conditionals": {
        "status": False,
        "type": "all",
        "conditions": [{"field": None, "operator": "=", "value": None}]
    },
    "enabled": True,
    "email_template": "",
    "pdf_attachments": []
}

print("Saving updated Admin Notification (Meta 20)...")
res_m20 = post_setting({
    "meta_id": 20,
    "meta_key": "notifications",
    "value": json.dumps(admin_notification)
})
print("Meta 20 updated:", res_m20)
print("\nAll templates successfully refreshed and cleaned!")
