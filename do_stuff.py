import sys
import markdown2
import re

if sys.version_info < (3, 7, 0):
    raise Exception('Use python 3!')

def command_parse(c):
    r = [i.split(',') for i in c.split('=')]
    assert len(r[0]) == 1
    r[0] = r[0][0]
    return r

def line_parse(s):
    if s and s[0] == '!' and len(s.split(' ')[0]) > 1:
        return {
            'command': command_parse(s.split(' ')[0][1:]),
            'rest': ' '.join(s.split(' ')[1:])
        }
    else:
        return s

def all_parse(s):
    return [line_parse(i) for i in s.split('\n')]

def get_versions(s):
    version_lines = [i for i in all_parse(s)
    if type(i) != str and i['command'][0] == 'versions']
    assert len(version_lines) == 1
    assert len(version_lines[0]['command']) == 2
    return version_lines[0]['command'][1]

def version_matches(version, l):
    return any((i[0] == '!' and i[1:] != version)
    or (i[0] != '!' and i == version) or i == 'all' for i in l)

def process(text, version):
    parsed = all_parse(text)
    result = []
    on = True
    commands_on = True
    in_block = False
    for i in parsed:
        if i == '```':
            in_block = not in_block
        elif type(i) == str:
            if on:
                if in_block:
                    result.append(' ' * 4 + i)
                else:
                    result.append(i)
        elif i['command'][0] == 'commandson':
            commands_on = True
        elif i['command'][0] == 'commandsoff':
            commands_on = False
        elif not commands_on:
            pass
        elif i['command'][0] == 'versions':
            pass
        elif i['command'][0] == 'version':
            if version_matches(version, i['command'][1]) and on:
                result.append(i['rest'])
        elif i['command'][0] == 'stop':
            assert i['rest'] == ''
            if version_matches(version, i['command'][1]):
                on = False
        elif i['command'][0] in ('start', 'restart'):
            assert i['rest'] == ''
            if version_matches(version, i['command'][1]):
                on = True
        elif i['command'][0] == 'unreached':
            if on:
                raise Exception(f'{i} should never be reached!')
        elif i['command'][0] == 'reached':
            if on:
                raise Exception(f'{i} should always be reached!')
        else:
            raise Exception(f'Unrecognized command {i["command"][0]} ')
    return '\n'.join(result)

def main():
    with open('two_sevens_four_sevens_draft.md', 'r') as f:
        all_text = f.read()
    with open('two_sevens_four_sevens_archive.md', 'w') as f:
        f.write(all_text)
    for version in get_versions(all_text):
        important_text = re.sub('\n{2,}', '\n\n', process(all_text, version).strip())
        assert all(i == '#' for i in important_text.split('\n')[0].split(' ')[0])
        title = important_text.split('\n')[0].replace('#', '').strip()
        print(f'Wordcount of version {version}: {len(important_text.split())}')
        with open('two_sevens_four_sevens_' + version + '.md', 'w') as f:
            f.write(important_text)
        html_text = markdown2.markdown(important_text)
        with open('two_sevens_four_sevens_' + version + '.html', 'w') as f:
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
