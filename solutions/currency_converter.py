def convert(dollars):
    if dollars < 0:
        return 'Cannot have negative value'
    
    header = "This program converts US dollars to Korean Won\n"

    won = convert_to_won(dollars)
    
    result = header + f'${dollars} is {won} won'
    return result

convert_to_won = lambda dollars: dollars * 1356.62
