import json
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
