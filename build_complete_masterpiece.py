import json
import base64
import urllib.request
import uuid

def uid(prefix='ax'):
    return f"{prefix}_{uuid.uuid4().hex[:8]}"

def native_heading(title, tag='h2', custom_css_class='', size='default', align='left', eid=None):
    settings = {
        "title": title,
        "header_size": tag,
        "align": align
    }
    if custom_css_class:
        settings["_css_classes"] = custom_css_class
    return {
        "id": eid or uid('hd'),
        "elType": "widget",
        "widgetType": "heading",
        "settings": settings,
        "elements": []
    }

def native_text(content, custom_css_class='', eid=None):
    settings = {
        "editor": f"<p>{content}</p>"
    }
    if custom_css_class:
        settings["_css_classes"] = custom_css_class
    return {
        "id": eid or uid('txt'),
        "elType": "widget",
        "widgetType": "text-editor",
        "settings": settings,
        "elements": []
    }

def native_icon(icon_class="fas fa-arrow-right", custom_css_class='', eid=None, color='#D4AF37'):
    settings = {
        "selected_icon": {
            "value": icon_class,
            "library": "fa-solid"
        },
        "view": "default",
        "primary_color": color
    }
    if custom_css_class:
        settings["_css_classes"] = custom_css_class
    return {
        "id": eid or uid('ico'),
        "elType": "widget",
        "widgetType": "icon",
        "settings": settings,
        "elements": []
    }

def native_button(text, link="#contact", icon_class="fas fa-arrow-right", custom_css_class='', eid=None):
    settings = {
        "text": text,
        "link": {"url": link, "is_external": "", "nofollow": ""},
        "selected_icon": {
            "value": icon_class,
            "library": "fa-solid"
        },
        "icon_align": "right"
    }
    if custom_css_class:
        settings["_css_classes"] = custom_css_class
    return {
        "id": eid or uid('btn'),
        "elType": "widget",
        "widgetType": "button",
        "settings": settings,
        "elements": []
    }

def native_image(url, img_id=0, alt="", custom_css_class='', eid=None):
    settings = {
        "image": {
            "url": url,
            "id": img_id
        },
        "image_size": "full",
        "caption_source": "none"
    }
    if custom_css_class:
        settings["_css_classes"] = custom_css_class
    return {
        "id": eid or uid('img'),
        "elType": "widget",
        "widgetType": "image",
        "settings": settings,
        "elements": []
    }

def native_shortcode(shortcode_text, custom_css_class='', eid=None):
    settings = {
        "shortcode": shortcode_text
    }
    if custom_css_class:
        settings["_css_classes"] = custom_css_class
    return {
        "id": eid or uid('sc'),
        "elType": "widget",
        "widgetType": "shortcode",
        "settings": settings,
        "elements": []
    }

def native_form(eid=None):

    settings = {
        "form_name": "AXELA Trade & Project Enquiry Form",
        "form_fields": [
            {
                "_id": "name",
                "custom_id": "name",
                "field_type": "text",
                "field_label": "Full Name",
                "placeholder": "e.g. Johnathan Doe",
                "required": "true",
                "width": "50"
            },
            {
                "_id": "company",
                "custom_id": "company",
                "field_type": "text",
                "field_label": "Company / Organisation",
                "placeholder": "e.g. PetroGlobal Trading LLC",
                "required": "true",
                "width": "50"
            },
            {
                "_id": "email_phone",
                "custom_id": "email_phone",
                "field_type": "text",
                "field_label": "Business Email & Phone / WhatsApp",
                "placeholder": "e.g. desk@company.com / +88 017...",
                "required": "true",
                "width": "50"
            },
            {
                "_id": "country",
                "custom_id": "country",
                "field_type": "text",
                "field_label": "Country of Operation",
                "placeholder": "e.g. Bangladesh / Singapore / UAE",
                "required": "true",
                "width": "50"
            },
            {
                "_id": "enquiry_type",
                "custom_id": "enquiry_type",
                "field_type": "select",
                "field_label": "Enquiry Type",
                "field_options": "Product Supply\nTender\nBrokerage\nInvestment\nAdvisory\nOther",
                "required": "true",
                "width": "50"
            },
            {
                "_id": "product_project",
                "custom_id": "product_project",
                "field_type": "text",
                "field_label": "Product or Project of Interest",
                "placeholder": "e.g. Gasoil 50ppm / Prilled Urea / Energy Project",
                "required": "true",
                "width": "50"
            },
            {
                "_id": "quantity_size",
                "custom_id": "quantity_size",
                "field_type": "text",
                "field_label": "Required Quantity or Estimated Project Size",
                "placeholder": "e.g. 50,000 MT / USD 10M",
                "width": "50"
            },
            {
                "_id": "destination",
                "custom_id": "destination",
                "field_type": "text",
                "field_label": "Destination / Location",
                "placeholder": "e.g. Chattogram Port / Matarbari / Mongla",
                "width": "50"
            },
            {
                "_id": "incoterm",
                "custom_id": "incoterm",
                "field_type": "text",
                "field_label": "Preferred Delivery Term (Incoterm)",
                "placeholder": "e.g. CIF Chattogram / CFR / FOB",
                "width": "50"
            },
            {
                "_id": "delivery_timeline",
                "custom_id": "delivery_timeline",
                "field_type": "text",
                "field_label": "Target Delivery Date or Project Timeline",
                "placeholder": "e.g. Q4 2026 / Prompt Delivery",
                "width": "50"
            },
            {
                "_id": "specs_summary",
                "custom_id": "specs_summary",
                "field_type": "textarea",
                "field_label": "Required Specifications or Project Summary",
                "placeholder": "Detail specific grades, quality parameters, origin preferences, or scope summary...",
                "rows": 3,
                "width": "100"
            },
            {
                "_id": "supporting_docs",
                "custom_id": "supporting_docs",
                "field_type": "upload",
                "field_label": "Message & Supporting Documents (Upload Spec Sheet / LOI / RFQ)",
                "file_types": "pdf,doc,docx,jpg,jpeg,png,webp",
                "max_file_size": "15",
                "width": "100"
            }
        ],
        "submit_actions": ["email", "save-to-database", "collect-submissions", "submissions"],
        "email_to": "anikaeti404@gmail.com",
        "email_subject": "New Trade & Project Enquiry - AXELA LTD.",
        "email_from_name": "AXELA Limited",
        "email_from_email": "noreply@axelaglobal.com",
        "email_reply_to": "[field id=\"email_phone\"]",
        "email_reply_to_field": "email_phone",
        "email_content": "[all-fields]",
        "button_text": "SUBMIT TRADE ENQUIRY",
        "button_width": "auto",
        "selected_button_icon": {
            "value": "fas fa-arrow-right",
            "library": "fa-solid"
        },
        "button_icon_align": "right",
        "_css_classes": "axela-native-pro-form axela-btn-red axela-btn-compact-submit"
    }
    return {
        "id": eid or uid('form'),
        "elType": "widget",
        "widgetType": "form",
        "settings": settings,
        "elements": []
    }

def native_container(elements=None, direction='column', wrap='nowrap', justify='flex-start', align='stretch', content_width='full', custom_css_class='', custom_id='', eid=None, padding=None, bg_color="#060B13"):
    settings = {
        "content_width": content_width,
        "flex_direction": direction,
        "flex_wrap": wrap,
        "justify_content": justify,
        "align_items": align
    }
    if bg_color and (custom_id or "axela-section" in custom_css_class):
        settings["background_background"] = "classic"
        settings["background_color"] = bg_color
    if padding:
        settings["padding"] = padding
    if custom_css_class:
        settings["_css_classes"] = custom_css_class
        settings["css_classes"] = custom_css_class
    if custom_id:
        settings["_css_id"] = custom_id
        settings["_element_id"] = custom_id
        settings["css_id"] = custom_id

    return {
        "id": eid or uid('con'),
        "elType": "container",
        "settings": settings,
        "elements": elements or []
    }

def native_html(html_code, eid=None):
    return {
        "id": eid or uid('html'),
        "elType": "widget",
        "widgetType": "html",
        "settings": {
            "html": html_code
        },
        "elements": []
    }

