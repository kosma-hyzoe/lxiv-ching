from datetime import datetime
import random as r
import argparse

from hexes import hexes
import history_settings as hs

txt_history = True

parser = argparse.ArgumentParser() # description=''

parser.add_argument('query', type=str)
parser.add_argument('--nh', help="don't write to history.txt", action='store_false', default=True)
# parser.add_argument('--dm', help="specify divination method", choices=['stalks', 'c3'] )


args = parser.parse_args()
query = args.query


def modern():
    h = r.randint(1, 64)
    th = r.randint(1, 64)
    time = datetime.now().isoformat(timespec='minutes').replace('T', ', ')
    output = f"{time}:\n{h}->{th}"

    changing_lines = []
    for i in range(0, 6):
        if hexes[h].code[::-1][i] != hexes[th].code[::-1][i]:
            changing_lines.append(i + 1)

    lines_to_read = []
    # 6 changing lines
    if len(changing_lines) == 6:
        if hexes[h].code == '111111' or hexes[h].code == '000000':
            lines_to_read.append('special line')  # special line
        else:
            lines_to_read.append(6)
    # 6 > changing lines > 3
    elif len(changing_lines) >= 4:
        for line in range(6, 0, -1):
            if line not in changing_lines:
                lines_to_read.append(line)
                break
    # 3 or less chaning lines
    else:
        for line in changing_lines:
            lines_to_read.append(line)

    lines_string = ''
    for line in lines_to_read:
        lines_string += f'{line}, '
    changing_lines = "Line(s) to read: " + lines_string[:-2]
    print(output + '\n' + changing_lines)

    hs.write(query, output, changing_lines, txt_history)


if __name__ == '__main__':
    modern()