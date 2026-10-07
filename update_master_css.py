import json
import base64
import urllib.request
import re

css_rules = """
/* =============================================================================
   AXELA GLOBAL — MASTER REFINEMENT STYLESHEET (FIX.SVG & PETROTRADERS SPEC)
   Sleek Compact Spacing, Clean Badges, Elegant Icons, Editorial Serif, Zero Overflow
   ============================================================================= */

@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;500;600;700&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

/* 100% Full Width Zero White Margins & Solid Minimal Deep Navy-Charcoal Foundation (#060B13) */
html,
body,
#page,
.site,
.site-content,
.ast-container,
#primary,
#main,
.entry-content,
.ast-plain-container,
.elementor-section-wrap,
.elementor,
.elementor-page-28,
.elementor-kit-7 {
  background-color: #060B13 !important;
  background: #060B13 !important;
  background-image: none !important;
  color: #94A3B8;
  width: 100% !important;
  max-width: 100% !important;
  margin: 0 !important;
  padding: 0 !important;
  box-sizing: border-box !important;
  overflow-x: hidden !important;
}

/* Hide Live Markets Top Ticker Completely (No Top Gap) */
.axela-top-ticker-outer,
#axela-top-ticker-outer,
.elementor-element-hdr_top_ticker_con {
  display: none !important;
  height: 0 !important;
  min-height: 0 !important;
  max-height: 0 !important;
  visibility: hidden !important;
  overflow: hidden !important;
  margin: 0 !important;
  padding: 0 !important;
  border: none !important;
}

/* Fully Fixed Sticky Header across Desktop and Mobile */
header.elementor-location-header,
header.elementor-location-header > div,
header,
.axela-sticky-header,
.elementor-element-hdr_container_main {
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  z-index: 999999 !important;
  width: 100% !important;
  background: #060B13 !important;
  margin: 0 !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5) !important;
}

/* Universal Section Spacing & Menu Scroll Margin Offset (Clean 75px Offset below 60-70px Fixed Header) */
#about, #services, #products, #approach, #network, #routes, #investment, #ethics, #contact,
.axela-section,
.axela-services-section,
.axela-products-section,
.axela-approach-section,
.axela-network-section,
.axela-invest-section,
.axela-ethics-section,
.axela-contact-section,
.axela-about-section {
  padding-top: 105px !important;
  padding-bottom: 105px !important;
  scroll-margin-top: 55px !important;
  position: relative !important;
  width: 100% !important;
  border-top: 1px solid rgba(255, 255, 255, 0.05) !important;
  box-sizing: border-box !important;
}

@media (max-width: 767px) {
  #about, #services, #products, #approach, #network, #routes, #investment, #ethics, #contact,
  .axela-section,
  .axela-services-section,
  .axela-products-section,
  .axela-approach-section,
  .axela-network-section,
  .axela-invest-section,
  .axela-ethics-section,
  .axela-contact-section,
  .axela-about-section {
    padding-top: 60px !important;
    padding-bottom: 60px !important;
    scroll-margin-top: 60px !important;
  }
}

/* Background Themes - Solid Deep Luxury Navy-Charcoal (#060B13) - ZERO GRADIENTS */
#hero, .elementor-element-hero_container,
#about, .elementor-element-sec_about, .axela-about-section,
#services, .elementor-element-sec_services, .axela-services-section,
#products, .elementor-element-sec_products, .axela-products-section,
#approach, .elementor-element-sec_approach, .axela-approach-section,
#network, #routes, .elementor-element-sec_network, .axela-network-section,
#investment, .elementor-element-sec_invest, .axela-invest-section,
#ethics, .elementor-element-sec_ethics, .axela-ethics-section,
#contact, .elementor-element-sec_contact, .axela-contact-section {
  background-color: #060B13 !important;
  background: #060B13 !important;
  background-image: none !important;
}

/* Transparent Header & Inner Boxed Wrappers (Zero Black Background Blocks Behind Headings) */
.axela-section-header,
.elementor-element-svc_head_con,
.elementor-element-services_inner_wrap,
.elementor-element-about_inner_wrap,
.elementor-element-products_inner_wrap,
.elementor-element-approach_inner_wrap,
.elementor-element-routes_inner_wrap,
.elementor-element-invest_inner_wrap,
.elementor-element-ethics_inner_wrap,
.elementor-element-contact_inner_wrap {
  background: transparent !important;
  background-color: transparent;
  background-image: none !important;
  box-shadow: none !important;
  border: none !important;
}

/* Boxed Container 1400px Standard */
.axela-container-boxed,
.axela-container-boxed.e-con,
.elementor-element-services_inner_wrap,
.elementor-element-about_inner_wrap,
.elementor-element-products_inner_wrap,
.elementor-element-approach_inner_wrap,
.elementor-element-routes_inner_wrap,
.elementor-element-invest_inner_wrap,
.elementor-element-ethics_inner_wrap,
.elementor-element-contact_inner_wrap {
  max-width: 1400px !important;
  width: 100% !important;
  margin: 0 auto !important;
  padding: 0 24px !important;
  box-sizing: border-box !important;
}

/* =============================================================================
   UNIVERSAL EDITORIAL SERIF TYPOGRAPHY (STRICT PETROTRADERS SPECIFICATION)
   Slim, luxury, elegant serif (Cormorant Garamond 400 / 300)
   ============================================================================= */
h1, h2,
.axela-hero-title,
.axela-hero-title .elementor-heading-title,
.axela-section-title,
.axela-section-title .elementor-heading-title,
.elementor-widget-heading h1,
.elementor-widget-heading h2 {
  /* font-family: 'Cormorant Garamond', Georgia, serif ; */
  font-weight: 300;
  letter-spacing: -0.015em;
  line-height: 1.15;
  color: #FFFFFF;
}

h1, h2, h3, h4,
.elementor-heading-title,
.axela-hero-title,
.axela-hero-title .elementor-heading-title,
.axela-section-title,
.axela-section-title .elementor-heading-title {
  max-width: 100% !important;
  word-break: normal !important;
  overflow-wrap: normal !important;
  white-space: normal !important;
}

.axela-section-title,
.axela-section-title .elementor-heading-title {
  line-height: 1.18;
  letter-spacing: -0.02em;
  margin: 0 0 6px 0 !important;
}

/* Eyebrows System - Barlow Condensed All-Caps Standard Gold (#D4AF37) */
.axela-section-eyebrow,
.axela-section-eyebrow .elementor-heading-title {
  /* font-family: 'Barlow Condensed', 'Plus Jakarta Sans', sans-serif ; */
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 2.2px;
  text-transform: uppercase !important;
  color: #D4AF37;
  margin-bottom: 4px !important;
  display: inline-block !important;
}

.axela-section-header {
  margin-bottom: 18px !important;
  text-align: left !important;
}

.axela-section-header p,
.axela-section-header .elementor-widget-text-editor,
.axela-section-subtitle p {
  /* font-family: 'Plus Jakarta Sans', -apple-system, sans-serif ; */
  font-size: 14px;
  font-weight: 400;
  line-height: 1.65;
  color: #94A3B8;
  max-width: 820px !important;
  margin: 0 !important;
}

/* =============================================================================
   TOP BAR: LIVE MARKETS & DHAKA DYNAMIC CLOCK (PETROTRADERS SPEC - 28px SLIM)
   ============================================================================= */
.axela-top-ticker-outer {
  background: rgba(6, 14, 22, 0.98) !important;
  border-bottom: 1px solid rgba(218, 66, 60, 0.25) !important;
  width: 100% !important;
  height: 28px !important;
  min-height: 28px !important;
  max-height: 28px !important;
  position: relative !important;
  z-index: 100000 !important;
  box-sizing: border-box !important;
  overflow: hidden !important;
}

.axela-top-bar-inner {
  max-width: 1400px !important;
  margin: 0 auto !important;
  padding: 0 24px !important;
  height: 28px !important;
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
  box-sizing: border-box !important;
}

.axela-top-bar-left {
  display: flex !important;
  align-items: center !important;
  overflow: hidden !important;
  height: 28px !important;
  flex: 1 1 auto !important;
  margin-right: 20px !important;
}

.axela-live-markets-badge {
  display: inline-flex !important;
  align-items: center !important;
  gap: 6px !important;
  height: 28px !important;
  padding: 0 10px !important;
  background: rgba(218, 66, 60, 0.15) !important;
  border-right: 1px solid rgba(218, 66, 60, 0.3) !important;
  /* font-family: 'Barlow Condensed', sans-serif ; */
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase !important;
  color: #FF3131;
  white-space: nowrap !important;
  flex-shrink: 0 !important;
}

.live-pulse-dot {
  width: 5px !important;
  height: 5px !important;
  border-radius: 50% !important;
  background: #FF3131 !important;
  box-shadow: 0 0 8px #FF3131 !important;
  display: inline-block !important;
}

.axela-ticker-marquee-wrap {
  overflow: hidden !important;
  white-space: nowrap !important;
  flex: 1 !important;
  height: 28px !important;
  display: flex !important;
  align-items: center !important;
}

.axela-ticker-marquee-track {
  display: inline-flex !important;
  align-items: center !important;
  white-space: nowrap !important;
}

.ticker-item {
  display: inline-flex !important;
  align-items: center !important;
  gap: 5px !important;
  padding: 0 14px !important;
  height: 28px !important;
  border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
}

.ticker-src {
  /* font-family: 'Barlow Condensed', sans-serif ; */
  font-size: 9px;
  letter-spacing: 0.12em;
  text-transform: uppercase !important;
  color: rgba(244, 240, 235, 0.45);
  white-space: nowrap !important;
}

.ticker-name {
  /* font-family: 'Barlow Condensed', sans-serif ; */
  font-size: 10px;
  letter-spacing: 0.06em;
  text-transform: uppercase !important;
  color: #F4F0EB;
  font-weight: 500;
  white-space: nowrap !important;
}

.ticker-val {
  /* font-family: 'Barlow Condensed', sans-serif ; */
  font-size: 10.5px;
  color: #F4F0EB;
  font-weight: 600;
  white-space: nowrap !important;
  letter-spacing: 0.02em;
  transition: color 0.4s ease !important;
}

.ticker-val.flash-up {
  color: #22C55E;
}

.ticker-val.flash-down {
  color: #EF4444;
}

.ticker-unit {
  /* font-family: 'Barlow Condensed', sans-serif ; */
  font-size: 8.5px;
  color: rgba(244, 240, 235, 0.35);
  white-space: nowrap !important;
}

.ticker-chg {
  /* font-family: 'Barlow Condensed', sans-serif ; */
  font-size: 9px;
  font-weight: 600;
  white-space: nowrap !important;
}

.ticker-chg.up {
  color: #22C55E;
}

.ticker-chg.down {
  color: #EF4444;
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
  /* font-family: 'Barlow Condensed', sans-serif ; */
  font-size: 10px;
  letter-spacing: 0.08em;
  color: rgba(244, 240, 235, 0.75);
  font-weight: 500;
  white-space: nowrap !important;
}

.clock-icon {
  font-size: 11px;
  opacity: 0.8 !important;
}

/* =============================================================================
   STICKY HEADER & NATIVE ELEMENTOR NAVBAR
   ============================================================================= */
/* Astra / Theme container overflow fix for native sticky header */
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

.axela-sticky-header {
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  z-index: 999999 !important;
  background: #060B13 !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5) !important;
  width: 100% !important;
  transition: all 0.3s ease !important;
}

.elementor-element-hdr_inner_con.e-con-boxed > .e-con-inner,
.axela-navbar-inner {
  max-width: 1400px !important;
  width: 100% !important;
  margin: 0 auto !important;
  padding: 4px 24px !important;
  min-height: 48px !important;
  height: 48px !important;
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
  height: 34px !important;
  max-height: 34px !important;
  width: auto !important;
  display: block !important;
  transition: opacity 0.2s ease !important;
}

.axela-native-logo img:hover {
  opacity: 0.85 !important;
}

.elementor-element-hdr_nav_btn_group,
.axela-hdr-nav-btn-group {
  flex: 0 0 auto !important;
  width: auto !important;
  display: flex !important;
  flex-direction: row !important;
  align-items: center !important;
  justify-content: flex-end !important;
  gap: 18px !important;
  margin-left: auto !important;
}

.elementor-element-axela_hdr_nav,
.axela-native-nav {
  flex: 0 0 auto !important;
  width: auto !important;
  margin: 0 !important;
}

.elementor-element-axela_hdr_btn,
.axela-native-hdr-btn {
  flex: 0 0 auto !important;
  width: auto !important;
  margin: 0 !important;
}

/* Elementor Nav Menu Styling - Modern Slim Sans-serif */
@media (min-width: 1025px) {
  .axela-native-nav .elementor-nav-menu--main {
    display: flex !important;
    align-items: center !important;
    gap: 20px !important;
  }
}

@media (max-width: 1024px) {
  header.elementor-location-header,
  header,
  .axela-sticky-header,
  .elementor-element-hdr_container_main {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    width: 100% !important;
    min-height: 48px !important;
    max-height: 48px !important;
    height: 48px !important;
    z-index: 999999 !important;
    background: #060B13 !important;
  }
  .elementor-element-hdr_inner_con.e-con-boxed > .e-con-inner,
  .axela-navbar-inner {
    padding: 0 16px !important;
    height: 48px !important;
    min-height: 48px !important;
    max-height: 48px !important;
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    align-items: center !important;
    justify-content: space-between !important;
  }
  .elementor-element-axela_hdr_logo img,
  .axela-native-logo img {
    height: 30px !important;
    max-height: 30px !important;
    width: auto !important;
  }
  .axela-native-nav .elementor-nav-menu--main {
    display: none !important;
  }
  .axela-native-nav .elementor-menu-toggle {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    background: transparent !important;
    color: #FFFFFF;
    border: none !important;
    padding: 6px !important;
    cursor: pointer !important;
  }
  .axela-native-nav .elementor-menu-toggle i,
  .axela-native-nav .elementor-menu-toggle svg {
    fill: #FFFFFF !important;
    color: #FFFFFF;
    font-size: 22px;
  }
  .axela-native-nav .elementor-nav-menu--dropdown {
    position: fixed !important;
    top: 48px !important;
    left: 0 !important;
    right: 0 !important;
    width: 100vw !important;
    max-width: 100vw !important;
    background: #060e1a !important;
    border-top: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-bottom: 2px solid #FF3131 !important;
    box-shadow: 0 20px 40px rgba(0,0,0,0.95) !important;
    z-index: 9999999 !important;
    padding: 8px 0 !important;
  }
  .axela-native-nav .elementor-nav-menu--dropdown a {
    color: #CBD5E1;
    font-size: 13.5px;
    letter-spacing: 0.5px;
    padding: 11px 20px !important;
  }
  .axela-native-nav .elementor-nav-menu--dropdown a:hover,
  .axela-native-nav .elementor-nav-menu--dropdown a.elementor-item-active {
    background: rgba(218, 66, 60, 0.25) !important;
    color: #FFFFFF;
  }
}

/* Mobile Header Slim Optimization (< 768px) */
@media (max-width: 767px) {
  .axela-top-ticker-outer {
    display: none !important;
    height: 0 !important;
    min-height: 0 !important;
    max-height: 0 !important;
    visibility: hidden !important;
    overflow: hidden !important;
  }
  .elementor-element-axela_hdr_btn,
  .axela-native-hdr-btn {
    display: none !important;
  }
  .elementor-element-hdr_nav_btn_group,
  .axela-hdr-nav-btn-group {
    gap: 0 !important;
    flex-wrap: nowrap !important;
    margin-left: auto !important;
  }
}

.elementor-element-axela_hdr_nav .elementor-item,
.axela-native-nav .elementor-item {
  /* font-family: 'Barlow Condensed', 'Plus Jakarta Sans', sans-serif ; */
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: 1.2px;
  text-transform: uppercase !important;
  color: #94A3B8;
  padding: 6px 10px !important;
  transition: color 0.2s ease !important;
  text-decoration: none !important;
}

.axela-native-nav .elementor-item:hover,
.axela-native-nav .elementor-item.elementor-item-active,
.axela-native-nav .elementor-item.highlighted {
  color: #FFFFFF;
}

.axela-native-nav .elementor-nav-menu--main .elementor-item::after {
  background-color: #FF3131 !important;
  height: 2px !important;
}

.axela-native-hdr-btn {
  flex-shrink: 0 !important;
}

/* Header Trade Enquiry CTA Button - Ultra-Slim & Compact */
.axela-native-hdr-btn .elementor-button,
.elementor-element-axela_hdr_btn .elementor-button {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 6px !important;
  background: linear-gradient(135deg, #FF3131 0%, #D92626 100%) !important;
  border: 1px solid rgba(218, 66, 60, 0.50) !important;
  color: #FFFFFF;
  font-size: 9.5px;
  font-weight: 700;
  letter-spacing: 0.10em;
  text-transform: uppercase !important;
  padding: 5px 12px !important;
  height: 28px !important;
  line-height: 1;
  border-radius: 2px !important;
  box-shadow: 0 2px 10px rgba(218, 66, 60, 0.3) !important;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

.axela-native-hdr-btn .elementor-button:hover,
.elementor-element-axela_hdr_btn .elementor-button:hover {
  background: linear-gradient(135deg, #FF4D4D 0%, #FF3131 100%) !important;
  color: #FFFFFF;
  border-color: rgba(218, 66, 60, 0.80) !important;
  box-shadow: 0 4px 14px rgba(218, 66, 60, 0.45) !important;
  transform: translateY(-1px) !important;
}

.axela-native-hdr-btn .elementor-button svg,
.axela-native-hdr-btn .elementor-button i,
.elementor-element-axela_hdr_btn .elementor-button svg,
.elementor-element-axela_hdr_btn .elementor-button i {
  fill: #FFFFFF !important;
  color: #FFFFFF;
  font-size: 9px;
  width: 9px !important;
  height: 9px !important;
}

/* =============================================================================
   HERO SECTION: CLEAN EDITORIAL LAYOUT (NO FAKE RIGHT STATS)
   ============================================================================= */
.axela-hero-section {
  min-height: 82vh !important;
  width: 100vw !important;
  max-width: 100vw !important;
  position: relative !important;
  left: 50% !important;
  right: 50% !important;
  margin-left: -50vw !important;
  margin-right: -50vw !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 90px 0 60px 0 !important;
  box-sizing: border-box !important;
}

/* Background Video Container & Dark Overlay */
.elementor-element-axela_hero_root > .elementor-background-video-container,
.axela-hero-section > .elementor-background-video-container {
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  width: 100% !important;
  height: 100% !important;
  overflow: hidden !important;
  z-index: 0 !important;
}

.elementor-element-axela_hero_root > .elementor-background-video-container video,
.axela-hero-section video {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  position: absolute !important;
  top: 50% !important;
  left: 50% !important;
  transform: translate(-50%, -50%) !important;
}

/* Hero Video Blend Effect - Premium Left-to-Right Fade (Reference Standard) */
.elementor-element-axela_hero_root > .elementor-background-overlay,
.axela-hero-section > .elementor-background-overlay,
.axela-hero-section::before {
  content: "" !important;
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  width: 100% !important;
  height: 100% !important;
  background: linear-gradient(90deg, 
    #060B13 0%, 
    rgba(6, 11, 19, 0.96) 28%, 
    rgba(6, 11, 19, 0.85) 45%, 
    rgba(6, 11, 19, 0.52) 72%, 
    rgba(6, 11, 19, 0.28) 100%
  ) !important;
  z-index: 1 !important;
  pointer-events: none !important;
}

@media (max-width: 991px) {
  .elementor-element-axela_hero_root > .elementor-background-overlay,
  .axela-hero-section > .elementor-background-overlay,
  .axela-hero-section::before {
    background: linear-gradient(180deg, 
      #060B13 0%, 
      rgba(6, 11, 19, 0.94) 40%, 
      rgba(6, 11, 19, 0.70) 75%, 
      rgba(6, 11, 19, 0.45) 100%
    ) !important;
  }
}

.axela-hero-content-wrap,
.elementor-element-axela_hero_content {
  position: relative !important;
  z-index: 2 !important;
  max-width: 1400px !important;
  width: 100% !important;
  margin: 0 auto !important;
  padding: 0 24px !important;
  box-sizing: border-box !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: flex-start !important;
}

.axela-hero-left-column,
.elementor-element-axela_hero_left {
  width: 100% !important;
  max-width: 1200px !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: flex-start !important;
}

/* Hero Badge System - Clean Uppercase Text with Bullets (Word Doc Spec) */
.axela-hero-badge,
.elementor-element-hero_badge_hd {
  display: inline-block !important;
  width: auto !important;
  max-width: fit-content !important;
  margin-bottom: 14px !important;
}

.axela-hero-badge .elementor-heading-title,
.elementor-element-hero_badge_hd .elementor-heading-title {
  display: inline-block !important;
  background: transparent !important;
  border: none !important;
  padding: 0 !important;
  font-size: 13.5px;
  font-weight: 600;
  letter-spacing: 2.5px;
  text-transform: uppercase !important;
  color: #D4AF37;
  /* font-family: 'Barlow Condensed', 'Plus Jakarta Sans', sans-serif ; */
  font-size: 11.5px;
  letter-spacing: 0.16em;
  font-weight: 600;
  width: auto !important;
  box-shadow: none !important;
}

.axela-hero-title,
.axela-hero-title .elementor-heading-title,
.elementor-element-hero_h1_hd .elementor-heading-title {
  /* font-family: 'Cormorant Garamond', Georgia, serif ; */
  font-size: 52px;
  font-weight: 400;
  line-height: 1.12;
  letter-spacing: -0.02em;
  color: #FFFFFF;
  margin: 0 0 16px 0 !important;
  max-width: 100% !important;
  width: 100% !important;
  white-space: normal !important;
  word-break: normal !important;
  overflow-wrap: normal !important;
}

.axela-hero-intro,
.axela-hero-intro p,
.elementor-element-hero_intro_txt p {
  /* font-family: 'Plus Jakarta Sans', sans-serif ; */
  font-size: 15.5px;
  font-weight: 400;
  line-height: 1.7;
  color: #CBD5E1;
  margin: 0 0 14px 0 !important;
  max-width: 880px !important;
}

.axela-hero-support,
.axela-hero-support p,
.elementor-element-hero_support_txt,
.elementor-element-hero_support_txt p {
  /* font-family: 'Plus Jakarta Sans', sans-serif ; */
  font-size: 14px;
  font-weight: 400;
  line-height: 1.65;
  color: #94A3B8;
  border-left: none !important;
  border-right: none !important;
  padding-left: 0 !important;
  margin: 0 0 20px 0 !important;
  max-width: 880px !important;
}

/* Hero Button Row */
.axela-hero-btn-row,
.elementor-element-hero_btn_con {
  display: flex !important;
  flex-direction: row !important;
  flex-wrap: nowrap !important;
  align-items: center !important;
  gap: 12px !important;
  width: auto !important;
  margin-top: 6px !important;
}

.elementor-element-hero_btn_con .elementor-widget-button,
.elementor-element-hero_btn_trade,
.elementor-element-hero_btn_supply,
.elementor-element-hero_btn_invest {
  width: auto !important;
  display: inline-block !important;
}

.axela-hero-btn .elementor-button,
.axela-hero-btn-compact .elementor-button,
.elementor-element-hero_btn_con .elementor-button {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 7px !important;
  padding: 7px 15px !important;
  height: 33px !important;
  box-sizing: border-box !important;
  border-radius: 2px !important;
  /* font-family: 'Plus Jakarta Sans', sans-serif ; */
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase !important;
  transition: all 0.25s ease !important;
  text-decoration: none !important;
  white-space: nowrap !important;
  width: auto !important;
  max-width: max-content !important;
}

.axela-hero-btn .elementor-button svg,
.axela-hero-btn .elementor-button i,
.elementor-element-hero_btn_con .elementor-button svg,
.elementor-element-hero_btn_con .elementor-button i {
  font-size: 9.5px;
  width: 9.5px !important;
  height: 9.5px !important;
}

/* 1. Signature Reddish Accent (#FF3131) */
.elementor-element-hero_btn_trade .elementor-button,
.axela-btn-red .elementor-button,
.axela-btn-primary .elementor-button,
.axela-btn-burgundy .elementor-button {
  background: linear-gradient(135deg, #FF3131 0%, #D92626 100%) !important;
  color: #FFFFFF;
  border: 1px solid rgba(218, 66, 60, 0.50) !important;
  box-shadow: 0 4px 18px rgba(218, 66, 60, 0.35) !important;
}

.elementor-element-hero_btn_trade .elementor-button:hover,
.axela-btn-red .elementor-button:hover,
.axela-btn-primary .elementor-button:hover,
.axela-btn-burgundy .elementor-button:hover {
  background: linear-gradient(135deg, #FF4D4D 0%, #FF3131 100%) !important;
  border-color: rgba(218, 66, 60, 0.80) !important;
  box-shadow: 0 6px 24px rgba(218, 66, 60, 0.45) !important;
  color: #FFFFFF;
}

.elementor-element-hero_btn_trade .elementor-button svg,
.elementor-element-hero_btn_trade .elementor-button i,
.axela-btn-red .elementor-button svg,
.axela-btn-red .elementor-button i,
.axela-btn-primary .elementor-button svg,
.axela-btn-primary .elementor-button i,
.axela-btn-burgundy .elementor-button svg,
.axela-btn-burgundy .elementor-button i {
  fill: #FFFFFF !important;
  color: #FFFFFF;
}

/* 2. Glassmorphic Secondary Outline Button with Gold Border */
.elementor-element-hero_btn_supply .elementor-button,
.axela-btn-ghost .elementor-button {
  background: rgba(255, 255, 255, 0.04) !important;
  color: #E2E8F0;
  border: 1px solid rgba(212, 175, 55, 0.35) !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2) !important;
}

.elementor-element-hero_btn_supply .elementor-button:hover,
.axela-btn-ghost .elementor-button:hover {
  background: rgba(218, 66, 60, 0.12) !important;
  border-color: #FF3131 !important;
  color: #FFFFFF;
  box-shadow: 0 4px 16px rgba(218, 66, 60, 0.25) !important;
}

/* 3. Subtle Premium Gold Accent - Borderless Clean Text Link (Annotation 6B) */
.elementor-element-hero_btn_invest,
.elementor-element-hero_btn_invest .elementor-button,
.elementor-element-hero_btn_invest .elementor-widget-container,
.axela-btn-gold-link,
.axela-btn-gold-link .elementor-button,
.axela-btn-gold,
.axela-btn-gold .elementor-button,
.hero_btn_invest,
.hero_btn_invest .elementor-button,
.hero-btn-explore,
.hero-btn-explore .elementor-button,
.axela-btn-gold-outline,
.axela-btn-gold-outline .elementor-button {
  background: transparent !important;
  background-color: transparent !important;
  color: #E5A93C;
  border: none !important;
  border-width: 0 !important;
  box-shadow: none !important;
  outline: none !important;
  padding: 7px 10px 7px 0 !important;
  text-decoration: none !important;
  /* font-family: 'Plus Jakarta Sans', sans-serif ; */
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase !important;
  display: inline-flex !important;
  align-items: center !important;
  height: 33px !important;
  gap: 7px !important;
  transition: all 0.25s ease !important;
}

.elementor-element-hero_btn_invest:hover,
.elementor-element-hero_btn_invest .elementor-button:hover,
.axela-btn-gold-link:hover,
.axela-btn-gold-link .elementor-button:hover,
.axela-btn-gold:hover,
.axela-btn-gold .elementor-button:hover,
.hero_btn_invest:hover,
.hero_btn_invest .elementor-button:hover,
.hero-btn-explore:hover,
.hero-btn-explore .elementor-button:hover,
.axela-btn-gold-outline:hover,
.axela-btn-gold-outline .elementor-button:hover {
  background: transparent !important;
  background-color: transparent !important;
  border: none !important;
  border-width: 0 !important;
  box-shadow: none !important;
  color: #F5C564;
  transform: translateX(4px) !important;
  text-decoration: none !important;
}

.elementor-element-hero_btn_invest .elementor-button svg,
.elementor-element-hero_btn_invest .elementor-button i,
.axela-btn-gold .elementor-button svg,
.axela-btn-gold .elementor-button i {
  fill: #E5A93C !important;
  color: #E5A93C;
  transition: transform 0.2s ease !important;
}

.elementor-element-hero_btn_invest .elementor-button:hover svg,
.elementor-element-hero_btn_invest .elementor-button:hover i,
.axela-btn-gold .elementor-button:hover svg,
.axela-btn-gold .elementor-button:hover i {
  fill: #F5C564 !important;
  color: #F5C564;
  transform: translateX(4px) !important;
}

/* =============================================================================
   SECTION 1: ABOUT AXELA LTD. (NO STATS BOXES / NO BUTTONS / DOC PURITY)
   ============================================================================= */
.axela-lead-text p {
  /* font-family: 'Plus Jakarta Sans', sans-serif ; */
  font-size: 16px;
  line-height: 1.75;
  color: #E2E8F0;
  margin-bottom: 12px !important;
  max-width: 920px !important;
}

.axela-sub-text p {
  /* font-family: 'Plus Jakarta Sans', sans-serif ; */
  font-size: 14.5px;
  line-height: 1.68;
  color: #94A3B8;
  margin-bottom: 0 !important;
  max-width: 920px !important;
}

/* =============================================================================
   SECTION 2: OUR SERVICES REFINEMENT (SLEEK COMPACT CARDS, NO BUTTONS)
   ============================================================================= */
.elementor-element-services_grid_con,
.axela-services-compact-grid {
  display: flex !important;
  flex-direction: row !important;
  flex-wrap: wrap !important;
  gap: 16px !important;
  width: 100% !important;
}

.elementor-element-services_grid_con > .e-con,
[class*="elementor-element-svc_card_"],
.axela-service-compact-card {
  flex: 0 0 calc(25% - 12px) !important;
  max-width: calc(25% - 12px) !important;
  width: calc(25% - 12px) !important;
  box-sizing: border-box !important;
  background: rgba(16, 29, 50, 0.45) !important;
  background-color: rgba(16, 29, 50, 0.45) !important;
  border: none !important;
  backdrop-filter: blur(16px) !important;
  -webkit-backdrop-filter: blur(16px) !important;
  padding: 18px 16px 18px 16px !important;
  border-radius: 8px !important;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35) !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: flex-start !important;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

.elementor-element-services_grid_con > .e-con:hover,
[class*="elementor-element-svc_card_"]:hover,
.axela-service-compact-card:hover {
  transform: translateY(-4px) !important;
  border-color: rgba(218, 66, 60, 0.35) !important;
  box-shadow: 0 14px 32px rgba(0, 0, 0, 0.55), 0 0 20px rgba(218, 66, 60, 0.15) !important;
}

.service-card-head {
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
  margin-bottom: 10px !important;
  width: 100% !important;
}

.service-card-num,
.service-card-num .elementor-heading-title {
  /* font-family: 'Barlow Condensed', monospace ; */
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.16em;
  color: #D4AF37;
}

.service-card-icon-sleek,
.service-card-icon-sleek .elementor-icon {
  width: 28px !important;
  height: 28px !important;
  border-radius: 50% !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  background: rgba(22, 40, 68, 0.55) !important;
  border: 1px solid rgba(212, 175, 55, 0.30) !important;
  color: #D4AF37;
  font-size: 12px;
  transition: all 0.25s ease !important;
}

.elementor-element-services_grid_con > .e-con:hover .service-card-icon-sleek .elementor-icon,
.axela-service-compact-card:hover .service-card-icon-sleek .elementor-icon {
  background: rgba(22, 40, 68, 0.55) !important;
  color: #FFFFFF;
  border-color: #FF3131;
  box-shadow: 0 0 12px rgba(218, 66, 60, 0.5) !important;
  transform: scale(1.05) !important;
}

.service-card-title,
.service-card-title .elementor-heading-title {
  /* font-family: 'Cormorant Garamond', Georgia, serif ; */
  font-size: 19px;
  font-weight: 400;
  color: #FFFFFF;
  line-height: 1.25;
  margin: 0 0 6px 0 !important;
}

.service-card-desc,
.service-card-desc p,
.elementor-element-services_grid_con p {
  /* font-family: 'Plus Jakarta Sans', sans-serif ; */
  font-size: 12px;
  line-height: 1.55;
  color: #94A3B8;
  margin: 0 !important;
}

/* =============================================================================
   SECTION 3: PRODUCTS & CATEGORIES (LUXURY VIGNETTE & COMPACT CARDS)
   ============================================================================= */
/* Split Blend Warehouse Banner (Petrotraders / Screenshot 2026-10-06 142745.jpg Spec) */
.axela-products-split-banner,
.elementor-element-prod_split_banner {
  position: relative !important;
  min-height: 420px !important;
  border-radius: 6px !important;
  overflow: hidden !important;
  margin-bottom: 24px !important;
  border: none !important;
  box-shadow: none !important;
  box-sizing: border-box !important;
  display: flex !important;
  align-items: center !important;
  background: url('https://axelaglobal.com/wp-content/uploads/2026/10/port-terminal-infrastructure.webp') no-repeat center right / cover !important;
  -webkit-mask-image: none !important;
  mask-image: none !important;
}

.axela-products-split-banner::before,
.elementor-element-prod_split_banner::before {
  content: '' !important;
  position: absolute !important;
  inset: 0 !important;
  background: linear-gradient(
    to right,
    rgba(6, 11, 19, 0.88) 0%,
    rgba(6, 11, 19, 0.78) 32%,
    rgba(6, 11, 19, 0.40) 55%,
    rgba(6, 11, 19, 0.10) 75%,
    transparent 100%
  ) !important;
  z-index: 1 !important;
  pointer-events: none !important;
}

.axela-prod-banner-text,
.elementor-element-prod_banner_text {
  position: relative !important;
  z-index: 2 !important;
  max-width: 620px !important;
  padding: 40px 32px !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: flex-start !important;
}

.axela-prod-banner-text .axela-section-eyebrow,
.axela-prod-banner-text .elementor-heading-title {
  margin-bottom: 4px !important;
}

.axela-prod-banner-text .axela-section-title,
.axela-prod-banner-text .elementor-heading-title {
  font-size: 34px;
  line-height: 1.15;
  margin: 0 0 4px 0 !important;
}

.axela-prod-banner-text p {
  font-size: 13.5px;
  line-height: 1.6;
  color: #CBD5E1;
  margin: 0 !important;
}

.axela-categories-compact-grid,
.elementor-element-categories_grid_con {
  display: flex !important;
  flex-direction: row !important;
  flex-wrap: wrap !important;
  gap: 16px !important;
  width: 100% !important;
}

.elementor-element-categories_grid_con > .e-con,
[class*="elementor-element-cat_card_"],
.axela-category-compact-card {
  flex: 0 0 calc(33.333% - 11px) !important;
  max-width: calc(33.333% - 11px) !important;
  box-sizing: border-box !important;
  background: rgba(16, 29, 50, 0.45) !important;
  background-color: rgba(16, 29, 50, 0.45) !important;
  border: none !important;
  backdrop-filter: blur(16px) !important;
  -webkit-backdrop-filter: blur(16px) !important;
  padding: 18px 16px !important;
  border-radius: 8px !important;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35) !important;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

.elementor-element-categories_grid_con > .e-con:hover,
[class*="elementor-element-cat_card_"]:hover,
.axela-category-compact-card:hover {
  transform: translateY(-4px) !important;
  border-color: rgba(218, 66, 60, 0.35) !important;
  box-shadow: 0 14px 32px rgba(0, 0, 0, 0.55), 0 0 20px rgba(218, 66, 60, 0.15) !important;
}

/* Product Category Cards: Left align icon and title with tight gap (Annotation 4) */
[data-id^="cat_card_"] > .e-con:first-child,
[class*="cat_card_"] > .e-con:first-child,
.axela-category-compact-card > .e-con:first-child,
.category-title-icon-row {
  display: flex !important;
  flex-direction: row !important;
  justify-content: flex-start !important;
  align-items: center !important;
  gap: 8px !important;
  min-height: auto !important;
  height: auto !important;
  margin-bottom: 4px !important;
  width: 100% !important;
}

[data-id^="cat_card_"] > .e-con:first-child .elementor-widget-icon,
[class*="cat_card_"] > .e-con:first-child .elementor-widget-icon,
.category-icon-inline {
  flex: 0 0 auto !important;
  width: auto !important;
  margin: 0 !important;
}

[data-id^="cat_card_"] > .e-con:first-child .elementor-widget-heading,
[class*="cat_card_"] > .e-con:first-child .elementor-widget-heading,
.category-card-title-sleek {
  flex: 0 1 auto !important;
  width: auto !important;
  margin: 0 !important;
  text-align: left !important;
}

.category-icon-inline .elementor-icon {
  font-size: 14px;
  color: #D4AF37;
  display: inline-flex !important;
  margin: 0 !important;
  padding: 0 !important;
  transition: color 0.25s ease !important;
}

.axela-category-compact-card:hover .category-icon-inline .elementor-icon {
  color: #D4AF37;
}

.category-card-title-sleek,
.category-card-title-sleek .elementor-heading-title,
[data-id^="cat_card_"] .elementor-heading-title {
  /* font-family: 'Cormorant Garamond', Georgia, serif ; */
  font-size: 19px;
  font-weight: 400;
  color: #FFFFFF;
  line-height: 1.25;
  margin: 0 !important;
  text-align: left !important;
}

.axela-category-compact-card p,
.elementor-element-categories_grid_con p {
  /* font-family: 'Plus Jakarta Sans', sans-serif ; */
  font-size: 12px;
  line-height: 1.55;
  color: #94A3B8;
  margin: 0 !important;
}

.axela-compliance-note-box {
  background: rgba(229, 169, 60, 0.05) !important;
  border-left: 3px solid #E5A93C !important;
  padding: 14px 18px !important;
  margin-top: 20px !important;
}

.compliance-title,
.compliance-title .elementor-heading-title {
  /* font-family: 'Barlow Condensed', sans-serif ; */
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase !important;
  color: #E5A93C;
  margin-bottom: 4px !important;
}

.axela-compliance-note-box p {
  font-size: 12px;
  color: #94A3B8;
  line-height: 1.55;
  margin: 0 !important;
}

/* =============================================================================
   SECTION 4: APPROACH (COMPACT PADDING, SLEEK ICONS)
   ============================================================================= */
.axela-approach-compact-grid,
.elementor-element-stages_grid_con {
  display: flex !important;
  flex-direction: row !important;
  gap: 14px !important;
  width: 100% !important;
}

.elementor-element-stages_grid_con > .e-con,
.axela-stage-compact-card {
  flex: 1 1 0 !important;
  background: rgba(16, 29, 50, 0.45) !important;
  background-color: rgba(16, 29, 50, 0.45) !important;
  border: none !important;
  backdrop-filter: blur(16px) !important;
  -webkit-backdrop-filter: blur(16px) !important;
  padding: 18px 14px !important;
  border-radius: 8px !important;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35) !important;
  position: relative !important;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

.elementor-element-stages_grid_con > .e-con:hover,
.axela-stage-compact-card:hover {
  transform: translateY(-4px) !important;
  border-color: rgba(218, 66, 60, 0.35) !important;
  box-shadow: 0 14px 32px rgba(0, 0, 0, 0.55), 0 0 20px rgba(218, 66, 60, 0.15) !important;
}

.stage-card-step,
.stage-card-step .elementor-heading-title {
  /* font-family: ui-monospace, SFMono-Regular, monospace ; */
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.14em;
  color: #D4AF37;
}

/* Stage icons: ALL GOLD (Annotation 3) */
.stage-icon-sleek,
.stage-icon-sleek .elementor-icon,
.stage-icon-sleek .elementor-icon i,
.stage-icon-sleek .elementor-icon svg,
.elementor-element-stages_grid_con .elementor-icon,
.elementor-element-stages_grid_con .elementor-icon i,
[class*="stage_card_"] .elementor-icon,
[class*="stage_card_"] .elementor-icon i {
  font-size: 15px;
  color: #E5A93C;
  fill: #E5A93C !important;
  transition: all 0.25s ease !important;
}

.elementor-element-stages_grid_con > .e-con:hover .stage-icon-sleek .elementor-icon,
.axela-stage-compact-card:hover .stage-icon-sleek .elementor-icon,
[class*="stage_card_"]:hover .elementor-icon {
  color: #F5C564;
  fill: #F5C564 !important;
  transform: scale(1.1) !important;
}

.stage-card-title,
.stage-card-title .elementor-heading-title {
  /* font-family: 'Cormorant Garamond', Georgia, serif ; */
  font-size: 17px;
  font-weight: 400;
  color: #FFFFFF;
  line-height: 1.25;
  margin: 4px 0 4px 0 !important;
}

.elementor-element-stages_grid_con p,
.axela-stage-compact-card p {
  font-size: 11.5px;
  color: #94A3B8;
  line-height: 1.5;
  margin: 0 !important;
}

/* =============================================================================
   SECTION 6: INVESTMENT & ETHICS (COMPACT HEIGHTS & BALANCED GAPS)
   ============================================================================= */
.axela-invest-split-grid,
.elementor-element-invest_split_grid {
  display: flex !important;
  flex-direction: row !important;
  gap: 28px !important;
  align-items: flex-start !important;
}

.axela-invest-col-left,
.axela-invest-col-right,
.elementor-element-inv_col_left,
.elementor-element-inv_col_right {
  flex: 1 1 calc(50% - 14px) !important;
}

.invest-box-title,
.invest-box-title .elementor-heading-title {
  /* font-family: 'Cormorant Garamond', Georgia, serif ; */
  font-size: 24px;
  font-weight: 400;
  color: #FFFFFF;
  margin-bottom: 10px !important;
}

.invest-pillars-eyebrow,
.invest-pillars-eyebrow .elementor-heading-title,
.invest-notice-eyebrow,
.invest-notice-eyebrow .elementor-heading-title {
  /* font-family: 'Barlow Condensed', sans-serif ; */
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase !important;
  color: #E5A93C;
  margin-top: 12px !important;
  display: block !important;
}

.axela-invest-banner-img img {
  border-radius: 8px !important;
  border: none !important;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35) !important;
  max-height: 250px !important;
  aspect-ratio: 16 / 10 !important;
  object-fit: cover !important;
  width: 100% !important;
  display: block !important;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

.axela-invest-banner-img:hover img,
.axela-invest-col-right:hover .axela-invest-banner-img img {
  border-color: rgba(218, 66, 60, 0.35) !important;
  transform: translateY(-4px) !important;
  box-shadow: 0 14px 32px rgba(0, 0, 0, 0.55), 0 0 20px rgba(218, 66, 60, 0.15) !important;
}

.axela-ethics-compact-grid,
.elementor-element-ethics_grid_con {
  display: flex !important;
  flex-direction: row !important;
  gap: 16px !important;
}

.elementor-element-ethics_grid_con > .e-con,
.axela-ethics-compact-card {
  flex: 1 1 calc(33.333% - 11px) !important;
  background: rgba(16, 29, 50, 0.45) !important;
  background-color: rgba(16, 29, 50, 0.45) !important;
  border: none !important;
  backdrop-filter: blur(16px) !important;
  -webkit-backdrop-filter: blur(16px) !important;
  padding: 20px 18px !important;
  border-radius: 8px !important;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35) !important;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

.elementor-element-ethics_grid_con > .e-con:hover,
.axela-ethics-compact-card:hover {
  transform: translateY(-4px) !important;
  border-color: rgba(218, 66, 60, 0.35) !important;
  box-shadow: 0 14px 32px rgba(0, 0, 0, 0.55), 0 0 20px rgba(218, 66, 60, 0.15) !important;
}

.ethics-card-tag,
.ethics-card-tag .elementor-heading-title {
  /* font-family: 'Barlow Condensed', sans-serif ; */
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.16em;
  color: #D4AF37;
}

.ethics-card-title,
.ethics-card-title .elementor-heading-title {
  /* font-family: 'Cormorant Garamond', Georgia, serif ; */
  font-size: 18px;
  font-weight: 400;
  color: #FFFFFF;
  margin: 8px 0 6px 0 !important;
}

.ethics-icon-sleek,
.ethics-icon-sleek .elementor-icon {
  font-size: 13px;
  color: #D4AF37;
  width: 24px !important;
  height: 24px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
}

.elementor-element-ethics_grid_con p,
.axela-ethics-compact-card p {
  font-size: 12px;
  color: #94A3B8;
  line-height: 1.55;
  margin: 0 !important;
}

/* =============================================================================
   SECTION 8: CONTACT SECTION
   ============================================================================= */
.axela-contact-split-grid,
.elementor-element-contact_split_con {
  display: flex !important;
  flex-direction: row !important;
  gap: 32px !important;
  align-items: flex-start !important;
  width: 100% !important;
}

.axela-contact-hub-left,
.elementor-element-contact_hub_left {
  flex: 0 0 42% !important;
  max-width: 42% !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 12px !important;
}

.axela-contact-form-right,
.elementor-element-contact_form_right {
  flex: 0 0 58% !important;
  max-width: 58% !important;
}

.contact-hub-tag,
.contact-hub-tag .elementor-heading-title {
  /* font-family: 'Barlow Condensed', sans-serif ; */
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase !important;
  color: #E5A93C;
  margin: 6px 0 2px 0 !important;
}

.axela-contact-hub-left p,
.elementor-element-contact_hub_left p {
  font-size: 13.5px;
  line-height: 1.6;
  color: #94A3B8;
  margin: 0 !important;
}

.axela-contact-hub-left a[href^="mailto:"],
.axela-contact-hub-left p a[href^="mailto:info@axelaglobal.com"] {
  color: #FFFFFF;
  font-weight: 600;
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.25) !important;
  text-decoration: none !important;
}

/* Elementor Pro Native Form Styling - Frameless Dark Integration (No Bulky Outer Box/Border) */
.axela-native-pro-form,
.axela-contact-form-right,
.axela-contact-form-right .elementor-form,
.elementor-element-contact_form_right,
.elementor-element-contact_form_right .elementor-form,
.elementor-widget-form .elementor-form {
  background: transparent !important;
  background-color: transparent !important;
  border: none !important;
  border-width: 0 !important;
  box-shadow: none !important;
  backdrop-filter: none !important;
  -webkit-backdrop-filter: none !important;
  padding: 0 !important;
}

.axela-native-pro-form .elementor-form-fields-wrapper {
  display: flex !important;
  flex-wrap: wrap !important;
  margin-left: -8px !important;
  margin-right: -8px !important;
}

.axela-native-pro-form .elementor-field-group {
  padding-left: 8px !important;
  padding-right: 8px !important;
  margin-bottom: 12px !important;
  box-sizing: border-box !important;
}

.axela-native-pro-form .elementor-field-group.elementor-column.elementor-col-50,
.axela-native-pro-form .elementor-col-50,
.axela-native-pro-form .elementor-md-50 {
  flex: 0 0 50% !important;
  max-width: 50% !important;
  width: 50% !important;
}

.axela-native-pro-form .elementor-field-group.elementor-column.elementor-col-100,
.axela-native-pro-form .elementor-col-100,
.axela-native-pro-form .elementor-md-100 {
  flex: 0 0 100% !important;
  max-width: 100% !important;
  width: 100% !important;
}

.axela-native-pro-form .elementor-field-type-upload input[type="file"] {
  background: rgba(6, 10, 16, 0.85) !important;
  border: 1px dashed rgba(255, 255, 255, 0.18) !important;
  color: #94A3B8;
  padding: 8px 12px !important;
  border-radius: 4px !important;
  font-size: 12px;
  cursor: pointer !important;
  width: 100% !important;
  box-sizing: border-box !important;
}

.axela-native-pro-form .elementor-field-label,
.axela-contact-form-right .elementor-field-label {
  /* font-family: 'Barlow Condensed', sans-serif ; */
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase !important;
  color: #94A3B8;
  margin-bottom: 6px !important;
  display: block !important;
}

.axela-native-pro-form .elementor-field-textual,
.axela-native-pro-form input[type="text"],
.axela-native-pro-form input[type="email"],
.axela-native-pro-form select,
.axela-native-pro-form textarea,
.axela-contact-form-right input,
.axela-contact-form-right select,
.axela-contact-form-right textarea {
  background: rgba(6, 10, 16, 0.85) !important;
  color: #F1F5F9;
  border: 1px solid rgba(255, 255, 255, 0.12) !important;
  border-radius: 4px !important;
  /* font-family: 'Plus Jakarta Sans', sans-serif ; */
  font-size: 13px;
  padding: 10px 14px !important;
  box-sizing: border-box !important;
  width: 100% !important;
  transition: border-color 0.25s ease, box-shadow 0.25s ease, background 0.25s ease !important;
}

.axela-native-pro-form .elementor-field-textual:focus,
.axela-native-pro-form input:focus,
.axela-native-pro-form select:focus,
.axela-native-pro-form textarea:focus,
.axela-contact-form-right input:focus,
.axela-contact-form-right select:focus,
.axela-contact-form-right textarea:focus {
  background: rgba(10, 16, 26, 0.95) !important;
  border-color: rgba(218, 66, 60, 0.60) !important;
  box-shadow: 0 0 0 2px rgba(218, 66, 60, 0.25) !important;
  outline: none !important;
}

.axela-native-pro-form .elementor-field-textual::placeholder,
.axela-contact-form-right input::placeholder,
.axela-contact-form-right textarea::placeholder {
  color: #64748B;
  font-size: 12.5px;
}

.axela-native-pro-form select option {
  background: #060e1d !important;
  color: #E2E8F0;
}

/* Compact Submit Button */
.axela-native-pro-form .elementor-button,
.axela-contact-form-right .elementor-button,
.axela-btn-compact-submit .elementor-button {
  background: linear-gradient(135deg, #FF3131 0%, #D92626 100%) !important;
  color: #FFFFFF;
  /* font-family: 'Barlow Condensed', sans-serif ; */
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase !important;
  padding: 8px 22px !important;
  height: 36px !important;
  border-radius: 2px !important;
  border: 1px solid rgba(218, 66, 60, 0.50) !important;
  cursor: pointer !important;
  width: auto !important;
  max-width: 240px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 8px !important;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
  box-shadow: 0 4px 14px rgba(218, 66, 60, 0.35) !important;
}

.axela-native-pro-form .elementor-button:hover,
.axela-contact-form-right .elementor-button:hover,
.axela-btn-compact-submit .elementor-button:hover {
  background: linear-gradient(135deg, #FF4D4D 0%, #FF3131 100%) !important;
  border-color: rgba(218, 66, 60, 0.80) !important;
  transform: translateY(-1px) !important;
  box-shadow: 0 6px 20px rgba(218, 66, 60, 0.45) !important;
  color: #FFFFFF;
}

/* Elementor Form Validation & Success / Danger Notices (Dark Theme) */
.elementor-message {
  border-radius: 4px !important;
  /* font-family: 'Plus Jakarta Sans', sans-serif ; */
  font-size: 13px;
  font-weight: 500;
  padding: 12px 18px !important;
  margin-top: 14px !important;
  backdrop-filter: blur(8px) !important;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4) !important;
}
.elementor-message.elementor-message-success {
  background: rgba(218, 66, 60, 0.15) !important;
  border: 1px solid #D4AF37 !important;
  color: #FFFFFF;
}
.elementor-message.elementor-message-danger,
.elementor-message.elementor-message-error {
  background: rgba(225, 29, 72, 0.22) !important;
  border: 1px solid #F43F5E !important;
  color: #FDA4AF;
}

/* =============================================================================
   AXELA FLUENT FORMS — LUXURY DARK BOX CONTAINER & SLIM SLICK STYLING
   ============================================================================= */
.axela-contact-form-right,
.axela-contact-box-container,
.fluentform_wrapper_3 {
  background: rgba(8, 14, 24, 0.78) !important;
  background-color: rgba(8, 14, 24, 0.78) !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.55), inset 0 1px 0 rgba(255, 255, 255, 0.04) !important;
  border-radius: 8px !important;
  padding: 32px 28px !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  box-sizing: border-box !important;
  position: relative !important;
}

@media (max-width: 767px) {
  .axela-contact-form-right,
  .axela-contact-box-container,
  .fluentform_wrapper_3 {
    padding: 22px 16px !important;
    border-radius: 6px !important;
  }
}

.axela-contact-form-right .fluentform,
.axela-contact-form-right .frm-fluent-form,
.fluentform.axela-fluent-form-wrap {
  background: transparent !important;
  background-color: transparent !important;
  border: none !important;
  box-shadow: none !important;
  padding: 0 !important;
  width: 100% !important;
}

.fluentform form.frm-fluent-form,
.fluentform fieldset {
  display: flex !important;
  flex-wrap: wrap !important;
  gap: 12px 14px !important;
  margin: 0 !important;
  padding: 0 !important;
  width: 100% !important;
  border: none !important;
}

.fluentform .ff-form-group,
.fluentform .ff-el-group {
  margin: 0 !important;
  margin-bottom: 0 !important;
  box-sizing: border-box !important;
}

.fluentform .ff-col-6 {
  width: calc(50% - 7px) !important;
  flex: 0 0 calc(50% - 7px) !important;
  max-width: calc(50% - 7px) !important;
  padding: 0 !important;
  margin: 0 !important;
  box-sizing: border-box !important;
  display: block !important;
}

.fluentform .ff-col-12 {
  width: 100% !important;
  flex: 0 0 100% !important;
  max-width: 100% !important;
  padding: 0 !important;
  margin: 0 !important;
  box-sizing: border-box !important;
}

@media (max-width: 767px) {
  .fluentform .ff-col-6 {
    width: 100% !important;
    flex: 0 0 100% !important;
    max-width: 100% !important;
  }
}

.fluentform .ff-el-input--label label,
.fluentform .ff-el-form-top label,
.fluentform label.ff-el-form-check-label {
  font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase !important;
  color: #94A3B8;
  margin-bottom: 5px !important;
  display: block !important;
  line-height: 1.2;
}

.fluentform .ff-el-input--label label span,
.fluentform .ff-el-form-top label span {
  color: #FF3131;
  margin-left: 2px !important;
}

.fluentform input.ff-el-form-control,
.fluentform select.ff-el-form-control,
.fluentform .axela-ff-input,
.fluentform .axela-ff-select {
  height: 38px !important;
  min-height: 38px !important;
  font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
  font-size: 12.5px;
  line-height: 38px;
  padding: 0 12px !important;
  background: rgba(5, 9, 15, 0.85) !important;
  background-color: rgba(5, 9, 15, 0.85) !important;
  color: #F1F5F9;
  border: 1px solid rgba(255, 255, 255, 0.10) !important;
  border-radius: 4px !important;
  box-sizing: border-box !important;
  width: 100% !important;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

.fluentform textarea.ff-el-form-control,
.fluentform .axela-ff-textarea {
  font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
  font-size: 12.5px;
  line-height: 1.5;
  padding: 10px 12px !important;
  background: rgba(5, 9, 15, 0.85) !important;
  background-color: rgba(5, 9, 15, 0.85) !important;
  color: #F1F5F9;
  border: 1px solid rgba(255, 255, 255, 0.10) !important;
  border-radius: 4px !important;
  box-sizing: border-box !important;
  width: 100% !important;
  resize: vertical !important;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

.fluentform input.ff-el-form-control:focus,
.fluentform select.ff-el-form-control:focus,
.fluentform textarea.ff-el-form-control:focus,
.fluentform .axela-ff-input:focus,
.fluentform .axela-ff-select:focus,
.fluentform .axela-ff-textarea:focus {
  background: rgba(8, 14, 24, 0.95) !important;
  border-color: rgba(218, 66, 60, 0.65) !important;
  box-shadow: 0 0 0 2px rgba(218, 66, 60, 0.20) !important;
  outline: none !important;
}

.fluentform input::placeholder,
.fluentform textarea::placeholder {
  color: #475569;
  font-size: 12px;
  letter-spacing: 0.01em;
}

.fluentform select option {
  background: #0B132B !important;
  color: #F1F5F9;
  padding: 8px 12px !important;
}

.fluentform .ff-btn-submit,
.fluentform button[type="submit"],
.fluentform .axela-ff-submit {
  background: linear-gradient(135deg, #FF3131 0%, #D92626 100%) !important;
  color: #FFFFFF;
  font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase !important;
  padding: 0 24px !important;
  height: 40px !important;
  line-height: 40px;
  border-radius: 3px !important;
  border: 1px solid rgba(218, 66, 60, 0.5) !important;
  cursor: pointer !important;
  width: auto !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  box-shadow: 0 4px 16px rgba(218, 66, 60, 0.35) !important;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
  margin-top: 4px !important;
}

.fluentform .ff-btn-submit:hover,
.fluentform button[type="submit"]:hover,
.fluentform .axela-ff-submit:hover {
  background: linear-gradient(135deg, #EF4444 0%, #FF3131 100%) !important;
  border-color: rgba(218, 66, 60, 0.8) !important;
  transform: translateY(-1px) !important;
  box-shadow: 0 6px 22px rgba(218, 66, 60, 0.45) !important;
  color: #FFFFFF;
}

.fluentform .ff-message-success {
  background: rgba(16, 185, 129, 0.12) !important;
  border: 1px solid rgba(16, 185, 129, 0.35) !important;
  color: #6EE7B7;
  border-radius: 6px !important;
  padding: 14px 18px !important;
  font-size: 13px;
  font-weight: 500;
  margin-top: 14px !important;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3) !important;
}

.fluentform .error,
.fluentform .text-danger,
.fluentform .ff-errors-in-stack {
  color: #F87171;
  font-size: 11px;
  margin-top: 4px !important;
}

/* =============================================================================
   BOTTOM-TO-TOP SCROLL BUTTON: SIGNATURE REDDISH #FF3131 & HOVER GLOW
   ============================================================================= */
#ast-scroll-top,
.ast-scroll-top,
.ast-scroll-to-top,
#scroll-to-top,
.back-to-top {
  background: linear-gradient(135deg, #FF3131 0%, #D92626 100%) !important;
  color: #FFFFFF;
  border: 1px solid rgba(218, 66, 60, 0.50) !important;
  box-shadow: 0 4px 14px rgba(218, 66, 60, 0.35) !important;
  border-radius: 4px !important;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

#ast-scroll-top:hover,
.ast-scroll-top:hover,
.ast-scroll-to-top:hover,
#scroll-to-top:hover,
.back-to-top:hover {
  background: linear-gradient(135deg, #FF4D4D 0%, #FF3131 100%) !important;
  box-shadow: 0 0 18px rgba(218, 66, 60, 0.65) !important;
  transform: translateY(-2px) !important;
}

#ast-scroll-top .ast-icon,
.ast-scroll-top .ast-icon,
.ast-scroll-top i,
.ast-scroll-top svg {
  color: #FFFFFF;
  fill: #FFFFFF !important;
}
.elementor-message.elementor-message-danger,
.elementor-message.elementor-message-error {
  background: rgba(225, 29, 72, 0.22) !important;
  border: 1px solid #F43F5E !important;
  color: #FDA4AF;
}

.axela-native-pro-form .elementor-button svg,
.axela-native-pro-form .elementor-button i,
.axela-contact-form-right .elementor-button svg,
.axela-contact-form-right .elementor-button i {
  fill: #FFFFFF !important;
  color: #FFFFFF;
}

/* =============================================================================
   RESPONSIVE MOBILE & TABLET LAYOUTS (< 992px & < 768px)
   Compact 2-Column Grid on Mobile for Services — No Endless Scroll!
   ============================================================================= */
@media (max-width: 991px) {
  .axela-hero-title,
  .axela-hero-title .elementor-heading-title,
  .elementor-element-hero_h1_hd .elementor-heading-title {
    font-size: 40px;
    line-height: 1.15;
  }
  .axela-section-title,
  .axela-section-title .elementor-heading-title {
    font-size: 32px;
  }
  .elementor-element-services_grid_con > .e-con,
  [class*="elementor-element-svc_card_"],
  .axela-service-compact-card {
    flex: 0 0 calc(50% - 8px) !important;
    max-width: calc(50% - 8px) !important;
    width: calc(50% - 8px) !important;
    padding: 16px 14px !important;
  }
  .elementor-element-categories_grid_con > .e-con,
  [class*="elementor-element-cat_card_"],
  .axela-category-compact-card {
    flex: 0 0 calc(50% - 8px) !important;
    max-width: calc(50% - 8px) !important;
    width: calc(50% - 8px) !important;
  }
  .elementor-element-stages_grid_con,
  .axela-approach-compact-grid {
    flex-wrap: wrap !important;
  }
  .elementor-element-stages_grid_con > .e-con,
  .axela-stage-compact-card {
    flex: 1 1 calc(50% - 7px) !important;
  }
  .axela-invest-split-grid,
  .elementor-element-contact_split_con,
  .axela-contact-split-grid {
    flex-direction: column !important;
    gap: 24px !important;
  }
  .axela-invest-col-left,
  .axela-invest-col-right,
  .axela-contact-hub-left,
  .axela-contact-form-right,
  .elementor-element-contact_hub_left,
  .elementor-element-contact_form_right {
    flex: 0 0 100% !important;
    max-width: 100% !important;
  }
}

@media (max-width: 767px) {
  /* 1. Universal Zero Horizontal Overflow */
  html, body, #page, .hfeed.site, .elementor {
    overflow-x: hidden !important;
    max-width: 100vw !important;
  }

  /* 2. Fluid Typography Scale Down (Hero H1: 28-32px, Section H2: 22-24px) */
  .axela-hero-title,
  .axela-hero-title .elementor-heading-title,
  .elementor-element-hero_h1_hd .elementor-heading-title,
  h1 {
    font-size: clamp(26px, 6.5vw, 32px);
    line-height: 1.18;
    max-width: 100% !important;
    word-break: normal !important;
  }

  .axela-section-title,
  .axela-section-title .elementor-heading-title,
  h2 {
    font-size: clamp(22px, 5vw, 24px);
    line-height: 1.25;
    max-width: 100% !important;
    word-break: normal !important;
  }

  .axela-prod-banner-text .axela-section-title,
  .axela-prod-banner-text .elementor-heading-title {
    font-size: clamp(22px, 5vw, 24px);
    line-height: 1.25;
  }

  /* 3. Hero Section & 3 Full-Width Stacked Buttons (Stacked one below another) */
  .axela-hero-section {
    padding: 80px 0 44px 0 !important;
    min-height: auto !important;
  }

  .elementor-element-axela_hero_root > .elementor-background-video-container,
  .axela-hero-section > .elementor-background-video-container {
    display: block !important;
    visibility: visible !important;
  }

  .axela-hero-badge,
  .elementor-element-hero_badge_hd {
    display: inline-block !important;
    width: auto !important;
    max-width: fit-content !important;
    margin-bottom: 12px !important;
  }

  .axela-hero-badge .elementor-heading-title,
  .elementor-element-hero_badge_hd .elementor-heading-title {
    font-size: 10px;
    padding: 0 !important;
    background: transparent !important;
    border: none !important;
    letter-spacing: 0.14em;
    white-space: normal !important;
    text-align: left !important;
    display: inline-block !important;
    box-shadow: none !important;
  }

  .elementor-element-hero_btn_con,
  .axela-hero-btn-row {
    display: flex !important;
    flex-direction: column !important;
    width: 100% !important;
    gap: 8px !important;
  }

  .elementor-element-hero_btn_con .elementor-widget-button,
  .elementor-element-hero_btn_trade,
  .elementor-element-hero_btn_supply,
  .elementor-element-hero_btn_invest {
    width: 100% !important;
    display: block !important;
  }

  .elementor-element-hero_btn_con .elementor-button,
  .axela-hero-btn,
  .axela-hero-btn .elementor-button,
  .axela-hero-btn-compact .elementor-button,
  .elementor-element-hero_btn_invest,
  .elementor-element-hero_btn_invest .elementor-button {
    width: 100% !important;
    max-width: 280px !important;
    display: flex !important;
    text-align: center !important;
    justify-content: center !important;
    align-items: center !important;
    padding: 8px 14px !important;
    height: 34px !important;
    font-size: 10.5px;
    box-sizing: border-box !important;
  }

  /* 4. Fluid Single-Column Vertical Stack for Services, Products, Working Approach, Ethics */
  .elementor-element-services_grid_con,
  .axela-services-compact-grid,
  .elementor-element-categories_grid_con,
  .axela-categories-compact-grid,
  .elementor-element-stages_grid_con,
  .axela-approach-compact-grid,
  .elementor-element-ethics_grid_con,
  .axela-ethics-compact-grid {
    display: flex !important;
    flex-direction: column !important;
    width: 100% !important;
    gap: 14px !important;
  }

  .elementor-element-services_grid_con > .e-con,
  .elementor-element-services_grid_con > .e-con-inner > .e-con,
  [class*="elementor-element-svc_card_"],
  .axela-service-compact-card,
  .elementor-element-categories_grid_con > .e-con,
  [class*="elementor-element-cat_card_"],
  .axela-category-compact-card,
  .elementor-element-stages_grid_con > .e-con,
  [class*="elementor-element-stage_card_"],
  .axela-stage-compact-card,
  .elementor-element-ethics_grid_con > .e-con,
  [class*="elementor-element-ethics_card_"],
  .axela-ethics-compact-card {
    flex: 0 0 100% !important;
    max-width: 100% !important;
    width: 100% !important;
    box-sizing: border-box !important;
    padding: 18px 16px !important;
  }

  .service-card-head {
    margin-bottom: 6px !important;
  }
  .service-card-num,
  .service-card-num .elementor-heading-title {
    font-size: 9.5px;
  }
  .service-card-icon-sleek,
  .service-card-icon-sleek .elementor-icon {
    width: 24px !important;
    height: 24px !important;
    font-size: 12px;
  }
  .service-card-title,
  .service-card-title .elementor-heading-title {
    font-size: 16px;
    line-height: 1.25;
    margin: 0 0 4px 0 !important;
  }
  .service-card-desc,
  .service-card-desc p,
  .elementor-element-services_grid_con p {
    font-size: 12px;
    line-height: 1.5;
    margin: 0 !important;
  }

  /* 5. Compact 16px to 20px Internal Container Padding */
  .axela-container-boxed,
  .axela-container-boxed.e-con,
  .elementor-element-services_inner_wrap,
  .elementor-element-about_inner_wrap,
  .elementor-element-products_inner_wrap,
  .elementor-element-approach_inner_wrap,
  .elementor-element-routes_inner_wrap,
  .elementor-element-invest_inner_wrap,
  .elementor-element-ethics_inner_wrap,
  .elementor-element-contact_inner_wrap {
    padding-left: 16px !important;
    padding-right: 16px !important;
  }

  .axela-section,
  .axela-services-section,
  .axela-products-section,
  .axela-approach-section,
  .axela-network-section,
  .axela-invest-section,
  .axela-ethics-section,
  .axela-contact-section,
  .axela-about-section {
    padding: 40px 0 !important;
  }

  .axela-products-split-banner,
  .elementor-element-prod_split_banner {
    min-height: auto !important;
  }
  .axela-prod-banner-text,
  .elementor-element-prod_banner_text {
    padding: 24px 16px !important;
  }

  .axela-native-pro-form,
  .axela-contact-form-right .elementor-form {
    padding: 18px 16px !important;
  }

  .axela-native-pro-form .elementor-field-group.elementor-column.elementor-col-50,
  .axela-native-pro-form .elementor-col-50,
  .axela-native-pro-form .elementor-md-50 {
    flex: 0 0 100% !important;
    max-width: 100% !important;
    width: 100% !important;
  }

  /* Mobile Navbar & Controls */
  .axela-navbar-inner {
    padding: 8px 16px !important;
    gap: 8px !important;
  }
  .axela-native-logo img {
    max-height: 24px !important;
  }
  .axela-native-hdr-btn .elementor-button {
    padding: 6px 12px !important;
    font-size: 10px;
    letter-spacing: 0.08em;
  }

  /* Mobile Stacked Grids */
  .axela-invest-split-grid,
  .elementor-element-invest_split_grid {
    flex-direction: column !important;
    gap: 20px !important;
  }
  .axela-invest-col-left,
  .axela-invest-col-right,
  .elementor-element-inv_col_left,
  .elementor-element-inv_col_right {
    flex: 0 0 100% !important;
    max-width: 100% !important;
    width: 100% !important;
  }
  .axela-ethics-compact-grid,
  .elementor-element-ethics_grid_con {
    flex-direction: column !important;
    gap: 14px !important;
  }
  .axela-contact-split-grid,
  .elementor-element-contact_split_con {
    flex-direction: column !important;
    gap: 24px !important;
  }
  .axela-contact-hub-left,
  .axela-contact-form-right,
  .elementor-element-contact_hub_left,
  .elementor-element-contact_form_right {
    flex: 0 0 100% !important;
    max-width: 100% !important;
    width: 100% !important;
  }
  .elementor-element-stages_grid_con,
  .axela-approach-compact-grid {
    flex-direction: column !important;
    gap: 14px !important;
  }
}

/* =============================================================================
   SECTION 8: SLIM MODERN FOOTER — 100% NATIVE ELEMENTOR ARCHITECTURE (SIDE-BY-SIDE)
   ============================================================================= */
.axela-footer-slim-root {
  background: #04070D !important;
  border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
  padding: 34px 0 20px 0 !important;
  width: 100% !important;
}

.axela-footer-inner {
  max-width: 1400px !important;
  margin: 0 auto !important;
  padding: 0 24px !important;
}

.axela-footer-top {
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
  flex-wrap: wrap !important;
  gap: 36px !important;
  margin-bottom: 20px !important;
}

.axela-footer-brand {
  display: flex !important;
  flex-direction: row !important;
  align-items: center !important;
  gap: 24px !important;
  max-width: 650px !important;
}

.axela-footer-logo-wrap img,
.axela-footer-logo {
  height: 38px !important;
  max-height: 40px !important;
  width: auto !important;
  min-width: 85px !important;
  aspect-ratio: 1156 / 499 !important;
  max-width: 150px !important;
  display: block !important;
  flex-shrink: 0 !important;
}

.axela-footer-services-text,
.axela-footer-services-text .elementor-heading-title {
  font-size: 10px;
  font-weight: 450;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #94A3B8;
  font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
  line-height: 1.5;
  max-width: 440px;
  margin: 0;
  text-align: left;
}

.axela-footer-nav-wrap {
  display: flex !important;
  flex-direction: row !important;
  gap: 32px !important;
  justify-content: flex-end !important;
}

.axela-footer-nav-wrap .elementor-icon-list-icon,
.axela-footer-bottom-links .elementor-icon-list-icon {
  display: none !important;
}

.axela-footer-nav-wrap .elementor-icon-list-item,
.axela-footer-nav-wrap .elementor-icon-list-item a {
  padding: 0 !important;
  margin: 0 !important;
}

.axela-footer-nav-wrap .elementor-icon-list-text {
  color: #94A3B8;
  font-size: 12.5px;
  font-weight: 450;
  font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
  transition: color 0.2s ease;
}

.axela-footer-nav-wrap .elementor-icon-list-item:hover .elementor-icon-list-text,
.axela-footer-nav-wrap .elementor-icon-list-item a:hover .elementor-icon-list-text {
  color: #FF3131;
}

.axela-footer-divider {
  margin: 0 0 14px 0 !important;
}

.axela-footer-divider .elementor-divider {
  padding: 0 !important;
}

.axela-footer-divider .elementor-divider-separator {
  border-top: 1px solid rgba(255, 255, 255, 0.18) !important;
}

.axela-footer-bottom {
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
  flex-wrap: wrap !important;
  gap: 16px !important;
}

.axela-footer-copy,
.axela-footer-copy .elementor-heading-title {
  margin: 0;
  font-size: 11.5px;
  font-weight: 400;
  color: #94A3B8;
  font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
}

.axela-footer-bottom-links .elementor-icon-list-items {
  display: flex !important;
  flex-direction: row !important;
  gap: 20px !important;
  align-items: center !important;
  flex-wrap: wrap !important;
}

.axela-footer-bottom-links .elementor-icon-list-text {
  color: #64748B;
  font-size: 11.5px;
  font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
  transition: color 0.2s ease;
}

.axela-footer-bottom-links .elementor-icon-list-item:hover .elementor-icon-list-text,
.axela-footer-bottom-links .elementor-icon-list-item a:hover .elementor-icon-list-text {
  color: #D4AF37;
}

@media (max-width: 768px) {
  .axela-footer-top {
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 20px !important;
  }
  .axela-footer-brand {
    flex-direction: column !important;
    align-items: flex-start !important;
    max-width: 100% !important;
    gap: 12px !important;
  }
  .axela-footer-services-text,
  .axela-footer-services-text .elementor-heading-title {
    max-width: 100%;
    font-size: 10px;
    line-height: 1.5;
  }
  .axela-footer-nav-wrap {
    flex-direction: row !important;
    flex-wrap: wrap !important;
    gap: 14px 24px !important;
    width: 100% !important;
    justify-content: flex-start !important;
  }
  .axela-footer-bottom {
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 12px !important;
  }
}"""

