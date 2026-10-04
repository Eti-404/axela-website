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

def native_icon(icon_class="fas fa-arrow-right", custom_css_class='', eid=None):
    settings = {
        "selected_icon": {
            "value": icon_class,
            "library": "fa-solid"
        },
        "view": "default"
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

def native_container(elements=None, direction='column', wrap='nowrap', justify='flex-start', align='stretch', content_width='full', custom_css_class='', custom_id='', eid=None):
    settings = {
        "content_width": content_width,
        "flex_direction": direction,
        "flex_wrap": wrap,
        "justify_content": justify,
        "align_items": align
    }
    if custom_css_class:
        settings["_css_classes"] = custom_css_class
    if custom_id:
        settings["_element_id"] = custom_id

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
      background: rgba(26, 188, 156, 0.12);
      border-color: #1ABC9C;
      color: #FFFFFF;
      box-shadow: 0 0 16px rgba(26, 188, 156, 0.25);
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
      border: 1px solid rgba(26, 188, 156, 0.25);
      padding: 6px 12px;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 10.5px;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: #5EEAD4;
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
      background: #10B981;
      box-shadow: 0 0 8px #10B981;
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
    .axela-hub-card {
      position: absolute;
      top: 16px;
      right: 16px;
      width: 320px;
      max-width: calc(100% - 32px);
      background: rgba(11, 20, 32, 0.95);
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 18px 20px;
      backdrop-filter: blur(14px);
      box-shadow: 0 20px 45px rgba(0, 0, 0, 0.6);
      border-radius: 4px;
      z-index: 10;
      transition: opacity 0.25s ease, transform 0.25s ease;
    }
    .axela-hub-card.hidden {
      opacity: 0;
      pointer-events: none;
      transform: translateY(-8px);
    }
    .axela-hub-type-row {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 6px;
    }
    .axela-hub-type-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      flex-shrink: 0;
    }
    .axela-hub-type-text {
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 10.5px;
      font-weight: 700;
      letter-spacing: 0.18em;
      text-transform: uppercase;
    }
    .axela-hub-title {
      font-family: 'Cormorant Garamond', Georgia, serif;
      font-size: 22px;
      color: #FFFFFF;
      font-weight: 600;
      line-height: 1.2;
      margin-bottom: 8px;
    }
    .axela-hub-desc {
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 12.5px;
      color: #94A3B8;
      line-height: 1.6;
      margin-bottom: 12px;
    }
    .axela-hub-meta {
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding-top: 8px;
      display: flex;
      justify-content: space-between;
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 10px;
      letter-spacing: 0.12em;
      color: #64748B;
      text-transform: uppercase;
    }
    .axela-hub-close {
      cursor: pointer;
      color: #2DD4BF;
      transition: color 0.2s;
    }
    .axela-hub-close:hover {
      color: #5EEAD4;
    }
    .interactive-node {
      cursor: pointer;
      pointer-events: all;
    }
    @media (max-width: 768px) {
      .axela-map-canvas-box {
        aspect-ratio: 16 / 10;
      }
      .axela-hub-card {
        top: auto;
        bottom: 8px;
        right: 8px;
        left: 8px;
        width: auto;
        padding: 12px 14px;
      }
      .axela-hub-title { font-size: 18px; }
      .axela-hub-desc { font-size: 11px; margin-bottom: 6px; }
      .axela-map-legend { display: none; }
    }
  </style>

  <div class="axela-routes-bar">
    <div class="axela-routes-tabs" id="axela-routes-tabs">
      <button class="axela-route-tab-btn active" data-tab="crude">
        <i class="fas fa-oil-can" style="font-size: 12px;"></i> Crude Oil Routes
      </button>
      <button class="axela-route-tab-btn" data-tab="lng">
        <i class="fas fa-fire-flame-simple" style="font-size: 12px;"></i> LNG &amp; Gas
      </button>
      <button class="axela-route-tab-btn" data-tab="defense">
        <i class="fas fa-shield-halved" style="font-size: 12px;"></i> Defense Logistics
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

    <!-- Active Hub Detail Floating Card -->
    <div class="axela-hub-card" id="axela-hub-card">
      <div class="axela-hub-type-row">
        <span class="axela-hub-type-dot" id="axela-card-dot" style="background: #1ABC9C;"></span>
        <span class="axela-hub-type-text" id="axela-card-type" style="color: #1ABC9C;">PRIMARY STRATEGIC HUB</span>
      </div>
      <h3 class="axela-hub-title" id="axela-card-title">Chattogram &amp; Matarbari Deep Sea Port</h3>
      <p class="axela-hub-desc" id="axela-card-desc">Axela's primary South Asian commercial and maritime anchor in the Bay of Bengal, coordinating high-volume physical discharge of petroleum, bulk fertilizers, LNG, and industrial feedstocks.</p>
      <div class="axela-hub-meta">
        <span>STATUS: ACTIVE DISCHARGE</span>
        <span class="axela-hub-close" onclick="closeAxelaCard()">CLICK TO CLOSE ✕</span>
      </div>
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
      <div class="axela-legend-item"><span class="axela-legend-dot" style="background: #E5A93C;"></span> Crude / Sourcing</div>
      <div class="axela-legend-item"><span class="axela-legend-dot" style="background: #1ABC9C;"></span> Refined &amp; Distribution</div>
      <div class="axela-legend-item"><span class="axela-legend-dot" style="background: #38BDF8;"></span> LNG &amp; Gas</div>
      <div class="axela-legend-item"><span class="axela-legend-dot" style="background: #F43F5E;"></span> Defense Logistics</div>
    </div>
  </div>
