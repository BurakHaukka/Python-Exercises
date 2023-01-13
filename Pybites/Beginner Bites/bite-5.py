"""
In this Bite you will work with a list of names.

1. Write a function that accepts a list of names and title cases them and removes duplicates.

2. Next, sort the list in alphabetical descending order by surname.

3. Finally, find the shortest first name.

You can assume that the names in the list are single strings composed of two words: one given name and one surname.

Python built-ins will be very useful for solving these problems in very concise ways. Get it sorted!
"""

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(NAMES):
    """Should return a list of title cased names,
       each name appears only once"""

    name_list = []

    #name_list.append(temp_name) for x in name_list if x not in name_list]

    for name in NAMES:
        temp_name = name.title()
        name_list.append(temp_name)

    # removes duplicates by converting list to set then back to list
    names = list(set(name_list))

    return names


pass


def sort_by_surname_desc(NAMES):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(NAMES)

    # Sort the list in alphabetical descending order by surname
    names.sort(key=lambda x: x.split()[1], reverse=True)

    return names


pass


def shortest_first_name(NAMES):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(NAMES)
    first_names = [name.split()[0] for name in names]
    #last_names = [name.split()[1] for name in names]

    shortest_first_name = min(first_names, key=lambda x: len(x))
    print(shortest_first_name)
    return shortest_first_name


pass

dedup_and_title_case_names(NAMES)
sort_by_surname_desc(NAMES)
shortest_first_name(NAMES)
