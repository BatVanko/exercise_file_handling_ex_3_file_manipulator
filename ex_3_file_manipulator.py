import os
commands = input()
while commands != 'End':
    manipulations = commands.split('-')
    if manipulations[0] == 'Create':
        file_name = manipulations[1]
        with open(f'./{file_name}', 'w') as file:
            file.write('')
    elif manipulations[0] == 'Add':
        file_name = manipulations[1]
        content = manipulations[2]
        with open(f'./{file_name}', 'a+') as file:
            file.write(f'{content}\n')
    elif manipulations[0] == 'Replace':
        file_name = manipulations[1]
        old_string = manipulations[2]
        new_string = manipulations[3]
        try:
            with open(f'./{file_name}', 'r+') as file:
                original_text = file.read()
                new_text = original_text.replace(old_string, new_string)
                file.truncate(0)
                file.seek(0)
                file.write(new_text)
        except:
            print("An error occurred")
    elif manipulations[0] == 'Delete':
        file_name = manipulations[1]
        try:
            os.remove(f'./{file_name}')
        except:
            print("An error occurred")

    commands = input()