def sync_css():
    # 1. Update custom-css/global-dark-theme.css (cleanly without duplicate stacking)
    css_path = r'c:\xampp\htdocs\axela-local\custom-css\global-dark-theme.css'
    with open(css_path, 'r', encoding='utf-8') as f:
        existing = f.read()

    base = existing.split('/* =============================================================================\n   AXELA GLOBAL — MASTER REFINEMENT STYLESHEET')[0].strip()
    full_css = base + "\n\n" + css_rules.strip()
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(full_css)
    print(f"Updated {css_path} successfully (cleaned duplicates, length: {len(full_css)})!")

    # 2. Update wp-content/themes/astra-child/style.css (cleanly without duplicate stacking)
    theme_css_path = r'c:\xampp\htdocs\axela-local\wp-content\themes\astra-child\style.css'
    with open(theme_css_path, 'r', encoding='utf-8') as f:
        theme_existing = f.read()

    theme_base = theme_existing.split('/* =============================================================================\n   AXELA GLOBAL — MASTER REFINEMENT STYLESHEET')[0].strip()
    theme_full = theme_base + "\n\n" + css_rules.strip()
    with open(theme_css_path, 'w', encoding='utf-8') as f:
        f.write(theme_full)
    print(f"Updated {theme_css_path} successfully (cleaned duplicates, length: {len(theme_full)})!")

    # 3. Synchronize to WordPress Post 40 (Customizer CSS)
    BASE_URL = "https://axelaglobal.com"
    AUTH_STR = "admin:FYCY 52pM wknI 1nOf 4RA2 t8zP"
    AUTH_B64 = base64.b64encode(AUTH_STR.encode("ascii")).decode("ascii")
    headers = {
        "Authorization": f"Basic {AUTH_B64}",
        "Content-Type": "application/json"
    }

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

    print("\n=== Updating Customizer CSS Post 40 in WordPress ===")
    clean_css = re.sub(r'/\*[\s\S]*?\*/', '', full_css)
    lines = [l.strip() for l in clean_css.splitlines() if l.strip()]
    minified = ' '.join(lines).replace('"', "'")
    res_p40 = run_wp_cli(f'post update 40 --post_content="{minified}"')
    print("Post 40 update result:", res_p40)

    print("\n=== Flushing Elementor CSS ===")
    res_elem = run_wp_cli("elementor flush-css --regenerate")
    print("Elementor CSS flush result:", res_elem)

    print("\n=== Purging LiteSpeed Cache ===")
    res_purge = run_wp_cli("litespeed-purge all")
    print("LiteSpeed purge result:", res_purge)

if __name__ == '__main__':
    sync_css()
