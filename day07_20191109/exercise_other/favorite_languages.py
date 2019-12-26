favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for name, language in favorite_languages.items():
    # print("Sarah's favorite languae is " + favorite_languages['jen'].title() + ".")
    print("{0}'s favorite languae is {1}.".format(name.title(), language.title()))

# Sarah's favorite languae is Python.
"""
Jen's favorite languae is Python.
Sarah's favorite languae is C.
Edward's favorite languae is Ruby.
Phil's favorite languae is Python.
"""


