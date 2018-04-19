import sys
import markdown2

if sys.version_info < (3, 7, 0):
    raise Exception('Use python 3!')

def main():
    with open('two_sevens_four_sevens_draft.md', 'r') as f:
        all_text = f.read()
    with open('two_sevens_four_sevens_archive.md', 'w') as f:
        f.write(all_text)
    parts = all_text.split('<END>')
    assert len(parts) == 2
    important_text = parts[0].strip()
    assert all(i == '#' for i in important_text.split('\n')[0].split(' ')[0])
    title = important_text.split('\n')[0].replace('#', '').strip()
    print('Wordcount: ' + str(len(important_text.split())))
    with open('two_sevens_four_sevens.md', 'w') as f:
        f.write(important_text)
    html_text = markdown2.markdown(important_text)
    with open('two_sevens_four_sevens.html', 'w') as f:
        f.write(f'''<!DOCTYPE html>
<html>
<head>
<title>{title}</title>
</head>
<body>
{html_text}
</body>
</html>''')


if __name__ == '__main__':
    main()
