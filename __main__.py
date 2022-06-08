from datetime import datetime
import random as r
import argparse
import readline

from hexes import hexes
import history_settings as hs

txt_history = True

parser = argparse.ArgumentParser()  # description=''

parser.add_argument('query', type=str)
parser.add_argument('--nh', help="don't write to history.txt", action='store_false', default=True)
# parser.add_argument('--dm', help="specify divination method", choices=['stalks', 'c3'] )

args = parser.parse_args()
query = args.query


def evaluation(lines, origin_code):
    to_read = []
    how_many_lines = len(lines)
    match how_many_lines:
        case 0:
            to_read = '...'
            commentary = '...'
            return to_read, commentary
        case 1:
            to_read = lines
            commentary = "original hexagram's changing line applies."
            return to_read, commentary
        case 2:
            to_read = lines
            commentary = "original hexagram's changing lines apply. the uppermost line of the two is most important"
            return to_read, commentary
        case 3:
            to_read = lines
            commentary = "original hexagram's changing lines apply. the middle line is most important"
            return to_read, commentary
        case 4:
            to_read = min(list({1, 2, 3, 4, 5, 6} - set(lines)))
            commentary = "transformed hexagram's lower, non-changing line applies."
            return to_read, commentary
        case 5:
            to_read = sorted(list({1, 2, 3, 4, 5, 6} - set(lines)))
            commentary = "transformed hexagram's non-changing line applies."
            return to_read, commentary
        case 6:
            if origin_hexagram_code == "111111" or origin_hexagram_code == '000000':
                to_read = "special"
                commentary = "read the special statement"
                return to_read, commentary
            to_read = {}
            commentary ="the first hexagram's situation is entirely past or on the brink of change, the second" \
                        " hexagram is more important, take the judgment"
            return to_read, commentary



if __name__ == '__main__':
    try:
        readline.remove_history_item(1)
    except ValueError:
        pass

    coin_values = ''
    origin_hexagram_code = ''
    trans_hexagram_code = ''
    for line in range(1, 7):
        line = r.choice([3, 2]) + r.choice([3, 2]) + r.choice([3, 2])
        coin_values += str(line)

    changing_lines = []
    for i in range(0, len(coin_values)):
        match coin_values[i]:
            case '6':
                origin_hexagram_code += '0'
                trans_hexagram_code += '1'
                changing_lines.append(i + 1)
            case '7':
                origin_hexagram_code += '1'
                trans_hexagram_code += '1'
            case '8':
                origin_hexagram_code += '0'
                trans_hexagram_code += '0'
            case '9':
                origin_hexagram_code += '1'
                trans_hexagram_code += '0'
                changing_lines.append(i + 1)

    origin_hexagram = hexes[origin_hexagram_code]
    trans_hexagram = hexes[trans_hexagram_code]

    lines_to_read, commentary = evaluation(changing_lines, origin_hexagram_code)

    lines_to_read_rep = ''
    for line in lines_to_read:
        lines_to_read_rep += f"{line}, "
    lines_to_read_rep = lines_to_read_rep[:-2]

    time = datetime.now().isoformat(timespec='minutes')
    output = f"{time}:\n{origin_hexagram}->{trans_hexagram}"

    hs.print_write(query, output, lines_to_read_rep, txt_history, commentary)
