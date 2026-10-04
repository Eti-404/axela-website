import json
import base64
import urllib.request
import re

css_rules = """
/* =============================================================================
   AXELA GLOBAL — MASTER REFINEMENT STYLESHEET (FIX.SVG & PETROTRADERS SPEC)
   Sleek Compact Spacing, Clean Badges, Elegant Icons, Blue/Ash Buttons, Zero Overflow
   ============================================================================= */

/* Universal Section Spacing (Eliminate Dead Margins & Whitespace) */
.axela-section,
.axela-services-section,
.axela-products-section,
.axela-approach-section,
.axela-network-section,
.axela-invest-section,
.axela-ethics-section,
.axela-contact-section,
.axela-about-section {
  padding: 55px 0 !important;
  position: relative !important;
  width: 100% !important;
  border-top: 1px solid rgba(255, 255, 255, 0.05) !important;
  box-sizing: border-box !important;
}

/* Background Themes */
.axela-about-section { background: #070B12 !important; }
.axela-services-section { background: #090E17 !important; }
.axela-products-section { background: #070B12 !important; }
.axela-approach-section { background: #090E17 !important; }
.axela-network-section { background: #070B12 !important; }
.axela-invest-section { background: #090E17 !important; }
.axela-ethics-section { background: #070B12 !important; }
.axela-contact-section { background: #090E17 !important; }

/* Boxed Container 1400px Standard */
.axela-container-boxed,
.axela-container-boxed.e-con {
  max-width: 1400px !important;
  width: 100% !important;
  margin: 0 auto !important;
  padding: 0 24px !important;
  box-sizing: border-box !important;
}

/* Section Header System */
.axela-section-header {
  margin-bottom: 28px !important;
  text-align: left !important;
}

.axela-section-eyebrow,
.axela-section-eyebrow .elementor-heading-title {
  font-family: 'Barlow Condensed', -apple-system, sans-serif !important;
  font-size: 11px !important;
  font-weight: 700 !important;
  letter-spacing: 0.20em !important;
  text-transform: uppercase !important;
  color: #1ABC9C !important;
  margin-bottom: 8px !important;
  display: inline-block !important;
}

.axela-section-title,
.axela-section-title .elementor-heading-title {
  font-family: 'Cormorant Garamond', Georgia, serif !important;
  font-size: 40px !important;
  font-weight: 400 !important;
  line-height: 1.15 !important;
  color: #FFFFFF !important;
  letter-spacing: -0.02em !important;
  margin: 0 0 12px 0 !important;
}

.axela-section-header p,
.axela-section-header .elementor-widget-text-editor {
  font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
  font-size: 14.5px !important;
  font-weight: 400 !important;
  line-height: 1.65 !important;
  color: #94A3B8 !important;
  max-width: 820px !important;
  margin: 0 !important;
}

/* -----------------------------------------------------------------------------
   SECTION 1: ABOUT US REFINEMENT (CLEAN & SIMPLE)
   ----------------------------------------------------------------------------- */
.axela-lead-text p {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 16px !important;
  line-height: 1.75 !important;
  color: #E2E8F0 !important;
  margin-bottom: 12px !important;
}

.axela-scale-metrics-grid {
  display: flex !important;
  flex-direction: row !important;
  flex-wrap: nowrap !important;
  gap: 20px !important;
  margin: 32px 0 !important;
  width: 100% !important;
}

.axela-scale-metric-card {
  flex: 1 1 25% !important;
  width: 25% !important;
  box-sizing: border-box !important;
  background: #0B1320 !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  padding: 24px 20px !important;
  border-radius: 3px !important;
  transition: all 0.3s ease !important;
  position: relative !important;
  overflow: hidden !important;
}

.axela-scale-metric-card:hover {
  border-color: rgba(229, 169, 60, 0.4) !important;
  transform: translateY(-3px) !important;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4) !important;
}

.axela-scale-metric-card::before {
  content: "" !important;
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  width: 100% !important;
  height: 2px !important;
  background: linear-gradient(90deg, transparent, #E5A93C, transparent) !important;
  opacity: 0 !important;
  transition: opacity 0.3s ease !important;
}

.axela-scale-metric-card:hover::before {
  opacity: 1 !important;
}

.axela-stat-val,
.axela-stat-val .elementor-heading-title {
  font-family: 'Cormorant Garamond', Georgia, serif !important;
  font-size: 38px !important;
  font-weight: 600 !important;
  color: #E5A93C !important;
  margin: 0 0 6px 0 !important;
  line-height: 1 !important;
}

.axela-stat-lbl p {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 12px !important;
  line-height: 1.55 !important;
  color: #94A3B8 !important;
  margin: 0 !important;
}

.axela-about-actions-row {
  display: flex !important;
  gap: 16px !important;
  margin-top: 10px !important;
}

/* Infallible Product Category Cards & Headings (Fix.svg [10, 11]) */
[data-id^="cat_card_"],
.axela-category-compact-card {
  background: #0B1320 !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  padding: 24px 22px !important;
  border-radius: 4px !important;
  transition: all 0.3s ease !important;
  box-sizing: border-box !important;
}

[data-id^="cat_card_"]:hover,
.axela-category-compact-card:hover {
  transform: translateY(-3px) !important;
  border-color: rgba(229, 169, 60, 0.4) !important;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.5) !important;
}

[data-id^="cat_card_"] > .e-con,
.category-title-icon-row {
  display: flex !important;
  flex-direction: row !important;
  align-items: center !important;
  justify-content: flex-start !important;
  gap: 12px !important;
  margin-bottom: 12px !important;
  width: 100% !important;
}

[data-id^="cat_card_"] > .e-con > .elementor-widget-icon,
.category-title-icon-row > .elementor-widget-icon {
  width: auto !important;
  flex-shrink: 0 !important;
  margin: 0 !important;
  display: inline-flex !important;
}

[data-id^="cat_card_"] > .e-con > .elementor-widget-icon .elementor-icon,
.category-title-icon-row .elementor-icon {
  font-size: 16px !important;
  color: #2DD4BF !important;
  line-height: 1 !important;
  margin: 0 !important;
}

[data-id^="cat_card_"] > .e-con > .elementor-widget-heading,
.category-title-icon-row > .elementor-widget-heading {
  width: auto !important;
  flex-grow: 1 !important;
  margin: 0 !important;
}

[data-id^="cat_card_"] .elementor-heading-title,
.category-card-title-sleek .elementor-heading-title {
  font-family: 'Cormorant Garamond', Georgia, serif !important;
  font-size: 21px !important;
  font-weight: 600 !important;
  color: #FFFFFF !important;
  margin: 0 !important;
}

/* Form Inputs Dark Aesthetic Fix */
.axela-contact-form-wrapper input,
.axela-contact-form-wrapper select,
.axela-contact-form-wrapper textarea,
#axela-trade-enquiry-form input,
#axela-trade-enquiry-form select,
#axela-trade-enquiry-form textarea {
  background: rgba(255, 255, 255, 0.05) !important;
  color: #FFFFFF !important;
  border: 1px solid rgba(255, 255, 255, 0.12) !important;
}

.axela-contact-form-wrapper input:focus,
.axela-contact-form-wrapper select:focus,
.axela-contact-form-wrapper textarea:focus,
#axela-trade-enquiry-form input:focus,
#axela-trade-enquiry-form select:focus,
#axela-trade-enquiry-form textarea:focus {
  background: rgba(255, 255, 255, 0.08) !important;
  border-color: #2DD4BF !important;
  box-shadow: 0 0 12px rgba(45, 212, 191, 0.25) !important;
}

.axela-contact-form-wrapper input::placeholder,
.axela-contact-form-wrapper textarea::placeholder,
#axela-trade-enquiry-form input::placeholder,
#axela-trade-enquiry-form textarea::placeholder {
  color: #64748B !important;
}

/* Footer Slim Logo Constraint */
.axela-footer-logo {
  max-height: 28px !important;
  width: auto !important;
  max-width: 140px !important;
  display: block !important;
}

/* -----------------------------------------------------------------------------
   SECTION 2: SERVICES REFINEMENT (SLEEK ICONS, BLUE/ASH BUTTONS, 24PX GAP)
   ----------------------------------------------------------------------------- */
.axela-services-compact-grid {
  display: flex !important;
  flex-direction: row !important;
  flex-wrap: wrap !important;
  gap: 24px !important;
  width: 100% !important;
}

.axela-service-compact-card {
  flex: 0 0 calc(25% - 18px) !important;
  max-width: calc(25% - 18px) !important;
  box-sizing: border-box !important;
  background: #0B1320 !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  padding: 24px 20px 20px 20px !important;
  border-radius: 3px !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

.axela-service-compact-card:hover {
  transform: translateY(-4px) !important;
  border-color: rgba(56, 189, 248, 0.4) !important;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.5) !important;
}

.service-card-head {
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
  margin-bottom: 14px !important;
}

.service-card-num,
.service-card-num .elementor-heading-title {
  font-family: ui-monospace, SFMono-Regular, monospace !important;
  font-size: 10px !important;
  font-weight: 700 !important;
  letter-spacing: 0.16em !important;
  color: #64748B !important;
}

/* Sleek compact icon badge */
.service-card-icon-sleek,
.service-card-icon-sleek .elementor-icon {
  width: 34px !important;
  height: 34px !important;
  border-radius: 50% !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  background: rgba(26, 188, 156, 0.1) !important;
  border: 1px solid rgba(26, 188, 156, 0.25) !important;
  color: #2DD4BF !important;
  font-size: 14px !important;
  transition: all 0.25s ease !important;
}

.axela-service-compact-card:hover .service-card-icon-sleek .elementor-icon {
  background: #1ABC9C !important;
  color: #FFFFFF !important;
  transform: scale(1.05) !important;
}

.service-card-title,
.service-card-title .elementor-heading-title {
  font-family: 'Cormorant Garamond', Georgia, serif !important;
  font-size: 21px !important;
  font-weight: 600 !important;
  color: #FFFFFF !important;
  line-height: 1.25 !important;
  margin: 0 0 10px 0 !important;
}

.axela-service-compact-card p,
.axela-service-compact-card .elementor-widget-text-editor {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 12.5px !important;
  line-height: 1.6 !important;
  color: #94A3B8 !important;
  margin: 0 0 18px 0 !important;
  flex-grow: 1 !important;
}

/* Blue / Ash Action Button (User Requirement [3]) */
.axela-btn-ash,
.axela-btn-ash .elementor-button {
  background: rgba(255, 255, 255, 0.04) !important;
  border: 1px solid #475569 !important;
  color: #CBD5E1 !important;
  font-family: 'Barlow Condensed', sans-serif !important;
  font-size: 11px !important;
  font-weight: 700 !important;
  letter-spacing: 0.14em !important;
  text-transform: uppercase !important;
  padding: 8px 14px !important;
  border-radius: 2px !important;
  transition: all 0.25s ease !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 6px !important;
  width: auto !important;
}

.axela-btn-ash:hover,
.axela-btn-ash .elementor-button:hover {
  background: rgba(56, 189, 248, 0.15) !important;
  border-color: #38BDF8 !important;
  color: #FFFFFF !important;
  box-shadow: 0 0 12px rgba(56, 189, 248, 0.3) !important;
}

/* -----------------------------------------------------------------------------
   SECTION 3: PRODUCTS & CATEGORIES (NO "CAT 01", SLEEK ICONS CLOSE TO TITLE)
   ----------------------------------------------------------------------------- */
.axela-banner-container {
  margin-bottom: 24px !important;
  border-radius: 4px !important;
  overflow: hidden !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
}

.axela-banner-img-styled img {
  width: 100% !important;
  max-height: 320px !important;
  object-fit: cover !important;
  display: block !important;
}

.axela-categories-compact-grid {
  display: flex !important;
  flex-direction: row !important;
  flex-wrap: wrap !important;
  gap: 20px !important;
  width: 100% !important;
}

.axela-category-compact-card {
  flex: 0 0 calc(33.333% - 14px) !important;
  max-width: calc(33.333% - 14px) !important;
  box-sizing: border-box !important;
  background: #0B1320 !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  padding: 22px 20px !important;
  border-radius: 3px !important;
  transition: all 0.3s ease !important;
}

.axela-category-compact-card:hover {
  transform: translateY(-3px) !important;
  border-color: rgba(229, 169, 60, 0.4) !important;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5) !important;
}

.category-title-icon-row {
  display: flex !important;
  flex-direction: row !important;
  align-items: center !important;
  gap: 10px !important;
  margin-bottom: 10px !important;
}

.category-icon-inline .elementor-icon {
  font-size: 15px !important;
  color: #2DD4BF !important;
  display: inline-flex !important;
  margin: 0 !important;
  padding: 0 !important;
}

.category-card-title-sleek,
.category-card-title-sleek .elementor-heading-title {
  font-family: 'Cormorant Garamond', Georgia, serif !important;
  font-size: 21px !important;
  font-weight: 600 !important;
  color: #FFFFFF !important;
  line-height: 1.25 !important;
  margin: 0 !important;
}

.axela-category-compact-card p,
.axela-category-compact-card .elementor-widget-text-editor {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 12.5px !important;
  line-height: 1.6 !important;
  color: #94A3B8 !important;
  margin: 0 0 16px 0 !important;
}

.axela-btn-link-ash,
.axela-btn-link-ash .elementor-button {
  background: transparent !important;
  border: none !important;
  padding: 0 !important;
  color: #64748B !important;
  font-family: 'Barlow Condensed', sans-serif !important;
  font-size: 11px !important;
  font-weight: 700 !important;
  letter-spacing: 0.14em !important;
  text-transform: uppercase !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 6px !important;
  transition: color 0.2s ease !important;
}

.axela-category-compact-card:hover .axela-btn-link-ash .elementor-button {
  color: #2DD4BF !important;
}

.axela-compliance-note-box {
  background: rgba(229, 169, 60, 0.05) !important;
  border-left: 3px solid #E5A93C !important;
  padding: 16px 20px !important;
  margin-top: 24px !important;
}

.compliance-title,
.compliance-title .elementor-heading-title {
  font-family: 'Barlow Condensed', sans-serif !important;
  font-size: 11.5px !important;
  font-weight: 700 !important;
  letter-spacing: 0.16em !important;
  text-transform: uppercase !important;
  color: #E5A93C !important;
  margin-bottom: 4px !important;
}

.axela-compliance-note-box p {
  font-size: 12px !important;
  color: #94A3B8 !important;
  line-height: 1.6 !important;
  margin: 0 !important;
}

/* -----------------------------------------------------------------------------
   SECTION 4: APPROACH (COMPACT PADDING, SLEEK ICONS)
   ----------------------------------------------------------------------------- */
.axela-approach-compact-grid {
  display: flex !important;
  flex-direction: row !important;
  gap: 16px !important;
  width: 100% !important;
}

.axela-stage-compact-card {
  flex: 1 1 0 !important;
  background: #0B1320 !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  padding: 20px 16px !important;
  border-radius: 3px !important;
  position: relative !important;
}

.stage-card-step,
.stage-card-step .elementor-heading-title {
  font-family: ui-monospace, SFMono-Regular, monospace !important;
  font-size: 10px !important;
  font-weight: 700 !important;
  letter-spacing: 0.14em !important;
  color: #2DD4BF !important;
}

.stage-icon-sleek .elementor-icon {
  font-size: 14px !important;
  color: #64748B !important;
}

.stage-card-title,
.stage-card-title .elementor-heading-title {
  font-family: 'Cormorant Garamond', Georgia, serif !important;
  font-size: 18px !important;
  font-weight: 600 !important;
  color: #FFFFFF !important;
  line-height: 1.25 !important;
  margin: 10px 0 8px 0 !important;
}

.axela-stage-compact-card p {
  font-size: 12px !important;
  color: #94A3B8 !important;
  line-height: 1.55 !important;
  margin: 0 !important;
}

/* -----------------------------------------------------------------------------
   SECTION 6: INVESTMENT & ETHICS (COMPACT HEIGHTS & BALANCED GAPS)
   ----------------------------------------------------------------------------- */
.axela-invest-split-grid {
  display: flex !important;
  flex-direction: row !important;
  gap: 32px !important;
  align-items: flex-start !important;
}

.axela-invest-col-left,
.axela-invest-col-right {
  flex: 1 1 calc(50% - 16px) !important;
}

.invest-box-title,
.invest-box-title .elementor-heading-title {
  font-family: 'Cormorant Garamond', Georgia, serif !important;
  font-size: 26px !important;
  color: #FFFFFF !important;
  margin-bottom: 12px !important;
}

.invest-pillars-eyebrow,
.invest-pillars-eyebrow .elementor-heading-title,
.invest-notice-eyebrow,
.invest-notice-eyebrow .elementor-heading-title {
  font-family: 'Barlow Condensed', sans-serif !important;
  font-size: 10.5px !important;
  font-weight: 700 !important;
  letter-spacing: 0.16em !important;
  text-transform: uppercase !important;
  color: #E5A93C !important;
  margin-top: 14px !important;
  display: block !important;
}

.axela-ethics-compact-grid {
  display: flex !important;
  flex-direction: row !important;
  gap: 20px !important;
}

.axela-ethics-compact-card {
  flex: 1 1 calc(33.333% - 14px) !important;
  background: #0B1320 !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  padding: 24px 20px !important;
  border-radius: 3px !important;
}

.ethics-card-tag,
.ethics-card-tag .elementor-heading-title {
  font-family: 'Barlow Condensed', sans-serif !important;
  font-size: 10.5px !important;
  font-weight: 700 !important;
  letter-spacing: 0.16em !important;
  color: #2DD4BF !important;
}

.ethics-card-title,
.ethics-card-title .elementor-heading-title {
  font-family: 'Cormorant Garamond', Georgia, serif !important;
  font-size: 21px !important;
  font-weight: 600 !important;
  color: #FFFFFF !important;
  margin: 10px 0 8px 0 !important;
}

.axela-ethics-compact-card p {
  font-size: 12.5px !important;
  color: #94A3B8 !important;
  line-height: 1.6 !important;
  margin: 0 !important;
}

/* -----------------------------------------------------------------------------
   SECTION 8: CONTACT SECTION REFINEMENT (2-COL MATCHING PETROTRADERS)
   ----------------------------------------------------------------------------- */
.axela-contact-split-grid {
  display: flex !important;
  flex-direction: row !important;
  gap: 40px !important;
  align-items: flex-start !important;
  width: 100% !important;
}

.axela-contact-hub-left {
  flex: 0 0 45% !important;
  max-width: 45% !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 16px !important;
}

.axela-contact-form-right {
  flex: 0 0 55% !important;
  max-width: 55% !important;
}

.contact-hub-tag,
.contact-hub-tag .elementor-heading-title {
  font-family: 'Barlow Condensed', sans-serif !important;
  font-size: 11px !important;
  font-weight: 700 !important;
  letter-spacing: 0.18em !important;
  text-transform: uppercase !important;
  color: #E5A93C !important;
  margin: 8px 0 2px 0 !important;
}

.axela-contact-hub-left p {
  font-size: 13.5px !important;
  line-height: 1.65 !important;
  color: #94A3B8 !important;
  margin: 0 !important;
}

/* Standard Button Styles */
.axela-btn-teal,
.axela-btn-teal .elementor-button {
  background: #168B8D !important;
  border: 1px solid rgba(45, 212, 191, 0.4) !important;
  color: #FFFFFF !important;
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 12px !important;
  font-weight: 700 !important;
  letter-spacing: 0.10em !important;
  text-transform: uppercase !important;
  padding: 11px 20px !important;
  border-radius: 2px !important;
  transition: all 0.25s ease !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 8px !important;
}

.axela-btn-teal:hover,
.axela-btn-teal .elementor-button:hover {
  background: #1ABC9C !important;
  box-shadow: 0 0 16px rgba(26, 188, 156, 0.4) !important;
}

.axela-btn-ghost,
.axela-btn-ghost .elementor-button {
  background: rgba(255, 255, 255, 0.04) !important;
  border: 1px solid rgba(255, 255, 255, 0.2) !important;
  color: #E2E8F0 !important;
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 12px !important;
  font-weight: 700 !important;
  letter-spacing: 0.10em !important;
  text-transform: uppercase !important;
  padding: 11px 20px !important;
  border-radius: 2px !important;
  transition: all 0.25s ease !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 8px !important;
}

.axela-btn-ghost:hover,
.axela-btn-ghost .elementor-button:hover {
  border-color: #E5A93C !important;
  color: #FFFFFF !important;
  box-shadow: 0 0 14px rgba(229, 169, 60, 0.3) !important;
}

/* -----------------------------------------------------------------------------
   RESPONSIVE MOBILE & TABLET LAYOUTS (< 992px & < 768px)
   ----------------------------------------------------------------------------- */
@media (max-width: 991px) {
  .axela-scale-metrics-grid {
    flex-wrap: wrap !important;
  }
  .axela-scale-metric-card {
    flex: 1 1 calc(50% - 10px) !important;
  }
  .axela-service-compact-card {
    flex: 0 0 calc(50% - 12px) !important;
    max-width: calc(50% - 12px) !important;
  }
  .axela-category-compact-card {
    flex: 0 0 calc(50% - 10px) !important;
    max-width: calc(50% - 10px) !important;
  }
  .axela-approach-compact-grid {
    flex-wrap: wrap !important;
  }
  .axela-stage-compact-card {
    flex: 1 1 calc(50% - 8px) !important;
  }
  .axela-invest-split-grid,
  .axela-contact-split-grid {
    flex-direction: column !important;
    gap: 30px !important;
  }
  .axela-invest-col-left,
  .axela-invest-col-right,
  .axela-contact-hub-left,
  .axela-contact-form-right {
    flex: 0 0 100% !important;
    max-width: 100% !important;
  }
}

@media (max-width: 640px) {
  .axela-scale-metrics-grid {
    flex-wrap: wrap !important;
    gap: 12px !important;
  }
  .axela-scale-metric-card {
    flex: 0 0 calc(50% - 6px) !important;
    max-width: calc(50% - 6px) !important;
    padding: 16px 12px !important;
  }
  .axela-service-compact-card,
  .axela-category-compact-card,
  .axela-stage-compact-card,
  .axela-ethics-compact-card {
    flex: 0 0 100% !important;
    max-width: 100% !important;
  }
  .axela-section-title,
  .axela-section-title .elementor-heading-title {
    font-size: 30px !important;
  }
}
"""

