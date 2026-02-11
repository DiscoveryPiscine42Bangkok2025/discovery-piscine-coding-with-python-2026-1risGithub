def array_of_names(people: dict) -> list:
    return [
        f"{first.capitalize()} {last.capitalize()}"
        for first, last in people.items()
    ]

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))