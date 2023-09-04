#part one
def padel_court_cost(court_type):
    if court_type == 'indoor':
        return (30)
    elif court_type == 'outdoor':
        return (20)
#part two
def rackest_cost(racekt_brand):
    if racekt_brand == "Bullpadel":
        return (100)
    elif racekt_brand == "Nox":
        return (140)
    elif racekt_brand == 'Siux':
        return (200)
#part three
def padel_balls_cost(ball_boxes):
    if ball_boxes == 1:
        return (2)
    elif ball_boxes == 2:
        return (3.5)
    elif ball_boxes == 3:
        return (5)
#part four
def padel_game_cost():
    the_Court_type = input('enter the court type ')
    the_racket_brand = input('enter the racket brand ')
    number_of_ball_boxes = input('enter the numbers of ball boxes ')
    padel_court_cost(the_Court_type)
    rackest_cost(the_racket_brand)
    padel_balls_cost(int(number_of_ball_boxes))
    result = padel_court_cost(the_Court_type) + rackest_cost(the_racket_brand) + padel_balls_cost(int(number_of_ball_boxes))
    print(result)
padel_game_cost()