def generate_interactive_routes_html():
    return """
<div class="axela-routes-interactive-wrapper">
  <style>
    @keyframes pulse-ring {
      0%   { r: 4;  opacity: 0.8; }
      100% { r: 24; opacity: 0; }
    }
    @keyframes vessel-blink {
      0%, 100% { opacity: 1; }
      50%      { opacity: 0.35; }
    }
    .axela-routes-interactive-wrapper {
      position: relative;
      width: 100%;
      margin: 0 auto;
    }
    .axela-routes-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      flex-wrap: wrap;
      gap: 16px;
    }
    .axela-routes-tabs {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }
    .axela-route-tab-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 18px;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 13px;
      font-weight: 600;
      letter-spacing: 0.10em;
      text-transform: uppercase;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #94A3B8;
      cursor: pointer;
      border-radius: 2px;
      transition: all 0.25s ease;
    }
    .axela-route-tab-btn:hover {
      border-color: rgba(255, 255, 255, 0.3);
      color: #FFFFFF;
      background: rgba(255, 255, 255, 0.06);
    }
    .axela-route-tab-btn.active {
      background: rgba(218, 66, 60, 0.22);
      border-color: #DA423C;
      color: #FFFFFF;
      box-shadow: 0 2px 14px rgba(218, 66, 60, 0.35);
    }
    .axela-map-canvas-box {
      position: relative;
      width: 100%;
      aspect-ratio: 2 / 1;
      background: #09131E;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 4px;
      overflow: hidden;
      box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    }
    .axela-map-svg {
      width: 100%;
      height: 100%;
      display: block;
    }
    .axela-map-badge {
      position: absolute;
      top: 14px;
      left: 14px;
      background: rgba(9, 19, 30, 0.88);
      border: 1px solid rgba(212, 175, 55, 0.35);
      padding: 6px 12px;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 10.5px;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: #D4AF37;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      backdrop-filter: blur(8px);
      border-radius: 2px;
      z-index: 5;
    }
    .axela-badge-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #DA423C;
      box-shadow: 0 0 8px #DA423C;
    }
    .axela-map-legend {
      position: absolute;
      bottom: 14px;
      left: 14px;
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      background: rgba(9, 19, 30, 0.88);
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 8px 14px;
      backdrop-filter: blur(8px);
      border-radius: 2px;
      z-index: 5;
    }
    .axela-legend-item {
      display: flex;
      align-items: center;
      gap: 6px;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 11px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: #94A3B8;
    }
    .axela-legend-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      flex-shrink: 0;
    }
    .interactive-node {
      cursor: pointer;
      pointer-events: all;
    }
    @media (max-width: 768px) {
      .axela-map-canvas-box {
        aspect-ratio: 16 / 10;
      }
      .axela-map-legend { display: none; }
    }
  </style>

  <div class="axela-routes-bar">
    <div class="axela-routes-tabs" id="axela-routes-tabs">
      <button class="axela-route-tab-btn active" data-tab="crude">
        <i class="fas fa-oil-can" style="font-size: 12px;"></i> Crude &amp; Petroleum Corridors
      </button>
      <button class="axela-route-tab-btn" data-tab="lng">
        <i class="fas fa-fire-flame-simple" style="font-size: 12px;"></i> LNG &amp; Gas
      </button>
      <button class="axela-route-tab-btn" data-tab="bulk">
        <i class="fas fa-wheat-awn" style="font-size: 12px;"></i> Bulk Fertilizers &amp; Agri
      </button>
      <button class="axela-route-tab-btn" data-tab="offices">
        <i class="fas fa-building" style="font-size: 12px;"></i> Global Trade Desks
      </button>
    </div>
  </div>

  <div class="axela-map-canvas-box" id="axela-map-box">
    <div class="axela-map-badge">
      <span class="axela-badge-dot"></span>
      Live Vessel &amp; Trade Routing Simulation
    </div>



    <svg class="axela-map-svg" viewBox="0 0 1000 500" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <filter id="ax-node-glow" x="-50%" y="-50%" width="200%" height="200%">
          <feGaussianBlur stdDeviation="2.5" result="blur" />
          <feMerge>
            <feMergeNode in="blur" />
            <feMergeNode in="SourceGraphic" />
          </feMerge>
        </filter>
        <filter id="ax-route-glow" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="1.8" result="blur" />
          <feMerge>
            <feMergeNode in="blur" />
            <feMergeNode in="SourceGraphic" />
          </feMerge>
        </filter>
        <radialGradient id="ax-ocean-grad" cx="50%" cy="50%" r="70%">
          <stop offset="0%" stop-color="#0e2235" />
          <stop offset="100%" stop-color="#070D16" />
        </radialGradient>
        <pattern id="ax-lat-lon-grid" width="55.5" height="55.5" patternUnits="userSpaceOnUse">
          <path d="M 55.5 0 L 0 0 0 55.5" fill="none" stroke="rgba(34,168,168,0.06)" stroke-width="0.5" />
        </pattern>
      </defs>

      <!-- Ocean Background & Lat-Lon Grid -->
      <rect width="1000" height="500" fill="url(#ax-ocean-grad)" />
      <rect width="1000" height="500" fill="url(#ax-lat-lon-grid)" />

      <!-- World Landmasses (Stylized Vector Continents) -->
      <!-- North America -->
      <path d="M 78,90 Q 105,72 148,78 Q 170,82 185,92 Q 205,80 235,80 Q 258,80 268,90 Q 282,102 278,118 Q 274,132 262,143 Q 278,142 285,152 Q 290,162 282,172 Q 272,182 258,185 Q 248,192 240,202 Q 230,212 222,208 Q 210,215 200,225 Q 190,238 178,246 Q 164,252 158,242 Q 148,230 150,210 Q 152,192 140,178 Q 122,162 105,148 Q 85,132 78,115 Z" fill="#0d2235" stroke="#1a5565" stroke-width="0.8" opacity="0.9" />
      <!-- Greenland -->
      <path d="M 300,60 Q 330,50 355,58 Q 370,65 365,80 Q 355,92 335,96 Q 310,95 298,83 Q 292,74 300,60 Z" fill="#0d2235" stroke="#1a5565" stroke-width="0.6" opacity="0.7" />
      <!-- South America -->
      <path d="M 232,255 Q 255,248 285,252 Q 312,258 330,278 Q 345,300 352,330 Q 360,365 352,398 Q 340,428 318,440 Q 295,448 272,440 Q 250,428 240,400 Q 228,368 232,335 Q 236,305 228,278 Q 226,265 232,255 Z" fill="#0d2235" stroke="#1a5565" stroke-width="0.8" opacity="0.9" />
      <!-- Europe -->
      <path d="M 435,92 Q 458,82 482,84 Q 502,86 518,94 Q 532,86 548,90 Q 558,96 553,108 Q 545,118 532,122 Q 518,128 508,138 Q 495,142 478,143 Q 460,142 448,134 Q 435,125 432,112 Q 430,102 435,92 Z" fill="#0d2235" stroke="#1a5565" stroke-width="0.8" opacity="0.9" />
      <!-- Scandinavia / UK -->
      <path d="M 482,60 Q 495,52 508,56 Q 518,62 514,74 Q 508,84 496,88 Q 485,87 480,78 Q 476,68 482,60 Z" fill="#0d2235" stroke="#1a5565" stroke-width="0.6" opacity="0.7" />
      <path d="M 442,100 Q 450,95 458,100 Q 462,108 456,114 Q 448,116 442,110 Z" fill="#0d2235" stroke="#1a5565" stroke-width="0.5" opacity="0.7" />
      <!-- Africa -->
      <path d="M 455,152 Q 482,144 515,150 Q 545,158 562,175 Q 582,195 585,220 Q 592,252 580,292 Q 565,332 548,362 Q 528,390 505,395 Q 480,393 460,368 Q 442,340 440,305 Q 438,268 445,238 Q 452,208 450,182 Q 448,164 455,152 Z" fill="#0d2235" stroke="#1a5565" stroke-width="0.8" opacity="0.9" />
      <!-- Middle East -->
      <path d="M 568,178 Q 592,172 620,180 Q 648,192 658,215 Q 650,230 635,232 Q 615,228 595,222 Q 578,215 568,200 Q 562,190 568,178 Z" fill="#0d2235" stroke="#1a5565" stroke-width="0.7" opacity="0.85" />
      <!-- South Asia / India / Bay of Bengal -->
      <path d="M 665,162 Q 690,155 708,162 Q 722,170 725,188 Q 720,210 708,228 Q 695,245 680,248 Q 668,242 660,228 Q 652,210 654,190 Q 656,172 665,162 Z" fill="#0d2235" stroke="#1a5565" stroke-width="0.7" opacity="0.85" />
      <!-- Northern Asia / Russia / China -->
      <path d="M 560,98 Q 635,85 720,88 Q 800,90 870,100 Q 920,110 940,128 Q 918,138 880,140 Q 830,135 780,128 Q 730,122 680,118 Q 635,115 590,120 Q 568,122 560,112 Z" fill="#0d2235" stroke="#1a5565" stroke-width="0.7" opacity="0.75" />
      <!-- East & Southeast Asia -->
      <path d="M 745,128 Q 800,120 848,132 Q 880,145 895,168 Q 900,188 892,202 Q 875,215 852,220 Q 825,222 802,218 Q 778,212 760,202 Q 742,190 738,172 Q 735,152 745,128 Z" fill="#0d2235" stroke="#1a5565" stroke-width="0.7" opacity="0.85" />
      <!-- Southeast Asia Islands -->
      <path d="M 775,225 Q 785,235 782,252 Q 778,265 768,268 Q 758,262 755,248 Q 753,235 760,228 Z" fill="#0d2235" stroke="#1a5565" stroke-width="0.6" opacity="0.75" />
      <path d="M 870,118 Q 880,112 890,116 Q 896,122 892,130 Q 886,136 876,132 Q 868,126 870,118 Z" fill="#0d2235" stroke="#1a5565" stroke-width="0.5" opacity="0.7" />
      <!-- Australia -->
      <path d="M 800,328 Q 835,315 868,322 Q 895,335 900,358 Q 898,385 878,398 Q 852,405 825,398 Q 800,385 792,360 Q 787,338 800,328 Z" fill="#0d2235" stroke="#1a5565" stroke-width="0.7" opacity="0.8" />

      <!-- Strategic Maritime Chokepoint Labels -->
      <g fill="rgba(244,240,235,0.22)" font-size="7.5" font-family="'Barlow Condensed', sans-serif" letter-spacing="1.5" text-anchor="middle">
        <text x="564" y="218">SUEZ</text>
        <text x="644" y="248">HORMUZ</text>
        <text x="768" y="296">MALACCA</text>
        <text x="455" y="168">GIBRALTAR</text>
        <text x="268" y="220">PANAMA</text>
        <text x="725" y="245">BAY OF BENGAL</text>
      </g>

      <!-- Dynamic Route Corridors Layer -->
      <g id="axela-routes-layer"></g>

      <!-- Interactive Global Hub Nodes Layer -->
      <g id="axela-nodes-layer"></g>
    </svg>

    <!-- Legend -->
    <div class="axela-map-legend">
      <div class="axela-legend-item"><span class="axela-legend-dot" style="background: #D4AF37;"></span> Crude &amp; Sourcing</div>
      <div class="axela-legend-item"><span class="axela-legend-dot" style="background: #DA423C;"></span> Refined &amp; Distribution</div>
      <div class="axela-legend-item"><span class="axela-legend-dot" style="background: #E5C07B;"></span> LNG &amp; Gas</div>
      <div class="axela-legend-item"><span class="axela-legend-dot" style="background: #DA423C;"></span> Bulk Commodities</div>
    </div>
  </div>
</div>

<script>
(function() {
  const HUB_DATA = {
    chattogram: {
      id: "chattogram", cx: 728, cy: 222, color: "#DA423C",
      type: "Primary South Asian Gateway · Bangladesh",
      name: "Chattogram & Matarbari Deep Sea Port",
      desc: "Axela Global's commercial and maritime anchor in the Bay of Bengal, coordinating high-volume physical discharge of petroleum, bulk fertilizers, LNG, and industrial feedstocks."
    },
    fujairah: {
      id: "fujairah", cx: 640, cy: 230, color: "#D4AF37",
      type: "Crude Export & Bunkering Hub · Middle East",
      name: "Ras Tanura & Fujairah Terminal",
      desc: "Core Arabian Gulf procurement and offshore blending terminal handling heavy sour, Arab Light, and marine fuel bunkering directly feeding Asian and European demand."
    },
    rotterdam: {
      id: "rotterdam", cx: 477, cy: 140, color: "#DA423C",
      type: "European Refining & Distribution · Netherlands",
      name: "Rotterdam ARA Hub",
      desc: "Europe's largest refining and inland waterway distribution node. Central discharge point for Atlantic Basin arbitrage cargoes, ultra-low sulfur diesel, and chemical feedstocks."
    },
    us_gulf: {
      id: "us_gulf", cx: 220, cy: 205, color: "#D4AF37",
      type: "North American Liquidity Desk · Houston / New Orleans",
      name: "US Gulf Coast Energy Corridor",
      desc: "Primary origination hub for WTI crude, LNG export terminals (Sabine Pass / Corpus Christi), and strategic refined products bound for transatlantic corridors."
    },
    singapore: {
      id: "singapore", cx: 788, cy: 278, color: "#DA423C",
      type: "Asian Pricing & Bunkering Node · Straits",
      name: "Singapore Straits Trading Hub",
      desc: "The nerve center of Asian physical cargo arbitrage, fuel oil price discovery, and regional transshipment across Southeast and East Asia."
    },
    west_africa: {
      id: "west_africa", cx: 472, cy: 302, color: "#D4AF37",
      type: "Atlantic Sweet Crude Basin · Nigeria / Angola",
      name: "West Africa Marine Terminals",
      desc: "Major offshore lifting origin for high-yield sweet grades (Bonny Light, Qua Iboe) feeding European refinery grids and Asian spot tenders."
    },
    suez: {
      id: "suez", cx: 565, cy: 203, color: "#DA423C",
      type: "Strategic Chokepoint & Regional Desk · Egypt",
      name: "Suez Maritime Control & Cairo Desk",
      desc: "Critical transit coordination desk ensuring scheduled passage, canal bunkering, and real-time risk hedging through the Suez-Red Sea maritime corridor."
    },
    qatar: {
      id: "qatar", cx: 635, cy: 222, color: "#E5C07B",
      type: "LNG Export Superhub · Arabian Gulf",
      name: "Ras Laffan LNG Terminal",
      desc: "Global epicenter of liquefied natural gas production, facilitating multi-year term agreements and flexible spot cargo supply to Bangladesh, India, and Europe."
    },
    tokyo: {
      id: "tokyo", cx: 880, cy: 155, color: "#DA423C",
      type: "Far East Energy & Industrial Terminal · Japan",
      name: "Tokyo Bay Commercial Gateway",
      desc: "Key East Asian destination terminal receiving clean distillates, LNG imports, and specialty chemical shipments."
    },
    melbourne: {
      id: "melbourne", cx: 855, cy: 370, color: "#D4AF37",
      type: "Asia-Pacific Minerals & Bulk Hub · Australia",
      name: "Port Hedland & Pacific Sourcing Desk",
      desc: "Strategic origination point for bulk industrial minerals, iron ore, clinker, and agricultural grain flows supporting Asian infrastructure."
    }
  };

  const ROUTES_BY_TAB = {
    crude: [
      { id: "c1", d: "M 640 230 Q 720 310 788 278", color: "#D4AF37", dur: 14 },
      { id: "c2", d: "M 640 230 Q 685 240 728 222", color: "#D4AF37", dur: 12 },
      { id: "c3", d: "M 640 230 Q 600 280 565 203 Q 525 170 477 140", color: "#DA423C", dur: 18 },
      { id: "c4", d: "M 472 302 Q 380 255 220 205", color: "#D4AF37", dur: 16 },
      { id: "c5", d: "M 220 205 Q 348 148 477 140", color: "#DA423C", dur: 15 },
      { id: "c6", d: "M 640 230 Q 565 290 472 302", color: "#D4AF37", dur: 14 }
    ],
    lng: [
      { id: "l1", d: "M 635 222 Q 560 270 467 138", color: "#E5C07B", dur: 17 },
      { id: "l2", d: "M 220 205 Q 342 162 477 140", color: "#E5C07B", dur: 14 },
      { id: "l3", d: "M 635 222 Q 680 230 728 222", color: "#E5C07B", dur: 10 },
      { id: "l4", d: "M 635 222 Q 720 255 788 278", color: "#E5C07B", dur: 13 },
      { id: "l5", d: "M 788 278 Q 840 210 880 155", color: "#E5C07B", dur: 12 }
    ],
    bulk: [
      { id: "b1", d: "M 855 370 Q 800 300 728 222", color: "#D4AF37", dur: 15 },
      { id: "b2", d: "M 640 230 Q 685 240 728 222", color: "#DA423C", dur: 12 },
      { id: "b3", d: "M 477 140 Q 560 220 728 222", color: "#D4AF37", dur: 16 },
      { id: "b4", d: "M 855 370 Q 820 310 788 278", color: "#D4AF37", dur: 13 }
    ],
    offices: [
      { id: "o1", d: "M 728 222 Q 685 226 640 230", color: "#DA423C", dur: 10 },
      { id: "o2", d: "M 640 230 Q 560 180 477 140", color: "#DA423C", dur: 12 },
      { id: "o3", d: "M 728 222 Q 755 250 788 278", color: "#DA423C", dur: 10 },
      { id: "o4", d: "M 477 140 Q 348 160 220 205", color: "#DA423C", dur: 14 }
    ]
  };

  const HUBS_BY_TAB = {
    crude: ["chattogram", "fujairah", "rotterdam", "us_gulf", "singapore", "west_africa", "suez"],
    lng: ["chattogram", "qatar", "rotterdam", "us_gulf", "singapore", "tokyo"],
    bulk: ["chattogram", "fujairah", "rotterdam", "melbourne", "singapore"],
    offices: ["chattogram", "fujairah", "rotterdam", "us_gulf", "singapore"]
  };

  let currentTab = 'crude';

  function renderAxelaMap() {
    const routesLayer = document.getElementById('axela-routes-layer');
    const nodesLayer = document.getElementById('axela-nodes-layer');
    if (!routesLayer || !nodesLayer) return;

    routesLayer.innerHTML = '';
    nodesLayer.innerHTML = '';

    const routes = ROUTES_BY_TAB[currentTab] || [];
    const hubIds = HUBS_BY_TAB[currentTab] || [];

    // Draw Routes
    routes.forEach(r => {
      const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
      g.setAttribute("filter", "url(#ax-route-glow)");

      // Background track
      const pathBg = document.createElementNS("http://www.w3.org/2000/svg", "path");
      pathBg.setAttribute("d", r.d);
      pathBg.setAttribute("fill", "none");
      pathBg.setAttribute("stroke", r.color);
      pathBg.setAttribute("stroke-width", "1");
      pathBg.setAttribute("opacity", "0.2");

      // Glow line
      const pathMain = document.createElementNS("http://www.w3.org/2000/svg", "path");
      pathMain.setAttribute("d", r.d);
      pathMain.setAttribute("fill", "none");
      pathMain.setAttribute("stroke", r.color);
      pathMain.setAttribute("stroke-width", "2");
      pathMain.setAttribute("stroke-linecap", "round");
      pathMain.setAttribute("opacity", "0.85");

      // Dashed overlay
      const pathDash = document.createElementNS("http://www.w3.org/2000/svg", "path");
      pathDash.setAttribute("d", r.d);
      pathDash.setAttribute("fill", "none");
      pathDash.setAttribute("stroke", r.color);
      pathDash.setAttribute("stroke-width", "1");
      pathDash.setAttribute("stroke-dasharray", "3 9");
      pathDash.setAttribute("opacity", "0.35");

      // Animated vessel dot
      const vessel = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      vessel.setAttribute("r", "3.5");
      vessel.setAttribute("fill", r.color);
      vessel.setAttribute("style", "filter: drop-shadow(0 0 4px " + r.color + "); animation: vessel-blink 2s ease-in-out infinite;");

      const anim = document.createElementNS("http://www.w3.org/2000/svg", "animateMotion");
      anim.setAttribute("dur", r.dur + "s");
      anim.setAttribute("repeatCount", "indefinite");
      anim.setAttribute("path", r.d);
      vessel.appendChild(anim);

      g.appendChild(pathBg);
      g.appendChild(pathMain);
      g.appendChild(pathDash);
      g.appendChild(vessel);
      routesLayer.appendChild(g);
    });

    // Draw Nodes
    hubIds.forEach(id => {
      const hub = HUB_DATA[id];
      if (!hub) return;

      const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
      g.setAttribute("class", "interactive-node");
      g.setAttribute("data-hub", id);

      // Pulse Ring 1
      const p1 = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      p1.setAttribute("cx", hub.cx);
      p1.setAttribute("cy", hub.cy);
      p1.setAttribute("r", "10");
      p1.setAttribute("fill", "none");
      p1.setAttribute("stroke", hub.color);
      p1.setAttribute("stroke-width", "0.9");
      p1.setAttribute("opacity", "0");
      p1.setAttribute("style", "animation: pulse-ring 2.4s ease-out infinite; transform-origin: " + hub.cx + "px " + hub.cy + "px;");

      // Pulse Ring 2
      const p2 = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      p2.setAttribute("cx", hub.cx);
      p2.setAttribute("cy", hub.cy);
      p2.setAttribute("r", "10");
      p2.setAttribute("fill", "none");
      p2.setAttribute("stroke", hub.color);
      p2.setAttribute("stroke-width", "0.9");
      p2.setAttribute("opacity", "0");
      p2.setAttribute("style", "animation: pulse-ring 2.4s ease-out 0.8s infinite; transform-origin: " + hub.cx + "px " + hub.cy + "px;");

      // Outer halo
      const halo = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      halo.setAttribute("cx", hub.cx);
      halo.setAttribute("cy", hub.cy);
      halo.setAttribute("r", "6");
      halo.setAttribute("fill", hub.color);
      halo.setAttribute("opacity", "0.2");

      // Center glowing circle
      const center = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      center.setAttribute("cx", hub.cx);
      center.setAttribute("cy", hub.cy);
      center.setAttribute("r", "3.8");
      center.setAttribute("fill", hub.color);
      center.setAttribute("filter", "url(#ax-node-glow)");

      // Micro core
      const core = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      core.setAttribute("cx", hub.cx);
      core.setAttribute("cy", hub.cy);
      core.setAttribute("r", "1.6");
      core.setAttribute("fill", "#FFFFFF");

      // Transparent click hit target
      const hit = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      hit.setAttribute("cx", hub.cx);
      hit.setAttribute("cy", hub.cy);
      hit.setAttribute("r", "16");
      hit.setAttribute("fill", "transparent");

      g.appendChild(p1);
      g.appendChild(p2);
      g.appendChild(halo);
      g.appendChild(center);
      g.appendChild(core);
      g.appendChild(hit);

      nodesLayer.appendChild(g);
    });
  }

  function initMap() {
    const tabs = document.querySelectorAll('.axela-route-tab-btn');
    tabs.forEach(btn => {
      btn.addEventListener('click', function() {
        tabs.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentTab = btn.getAttribute('data-tab');
        renderAxelaMap();
      });
    });
    renderAxelaMap();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMap);
  } else {
    initMap();
  }
})();
</script>
"""

