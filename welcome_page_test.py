import instructions_page_test

message = "Welcome to Webble"
print(message)

how_do_i_play = input("How do I play? : 1 \t \n")


selection = [how_do_i_play == "1"]

for select in selection:
    if how_do_i_play:
        print(instructions_page_test.how_to_play)
    else:
        print("Goodbye")


