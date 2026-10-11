# AXELA Limited — Production Website Repository

Official production repository for **AXELA Limited** (`https://axelaglobal.com`).  
This repository contains the complete frontend templates, Elementor page builder data, Fluent Forms configurations, custom design system stylesheets, and deployment utilities.

---

## 🌐 Production Environment & Tech Stack

- **Live URL:** [https://axelaglobal.com](https://axelaglobal.com)
- **CMS:** WordPress 6.8+
- **Theme:** Astra Child Theme
- **Page Builder:** Elementor & Elementor Pro
- **Forms Engine:** Fluent Forms
- **DNS Registrar:** Namecheap
- **Web & Mail Hosting:** Hostinger (Server IP: `145.79.28.40`)
- **Official Mailbox:** `info@axelaglobal.com`

---

## 📁 Repository Directory Structure

```text
├── assets/
│   ├── logo/                       # Official logos (WebP and PNG formats for light/dark headers)
│   └── video/                      # Optimized hero video loop & poster fallback
├── backups/
│   ├── final-production-release/   # Complete frozen state of the live production site
│   │   ├── post-28-homepage.json
│   │   ├── post-28-elementor-data.json
│   │   ├── post-29-header.json
│   │   ├── post-29-elementor-data.json
│   │   ├── post-38-footer.json
│   │   ├── post-38-elementor-data.json
│   │   ├── post-40-customizer-css.json
│   │   └── fluentform-3-complete-final.json
│   └── checkpoint-*/               # Incremental restoration checkpoints
├── custom-css/
│   └── global-dark-theme.css       # Master stylesheet (Obsidian palette, typography, glassmorphism)
├── elementor-templates/
│   ├── homepage-template.json      # Full homepage layout (Post 28)
│   ├── header-template.json        # Sticky glassmorphism global header (Post 29)
│   └── footer-template.json        # 4-column desktop / stacked mobile footer (Post 38)
├── fluentform-config/
│   └── fluentform-3-complete-final.json # Trade Enquiry Form 3 (Fields, Ajax reset & notifications)
├── wp-content/themes/astra-child/  # Astra Child theme files
├── configure_fluent_form3.py       # Fluent Form 3 REST setup script
├── update_email_templates.py       # Auto-responder & Admin notification updater
└── export_complete_production_repository.py # Production sync & export utility
```

---

## 🎨 Design System & Brand Palette

- **Obsidian Dark (Primary Background):** `#060B13`
- **Surface Elevation (Cards/Containers):** `#0b1322` / `#0f172a`
- **Crimson Red (Brand Accent):** `#FF3131`
- **Gold Accent (Subtle Highlights):** `#D4AF37`
- **Slate Text (Muted / Subtext):** `#94A3B8` / `#64748B`
- **Typography:**
  - Headings: `Barlow Condensed` / `Plus Jakarta Sans` / `Inter`
  - Body & Form Tables: `Arial, Helvetica, sans-serif` (Universal email & web safe)

---

## 📋 Features & Components

### 1. Global Sticky Header (Post 29)
- Glassmorphism effect with backdrop blur.
- Live commodities & trade marquee ticker.
- Responsive mobile drawer menu with "Trade Enquiry" direct action button.

### 2. Homepage (Post 28)
- **Hero Section:** High-performance background video loop with WebP poster fallback and dual CTA buttons.
- **Corporate Overview & Stats:** Key performance metrics with responsive grid alignments.
- **Core Operations & Trading Desks:** Energy, Commodities, Project Development, and Investment Advisory cards.
- **Global Sourcing Map:** Interactive trade corridors visualization.
- **Trade Enquiry Desk (Form 3):** Fully integrated contact portal.

### 3. Trade Enquiry Form (Fluent Forms Form 3)
- **Clean Field Partition:** Dedicated, validated `Business Email Address` (`email`) and optional `Phone / WhatsApp` (`phone_whatsapp`).
- **Instant AJAX Reset:** Form instantly blanks out on successful submission without page reload (`samePageFormBehavior: reset_form`).
- **Bidirectional Notifications:**
  - **Customer Auto-Responder:** Executive branded HTML confirmation with a complete trade enquiry summary table sent directly to the customer's Primary Inbox.
  - **Admin Lead Alert:** Instant notification dispatched to `info@axelaglobal.com` and administrative backup mailboxes.

### 4. Global Footer (Post 38)
- 4-column structured layout for desktop.
- Clean vertical stack for mobile viewports.
- Integrated quick navigation links, compliance notices, and copyright.

---

## ⚙️ DNS & Email Deliverability Configuration

Configured on Namecheap pointing to Hostinger:

| Record Type | Host | Value / Target | Notes |
| :--- | :--- | :--- | :--- |
| **A Record** | `@` | `145.79.28.40` | Points apex domain to Hostinger web server |
| **CNAME** | `www` | `axelaglobal.com` | Aliases www traffic to apex |
| **Custom MX** | `@` | `mx1.hostinger.com` (Priority 5) | Primary Hostinger Mail Exchanger |
| **Custom MX** | `@` | `mx2.hostinger.com` (Priority 10) | Secondary Hostinger Mail Exchanger |
| **TXT (SPF)** | `@` | `v=spf1 include:_spf.mail.hostinger.com ~all` | Authorizes Hostinger mail dispatch |
| **CNAME (DKIM)**| `hostingermail-a._domainkey` | `hostingermail-a.dkim.mail.hostinger.com` | Cryptographic signature selector A |
| **CNAME (DKIM)**| `hostingermail-b._domainkey` | `hostingermail-b.dkim.mail.hostinger.com` | Cryptographic signature selector B |
| **CNAME (DKIM)**| `hostingermail-c._domainkey` | `hostingermail-c.dkim.mail.hostinger.com` | Cryptographic signature selector C |
| **TXT (DMARC)**| `_dmarc` | `v=DMARC1; p=none` | Enterprise compliance with Google/Yahoo |

---

## 🚀 How to Clone & Modify for Future Development

### 1. Clone the Repository
```bash
git clone https://github.com/Eti-404/axela-website.git
cd axela-website
```

### 2. Modifying Elementor Templates
- Import templates from `elementor-templates/*.json` directly into **Elementor ➔ Saved Templates ➔ Import Templates**.
- Or use the REST API scripts to programmatically push updates to live pages.

### 3. Modifying Fluent Forms
- The complete form configuration is saved in `fluentform-config/fluentform-3-complete-final.json`.
- Can be imported via **Fluent Forms ➔ Tools ➔ Import Forms**.

### 4. Modifying Custom CSS
- Master CSS is located at `custom-css/global-dark-theme.css`.
- Applies globally through Astra Customizer Additional CSS or Astra Child Theme `style.css`.
