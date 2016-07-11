# your code goes here
def display_restaurant_ratings(filename):
    """Displays restaurant name and rating for a group of restaurants.

    Takes a file name as a parameter and returns strings detailing each restaurant's name
    and rating. Works with file formatted as restaurant_name: restaurant_rating on each line.
    """
    with open(filename) as restaurant_list: #opens file and sets it equal to the variable restaurant_list
        rest_and_ratings = {} #creates blank dictionary to store restaurants and ratings
        for line in restaurant_list: 
            line = line.rstrip() #strips line of white space
            keys_values = line.split(':') #splits line into a list with : as a delimiter
            restaurant_name = keys_values[0] #sets name equal to first item in list
            restaurant_rating = int(keys_values[1]) #sets rating equal to second item in list, made into an int
            rest_and_ratings[restaurant_name] = rest_and_ratings.get(restaurant_name, 
                                                                    restaurant_rating)
            #if restaurant_name not already in dictionary, puts it in with restaurant_rating as default value

        for restaurant_name, restaurant_rating in rest_and_ratings.items():
            #for name and rating in the dictionary's items
            print "{} is rated at {}".format(restaurant_name, restaurant_rating)
            #prints a string with name and rating

display_restaurant_ratings('scores.txt')