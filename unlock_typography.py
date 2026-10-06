import re

def process_file():
    with open('update_master_css.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the Footer CSS block to side-by-side horizontal layout and compact padding
    old_footer_pattern = re.compile(
        r'/\* =+ \n\s*SECTION 8: SLIM MODERN FOOTER — 100% NATIVE ELEMENTOR ARCHITECTURE[\s\S]*?@media \(max-width: 768px\) \{[\s\S]*?\}\s*\}',
        re.DOTALL
    )

    new_footer_css = """/* =============================================================================
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
  color: #DA423C;
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

    # 2. Systematically unlock typography by removing '!important' from font/color rules on headings and text blocks
    # Specifically target:
    # font-size: Xpx !important; -> font-size: Xpx;
    # font-family: X !important; -> font-family: X;
    # font-weight: X !important; -> font-weight: X;
    # line-height: X !important; -> line-height: X;
    # letter-spacing: X !important; -> letter-spacing: X;
    # Except for: buttons (where sizing is structural), sticky header dimensions, and form inputs
    
    # We will remove !important from typography inside heading and text selectors:
    def unlock_props(match):
        block = match.group(0)
        # Protect buttons, inputs, tickers if needed, but for headings, titles, eyebrows, subtitles, cards:
        # remove !important on font-size, font-weight, line-height, letter-spacing, font-family, and text color
        unlocked = re.sub(r'(font-size:\s*[^;]+?)\s*!important;', r'\1;', block)
        unlocked = re.sub(r'(font-family:\s*[^;]+?)\s*!important;', r'\1;', block)
        unlocked = re.sub(r'(font-weight:\s*[^;]+?)\s*!important;', r'\1;', block)
        unlocked = re.sub(r'(line-height:\s*[^;]+?)\s*!important;', r'\1;', block)
        unlocked = re.sub(r'(letter-spacing:\s*[^;]+?)\s*!important;', r'\1;', block)
        unlocked = re.sub(r'(color:\s*[^;]+?)\s*!important;', r'\1;', unlocked)
        return unlocked

    # Target heading, title, eyebrow, subtitle, card text selectors
    target_selectors_pattern = re.compile(
        r'(\.(?:axela-hero-title|axela-section-title|axela-section-eyebrow|axela-section-header|axela-section-subtitle|service-card-|category-card-|stage-card-|invest-box-|invest-pillars-|compliance-title|approach-title|axela-footer-services-text|axela-footer-copy)[^{]*?\{[^}]*?\})',
        re.DOTALL
    )

    unlocked_content = target_selectors_pattern.sub(unlock_props, content)
    
    # Also unlock universal editorial serif block lines 166-178
    unlocked_content = re.sub(
        r'(h1,\s*h2,[\s\S]*?\.elementor-widget-heading h2\s*\{[^}]*?\})',
        unlock_props,
        unlocked_content
    )

    # Replace footer section
    if "SECTION 8: SLIM MODERN FOOTER — 100% NATIVE ELEMENTOR ARCHITECTURE" in unlocked_content:
        # replace up to the end of that section
        start_idx = unlocked_content.find("/* =============================================================================\n   SECTION 8: SLIM MODERN FOOTER — 100% NATIVE ELEMENTOR ARCHITECTURE")
        end_idx = unlocked_content.find('"""', start_idx)
        if start_idx != -1 and end_idx != -1:
            unlocked_content = unlocked_content[:start_idx] + new_footer_css + "\n" + unlocked_content[end_idx:]

    with open('update_master_css.py', 'w', encoding='utf-8') as f:
        f.write(unlocked_content)

    print("update_master_css.py updated with unlocked typography and side-by-side footer!")

if __name__ == '__main__':
    process_file()
