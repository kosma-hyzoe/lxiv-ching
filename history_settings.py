# settings
path = 'lxivChing/history-lxiv.txt'


def print_write(query, output, lines_to_read, txt_history, commentary):
    print(
        f"Query: {query}" + '\n' +
        f"Result: {output}" + '\n' +
        f"Lines_to_read: {lines_to_read}" + '\n' +
        f'Commentary: {commentary}'
    )

    if txt_history:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(
                query + '\n' +
                output + '\n' +
                lines_to_read
            )
            f.write('\n' * 2)


# with open(path + "lxiv-his.json", 'aw', encoding='utf-8') as f:
#     f.write(
#         query + '\n' +
#         output + '\n' +
#         changing_lines
#     )
#     f.write('\n' * 2)
