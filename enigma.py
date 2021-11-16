#switch statement for python

def choose_letter(letter):
    switcher = {
        '11': 'A',
        '12': 'B',
        '13': 'C',
        '21': 'D',
        '22': 'E',
        '23': 'F',
        '31': 'G',
        '32': 'H',
        '33': 'I',
        '41': 'J',
        '42': 'K',
        '43': 'L',
        '51': 'M',
        '52': 'N',
        '53': 'O',
        '61': 'P',
        '62': 'Q',
        '63': 'R',
        '71': 'S',
        '72': 'T',
        '73': 'U',
        '81': 'V',
        '82': 'W',
        '83': 'X',
        '91': 'Y',
        '92': 'Z',
        '00': ' ',
    }
    return switcher.get(letter, " ")

string = input('Message Intercepted: ').replace(' ', '00')


def break_string(string):
    return [string[i:i+2] for i in range(0, len(string), 2)]

list_string = list(break_string(string))

message_list = []
#iterate over list_string above and return respective letter from choose_letter function
for i in range(len(list_string)):
    message_list.append(choose_letter(list_string[i]))

# convert message_list to string
message = ''.join(message_list)
print(f"Meaning of Message: {message}")