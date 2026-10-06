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

def run_cli(command):
    url = f"{BASE_URL}/wp-json/wpvibe/v1/cli/run"
    payload = json.dumps({"command": command}).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"Error running CLI command '{command}':", e)
        return None

def build_header():
    # Load current header to preserve top ticker container 0
    with open('header_post29_raw.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    ticker_container = data[0]
    ticker_html = """
<style>
/* 1. Theme container overflow fix for native sticky header */
html, body, #page, .hfeed.site {
  overflow-x: clip !important;
  overflow-y: visible !important;
}

header.elementor-location-header,
header {
  position: sticky !important;
  top: 0 !important;
  z-index: 999999 !important;
  width: 100% !important;
}

/* 2. Top Ticker: 28px Slim Height matching petrotraders.com */
.axela-top-ticker-outer {
  background: rgba(6, 14, 22, 0.98) !important;
  border-bottom: 1px solid rgba(26, 107, 107, 0.25) !important;
  width: 100% !important;
  height: 28px !important;
  min-height: 28px !important;
  max-height: 28px !important;
  position: relative !important;
  z-index: 100000 !important;
  display: flex !important;
  align-items: center !important;
  overflow: hidden !important;
  box-sizing: border-box !important;
}

.axela-top-bar-inner {
  max-width: 1400px !important;
  margin: 0 auto !important;
  padding: 0 24px !important;
  height: 28px !important;
  width: 100% !important;
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
  box-sizing: border-box !important;
}

.axela-top-bar-left {
  display: flex !important;
  align-items: center !important;
  height: 28px !important;
  overflow: hidden !important;
  flex: 1 1 auto !important;
  margin-right: 20px !important;
}

.axela-live-markets-badge {
  display: inline-flex !important;
  align-items: center !important;
  gap: 6px !important;
  height: 28px !important;
  padding: 0 10px !important;
  background: rgba(26, 107, 107, 0.18) !important;
  border-right: 1px solid rgba(26, 107, 107, 0.3) !important;
  font-family: 'Barlow Condensed', sans-serif !important;
  font-size: 9px !important;
  letter-spacing: 0.18em !important;
  text-transform: uppercase !important;
  color: #22A8A8 !important;
  font-weight: 700 !important;
  white-space: nowrap !important;
  flex-shrink: 0 !important;
  z-index: 10 !important;
}

.live-pulse-dot {
  width: 5px !important;
  height: 5px !important;
  border-radius: 50% !important;
  background: #22A8A8 !important;
  box-shadow: 0 0 8px #22A8A8 !important;
  animation: pulseDot 1.8s infinite ease-in-out !important;
}

@keyframes pulseDot {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.4; transform: scale(0.8); }
}

.axela-ticker-marquee-wrap {
  flex: 1 !important;
  overflow: hidden !important;
  position: relative !important;
  height: 28px !important;
  display: flex !important;
  align-items: center !important;
}

.axela-ticker-marquee-track {
  display: flex !important;
  align-items: center !important;
  white-space: nowrap !important;
  will-change: transform !important;
}

.ticker-item {
  display: inline-flex !important;
  align-items: center !important;
  gap: 5px !important;
  padding: 0 14px !important;
  height: 28px !important;
  border-right: 1px solid rgba(26, 107, 107, 0.14) !important;
}

.ticker-src {
  font-family: 'Barlow Condensed', sans-serif !important;
  font-size: 9px !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  color: rgba(244, 240, 235, 0.45) !important;
  white-space: nowrap !important;
}

.ticker-name {
  font-family: 'Barlow Condensed', sans-serif !important;
  font-size: 10px !important;
  letter-spacing: 0.06em !important;
  text-transform: uppercase !important;
  color: #F4F0EB !important;
  font-weight: 500 !important;
  white-space: nowrap !important;
}

.ticker-val {
  font-family: 'Barlow Condensed', sans-serif !important;
  font-size: 10.5px !important;
  color: #F4F0EB !important;
  font-weight: 600 !important;
  white-space: nowrap !important;
  letter-spacing: 0.02em !important;
  transition: color 0.4s ease !important;
}

.ticker-val.flash-up {
  color: #22C55E !important;
}

.ticker-val.flash-down {
  color: #EF4444 !important;
}

.ticker-unit {
  font-family: 'Barlow Condensed', sans-serif !important;
  font-size: 8.5px !important;
  color: rgba(244, 240, 235, 0.35) !important;
  white-space: nowrap !important;
}

.ticker-chg {
  font-family: 'Barlow Condensed', sans-serif !important;
  font-size: 9px !important;
  font-weight: 600 !important;
  white-space: nowrap !important;
}

.ticker-chg.up {
  color: #22C55E !important;
}

.ticker-chg.down {
  color: #EF4444 !important;
}

.axela-top-bar-right {
  flex-shrink: 0 !important;
  display: flex !important;
  align-items: center !important;
  height: 28px !important;
}

.axela-dhaka-clock-box {
  display: inline-flex !important;
  align-items: center !important;
  gap: 5px !important;
  height: 28px !important;
  font-family: 'Barlow Condensed', sans-serif !important;
  font-size: 10px !important;
  letter-spacing: 0.08em !important;
  color: rgba(244, 240, 235, 0.75) !important;
  font-weight: 500 !important;
  white-space: nowrap !important;
}

/* 3. Sticky Navbar Container & Inner Layout */
.axela-sticky-header {
  position: sticky !important;
  top: 0 !important;
  z-index: 999999 !important;
  background: rgba(7, 11, 17, 0.96) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
  width: 100% !important;
}

.elementor-element-hdr_inner_con.e-con-boxed > .e-con-inner,
.axela-navbar-inner {
  max-width: 1400px !important;
  width: 100% !important;
  margin: 0 auto !important;
  padding: 6px 24px !important;
  display: flex !important;
  flex-direction: row !important;
  align-items: center !important;
  justify-content: space-between !important;
  box-sizing: border-box !important;
}

.elementor-element-axela_hdr_logo,
.axela-native-logo {
  flex: 0 0 auto !important;
  width: auto !important;
  margin-right: auto !important;
}

.elementor-element-axela_hdr_logo img,
.axela-native-logo img {
  height: 42px !important;
  max-height: 42px !important;
  width: auto !important;
  display: block !important;
}

.elementor-element-hdr_nav_btn_group,
.axela-hdr-nav-btn-group {
  flex: 0 0 auto !important;
  width: auto !important;
  margin-left: auto !important;
  display: flex !important;
  flex-direction: row !important;
  align-items: center !important;
  justify-content: flex-end !important;
  gap: 22px !important;
}

.elementor-element-axela_hdr_nav,
.axela-native-nav {
  flex: 0 0 auto !important;
  width: auto !important;
  margin: 0 !important;
}

/* 4. Smaller Menu Font Size (Reference Site Standard: 10.5px Barlow Condensed) */
.elementor-element-axela_hdr_nav .elementor-item,
.axela-native-nav .elementor-item {
  font-family: 'Barlow Condensed', 'Plus Jakarta Sans', sans-serif !important;
  font-size: 10.5px !important;
  font-weight: 600 !important;
  letter-spacing: 1.2px !important;
  text-transform: uppercase !important;
  color: #94A3B8 !important;
  padding: 6px 10px !important;
  transition: color 0.2s ease !important;
}

.elementor-element-axela_hdr_nav .elementor-item:hover,
.elementor-element-axela_hdr_nav .elementor-item.elementor-item-active,
.axela-native-nav .elementor-item:hover,
.axela-native-nav .elementor-item.elementor-item-active {
  color: #FFFFFF !important;
}

.elementor-element-axela_hdr_btn,
.axela-native-hdr-btn {
  flex: 0 0 auto !important;
  width: auto !important;
  margin: 0 !important;
}

.elementor-element-axela_hdr_btn .elementor-button,
.axela-native-hdr-btn .elementor-button {
  font-family: 'Barlow Condensed', 'Plus Jakarta Sans', sans-serif !important;
  font-size: 10.5px !important;
  font-weight: 700 !important;
  letter-spacing: 1.2px !important;
  text-transform: uppercase !important;
  padding: 7px 16px !important;
}
</style>

<div class="axela-top-ticker-outer" id="axela-top-ticker-outer">
  <div class="axela-top-bar-inner">
    <div class="axela-top-bar-left">
      <div class="axela-live-markets-badge">
        <span class="live-pulse-dot"></span> LIVE MARKETS
      </div>
      <div class="axela-ticker-marquee-wrap" id="axelaTickerWrap">
        <div class="axela-ticker-marquee-track" id="axelaTickerTrack"></div>
      </div>
    </div>
    <div class="axela-top-bar-right">
      <div class="axela-dhaka-clock-box">
        <span>🕒</span>
        <span id="axelaDhakaClock">--:-- -- GMT+6</span>
      </div>
    </div>
  </div>
</div>

<script>
(function() {
  const commodities = [
    { id: "brent", label: "Dated Brent", source: "Platts", price: 74.92, unit: "$/bbl", decimals: 2, vol: 0.18 },
    { id: "wti", label: "WTI Crude", source: "NYMEX", price: 71.30, unit: "$/bbl", decimals: 2, vol: 0.17 },
    { id: "arab_med", label: "Arab Lt Med", source: "Platts", price: 73.80, unit: "$/bbl", decimals: 2, vol: 0.15 },
    { id: "gold", label: "Gold Spot", source: "LBMA", price: 2658.40, unit: "$/oz", decimals: 2, vol: 2.8 },
    { id: "silver", label: "Silver Spot", source: "LBMA", price: 31.85, unit: "$/oz", decimals: 2, vol: 0.16 },
    { id: "jkm", label: "LNG JKM", source: "Platts", price: 13.48, unit: "$/MMBtu", decimals: 3, vol: 0.04 },
    { id: "ttf", label: "TTF Gas", source: "ICE", price: 38.45, unit: "€/MWh", decimals: 2, vol: 0.05 },
    { id: "henry", label: "Henry Hub", source: "NYMEX", price: 2.85, unit: "$/MMBtu", decimals: 3, vol: 0.02 },
    { id: "urea", label: "Urea Granular", source: "Platts", price: 345.00, unit: "$/MT", decimals: 2, vol: 0.45 },
    { id: "gasoil", label: "Rotterdam Gasoil", source: "Platts", price: 720.00, unit: "$/MT", decimals: 2, vol: 1.1 },
    { id: "vlsfo", label: "VLSFO Singapore", source: "Platts", price: 615.00, unit: "$/MT", decimals: 2, vol: 0.9 },
    { id: "coal", label: "RB Coal API 2", source: "Argus", price: 102.40, unit: "$/MT", decimals: 2, vol: 0.3 },
    { id: "iron", label: "Iron Ore 62%", source: "Platts", price: 108.55, unit: "$/dmt", decimals: 2, vol: 0.4 }
  ];

  let state = commodities.map(c => ({
    ...c,
    currentPrice: c.price,
    basePrice: c.price,
    change: 0,
    changePct: 0
  }));

  const track = document.getElementById('axelaTickerTrack');

  function renderItems() {
    if (!track) return;
    let html = '';
    for (let r = 0; r < 2; r++) {
      state.forEach(c => {
        const isUp = c.change >= 0;
        const sign = isUp ? '+' : '';
        const chgClass = isUp ? 'up' : 'down';
        const arrow = isUp ? '▲' : '▼';
        html += `
          <div class="ticker-item" data-id="${c.id}">
            <span class="ticker-src">${c.source}</span>
            <span class="ticker-name">${c.label}</span>
            <span class="ticker-val" id="val_${r}_${c.id}">${c.currentPrice.toFixed(c.decimals)}</span>
            <span class="ticker-unit">${c.unit}</span>
            <span class="ticker-chg ${chgClass}" id="chg_${r}_${c.id}">${arrow} ${sign}${c.changePct.toFixed(2)}%</span>
          </div>
        `;
      });
    }
    track.innerHTML = html;
  }

  renderItems();

  setInterval(() => {
    const count = 1 + Math.floor(Math.random() * 2);
    for (let k = 0; k < count; k++) {
      const idx = Math.floor(Math.random() * state.length);
      const c = state[idx];
      const delta = (Math.random() - 0.48) * 2 * c.vol;
      const oldPrice = c.currentPrice;
      const newPrice = Math.max(c.currentPrice + delta, c.basePrice * 0.7);
      const chg = newPrice - c.basePrice;
      const chgPct = (chg / c.basePrice) * 100;
      c.currentPrice = newPrice;
      c.change = chg;
      c.changePct = chgPct;

      const isUp = newPrice >= oldPrice;
      const flashClass = isUp ? 'flash-up' : 'flash-down';

      for (let r = 0; r < 2; r++) {
        const valEl = document.getElementById(`val_${r}_${c.id}`);
        const chgEl = document.getElementById(`chg_${r}_${c.id}`);
        if (valEl) {
          valEl.textContent = newPrice.toFixed(c.decimals);
          valEl.classList.remove('flash-up', 'flash-down');
          valEl.classList.add(flashClass);
          setTimeout(() => {
            valEl.classList.remove('flash-up', 'flash-down');
          }, 800);
        }
        if (chgEl) {
          const arrow = chg >= 0 ? '▲' : '▼';
          const sign = chg >= 0 ? '+' : '';
          chgEl.className = `ticker-chg ${chg >= 0 ? 'up' : 'down'}`;
          chgEl.textContent = `${arrow} ${sign}${chgPct.toFixed(2)}%`;
        }
      }
    }
  }, 3200);

  let isPaused = false;
  let scrollPos = 0;
  const wrap = document.getElementById('axelaTickerWrap');
  if (wrap) {
    wrap.addEventListener('mouseenter', () => isPaused = true);
    wrap.addEventListener('mouseleave', () => isPaused = false);
  }

  function animate() {
    if (!isPaused && track) {
      scrollPos -= 0.55;
      const halfWidth = track.scrollWidth / 2;
      if (Math.abs(scrollPos) >= halfWidth) {
        scrollPos = 0;
      }
      track.style.transform = `translateX(${scrollPos}px)`;
    }
    requestAnimationFrame(animate);
  }
  requestAnimationFrame(animate);

  function updateDhakaClock() {
    try {
      const now = new Date();
      const timeStr = now.toLocaleTimeString('en-US', {
        timeZone: 'Asia/Dhaka',
        hour: '2-digit',
        minute: '2-digit',
        hour12: true
      });
      const el = document.getElementById('axelaDhakaClock');
      if (el) el.textContent = timeStr + ' GMT+6';
    } catch(e) {}
  }
  updateDhakaClock();
  setInterval(updateDhakaClock, 1000);

  function initStickyHeader() {
    const headerEl = document.querySelector('header.elementor-location-header') || document.querySelector('header');
    const navContainer = document.getElementById('hdr_container_main') || document.querySelector('.axela-sticky-header');

    if (headerEl) {
      headerEl.style.position = 'sticky';
      headerEl.style.top = '0px';
      headerEl.style.zIndex = '999999';
      headerEl.style.width = '100%';
    }

    window.addEventListener('scroll', function() {
      const scrollY = window.pageYOffset || document.documentElement.scrollTop;
      if (scrollY > 28) {
        if (headerEl) headerEl.classList.add('header-scrolled');
        if (navContainer) navContainer.classList.add('nav-scrolled');
      } else {
        if (headerEl) headerEl.classList.remove('header-scrolled');
        if (navContainer) navContainer.classList.remove('nav-scrolled');
      }
    }, { passive: true });
  }

  function initTradeEnquiryCollapse() {
    document.addEventListener('click', function(e) {
      const btn = e.target.closest('a[href="#contact"], .axela-native-hdr-btn, .axela-btn-trade-enquiry');
      if (btn) {
        const ticker = document.getElementById('hdr_top_ticker_con') || document.getElementById('axela-top-ticker-outer');
        if (ticker) {
          ticker.style.transition = 'all 0.4s ease-out';
          ticker.style.overflow = 'hidden';
          ticker.style.maxHeight = '0px';
          ticker.style.minHeight = '0px';
          ticker.style.opacity = '0';
          ticker.style.padding = '0';
          ticker.style.margin = '0';
          ticker.style.border = 'none';
        }
        const contactSec = document.getElementById('contact');
        if (contactSec) {
          e.preventDefault();
          contactSec.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      initStickyHeader();
      initTradeEnquiryCollapse();
    });
  } else {
    initStickyHeader();
    initTradeEnquiryCollapse();
  }
})();
</script>
"""
    ticker_container['elements'][0]['settings']['html'] = ticker_html

    # Native Logo Image Widget (Bigger Height: 42px)
    logo_widget = {
        "id": "axela_hdr_logo",
        "elType": "widget",
        "widgetType": "image",
        "settings": {
            "image": {
                "url": "https://axelaglobal.com/wp-content/uploads/2026/10/axela-logo-dark.webp",
                "id": 19
            },
            "image_size": "full",
            "link_to": "custom",
            "link": {
                "url": "#home",
                "is_external": "",
                "nofollow": ""
            },
            "_css_classes": "axela-native-logo"
        },
        "elements": []
    }

    # Native Nav Menu Widget pointing to Menu 11
    nav_widget = {
        "id": "axela_hdr_nav",
        "elType": "widget",
        "widgetType": "nav-menu",
        "settings": {
            "menu": "11",
            "layout": "horizontal",
            "align_items": "center",
            "pointer": "underline",
            "indicator": "classic",
            "toggle": "burger",
            "toggle_align": "right",
            "full_width": "yes",
            "text_align": "aside",
            "dropdown": "tablet",
            "breakpoint": "tablet",
            "_css_classes": "axela-native-nav"
        },
        "elements": []
    }

    # Native CTA Button Widget
    cta_btn_widget = {
        "id": "axela_hdr_btn",
        "elType": "widget",
        "widgetType": "button",
        "settings": {
            "text": "TRADE ENQUIRY",
            "link": {
                "url": "#contact",
                "is_external": "",
                "nofollow": ""
            },
            "selected_icon": {
                "value": "fas fa-arrow-right",
                "library": "fa-solid"
            },
            "icon_align": "right",
            "_css_classes": "axela-native-hdr-btn axela-btn-teal"
        },
        "elements": []
    }

    # Group for nav items and CTA button locked right
    nav_and_btn_group = {
        "id": "hdr_nav_btn_group",
        "elType": "container",
        "settings": {
            "content_width": "full",
            "flex_direction": "row",
            "flex_wrap": "nowrap",
            "align_items": "center",
            "justify_content": "flex-end",
            "gap": {"unit": "px", "size": 22},
            "_css_classes": "axela-hdr-nav-btn-group"
        },
        "elements": [
            nav_widget,
            cta_btn_widget
        ]
    }

    # Inner container for navbar (max-width 1400px, flex row space-between)
    navbar_inner_container = {
        "id": "hdr_inner_con",
        "elType": "container",
        "settings": {
            "content_width": "boxed",
            "width": {"unit": "px", "size": 1400},
            "flex_direction": "row",
            "flex_wrap": "nowrap",
            "justify_content": "space-between",
            "align_items": "center",
            "padding": {"unit": "px", "top": "12", "right": "24", "bottom": "12", "left": "24", "isLinked": False},
            "_css_classes": "axela-navbar-inner"
        },
        "elements": [
            logo_widget,
            nav_and_btn_group
        ]
    }

    # Main Header Container (sticky, background #040911, border-bottom)
    main_nav_container = {
        "id": "hdr_container_main",
        "elType": "container",
        "settings": {
            "content_width": "full",
            "width": {"unit": "%", "size": 100},
            "padding": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True},
            "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True},
            "background_background": "classic",
            "background_color": "#040911",
            "position": "sticky",
            "z_index": 99999,
            "_css_classes": "axela-sticky-header"
        },
        "elements": [
            navbar_inner_container
        ]
    }

    new_header_data = [
        ticker_container,
        main_nav_container
    ]

    print("\n=== Updating Header Post 29 in WordPress ===")
    payload = {
        "id": 29,
        "title": "AXELA LTD. — Global Dark Header",
        "status": "publish",
        "data": new_header_data
    }
    req = urllib.request.Request(
        f"{BASE_URL}/wp-json/wpvibe/v1/elementor/save-page",
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST"
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        print("WPVibe Header update result:", res)

    print("\n=== Regenerating Elementor CSS & Flushing Cache ===")
    res_elem = run_cli("elementor flush-css --regenerate")
    print("Elementor CSS flush:", res_elem)
    res_purge = run_cli("litespeed-purge all")
    print("LiteSpeed purge:", res_purge)

if __name__ == '__main__':
    build_header()
