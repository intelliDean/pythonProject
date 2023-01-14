from typing import Set, Any


def custom_sets(lists: list) -> list[Any]:
    new_set = [lists[0]]
    for i in lists:
        if i not in new_set:
            new_set.append(i)
    return new_set


def built_in_sets(lists: list) -> set[Any]:
    return set(lists)


if __name__ == '__main__':
    lang1 = ['yoruba', 'igbo', 'hausa', 'urobo']
    lang2 = ['itshekiri', 'yoruba', 'hausa', 'tiffi']
    lang3 = ['igbo', 'tiffi', 'urobo', 'yoruba']

    languages = lang1 + lang2 + lang3

    print(custom_sets(languages))

    print(built_in_sets(languages))