# Note: Contact form is rendered via Elementor Pro native_form() widget in Section 8

def build_homepage():
    json_path = r'c:\xampp\htdocs\axela-local\elementor-templates\homepage-template.json'
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if isinstance(data, list):
        elements = data
    else:
        elements = data.get('content', [])

    # =========================================================================
    # SECTION 0: HERO SECTION (#home) - 100% NATIVE ELEMENTOR, EDITORIAL SERIF
    # Strict doc alignment: Section 1 of Word Doc (NO fake stats on right)
    # =========================================================================
    hero_badge = native_heading(
        "ENERGY &bull; COMMODITIES TRADING &bull; SUPPLY &bull; PROJECT DEVELOPMENT &bull; INVESTMENT ADVISORY",
        tag="span",
        custom_css_class="axela-hero-badge",
        eid="hero_badge_hd"
    )
    hero_h1 = native_heading(
        "Connecting Trade, Supply and Investment Opportunities",
        tag="h1",
        custom_css_class="axela-hero-title",
        eid="hero_h1_hd"
    )
    hero_intro = native_text(
        "AXELA Limited is a Dhaka based trading, indenting, commercial brokerage and business advisory company. We connect buyers, suppliers, project owners and prospective investors to support product sourcing, supply requirements, tender opportunities and investment proposals.",
        custom_css_class="axela-hero-intro",
        eid="hero_intro_txt"
    )
    hero_support = native_text(
        "From commodity sourcing and commercial coordination to investment opportunity origination and corporate advisory, we help clients assess requirements, engage relevant counterparties and progress business opportunities.",
        custom_css_class="axela-hero-support",
        eid="hero_support_txt"
    )
    btn_trade = native_button(
        "Submit a Trade Enquiry",
        link="#contact",
        icon_class="fas fa-arrow-right",
        custom_css_class="axela-hero-btn axela-btn-red axela-hero-btn-compact",
        eid="hero_btn_trade"
    )
    btn_supply = native_button(
        "Discuss a Supply Requirement",
        link="#services",
        icon_class="fas fa-arrow-right",
        custom_css_class="axela-hero-btn axela-btn-ghost axela-hero-btn-compact",
        eid="hero_btn_supply"
    )
    btn_invest = native_button(
        "Explore Investment Opportunities",
        link="#investment",
        icon_class="fas fa-arrow-right",
        custom_css_class="axela-hero-btn axela-btn-gold-link axela-hero-btn-compact",
        eid="hero_btn_invest"
    )
    hero_btn_row = native_container(
        elements=[btn_trade, btn_supply, btn_invest],
        direction="row",
        wrap="wrap",
        justify="flex-start",
        align="center",
        content_width="full",
        custom_css_class="axela-hero-btn-row",
        eid="hero_btn_con"
    )

    hero_left_con = native_container(
        elements=[hero_badge, hero_h1, hero_intro, hero_support, hero_btn_row],
        direction="column",
        align="flex-start",
        content_width="full",
        custom_css_class="axela-hero-left-column",
        eid="axela_hero_left"
    )

    hero_content = native_container(
        elements=[hero_left_con],
        direction="column",
        align="flex-start",
        content_width="boxed",
        custom_css_class="axela-hero-content-wrap",
        eid="axela_hero_content"
    )

    hero_section = {
        "id": "axela_hero_root",
        "elType": "container",
        "settings": {
            "content_width": "full",
            "width": {"unit": "%", "size": 100},
            "min_height": {"unit": "vh", "size": 82},
            "flex_direction": "column",
            "justify_content": "center",
            "align_items": "center",
            "padding": {"unit": "px", "top": "90", "right": "0", "bottom": "60", "left": "0", "isLinked": False},
            "background_background": "video",
            "background_video_link": "https://axelaglobal.com/wp-content/uploads/2026/10/lv_0_20261006163733.mp4",
            "background_play_on_mobile": "yes",
            "background_play_once": "",
            "background_video_fallback": {
                "url": "https://axelaglobal.com/wp-content/uploads/2026/10/axela-hero-poster-20261006.jpg",
                "id": 217
            },
            "background_overlay_background": "classic",
            "background_overlay_color": "rgba(6, 11, 19, 0.75)",
            "background_overlay_opacity": {"unit": "px", "size": 1},
            "html_tag": "section",
            "_css_id": "home",
            "_element_id": "home",
            "_css_classes": "axela-hero-section"
        },
        "elements": [hero_content]
    }

    # =========================================================================
    # SECTION 1: ABOUT US (#about) - 100% NATIVE ELEMENTOR, CLEAN & SIMPLE
    # Heading: "About AXELA LTD."
    # Body copy strictly from Section 2 of Word Document
    # NO STATS BOXES / NO INVENTED NUMBERS
    # =========================================================================
    about_eyebrow = native_heading("01 / ABOUT US", tag="span", custom_css_class="axela-section-eyebrow", eid="abt_eye")
    about_title = native_heading("About AXELA LTD.", tag="h2", custom_css_class="axela-section-title", eid="abt_h2")
    
    about_narrative_1 = native_text(
        "AXELA Limited works at the intersection of international trade, product supply and commercial advisory. Our role is to help identify opportunities, connect relevant parties and coordinate the commercial steps required to move a transaction forward.",
        custom_css_class="axela-lead-text",
        eid="abt_p1"
    )
    about_narrative_2 = native_text(
        "We aim to build business relationships through clear communication, professional conduct, confidentiality and a practical understanding of buyer and supplier requirements.",
        custom_css_class="axela-sub-text",
        eid="abt_p2"
    )

    about_boxed_wrap = native_container(
        elements=[about_eyebrow, about_title, about_narrative_1, about_narrative_2],
        direction="column",
        content_width="boxed",
        custom_css_class="axela-container-boxed",
        eid="about_inner_wrap"
    )

    SECTION_PADDING = {
        "unit": "px",
        "top": "105",
        "bottom": "105",
        "left": "0",
        "right": "0",
        "isLinked": False
    }

    about_section = native_container(
        elements=[about_boxed_wrap],
        direction="column",
        content_width="full",
        custom_css_class="axela-section axela-about-section",
        custom_id="about",
        eid="sec_about",
        padding=SECTION_PADDING
    )

    # =========================================================================
    # SECTION 2: OUR SERVICES (#services)
    # 8 Compact cards strictly from doc
    # Sleek padding, small icons, NO "DISCUSS SUPPLY" buttons
    # =========================================================================
    services_eyebrow = native_heading("02 / CORE CAPABILITIES", tag="span", custom_css_class="axela-section-eyebrow", eid="svc_eye")
    services_title = native_heading("Our Services", tag="h2", custom_css_class="axela-section-title", eid="svc_h2")
    services_subtitle = native_text(
        "Sourcing and coordinating supply of petroleum products, commercial brokerage, tender support and advisory services.",
        custom_css_class="axela-section-subtitle",
        eid="svc_sub"
    )
    services_header_con = native_container(
        elements=[services_eyebrow, services_title, services_subtitle],
        direction="column",
        custom_css_class="axela-section-header",
        eid="svc_head_con"
    )

    services_data = [
        {
            "num": "01", "icon": "fas fa-gas-pump",
            "title": "Trading and Product Supply",
            "desc": "Sourcing and coordinating supply of petroleum products, petrochemicals, fertilizers, industrial chemicals and other agreed commodities or commercial products, subject to product availability, applicable approvals and agreed contract terms."
        },
        {
            "num": "02", "icon": "fas fa-handshake",
            "title": "Indenting and Commercial Brokerage",
            "desc": "Introducing buyers and suppliers, facilitating commercial discussions, coordinating offers and supporting transactions under agreed mandates and commission arrangements."
        },
        {
            "num": "03", "icon": "fas fa-file-signature",
            "title": "Tender and Institutional Supply Support",
            "desc": "Identifying relevant supply tenders and assisting with supplier coordination, quotations, product specifications, commercial documentation and bid or contract coordination where authorised."
        },
        {
            "num": "04", "icon": "fas fa-chart-line",
            "title": "Sourcing and Market Coordination",
            "desc": "Helping clarify product requirements, quantity, quality specifications, origin, delivery schedule and trade terms; coordinating enquiries with potential suppliers and service providers."
        },
        {
            "num": "05", "icon": "fas fa-lightbulb",
            "title": "Investment Opportunity Origination",
            "desc": "Identifying and developing business proposals, project concepts, strategic partnerships and investment opportunities for review by potential local and international investors."
        },
        {
            "num": "06", "icon": "fas fa-globe-asia",
            "title": "Foreign Investor Facilitation in Bangladesh",
            "desc": "Supporting international investors with local introductions, opportunity screening, business coordination and communication with relevant counterparties. Legal, tax, licensing and regulated services should be provided by appropriately qualified professionals."
        },
        {
            "num": "07", "icon": "fas fa-balance-scale",
            "title": "Corporate Advisory and Financial Structuring",
            "desc": "Commercial support for business plans, transaction structures, strategic partnerships, capital proposals and financing discussions, working with relevant professional advisers where required."
        },
        {
            "num": "08", "icon": "fas fa-truck-moving",
            "title": "Transaction and Logistics Coordination",
            "desc": "Coordinating commercial documentation, delivery requirements, shipment-related communication and counterparty follow-up as agreed for each transaction. AXELA does not represent itself as a carrier, insurer or logistics operator unless separately authorised to provide those services."
        }
    ]

    service_cards = []
    for idx, s in enumerate(services_data):
        card_id = f"svc_card_{idx+1}"
        head_num = native_heading(f"{s['num']}", tag="span", custom_css_class="service-card-num")
        head_icon = native_icon(s['icon'], custom_css_class="service-card-icon-sleek")
        head_row = native_container(
            elements=[head_num, head_icon],
            direction="row",
            justify="space-between",
            align="center",
            custom_css_class="service-card-head"
        )
        c_title = native_heading(s['title'], tag="h3", custom_css_class="service-card-title")
        c_desc = native_text(s['desc'], custom_css_class="service-card-desc")

        # Sleek, compact card: Head row (num + icon), Title, Description. No extra buttons!
        card = native_container(
            elements=[head_row, c_title, c_desc],
            direction="column",
            content_width="full",
            custom_css_class="axela-service-compact-card",
            eid=card_id
        )
        service_cards.append(card)

    services_grid_con = native_container(
        elements=service_cards,
        direction="row",
        wrap="wrap",
        justify="space-between",
        content_width="full",
        custom_css_class="axela-services-compact-grid",
        eid="services_grid_con"
    )

    services_boxed_wrap = native_container(
        elements=[services_header_con, services_grid_con],
        direction="column",
        content_width="boxed",
        custom_css_class="axela-container-boxed",
        eid="services_inner_wrap"
    )

    services_section = native_container(
        elements=[services_boxed_wrap],
        direction="column",
        content_width="full",
        custom_css_class="axela-section axela-services-section",
        custom_id="services",
        eid="sec_services",
        padding=SECTION_PADDING
    )

    # =========================================================================
    # SECTION 3: PRODUCTS & TRADING CATEGORIES (#products)
    # Fulfills user annotations:
    # "No need these CAT 1,2,3 ...."
    # "reduce icon size and make them more closer to their headings , and add icons to every section/card here"
    # "Add any relevent better image" -> high res refinery banner
    # =========================================================================
    # Split Blend Warehouse Banner (Petrotraders / Screenshot 2026-10-06 142745.jpg style)
    products_eyebrow = native_heading("03 / COMMODITY SCOPE", tag="span", custom_css_class="axela-section-eyebrow", eid="prod_eye")
    products_title = native_heading("Products and Trading Categories", tag="h2", custom_css_class="axela-section-title", eid="prod_h2")
    products_subtitle = native_text(
        "AXELA LTD. may consider sourcing and supply enquiries across the following categories, depending on the specific requirement, supplier availability, applicable permissions and transaction terms.",
        eid="prod_sub"
    )
    products_intro_con = native_container(
        elements=[products_eyebrow, products_title, products_subtitle],
        direction="column",
        align="flex-start",
        content_width="full",
        custom_css_class="axela-prod-banner-text",
        eid="prod_banner_text"
    )

    products_split_banner = {
        "id": "prod_split_banner",
        "elType": "container",
        "settings": {
            "content_width": "full",
            "width": {"unit": "%", "size": 100},
            "min_height": {"unit": "px", "size": 420},
            "flex_direction": "row",
            "align_items": "center",
            "justify_content": "flex-start",
            "padding": {"unit": "px", "top": "60", "right": "40", "bottom": "60", "left": "50", "isLinked": False},
            "background_background": "classic",
            "background_image": {
                "url": "https://axelaglobal.com/wp-content/uploads/2026/10/port-terminal-infrastructure.webp",
                "id": 86
            },
            "background_position": "center right",
            "background_size": "cover",
            "background_repeat": "no-repeat",
            "background_overlay_background": "gradient",
            "background_overlay_color": "rgba(6, 11, 19, 0.78)",
            "background_overlay_color_b": "rgba(6, 11, 19, 0.0)",
            "background_overlay_gradient_type": "linear",
            "background_overlay_gradient_angle": {"unit": "deg", "size": 90},
            "background_overlay_opacity": {"unit": "px", "size": 0.85},
            "_css_classes": "axela-products-split-banner",
            "css_classes": "axela-products-split-banner"
        },
        "elements": [products_intro_con]
    }

    # Categories strictly without "CAT 01" / "CAT 02", with small icons close to headings!
    categories_data = [
        {
            "icon": "fas fa-gas-pump",
            "title": "Energy and Petroleum",
            "desc": "Diesel, gasoil, fuel oil, jet fuel, LNG, bitumen and other petroleum products where permitted and available."
        },
        {
            "icon": "fas fa-flask",
            "title": "Petrochemicals",
            "desc": "Selected petrochemical feedstocks, aromatics, olefins, and industrial raw materials for processing facilities."
        },
        {
            "icon": "fas fa-seedling",
            "title": "Fertilizers & Agrochemicals",
            "desc": "Granular and prilled Urea, DAP, NPK compounds, potash (MOP), and key agricultural soil enrichment inputs."
        },
        {
            "icon": "fas fa-vial",
            "title": "Industrial and Specialty Chemicals",
            "desc": "Essential industrial process chemicals, solvents, caustics, and water treatment reagents under strict quality control."
        },
        {
            "icon": "fas fa-leaf",
            "title": "Agricultural Commodities",
            "desc": "Rice, milling wheat, feed grains, pulses, refined sugar, and edible oils tailored to institutional and national requirements."
        },
        {
            "icon": "fas fa-cube",
            "title": "Metals, Minerals and Industrial Products",
            "desc": "Industrial raw materials, steel scrap, iron ore, clinker, capital equipment, and commercial goods based on verified tenders."
        }
    ]

    cat_cards = []
    for idx, c in enumerate(categories_data):
        # Icon right next to heading
        c_icon = native_icon(c['icon'], custom_css_class="category-icon-inline")
        c_title = native_heading(c['title'], tag="h3", custom_css_class="category-card-title-sleek")
        
        c_title_row = native_container(
            elements=[c_icon, c_title],
            direction="row",
            align="center",
            custom_css_class="category-title-icon-row"
        )
        
        c_desc = native_text(c['desc'])

        card = native_container(
            elements=[c_title_row, c_desc],
            direction="column",
            content_width="full",
            custom_css_class="axela-category-compact-card",
            eid=f"cat_card_{idx+1}"
        )
        cat_cards.append(card)

    categories_grid_con = native_container(
        elements=cat_cards,
        direction="row",
        wrap="wrap",
        justify="space-between",
        content_width="full",
        custom_css_class="axela-categories-compact-grid",
        eid="categories_grid_con"
    )

    products_boxed_wrap = native_container(
        elements=[products_split_banner, categories_grid_con],
        direction="column",
        content_width="boxed",
        custom_css_class="axela-container-boxed",
        eid="products_inner_wrap"
    )

    products_section = native_container(
        elements=[products_boxed_wrap],
        direction="column",
        content_width="full",
        custom_css_class="axela-section axela-products-section",
        custom_id="products",
        eid="sec_products",
        padding=SECTION_PADDING
    )

    # =========================================================================
    # SECTION 4: OUR WORKING APPROACH (#approach)
    # Fulfills user annotations: "reduce icon size", "reduce gap"
    # =========================================================================
    approach_eyebrow = native_heading("04 / DISCIPLINED EXECUTION", tag="span", custom_css_class="axela-section-eyebrow", eid="appr_eye")
    approach_title = native_heading("Our Working Approach", tag="h2", custom_css_class="axela-section-title", eid="appr_h2")
    approach_subtitle = native_text(
        "A structured, transparent and disciplined methodology guiding commercial discussions from initial enquiry to contract execution.",
        eid="appr_sub"
    )
    approach_header_con = native_container(
        elements=[approach_eyebrow, approach_title, approach_subtitle],
        direction="column",
        custom_css_class="axela-section-header",
        eid="appr_head_con"
    )

    approach_stages = [
        {
            "step": "01", "icon": "fas fa-clipboard-list",
            "title": "Understand the requirement",
            "desc": "Confirm product or project scope, specifications, volume, destination, timing and commercial terms."
        },
        {
            "step": "02", "icon": "fas fa-users",
            "title": "Identify potential counterparties",
            "desc": "Coordinate with suitable suppliers, buyers, project owners, advisers or investors."
        },
        {
            "step": "03", "icon": "fas fa-file-contract",
            "title": "Clarify commercial terms",
            "desc": "Support discussion of price basis, delivery terms, documentation, payment conditions and responsibilities."
        },
        {
            "step": "04", "icon": "fas fa-network-wired",
            "title": "Coordinate the process",
            "desc": "Help keep communication, documents and agreed follow-up steps organised."
        },
        {
            "step": "05", "icon": "fas fa-medal",
            "title": "Maintain professional standards",
            "desc": "Promote confidentiality, transparent communication, responsible business conduct and compliance."
        }
    ]

    stage_cards = []
    for idx, st in enumerate(approach_stages):
        st_num = native_heading(f"STAGE {st['step']}", tag="span", custom_css_class="stage-card-step")
        st_icon = native_icon(st['icon'], custom_css_class="stage-icon-sleek")
        st_head_row = native_container(
            elements=[st_num, st_icon],
            direction="row",
            justify="space-between",
            align="center",
            custom_css_class="stage-card-head"
        )
        st_title = native_heading(st['title'], tag="h3", custom_css_class="stage-card-title")
        st_desc = native_text(st['desc'])

        card = native_container(
            elements=[st_head_row, st_title, st_desc],
            direction="column",
            content_width="full",
            custom_css_class="axela-stage-compact-card",
            eid=f"stage_card_{idx+1}"
        )
        stage_cards.append(card)

    approach_grid_con = native_container(
        elements=stage_cards,
        direction="row",
        wrap="nowrap",
        justify="space-between",
        content_width="full",
        custom_css_class="axela-approach-compact-grid",
        eid="approach_grid_con"
    )

    approach_boxed_wrap = native_container(
        elements=[approach_header_con, approach_grid_con],
        direction="column",
        content_width="boxed",
        custom_css_class="axela-container-boxed",
        eid="approach_inner_wrap"
    )

    approach_section = native_container(
        elements=[approach_boxed_wrap],
        direction="column",
        content_width="full",
        custom_css_class="axela-section axela-approach-section",
        custom_id="approach",
        eid="sec_approach",
        padding=SECTION_PADDING
    )

    # =========================================================================
    # SECTION 5: INTERACTIVE GLOBAL TRADE ROUTES MAP (#network / #routes)
    # Fulfills user annotations: "do it like the screen recording of the reference attached here"
    # =========================================================================
    routes_eyebrow = native_heading("05 / GLOBAL TRADE ROUTES & MARITIME CORRIDORS", tag="span", custom_css_class="axela-section-eyebrow", eid="net_eye")
    routes_title = native_heading("Interactive Global Trade Routes", tag="h2", custom_css_class="axela-section-title", eid="net_h2")
    routes_subtitle = native_text(
        "Tracking physical crude, refined products, LNG, fertilizers and commercial commodities across key international maritime trade corridors.",
        eid="net_sub"
    )
    routes_header_con = native_container(
        elements=[routes_eyebrow, routes_title, routes_subtitle],
        direction="column",
        custom_css_class="axela-section-header",
        eid="net_head_con"
    )

    # Embed the full interactive routes map widget
    interactive_map_widget = native_html(generate_interactive_routes_html(), eid="interactive_map_widget")

    routes_boxed_wrap = native_container(
        elements=[routes_header_con, interactive_map_widget],
        direction="column",
        content_width="boxed",
        custom_css_class="axela-container-boxed",
        eid="routes_inner_wrap"
    )

    network_section = native_container(
        elements=[routes_boxed_wrap],
        direction="column",
        content_width="full",
        custom_css_class="axela-section axela-network-section",
        custom_id="network",
        eid="sec_network",
        padding=SECTION_PADDING
    )

    # =========================================================================
    # SECTION 6: INVESTMENT OPPORTUNITIES (#investment)
    # Fulfills user annotations: "reduce icon size", "reduce gap"
    # =========================================================================
    invest_eyebrow = native_heading("06 / CAPITAL & ORIGINATION", tag="span", custom_css_class="axela-section-eyebrow", eid="inv_eye")
    invest_title = native_heading("Investment and Project Opportunities", tag="h2", custom_css_class="axela-section-title", eid="inv_h2")
    invest_subtitle = native_text(
        "AXELA LTD. supports the origination and presentation of selected investment and project opportunities in Bangladesh.",
        eid="inv_sub"
    )
    invest_header_con = native_container(
        elements=[invest_eyebrow, invest_title, invest_subtitle],
        direction="column",
        custom_css_class="axela-section-header",
        eid="inv_head_con"
    )

    invest_left_title = native_heading("Facilitating Inbound Capital & Strategic Project Development", tag="h3", custom_css_class="invest-box-title")
    invest_left_text = native_text(
        "Depending on the mandate, activities may include preparing an initial opportunity summary, identifying prospective investors or strategic partners, arranging introductions, coordinating preliminary discussions and helping organise commercial information for review."
    )
    invest_pillars_title = native_heading("CORE INVESTMENT FACILITATION PILLARS", tag="span", custom_css_class="invest-pillars-eyebrow")
    invest_pillars_list = native_text(
        "• Opportunity Summary & Concept Structuring<br>"
        "• Local Introductions & Inbound Investor Screening<br>"
        "• Commercial Information Organization & Transaction Alignment"
    )
    invest_left_con = native_container(
        elements=[invest_left_title, invest_left_text, invest_pillars_title, invest_pillars_list],
        direction="column",
        content_width="full",
        custom_css_class="axela-invest-col-left",
        eid="inv_col_left"
    )

    invest_banner = native_image(
        url="https://axelaglobal.com/wp-content/uploads/2026/10/warehouse-logistics-investment.jpg",
        img_id=199,
        alt="Warehouse & Distribution Logistics and Strategic Investment Opportunities",
        custom_css_class="axela-invest-banner-img",
        eid="inv_banner_img"
    )
    invest_notice_title = native_heading("INDEPENDENT DUE DILIGENCE REQUIREMENT", tag="span", custom_css_class="invest-notice-eyebrow")
    invest_notice_text = native_text(
        "All investment opportunities are subject to independent due diligence, applicable regulatory requirements, definitive documentation and agreement between the relevant parties. Website information is not an offer to sell securities or a guarantee of investment performance."
    )
    invest_right_con = native_container(
        elements=[invest_banner, invest_notice_title, invest_notice_text],
        direction="column",
        content_width="full",
        custom_css_class="axela-invest-col-right",
        eid="inv_col_right"
    )

    invest_split_grid = native_container(
        elements=[invest_left_con, invest_right_con],
        direction="row",
        justify="space-between",
        content_width="full",
        custom_css_class="axela-invest-split-grid",
        eid="invest_split_grid"
    )

    invest_boxed_wrap = native_container(
        elements=[invest_header_con, invest_split_grid],
        direction="column",
        content_width="boxed",
        custom_css_class="axela-container-boxed",
        eid="invest_inner_wrap"
    )

    investment_section = native_container(
        elements=[invest_boxed_wrap],
        direction="column",
        content_width="full",
        custom_css_class="axela-section axela-invest-section",
        custom_id="investment",
        eid="sec_investment",
        padding=SECTION_PADDING
    )

    # =========================================================================
    # SECTION 7: ETHICS, COMPLIANCE AND CONFIDENTIALITY (#ethics)
    # Fulfills user annotations: "reduce icon size", "reduce gap"
    # =========================================================================
    ethics_eyebrow = native_heading("07 / GOVERNANCE & INTEGRITY", tag="span", custom_css_class="axela-section-eyebrow", eid="eth_eye")
    ethics_title = native_heading("Ethics, Compliance and Confidentiality", tag="h2", custom_css_class="axela-section-title", eid="eth_h2")
    ethics_subtitle = native_text(
        "AXELA LTD. aims to conduct business with integrity, professionalism and respect for applicable laws and contractual obligations.",
        eid="eth_sub"
    )
    ethics_header_con = native_container(
        elements=[ethics_eyebrow, ethics_title, ethics_subtitle],
        direction="column",
        custom_css_class="axela-section-header",
        eid="eth_head_con"
    )

    ethics_pillars = [
        {
            "tag": "PROFESSIONAL INTEGRITY", "icon": "fas fa-balance-scale",
            "title": "Integrity & Contractual Discipline",
            "desc": "We value clear mandates, accurate commercial documentation and responsible engagement with suppliers, buyers, investors and institutional counterparties."
        },
        {
            "tag": "INFORMATION SECURITY", "icon": "fas fa-lock",
            "title": "Strict Confidentiality Standards",
            "desc": "Protecting counterparty proprietary intelligence, pricing structures, trade strategies and non-disclosure obligations throughout all transaction stages."
        },
        {
            "tag": "STATUTORY ADHERENCE", "icon": "fas fa-shield-alt",
            "title": "Regulatory & Sanctions Compliance",
            "desc": "Product transactions and advisory assignments remain subject to relevant licensing, sanctions screening, customs, tax, and governance compliance requirements."
        }
    ]

    ethics_cards = []
    for idx, ep in enumerate(ethics_pillars):
        ep_tag = native_heading(ep['tag'], tag="span", custom_css_class="ethics-card-tag")
        ep_icon = native_icon(ep['icon'], custom_css_class="ethics-icon-sleek")
        ep_head_row = native_container(
            elements=[ep_tag, ep_icon],
            direction="row",
            justify="space-between",
            align="center",
            custom_css_class="ethics-card-head"
        )
        ep_title = native_heading(ep['title'], tag="h3", custom_css_class="ethics-card-title")
        ep_desc = native_text(ep['desc'])

        card = native_container(
            elements=[ep_head_row, ep_title, ep_desc],
            direction="column",
            content_width="full",
            custom_css_class="axela-ethics-compact-card",
            eid=f"ethics_card_{idx+1}"
        )
        ethics_cards.append(card)

    ethics_grid_con = native_container(
        elements=ethics_cards,
        direction="row",
        wrap="wrap",
        justify="space-between",
        content_width="full",
        custom_css_class="axela-ethics-compact-grid",
        eid="ethics_grid_con"
    )

    ethics_boxed_wrap = native_container(
        elements=[ethics_header_con, ethics_grid_con],
        direction="column",
        content_width="boxed",
        custom_css_class="axela-container-boxed",
        eid="ethics_inner_wrap"
    )

    ethics_section = native_container(
        elements=[ethics_boxed_wrap],
        direction="column",
        content_width="full",
        custom_css_class="axela-section axela-ethics-section",
        custom_id="ethics",
        eid="sec_ethics",
        padding=SECTION_PADDING
    )

    # =========================================================================
    # SECTION 8: CONTACT SECTION (#contact)
    # Fulfills user annotations: "make this contact section like the reference site's contact us section , keep our site's informations .."
    # =========================================================================
    contact_eyebrow = native_heading("08 / GLOBAL TRADING DESK & CONTACT", tag="span", custom_css_class="axela-section-eyebrow", eid="cnt_eye")
    contact_title = native_heading("Contact Us", tag="h2", custom_css_class="axela-section-title", eid="cnt_h2")
    contact_subtitle = native_text(
        "For product supply enquiries, tender opportunities, commercial mandates, investment proposals or advisory requirements, contact AXELA LTD. to discuss the scope and potential next steps.",
        custom_css_class="axela-section-subtitle",
        eid="cnt_sub"
    )
    contact_header_con = native_container(
        elements=[contact_eyebrow, contact_title, contact_subtitle],
        direction="column",
        custom_css_class="axela-section-header",
        eid="cnt_head_con"
    )

    # Left Desk Info
    desk_h4_1 = native_heading("BANGLADESH HEADQUARTERS", tag="h4", custom_css_class="contact-hub-tag")
    desk_p_1 = native_text("Plot- 19, Road- 17, Priyo Prangon Tower<br>Kemal Ataturk Avenue, Banani<br>Dhaka-1213, Bangladesh")

    desk_h4_2 = native_heading("DIRECT PHONE", tag="h4", custom_css_class="contact-hub-tag")
    desk_p_2 = native_text("<a href='tel:+8809658511309' style='color:#E2E8F0; text-decoration:none;'>+88 096585 11309</a>")

    desk_h4_3 = native_heading("GENERAL TRADE INQUIRIES", tag="h4", custom_css_class="contact-hub-tag")
    desk_p_3 = native_text("<a href='mailto:info@axelaglobal.com' style='color:#FFFFFF !important; text-decoration:none; font-weight:600;'>info@axelaglobal.com</a>")

    desk_h4_4 = native_heading("OFFICIAL WEBSITE", tag="h4", custom_css_class="contact-hub-tag")
    desk_p_4 = native_text("<a href='https://axelaglobal.com' style='color:#94A3B8; text-decoration:none;'>axelaglobal.com</a>")

    contact_desk_con = native_container(
        elements=[desk_h4_1, desk_p_1, desk_h4_2, desk_p_2, desk_h4_3, desk_p_3, desk_h4_4, desk_p_4],
        direction="column",
        content_width="full",
        custom_css_class="axela-contact-hub-left",
        eid="contact_hub_left"
    )

    # Right Privacy-Friendly Fluent Form 3 (Zero IP Tracking, SMTP Notifications)
    contact_form_widget = native_shortcode('[fluentform id="3"]', custom_css_class="axela-fluentform-widget", eid="axela_contact_form")

    contact_form_con = native_container(
        elements=[contact_form_widget],
        direction="column",
        content_width="full",
        custom_css_class="axela-contact-form-right axela-contact-box-container",
        eid="contact_form_right"
    )

    contact_split_con = native_container(
        elements=[contact_desk_con, contact_form_con],
        direction="row",
        justify="space-between",
        align="flex-start",
        content_width="full",
        custom_css_class="axela-contact-split-grid",
        eid="contact_split_con"
    )

    contact_boxed_wrap = native_container(
        elements=[contact_header_con, contact_split_con],
        direction="column",
        content_width="boxed",
        custom_css_class="axela-container-boxed",
        eid="contact_inner_wrap"
    )

    contact_section = native_container(
        elements=[contact_boxed_wrap],
        direction="column",
        content_width="full",
        custom_css_class="axela-section axela-contact-section",
        custom_id="contact",
        eid="sec_contact",
        padding=SECTION_PADDING
    )

    # Assemble all 9 sections
    new_sections = [
        hero_section,
        about_section,
        services_section,
        products_section,
        approach_section,
        network_section,
        investment_section,
        ethics_section,
        contact_section
    ]

    save_data = new_sections if isinstance(data, list) else {"content": new_sections}

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(save_data, f, indent=2)
    print(f"Updated {json_path} successfully with {len(new_sections)} sections!")

    # Deploy to WordPress via WPVibe REST API
    BASE_URL = "https://axelaglobal.com"
    AUTH_STR = "admin:FYCY 52pM wknI 1nOf 4RA2 t8zP"
    AUTH_B64 = base64.b64encode(AUTH_STR.encode("ascii")).decode("ascii")
    headers = {
        "Authorization": f"Basic {AUTH_B64}",
        "Content-Type": "application/json"
    }

    def run_wp_cli(command):
        url = f"{BASE_URL}/wp-json/wpvibe/v1/cli/run"
        payload = json.dumps({"command": command}).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers=headers)
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data
        except Exception as e:
            print(f"Error running CLI command '{command}':", e)
            return None

    print("\n=== Updating Homepage Post 28 in WordPress ===")
    page_payload = {
        "id": 28,
        "title": "AXELA LTD. — Trading • Supply • Advisory",
        "status": "publish",
        "page_template": "elementor_header_footer",
        "data": new_sections
    }
    req_page = urllib.request.Request(
        f"{BASE_URL}/wp-json/wpvibe/v1/elementor/save-page",
        data=json.dumps(page_payload).encode("utf-8"),
        headers=headers,
        method="POST"
    )
    try:
        with urllib.request.urlopen(req_page) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            print("WPVibe Homepage update result:", res)
    except Exception as e:
        print("WPVibe Homepage update error:", e)

    # Regenerate Elementor CSS & Flush Cache
    print("\n=== Regenerating Elementor CSS & Data ===")
    res_elem = run_wp_cli("elementor flush-css --regenerate")
    print("Elementor regenerate CSS result:", res_elem)

    # Purge LiteSpeed & Site Cache
    print("\n=== Purging LiteSpeed & Site Cache ===")
    res_purge = run_wp_cli("litespeed-purge all")
    print("Purge cache result:", res_purge)

if __name__ == '__main__':
    build_homepage()
