# Excercise 8 - http://learnpythonthehardway.org/book/ex8.html

formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# Extra Credit
# 1: Checked my work, no mistakes
# 2: The double quotes show up on the third sentence because it has an apostrophe.

