def convert(number):
    my_list = []
    my_string = ''
    try:
        for i in range(1, number + 1):
            if number % i == 0:
                my_list.append(i)
        if (3 in my_list) or (5 in my_list) or (7 in my_list):
            for n in my_list:
                if n == 3:
                    my_string += 'Pling'
                elif n == 5:
                    my_string += 'Plang'
                elif n ==7:
                    my_string += 'Plong'
            return my_string
        else:
            return (str(number))
    except ValueError:
        raise Exception ("Supplied argument is not a valid integer.")cd