# settings
path = 'lxivChing/history-lxiv.txt'


def write(query, output, changing_lines, txt_history):
    if txt_history:
        print('ye')
        with open(path, 'a', encoding='utf-8') as f:
            f.write(
                query + '\n' +
                output + '\n' +
                changing_lines
            )
            f.write('\n' * 2)


# with open(path + "lxiv-his.json", 'aw', encoding='utf-8') as f:
#     f.write(
#         query + '\n' +
#         output + '\n' +
#         changing_lines
#     )
#     f.write('\n' * 2)
