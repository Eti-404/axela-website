import re

files_to_clean = [
    'wp-content/themes/astra-child/style.css',
    'build_native_header.py',
    'custom-css/global-dark-theme.css',
    'update_master_css.py'
]

for fpath in files_to_clean:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    count_before = len(re.findall(r'font-family:[^;]+!important;', content))
    # Remove !important from font-family
    new_content = re.sub(r'(font-family:\s*[^;!]+?)\s*!important;', r'\1;', content)
    count_after = len(re.findall(r'font-family:[^;]+!important;', new_content))

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"{fpath}: stripped {count_before - count_after} instances (remaining: {count_after})")
