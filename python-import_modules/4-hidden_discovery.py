#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    list_hidden_4 = dir(hidden_4)
    for i in range(0, len(list_hidden_4)):
        if not list_hidden_4[i].startswith("__"):
            print(list_hidden_4[i])

# version chat-gpt :
# if __name__ == "__main__":
#   for name in dir(hidden_4):
#       if not name.startswith("__"):
#           print(name)
# visiblement, Python n'a pas besoin d'index... ><
