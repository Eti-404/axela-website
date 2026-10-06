import json
import urllib.request
import base64

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
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

def build_native_footer():
    # 1. Nav Column 1 (Home, About Us, Services)
    nav_col_1 = {
        "id": "axela_footer_nav_list_1",
        "elType": "widget",
        "widgetType": "icon-list",
        "settings": {
            "_title": "Navigation Links (1-3)",
            "icon_list": [
                {
                    "_id": "nav_link_home",
                    "text": "Home",
                    "link": {"url": "#home", "is_external": "", "nofollow": ""},
                    "selected_icon": {"value": "", "library": ""}
                },
                {
                    "_id": "nav_link_about",
                    "text": "About Us",
                    "link": {"url": "#about", "is_external": "", "nofollow": ""},
                    "selected_icon": {"value": "", "library": ""}
                },
                {
                    "_id": "nav_link_services",
                    "text": "Services",
                    "link": {"url": "#services", "is_external": "", "nofollow": ""},
                    "selected_icon": {"value": "", "library": ""}
                }
            ],
            "icon_align": "left",
            "text_color": "#94A3B8",
            "text_color_hover": "#DA423C",
            "typography_typography": "custom",
            "typography_font_family": "Plus Jakarta Sans",
            "typography_font_size": {"unit": "px", "size": 12.5},
            "typography_font_weight": "450",
            "space_between": {"unit": "px", "size": 10}
        },
        "elements": []
    }

    # 2. Nav Column 2 (Products, Approach, Routes)
    nav_col_2 = {
        "id": "axela_footer_nav_list_2",
        "elType": "widget",
        "widgetType": "icon-list",
        "settings": {
            "_title": "Navigation Links (4-6)",
            "icon_list": [
                {
                    "_id": "nav_link_products",
                    "text": "Products",
                    "link": {"url": "#products", "is_external": "", "nofollow": ""},
                    "selected_icon": {"value": "", "library": ""}
                },
                {
                    "_id": "nav_link_approach",
                    "text": "Approach",
                    "link": {"url": "#approach", "is_external": "", "nofollow": ""},
                    "selected_icon": {"value": "", "library": ""}
                },
                {
                    "_id": "nav_link_routes",
                    "text": "Routes",
                    "link": {"url": "#network", "is_external": "", "nofollow": ""},
                    "selected_icon": {"value": "", "library": ""}
                }
            ],
            "icon_align": "left",
            "text_color": "#94A3B8",
            "text_color_hover": "#DA423C",
            "typography_typography": "custom",
            "typography_font_family": "Plus Jakarta Sans",
            "typography_font_size": {"unit": "px", "size": 12.5},
            "typography_font_weight": "450",
            "space_between": {"unit": "px", "size": 10}
        },
        "elements": []
    }

    # 3. Nav Column 3 (Investment, Ethics, Contact)
    nav_col_3 = {
        "id": "axela_footer_nav_list_3",
        "elType": "widget",
        "widgetType": "icon-list",
        "settings": {
            "_title": "Navigation Links (7-9)",
            "icon_list": [
                {
                    "_id": "nav_link_investment",
                    "text": "Investment",
                    "link": {"url": "#investment", "is_external": "", "nofollow": ""},
                    "selected_icon": {"value": "", "library": ""}
                },
                {
                    "_id": "nav_link_ethics",
                    "text": "Ethics",
                    "link": {"url": "#ethics", "is_external": "", "nofollow": ""},
                    "selected_icon": {"value": "", "library": ""}
                },
                {
                    "_id": "nav_link_contact",
                    "text": "Contact",
                    "link": {"url": "#contact", "is_external": "", "nofollow": ""},
                    "selected_icon": {"value": "", "library": ""}
                }
            ],
            "icon_align": "left",
            "text_color": "#94A3B8",
            "text_color_hover": "#DA423C",
            "typography_typography": "custom",
            "typography_font_family": "Plus Jakarta Sans",
            "typography_font_size": {"unit": "px", "size": 12.5},
            "typography_font_weight": "450",
            "space_between": {"unit": "px", "size": 10}
        },
        "elements": []
    }

    footer_data = [
        {
            "id": "axela_footer_root_container",
            "elType": "container",
            "isInner": False,
            "settings": {
                "_title": "Global Footer Root Container",
                "content_width": "full",
                "background_background": "classic",
                "background_color": "#04070D",
                "border_border": "solid",
                "border_width": {
                    "unit": "px",
                    "top": "1",
                    "right": "0",
                    "bottom": "0",
                    "left": "0",
                    "isLinked": False
                },
                "border_color": "rgba(255, 255, 255, 0.08)",
                "padding": {
                    "unit": "px",
                    "top": "34",
                    "right": "24",
                    "bottom": "20",
                    "left": "24",
                    "isLinked": False
                },
                "_css_classes": "axela-footer-slim-root",
                "css_classes": "axela-footer-slim-root"
            },
            "elements": [
                {
                    "id": "axela_footer_inner_container",
                    "elType": "container",
                    "isInner": True,
                    "settings": {
                        "_title": "Footer Content Wrapper (1400px)",
                        "content_width": "boxed",
                        "boxed_width": {"unit": "px", "size": 1400},
                        "flex_direction": "column",
                        "gap": {"unit": "px", "column": 0, "row": 20},
                        "_css_classes": "axela-footer-inner",
                        "css_classes": "axela-footer-inner"
                    },
                    "elements": [
                        # Top Row Container (Brand Column + Nav Column)
                        {
                            "id": "axela_footer_top_row",
                            "elType": "container",
                            "isInner": True,
                            "settings": {
                                "_title": "Footer Top Row (Brand & Nav)",
                                "flex_direction": "row",
                                "flex_direction_mobile": "column",
                                "flex_justify_content": "space-between",
                                "flex_align_items": "center",
                                "flex_align_items_mobile": "flex-start",
                                "flex_wrap": "wrap",
                                "gap": {"unit": "px", "column": 36, "row": 20},
                                "_css_classes": "axela-footer-top",
                                "css_classes": "axela-footer-top"
                            },
                            "elements": [
                                # Brand Column (Side-by-Side: Logo + Core Services Text)
                                {
                                    "id": "axela_footer_brand_col",
                                    "elType": "container",
                                    "isInner": True,
                                    "settings": {
                                        "_title": "Brand & Core Services (Side-by-Side)",
                                        "flex_direction": "row",
                                        "flex_direction_mobile": "column",
                                        "flex_align_items": "center",
                                        "flex_align_items_mobile": "flex-start",
                                        "gap": {"unit": "px", "column": 24, "row": 12},
                                        "width": {"unit": "px", "size": 650},
                                        "width_mobile": {"unit": "%", "size": 100},
                                        "_css_classes": "axela-footer-brand",
                                        "css_classes": "axela-footer-brand"
                                    },
                                    "elements": [
                                        # Logo Image Widget
                                        {
                                            "id": "axela_footer_logo_widget",
                                            "elType": "widget",
                                            "widgetType": "image",
                                            "settings": {
                                                "_title": "AXELA Logo (Clickable)",
                                                "image": {
                                                    "url": "https://axelaglobal.com/wp-content/uploads/2026/10/cropped-Axela-Limited-Transparent-Logo.png",
                                                    "id": 48
                                                },
                                                "image_size": "full",
                                                "link_to": "custom",
                                                "link": {"url": "#home", "is_external": "", "nofollow": ""},
                                                "align": "left",
                                                "width": {"unit": "px", "size": 140},
                                                "image_custom_dimension": {"width": 140, "height": 38},
                                                "_css_classes": "axela-footer-logo-wrap",
                                                "css_classes": "axela-footer-logo-wrap"
                                            },
                                            "elements": []
                                        },
                                        # Core Services Heading Widget (Side-by-Side, Refined Slim Typography)
                                        {
                                            "id": "axela_footer_services_widget",
                                            "elType": "widget",
                                            "widgetType": "heading",
                                            "settings": {
                                                "_title": "Core Services Text",
                                                "title": "ENERGY • COMMODITIES • TRADING • SUPPLY • PROJECT DEVELOPMENT • INVESTMENT ADVISORY",
                                                "header_size": "div",
                                                "title_color": "#94A3B8",
                                                "typography_typography": "custom",
                                                "typography_font_family": "Plus Jakarta Sans",
                                                "typography_font_size": {"unit": "px", "size": 10},
                                                "typography_font_weight": "450",
                                                "typography_letter_spacing": {"unit": "em", "size": 0.08},
                                                "typography_line_height": {"unit": "em", "size": 1.5},
                                                "typography_text_transform": "uppercase",
                                                "_css_classes": "axela-footer-services-text",
                                                "css_classes": "axela-footer-services-text"
                                            },
                                            "elements": []
                                        }
                                    ]
                                },
                                # Navigation Links 3-column Flex Container
                                {
                                    "id": "axela_footer_nav_container",
                                    "elType": "container",
                                    "isInner": True,
                                    "settings": {
                                        "_title": "Footer Navigation Links (3 Columns)",
                                        "flex_direction": "row",
                                        "flex_justify_content": "flex-end",
                                        "gap": {"unit": "px", "column": 32, "row": 10},
                                        "_css_classes": "axela-footer-nav-wrap",
                                        "css_classes": "axela-footer-nav-wrap"
                                    },
                                    "elements": [
                                        nav_col_1,
                                        nav_col_2,
                                        nav_col_3
                                    ]
                                }
                            ]
                        },
                        # Divider Line Widget (Compact 14px bottom margin)
                        {
                            "id": "axela_footer_divider_widget",
                            "elType": "widget",
                            "widgetType": "divider",
                            "settings": {
                                "_title": "Footer Horizontal Divider",
                                "style": "solid",
                                "weight": {"unit": "px", "size": 1},
                                "color": "rgba(255, 255, 255, 0.18)",
                                "gap": {"unit": "px", "size": 0},
                                "margin": {
                                    "unit": "px",
                                    "top": "0",
                                    "right": "0",
                                    "bottom": "0",
                                    "left": "0",
                                    "isLinked": True
                                },
                                "_css_classes": "axela-footer-divider",
                                "css_classes": "axela-footer-divider"
                            },
                            "elements": []
                        },
                        # Bottom Row Container (Copyright & Legal)
                        {
                            "id": "axela_footer_bottom_row",
                            "elType": "container",
                            "isInner": True,
                            "settings": {
                                "_title": "Footer Bottom Row (Copyright & Legal)",
                                "flex_direction": "row",
                                "flex_direction_mobile": "column",
                                "flex_justify_content": "space-between",
                                "flex_align_items": "center",
                                "flex_align_items_mobile": "flex-start",
                                "gap": {"unit": "px", "column": 16, "row": 12},
                                "_css_classes": "axela-footer-bottom"
                            },
                            "elements": [
                                # Copyright Text Widget
                                {
                                    "id": "axela_footer_copyright_widget",
                                    "elType": "widget",
                                    "widgetType": "heading",
                                    "settings": {
                                        "_title": "Copyright & Partner Notice",
                                        "title": "© 2026 AXELA LTD. All rights reserved | Digital Growth Partner: E-GUIDER",
                                        "header_size": "div",
                                        "title_color": "#94A3B8",
                                        "typography_typography": "custom",
                                        "typography_font_family": "Plus Jakarta Sans",
                                        "typography_font_size": {"unit": "px", "size": 12},
                                        "typography_font_weight": "400",
                                        "_css_classes": "axela-footer-copy"
                                    },
                                    "elements": []
                                },
                                # Legal Links (Inline Icon-List)
                                {
                                    "id": "axela_footer_legal_widget",
                                    "elType": "widget",
                                    "widgetType": "icon-list",
                                    "settings": {
                                        "_title": "Privacy & Terms Links",
                                        "view": "inline",
                                        "space_between": {"unit": "px", "size": 20},
                                        "text_color": "#64748B",
                                        "text_color_hover": "#D4AF37",
                                        "typography_typography": "custom",
                                        "typography_font_family": "Plus Jakarta Sans",
                                        "typography_font_size": {"unit": "px", "size": 12},
                                        "typography_font_weight": "400",
                                        "icon_list": [
                                            {
                                                "_id": "legal_privacy",
                                                "text": "Privacy & Compliance",
                                                "link": {"url": "#ethics", "is_external": "", "nofollow": ""},
                                                "selected_icon": {"value": "", "library": ""}
                                            },
                                            {
                                                "_id": "legal_terms",
                                                "text": "Terms of Trade",
                                                "link": {"url": "#approach", "is_external": "", "nofollow": ""},
                                                "selected_icon": {"value": "", "library": ""}
                                            }
                                        ],
                                        "_css_classes": "axela-footer-bottom-links"
                                    },
                                    "elements": []
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]

    print("Deploying 100% Native Elementor Footer to Post 38...")
    payload = {
        "id": 38,
        "title": "AXELA LTD. — Global Dark Footer",
        "status": "publish",
        "data": footer_data
    }
    req = urllib.request.Request(
        f"{BASE_URL}/wp-json/wpvibe/v1/elementor/save-page",
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST"
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        print("WPVibe Save Result:", res)

    print("Flushing Elementor CSS...")
    print(run_cli("elementor flush-css"))
    print("Purging LiteSpeed Cache...")
    print(run_cli("litespeed-purge all"))
    print("Footer updated to 100% Native Elementor Widgets successfully!")

if __name__ == "__main__":
    build_native_footer()
