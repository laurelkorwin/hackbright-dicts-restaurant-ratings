# your code goes here
def display_restaurant_ratings(filename):
    with open(filename) as restaurant_list:
        restaurants_and_ratings = {}
        for line in restaurant_list:
            line = line.rstrip()
            keys_values = line.split(':')
            restaurant_name = keys_values[0]
            restaurant_rating = int(keys_values[1])
            restaurants_and_ratings[restaurant_name] = restaurants_and_ratings.get(restaurant_name, restaurant_rating)

        # print restaurants_and_ratings
        for restaurant_name, restaurant_rating in restaurants_and_ratings.items():
            print "{} is rated at {}".format(restaurant_name, restaurant_rating)

display_restaurant_ratings('scores.txt')