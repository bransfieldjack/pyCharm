import instructions_page_test


"""
Checks that the value returned is a string
"""
if isinstance(instructions_page_test.how_to_play, str) & isinstance(instructions_page_test.will_exit_when, str):
    print("True")

