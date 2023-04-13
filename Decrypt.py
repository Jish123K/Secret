import torch

import string

import dictionary as dict

# Converting the dictionary to tensors for faster lookup

morse_code_dict = dict.MORSE_CODE_DICT

keys = list(morse_code_dict.keys())

values = list(morse_code_dict.values())

keys_tensor = torch.tensor([ord(k) for k in keys])

values_tensor = torch.tensor([v for v in values])

# A function used to decrypt morse code into plain text

def decryptor(text):

    # Adding a space at the end so that it can access the last letter

    text += " "

    morse_code = ""

    plain_text = ""

    for letter in text:

        if letter == "." or letter == "-":

            morse_code += letter

        elif letter == " ":

            if morse_code != "":

                idx = (values_tensor == morse_code).nonzero(as_tuple=True)[0]

                if idx.numel() > 0:

                    plain_text += chr(keys_tensor[idx])

                else:

                    plain_text += "[unknown]"

                morse_code = ""

        else:

            # Ignore non-morse code characters

            pass

    print("The plain text is: ", plain_text)

    return plain_text

