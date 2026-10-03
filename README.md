# AXELA LTD. — Official Website

> **Trading • Supply • Commercial Brokerage • Investment & Advisory**

This repository maintains the version-controlled assets, custom themes, templates, and styling for the official website of **AXELA LTD.** (`https://axelaglobal.com`).

---

## 🛠 Tech Stack
- **CMS:** WordPress
- **Base Theme:** Astra
- **Page Builder:** Elementor Pro (Modern Flexbox Containers)
- **Design System:** Obsidian Dark Aesthetic inspired by institutional commodity trading houses (`petrotraders.com`)
- **Typography & Brand:** Custom Ultra-HD Dark-mode adapted Axela Logo, Cormorant / Inter clean typography, Crimson Red Brand Accents (`#E52E2E`)

---

## 🌳 Git Branching Strategy
We adhere to a strict multi-branch development lifecycle:

1. **`main`**: Production-ready, stable releases only. Direct commits and pushes to `main` are strictly prohibited.
2. **`develop`**: The primary integration branch where all tested features are aggregated.
3. **`feature/*`**: Individual feature branches created for each development milestone.
   - `feature/setup-and-assets` (Logo processing, theme setup, design tokens)
   - `feature/header-and-nav` (Transparent sticky header, mobile drawer, anchor navigation)
   - `feature/hero-section` (Video loop background, typography, CTA buttons)
   - `feature/about-section` (Company profile, core value cards)
   - `feature/services-section` (8 institutional service grids)
   - `feature/products-section` (6 trading categories & commodity specifications)
   - `feature/approach-and-roadmap` (5-step commercial process)
   - `feature/investment-and-ethics` (Investment origination & compliance trust statements)
   - `feature/enquiry-form` (12-field Elementor Pro interactive trade form)
   - `feature/contact-and-footer` (Corporate contact info & multi-column footer)

---

## 🔒 Security & Privacy Protocol
- All WordPress core files, `wp-config.php`, sensitive environment variables, secrets, and database credentials are excluded via `.gitignore`.
- Only theme customizations, custom CSS, assets, and Elementor JSON template exports are tracked in version control.