def sync_css():
    # 1. Update custom-css/global-dark-theme.css
    css_path = r'c:\xampp\htdocs\axela-local\custom-css\global-dark-theme.css'
    with open(css_path, 'r', encoding='utf-8') as f:
        existing = f.read()

    full_css = existing + "\n\n" + css_rules
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(full_css)
    print(f"Updated {css_path} successfully!")

    # 2. Update wp-content/themes/astra-child/style.css
    theme_css_path = r'c:\xampp\htdocs\axela-local\wp-content\themes\astra-child\style.css'
    with open(theme_css_path, 'r', encoding='utf-8') as f:
        theme_existing = f.read()

    theme_full = theme_existing + "\n\n" + css_rules
    with open(theme_css_path, 'w', encoding='utf-8') as f:
        f.write(theme_full)
    print(f"Updated {theme_css_path} successfully!")

    # 3. Sync to WordPress Customizer Post 40
    BASE_URL = "https://axelaglobal.com"
    AUTH_STR = "admin:FYCY 52pM wknI 1nOf 4RA2 t8zP"
    AUTH_B64 = base64.b64encode(AUTH_STR.encode("ascii")).decode("ascii")
    headers = {
        "Authorization": f"Basic {AUTH_B64}",
        "Content-Type": "application/json"
    }

    print("\n=== Updating Customizer CSS (Post 40) ===")
    url = f"{BASE_URL}/wp-json/wp/v2/custom_css/40"
    payload = json.dumps({"content": full_css}).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print("Post 40 Customizer CSS updated successfully! ID:", data.get("id"))
    except Exception as e:
        print("Error updating Post 40 Customizer CSS:", e)

    # 4. Flush Elementor CSS & Purge LiteSpeed
    def run_wp_cli(command):
        cli_url = f"{BASE_URL}/wp-json/wpvibe/v1/cli/run"
        p = json.dumps({"command": command}).encode("utf-8")
        r = urllib.request.Request(cli_url, data=p, headers=headers)
        try:
            with urllib.request.urlopen(r) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            print(f"Error running CLI command '{command}':", e)
            return None

    print("\n=== Flushing Elementor CSS ===")
    res_elem = run_wp_cli("elementor flush-css --regenerate")
    print("Elementor CSS flush result:", res_elem)

    print("\n=== Purging LiteSpeed Cache ===")
    res_purge = run_wp_cli("litespeed-purge all")
    print("LiteSpeed purge result:", res_purge)

if __name__ == '__main__':
    sync_css()