</div>

<script>
(function() {
  const HUB_DATA = {
    chattogram: {
      id: "chattogram", cx: 728, cy: 222, color: "#1ABC9C",
      type: "Primary South Asian Gateway · Bangladesh",
      name: "Chattogram & Matarbari Deep Sea Port",
      desc: "Axela Global's commercial and maritime anchor in the Bay of Bengal, coordinating high-volume physical discharge of petroleum, bulk fertilizers, LNG, and industrial feedstocks."
    },
    fujairah: {
      id: "fujairah", cx: 640, cy: 230, color: "#E5A93C",
      type: "Crude Export & Bunkering Hub · Middle East",
      name: "Ras Tanura & Fujairah Terminal",
      desc: "Core Arabian Gulf procurement and offshore blending terminal handling heavy sour, Arab Light, and marine fuel bunkering directly feeding Asian and European demand."
    },
    rotterdam: {
      id: "rotterdam", cx: 477, cy: 140, color: "#1ABC9C",
      type: "European Refining & Distribution · Netherlands",
      name: "Rotterdam ARA Hub",
      desc: "Europe's largest refining and inland waterway distribution node. Central discharge point for Atlantic Basin arbitrage cargoes, ultra-low sulfur diesel, and chemical feedstocks."
    },
    us_gulf: {
      id: "us_gulf", cx: 220, cy: 205, color: "#1ABC9C",
      type: "North American Liquidity Desk · Houston / New Orleans",
      name: "US Gulf Coast Energy Corridor",
      desc: "Primary origination hub for WTI crude, LNG export terminals (Sabine Pass / Corpus Christi), and strategic refined products bound for transatlantic corridors."
    },
    singapore: {
      id: "singapore", cx: 788, cy: 278, color: "#E5A93C",
      type: "Asian Pricing & Bunkering Node · Straits",
      name: "Singapore Straits Trading Hub",
      desc: "The nerve center of Asian physical cargo arbitrage, fuel oil price discovery, and regional transshipment across Southeast and East Asia."
    },
    west_africa: {
      id: "west_africa", cx: 472, cy: 302, color: "#1ABC9C",
      type: "Atlantic Sweet Crude Basin · Nigeria / Angola",
      name: "West Africa Marine Terminals",
      desc: "Major offshore lifting origin for high-yield sweet grades (Bonny Light, Qua Iboe) feeding European refinery grids and Asian spot tenders."
    },
    suez: {
      id: "suez", cx: 565, cy: 203, color: "#E5A93C",
      type: "Strategic Chokepoint & Regional Desk · Egypt",
      name: "Suez Maritime Control & Cairo Desk",
      desc: "Critical transit coordination desk ensuring scheduled passage, canal bunkering, and real-time risk hedging through the Suez-Red Sea maritime corridor."
    },
    qatar: {
      id: "qatar", cx: 635, cy: 222, color: "#38BDF8",
      type: "LNG Export Superhub · Arabian Gulf",
      name: "Ras Laffan LNG Terminal",
      desc: "Global epicenter of liquefied natural gas production, facilitating multi-year term agreements and flexible spot cargo supply to Bangladesh, India, and Europe."
    },
    defense_hq: {
      id: "defense_hq", cx: 230, cy: 193, color: "#F43F5E",
      type: "Defense & Strategic Procurement Command",
      name: "US / NATO Procurement Liaison Desk",
      desc: "Dedicated operations unit managing Mil-Spec fuel procurement (F-76, JP-8), secure supply chains, and rapid-response logistical contracts."
    },
    black_sea: {
      id: "black_sea", cx: 543, cy: 157, color: "#F43F5E",
      type: "Forward Defense Logistics Node · Eastern Europe",
      name: "Constanta Operations & Logistics Depot",
      desc: "Secure tactical supply base managing forward fuel stockpiles, pipeline interconnection, and high-priority logistics under defense contracts."
    }
  };

  const ROUTES_BY_TAB = {
    crude: [
      { id: "c1", d: "M 640 230 Q 720 310 788 278", color: "#E5A93C", dur: 14 },
      { id: "c2", d: "M 640 230 Q 685 240 728 222", color: "#E5A93C", dur: 12 },
      { id: "c3", d: "M 640 230 Q 600 280 565 203 Q 525 170 477 140", color: "#1ABC9C", dur: 18 },
      { id: "c4", d: "M 472 302 Q 380 255 220 205", color: "#E5A93C", dur: 16 },
      { id: "c5", d: "M 220 205 Q 348 148 477 140", color: "#1ABC9C", dur: 15 },
      { id: "c6", d: "M 640 230 Q 565 290 472 302", color: "#E5A93C", dur: 14 }
    ],
    lng: [
      { id: "l1", d: "M 635 222 Q 560 270 467 138", color: "#38BDF8", dur: 17 },
      { id: "l2", d: "M 220 205 Q 342 162 477 140", color: "#38BDF8", dur: 14 },
      { id: "l3", d: "M 635 222 Q 680 230 728 222", color: "#38BDF8", dur: 10 },
      { id: "l4", d: "M 635 222 Q 720 255 788 278", color: "#38BDF8", dur: 13 }
    ],
    defense: [
      { id: "d1", d: "M 230 193 Q 390 148 543 157", color: "#F43F5E", dur: 14 },
      { id: "d2", d: "M 230 193 Q 395 260 565 203", color: "#F43F5E", dur: 15 },
      { id: "d3", d: "M 565 203 Q 640 215 728 222", color: "#F43F5E", dur: 12 },
      { id: "d4", d: "M 565 203 Q 530 240 472 302", color: "#F43F5E", dur: 11 }
    ],
    offices: [
      { id: "o1", d: "M 728 222 Q 685 226 640 230", color: "#1ABC9C", dur: 10 },
      { id: "o2", d: "M 640 230 Q 560 180 477 140", color: "#1ABC9C", dur: 12 },
      { id: "o3", d: "M 728 222 Q 755 250 788 278", color: "#1ABC9C", dur: 10 },
      { id: "o4", d: "M 477 140 Q 348 160 220 205", color: "#1ABC9C", dur: 14 }
    ]
  };

  const HUBS_BY_TAB = {
    crude: ["chattogram", "fujairah", "rotterdam", "us_gulf", "singapore", "west_africa", "suez"],
    lng: ["chattogram", "qatar", "rotterdam", "us_gulf", "singapore"],
    defense: ["defense_hq", "black_sea", "suez", "chattogram", "west_africa"],
    offices: ["chattogram", "fujairah", "rotterdam", "us_gulf", "singapore"]
  };

  let currentTab = 'crude';

  window.showAxelaHub = function(hubId) {
    const hub = HUB_DATA[hubId];
    if (!hub) return;
    const card = document.getElementById('axela-hub-card');
    const dot = document.getElementById('axela-card-dot');
    const type = document.getElementById('axela-card-type');
    const title = document.getElementById('axela-card-title');
    const desc = document.getElementById('axela-card-desc');
    if (!card) return;

    dot.style.background = hub.color;
    type.style.color = hub.color;
    type.textContent = hub.type;
    title.textContent = hub.name;
    desc.textContent = hub.desc;
    card.classList.remove('hidden');
  };

  window.closeAxelaCard = function() {
    const card = document.getElementById('axela-hub-card');
    if (card) card.classList.add('hidden');
  };

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

      g.addEventListener("mouseenter", function() { window.showAxelaHub(id); });
      g.addEventListener("click", function() { window.showAxelaHub(id); });

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

def generate_contact_form_html():
    return """
<div class="axela-contact-form-wrapper">
  <style>
    .axela-contact-form-wrapper {
      background: #0B1320;
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 36px 32px;
      border-radius: 4px;
      box-shadow: 0 20px 45px rgba(0, 0, 0, 0.4);
    }
    .axela-form-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin-bottom: 16px;
    }
    .axela-form-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-bottom: 16px;
    }
    .axela-form-label {
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 10.5px;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #2DD4BF;
      font-weight: 700;
    }
    .axela-form-input,
    .axela-form-select,
    .axela-form-textarea {
      width: 100%;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #FFFFFF;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 13.5px;
      padding: 11px 14px;
      border-radius: 2px;
      outline: none;
      transition: all 0.25s ease;
      box-sizing: border-box;
    }
    .axela-form-select option {
      background: #0B1320;
      color: #FFFFFF;
    }
    .axela-form-input:focus,
    .axela-form-select:focus,
    .axela-form-textarea:focus {
      border-color: #2DD4BF;
      background: rgba(255, 255, 255, 0.07);
      box-shadow: 0 0 12px rgba(45, 212, 191, 0.2);
    }
    .axela-form-textarea {
      min-height: 90px;
      resize: vertical;
    }
    .axela-form-submit-btn {
      width: 100%;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      background: #168B8D;
      border: 1px solid rgba(45, 212, 191, 0.4);
      color: #FFFFFF;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      padding: 13px 24px;
      border-radius: 2px;
      cursor: pointer;
      transition: all 0.25s ease;
      box-shadow: 0 4px 18px rgba(22, 139, 141, 0.35);
    }
    .axela-form-submit-btn:hover {
      background: #1ABC9C;
      color: #FFFFFF;
      box-shadow: 0 6px 24px rgba(26, 188, 156, 0.5);
      transform: translateY(-1px);
    }
    @media (max-width: 600px) {
      .axela-form-row {
        grid-template-columns: 1fr;
        gap: 0;
      }
      .axela-contact-form-wrapper {
        padding: 24px 18px;
      }
    }
  </style>

  <form id="axela-trade-enquiry-form" onsubmit="event.preventDefault(); alert('Trade enquiry submitted. Our trading desk will contact you within 24 business hours.');">
    <div class="axela-form-row">
      <div class="axela-form-group">
        <label class="axela-form-label">Full Name &amp; Title</label>
        <input type="text" class="axela-form-input" placeholder="e.g. Johnathan Doe, Principal" required />
      </div>
      <div class="axela-form-group">
        <label class="axela-form-label">Corporate Email</label>
        <input type="email" class="axela-form-input" placeholder="desk@company.com" required />
      </div>
    </div>

    <div class="axela-form-row">
      <div class="axela-form-group">
        <label class="axela-form-label">Commodity / Trading Division</label>
        <select class="axela-form-select" required>
          <option value="" disabled selected>Select Sourcing Division</option>
          <option value="energy">Energy &amp; Petroleum Products</option>
          <option value="petrochem">Petrochemical Feedstocks</option>
          <option value="fertilizer">Fertilizers &amp; Agrochemicals</option>
          <option value="metals">Industrial Metals &amp; Minerals</option>
          <option value="defense">Defense &amp; Strategic Logistics</option>
          <option value="advisory">Corporate Advisory &amp; Inbound Capital</option>
        </select>
      </div>
      <div class="axela-form-group">
        <label class="axela-form-label">Target Volume / Delivery Incoterm</label>
        <input type="text" class="axela-form-input" placeholder="e.g. 50,000 MT / CIF Chattogram" />
      </div>
    </div>

    <div class="axela-form-group">
      <label class="axela-form-label">Commercial Specifications &amp; Inquiry Scope</label>
      <textarea class="axela-form-textarea" placeholder="Detail specific grade specifications, required delivery timeline, and counterpart terms..."></textarea>
    </div>

    <button type="submit" class="axela-form-submit-btn">
      <span>Submit Trade Enquiry</span>
      <i class="fas fa-arrow-right"></i>
    </button>
  </form>
</div>
"""

def build_homepage():
    json_path = r'c:\xampp\htdocs\axela-local\elementor-templates\homepage-template.json'
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if isinstance(data, list):
        elements = data
    else:
        elements = data.get('content', [])

    # Keep Hero section (element 0)
    hero_section = elements[0]

    # =========================================================================
    # SECTION 1: ABOUT US (#about) - 100% NATIVE ELEMENTOR, CLEAN & SIMPLE
    # Fulfills user annotation: "Dont need to add this section, keep it simple"
    # =========================================================================
    about_eyebrow = native_heading("01 / ABOUT AXELA GLOBAL", tag="span", custom_css_class="axela-section-eyebrow", eid="abt_eye")
    about_title = native_heading("Connecting Trade, Product Supply and Commercial Advisory", tag="h2", custom_css_class="axela-section-title", eid="abt_h2")
    
    about_narrative_1 = native_text(
        "AXELA LTD. works at the intersection of international trade, product supply and commercial advisory. Our role is to help identify opportunities, connect relevant counterparties, and coordinate the commercial steps required to move complex physical transactions forward.",
        custom_css_class="axela-lead-text",
        eid="abt_p1"
    )
    about_narrative_2 = native_text(
        "We aim to build enduring business relationships founded on transparent communication, professional conduct, strict confidentiality, and a practical, on-the-ground understanding of buyer and supplier requirements across Bangladesh and international markets.",
        eid="abt_p2"
    )

    # 4 Scale metrics (Just like petrotraders scale row)
    metrics_data = [
        {"val": "20M+", "lbl": "MT Moved / Sourced Annually Across Global Energy & Commodity Corridors"},
        {"val": "70+", "lbl": "Tier-1 International Financial, Banking & Trade Finance Institutions"},
        {"val": "25+", "lbl": "Years Collective Physical Trading & Cross-Border Supply Execution"},
        {"val": "4", "lbl": "Continents with Active Strategic Operations & Origin Desks"}
    ]

    metric_cols = []
    for idx, m in enumerate(metrics_data):
        m_val = native_heading(m["val"], tag="h3", custom_css_class="axela-stat-val")
        m_lbl = native_text(m["lbl"], custom_css_class="axela-stat-lbl")
        card = native_container(
            elements=[m_val, m_lbl],
            direction="column",
            content_width="full",
            custom_css_class="axela-scale-metric-card",
            eid=f"scale_card_{idx+1}"
        )
        metric_cols.append(card)

    scale_grid_con = native_container(
        elements=metric_cols,
        direction="row",
        wrap="nowrap",
        justify="space-between",
        content_width="full",
        custom_css_class="axela-scale-metrics-grid",
        eid="scale_grid_con"
    )

    # Action buttons row
    btn_consult = native_button("Request a Trading Consultation", link="#contact", icon_class="fas fa-arrow-right", custom_css_class="axela-btn-teal", eid="abt_btn_consult")
    btn_categories = native_button("Explore Trading Categories", link="#products", icon_class="fas fa-arrow-right", custom_css_class="axela-btn-ghost", eid="abt_btn_cat")
    
    actions_row = native_container(
        elements=[btn_consult, btn_categories],
        direction="row",
        wrap="wrap",
        align="center",
        custom_css_class="axela-about-actions-row",
        eid="abt_act_row"
    )

    about_boxed_wrap = native_container(
        elements=[about_eyebrow, about_title, about_narrative_1, about_narrative_2, scale_grid_con, actions_row],
        direction="column",
        content_width="boxed",
        custom_css_class="axela-container-boxed",
        eid="about_inner_wrap"
    )

    about_section = native_container(
        elements=[about_boxed_wrap],
        direction="column",
        content_width="full",
        custom_css_class="axela-section axela-about-section",
        custom_id="about",
        eid="sec_about"
    )

    # =========================================================================
    # SECTION 2: OUR SERVICES (#services)
    # Fulfills user annotations: "Reduce the icon's size & little more gap between the cards & action button in blue/ash type colour"
    # =========================================================================
    services_eyebrow = native_heading("02 / CORE CAPABILITIES", tag="span", custom_css_class="axela-section-eyebrow", eid="svc_eye")
    services_title = native_heading("Our Services", tag="h2", custom_css_class="axela-section-title", eid="svc_h2")
    services_subtitle = native_text(
        "Sourcing and coordinating supply of petroleum products, commercial brokerage, tender support and advisory services.",
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
            "desc": "Sourcing and coordinating supply of petroleum products, petrochemicals, fertilizers, industrial chemicals and other agreed commodities, subject to product availability and contract terms."
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
            "desc": "Supporting international investors with local introductions, opportunity screening, business coordination and communication with relevant counterparties."
        },
        {
            "num": "07", "icon": "fas fa-balance-scale",
            "title": "Corporate Advisory and Financial Structuring",
            "desc": "Commercial support for business plans, transaction structures, strategic partnerships, capital proposals and financing discussions with professional advisers."
        },
        {
            "num": "08", "icon": "fas fa-truck-moving",
            "title": "Transaction and Logistics Coordination",
            "desc": "Coordinating commercial documentation, delivery requirements, shipment-related communication and counterparty follow-up as agreed for each transaction."
        }
    ]

    service_cards = []
    for idx, s in enumerate(services_data):
        card_id = f"svc_card_{idx+1}"
        head_num = native_heading(f"{s['num']} / SERVICE", tag="span", custom_css_class="service-card-num")
        head_icon = native_icon(s['icon'], custom_css_class="service-card-icon-sleek")
        head_row = native_container(
            elements=[head_num, head_icon],
            direction="row",
            justify="space-between",
            align="center",
            custom_css_class="service-card-head"
        )
        c_title = native_heading(s['title'], tag="h3", custom_css_class="service-card-title")
        c_desc = native_text(s['desc'])
        # Blue/ash type button per user instruction
        c_btn = native_button("DISCUSS SUPPLY", link="#contact", icon_class="fas fa-arrow-right", custom_css_class="axela-btn-ash", eid=f"svc_btn_{idx+1}")

        card = native_container(
            elements=[head_row, c_title, c_desc, c_btn],
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
        eid="sec_services"
    )

    # =========================================================================
    # SECTION 3: PRODUCTS & TRADING CATEGORIES (#products)
    # Fulfills user annotations:
    # "No need these CAT 1,2,3 ...."
    # "reduce icon size and make them more closer to their headings , and add icons to every section/card here"
    # "Add any relevent better image" -> high res refinery banner
    # =========================================================================
    products_eyebrow = native_heading("03 / COMMODITY SCOPE", tag="span", custom_css_class="axela-section-eyebrow", eid="prod_eye")
    products_title = native_heading("Products and Trading Categories", tag="h2", custom_css_class="axela-section-title", eid="prod_h2")
    products_subtitle = native_text(
        "AXELA LTD. may consider sourcing and supply enquiries across the following categories, depending on the specific requirement, supplier availability, applicable permissions and transaction terms.",
        eid="prod_sub"
    )
    products_header_con = native_container(
        elements=[products_eyebrow, products_title, products_subtitle],
        direction="column",
        custom_css_class="axela-section-header",
        eid="prod_head_con"
    )

    # High-res refinery banner
    products_banner = native_image(
        url="https://axelaglobal.com/wp-content/uploads/2026/10/axela-petroleum-refinery-banner.webp",
        img_id=95,
        alt="Industrial Petroleum Refinery and Energy Sourcing Operations",
        custom_css_class="axela-banner-img-styled",
        eid="prod_banner_img"
    )
    products_banner_con = native_container(
        elements=[products_banner],
        direction="column",
        content_width="full",
        custom_css_class="axela-banner-container",
        eid="prod_banner_con"
    )

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
        c_btn = native_button("ENQUIRE CATEGORY", link="#contact", icon_class="fas fa-arrow-right", custom_css_class="axela-btn-link-ash")

        card = native_container(
            elements=[c_title_row, c_desc, c_btn],
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

    # Compliance Note
    comp_icon = native_icon("fas fa-shield-halved", custom_css_class="compliance-icon-sleek")
    comp_title = native_heading("Commercial Sourcing Assessment Standard", tag="h4", custom_css_class="compliance-title")
    comp_text = native_text(
        "Each enquiry should be assessed individually. Product name, grade, specifications, origin, quantity, packing, delivery schedule, Incoterm, inspection requirements and payment terms must be confirmed before any offer is treated as firm."
    )
    compliance_box = native_container(
        elements=[comp_icon, comp_title, comp_text],
        direction="column",
        content_width="full",
        custom_css_class="axela-compliance-note-box",
        eid="prod_compliance_box"
    )

    products_boxed_wrap = native_container(
        elements=[products_header_con, products_banner_con, categories_grid_con, compliance_box],
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
        eid="sec_products"
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
            "step": "02", "icon": "fas fa-users-gear",
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
        eid="sec_approach"
    )

    # =========================================================================
    # SECTION 5: INTERACTIVE GLOBAL TRADE ROUTES MAP (#network / #routes)
    # Fulfills user annotations: "do it like the screen recording of the reference attached here"
    # =========================================================================
    routes_eyebrow = native_heading("05 / GLOBAL PRESENCE & LOGISTICS", tag="span", custom_css_class="axela-section-eyebrow", eid="net_eye")
    routes_title = native_heading("Interactive Global Trade Routes", tag="h2", custom_css_class="axela-section-title", eid="net_h2")
    routes_subtitle = native_text(
        "Tracking high-volume physical crude, refined products, LNG and strategic defense cargo movements across key international maritime corridors.",
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
        eid="sec_network"
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
        url="https://axelaglobal.com/wp-content/uploads/2026/10/port-terminal-infrastructure.webp",
        img_id=86,
        alt="Strategic Port Infrastructure and Investment Opportunities",
        custom_css_class="axela-invest-banner-img",
        eid="inv_banner_img"
    )
    invest_notice_title = native_heading("INDEPENDENT DUE DILIGENCE REQUIREMENT", tag="span", custom_css_class="invest-notice-eyebrow")
    invest_notice_text = native_text(
        "All investment opportunities are subject to independent due diligence, applicable regulatory requirements, definitive documentation and agreement between the relevant parties. Website information is not an offer to sell securities or a guarantee of investment performance."
    )
    invest_cta_btn = native_button("EXPLORE INVESTMENT OPPORTUNITIES", link="#contact", icon_class="fas fa-arrow-right", custom_css_class="axela-btn-teal", eid="inv_cta_btn")
    
    invest_right_con = native_container(
        elements=[invest_banner, invest_notice_title, invest_notice_text, invest_cta_btn],
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
        eid="sec_investment"
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
            "tag": "PROFESSIONAL INTEGRITY", "icon": "fas fa-scale-balanced",
            "title": "Integrity & Contractual Discipline",
            "desc": "We value clear mandates, accurate commercial documentation and responsible engagement with suppliers, buyers, investors and institutional counterparties."
        },
        {
            "tag": "INFORMATION SECURITY", "icon": "fas fa-lock",
            "title": "Strict Confidentiality Standards",
            "desc": "Protecting counterparty proprietary intelligence, pricing structures, trade strategies and non-disclosure obligations throughout all transaction stages."
        },
        {
            "tag": "STATUTORY ADHERENCE", "icon": "fas fa-shield-halved",
            "title": "Regulatory & Sanctions Compliance",
            "desc": "Product transactions and advisory assignments remain subject to relevant licensing, sanctions screening, customs, tax, and anti-bribery compliance requirements."
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
        eid="sec_ethics"
    )

    # =========================================================================
    # SECTION 8: CONTACT SECTION (#contact)
    # Fulfills user annotations: "make this contact section like the reference site's contact us section , keep our site's informations .."
    # =========================================================================
    contact_eyebrow = native_heading("08 / GLOBAL TRADING DESK & CONTACT", tag="span", custom_css_class="axela-section-eyebrow", eid="cnt_eye")
    contact_title = native_heading("Ready to trade with us?", tag="h2", custom_css_class="axela-section-title", eid="cnt_h2")
    contact_subtitle = native_text(
        "For product supply enquiries, tender opportunities, commercial mandates, investment proposals or advisory requirements, connect directly with our trading principals.",
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
    desk_p_1 = native_text("House 12, Road 4, Banani / Gulshan Commercial Zone<br>Dhaka 1213, Bangladesh<br><a href='tel:+8801711000000' style='color:#94A3B8;'>+880 1711-000000</a> · <a href='tel:+88029876543' style='color:#94A3B8;'>+880 2 9876543</a>")

    desk_h4_2 = native_heading("MIDDLE EAST TRADING DESK", tag="h4", custom_css_class="contact-hub-tag")
    desk_p_2 = native_text("Dubai & Fujairah Offshore Operations, UAE<br><a href='tel:+97140000000' style='color:#94A3B8;'>+971 4 000 0000</a>")

    desk_h4_3 = native_heading("ASIA-PACIFIC & EUROPEAN GATEWAYS", tag="h4", custom_css_class="contact-hub-tag")
    desk_p_3 = native_text("Singapore Straits · Rotterdam ARA Hub · Chattogram Port")

    desk_h4_4 = native_heading("GENERAL TRADE INQUIRIES", tag="h4", custom_css_class="contact-hub-tag")
    desk_p_4 = native_text("<a href='mailto:trade@axelaglobal.com' style='color:#FFFFFF; font-weight:600;'>trade@axelaglobal.com</a> · <a href='mailto:info@axelaglobal.com' style='color:#94A3B8;'>info@axelaglobal.com</a>")

    contact_desk_con = native_container(
        elements=[desk_h4_1, desk_p_1, desk_h4_2, desk_p_2, desk_h4_3, desk_p_3, desk_h4_4, desk_p_4],
        direction="column",
        content_width="full",
        custom_css_class="axela-contact-hub-left",
        eid="contact_hub_left"
    )

    # Right interactive trade enquiry form widget
    contact_form_widget = native_html(generate_contact_form_html(), eid="contact_form_widget")

    contact_form_con = native_container(
        elements=[contact_form_widget],
        direction="column",
        content_width="full",
        custom_css_class="axela-contact-form-right",
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
        eid="sec_contact"
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
        "data": save_data
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
