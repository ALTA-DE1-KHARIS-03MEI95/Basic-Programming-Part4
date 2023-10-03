def draw_xyz(N):
    pattern = ""
    number = 1
    for i in range(N):
        for j in range(N):
            if number % 3 == 0:
                pattern += 'X '
            elif number % 2 == 0:
                pattern += 'Z '
            else:
                pattern += 'Y '
            number += 1
        pattern += '\n'
    return pattern

if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """


    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """