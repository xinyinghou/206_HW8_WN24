# Your name: 
# Your student id:
# Your email:
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it.  
# e.g.: 
# Asked Chatgpt hints for debugging and suggesting the general sturcture of the code

import matplotlib.pyplot as plt
import os
import sqlite3
import unittest


def restaurant_data_loader(db):
    """
    This function accepts the filename of the database as a parameter, and returns a nested dictionary. Each outer 
    key of the dictionary is the name of each restaurant in the database, and each inner key is a dictionary, where the 
    key:value pairs should be the food_type, building_number, star_rating, and num_ratings for the restaurant.
    """
    pass


def plot_low_num_rating_by_type(db):
    """
    This function accepts the filename of the database as a parameter and returns a dictionary. 
    Only the restaurants with fewer than 50 ratings are included when finding the minimum num_ratings for each food_type. 
    It returns a dictionary where the keys are food types, and the values are the minimum number of ratings among the restaurants in that food type. 
    (Hint: use the SQL MIN keyword). 

    This function should also plot a bar chart with restaurant food_types along one axis and the corresponding minimum
    num_ratings along the other axis. In the chart, minimum num_ratings should be in descending order.
    """
    pass


def find_restaurant_with_star(star_rating, db):
    """
    This function accepts the star_rating and the filename of the database as parameters.
    It returns a list with the restaurants of the same star_rating in db. 
    The restaurants should be sorted by their building_number from largest to smallest 
    (Hint: Use the SQL WHERE keyword).
    """
    pass


# EXTRA CREDIT
def get_highest_weighted_average_ratings(db):  # Do this through DB as well
    """
    This function returns a dictionary with two key-value pairs. 
    The first key is the name of the highest-rated restaurant food_type, the value is its corresponding weighted average star rating; 
    the second key is the highest rated building_number, and the value is its corresponding weighted average star rating.

    This function should also plot two barcharts in one figure. 
    For the first bar chart, the y-axis will be different food_type of each restaurant. The x-axis will be the 
    weighted average star_rating for the restaurants of each food_type. The average values should be rounded to 
    two decimal places. Sort the y-axis in descending order from top-to-bottom by rating. 

    For the second bar chart, the y-axis will be different building_numbers. The x-axis will be the weighted 
    average star_rating for the restaurants in each building. The average values should also be rounded to two 
    decimal places, and the y-axis should be sorted in descending order by rating. 

    """
    pass


def main():  # Try calling your functions here
    pass


class TestHW8(unittest.TestCase):
    def setUp(self):
        self.rest_dict = {
            'food_type': 'Cafe',
            'building_number': 1101,
            'star_rating': 3.8,
            'num_ratings': 543
        }
        self.low_rating_food_type = {
            'Bar': 3, 
            'Cookie Shop': 19, 
            'Asian Cuisine': 23, 
            'Cafe': 34, 
            'Pizzeria': 42, 
            'Juice Shop': 45, 
            'Korean Restaurant': 45, 
            'Mediterranean Restaurant': 45
        }
        self.w_avg_food_type = [
            ('Bubble Tea Shop', 4.82),
            ('Korean Restaurant', 4.5),
            ('Japanese Restaurant', 4.4),
            ('Mexican Restaurant', 4.22),
            ('Juice Shop', 4.2),
            ('Asian Cuisine', 4.15),
            ('Thai Restaurant', 4.1),
            ('Bar', 4.1),
            ('Mediterranean Restaurant', 4.0),
            ('Deli', 4.0),
            ('Cafe', 3.88),
            ('Sandwich Shop', 3.84),
            ('Cookie Shop', 3.8),
            ('Pizzeria', 3.67)
        ]
        self.w_avg_building_num = [
            (1220, 4.97),
            (1335, 4.8),
            (1327, 4.5),
            (1313, 4.5),
            (1205, 4.5),
            (1107, 4.4),
            (1321, 4.4),
            (1140, 4.16),
            (1300, 4.13),
            (1204, 4.1),
            (1208, 4.1),
            (1201, 4.0),
            (1235, 4.0),
            (1329, 4.0),
            (1207, 3.9),
            (1229, 3.8),
            (1101, 3.8),
            (1214, 3.66),
            (1315, 3.0)
        ]
        self.highest_weighted_ratings = {self.w_avg_food_type[0][0]: self.w_avg_food_type[0][1] , str(self.w_avg_building_num[0][0]): self.w_avg_building_num[0][1]}


    def test_load_restaurant_data(self):
        rest_data = restaurant_data_loader('restaurants_south_u.db')
        self.assertIsInstance(rest_data, dict)
        self.assertEqual(
            rest_data['M-36 Coffee Roasters Cafe'], self.rest_dict)
        self.assertEqual(len(rest_data), 25)
        self.assertEqual(
            rest_data['M-36 Coffee Roasters Cafe']['num_ratings'], 543)

    def test_plot_low_num_rating_by_type(self):
        low_rating_data = plot_low_num_rating_by_type(
            'restaurants_south_u.db')
        self.assertIsInstance(low_rating_data, dict)
        for key in low_rating_data:
            self.assertAlmostEqual(
                low_rating_data[key], self.low_rating_food_type[key], 1)
        self.assertEqual(len(low_rating_data), 8)
        self.assertEqual(low_rating_data['Bar'], 3)
        self.assertEqual(low_rating_data['Cafe'], 34)

    def test_find_restaurant_with_star(self):
        restaurant_list_3_8 = find_restaurant_with_star(
            3.8, 'restaurants_south_u.db')
        self.assertIsInstance(restaurant_list_3_8, list)
        self.assertEqual(len(restaurant_list_3_8), 2)
        self.assertEqual(restaurant_list_3_8[0], 'Insomnia Cookies')

        restaurant_list_4_1 = find_restaurant_with_star(
            4.1, 'restaurants_south_u.db')
        self.assertIsInstance(restaurant_list_4_1, list)
        self.assertEqual(len(restaurant_list_4_1), 4)
        self.assertEqual(restaurant_list_4_1[-1], 'Brown Jug')


    def test_get_highest_weighted_average_ratings(self):
        food_type_ratings = get_highest_weighted_average_ratings(
            'restaurants_south_u.db')
        self.assertEqual(food_type_ratings, self.highest_weighted_ratings)
        self.assertEqual(len(food_type_ratings), 2)
        self.assertIsInstance(food_type_ratings, dict)


if __name__ == '__main__':
    main()
    unittest.main(verbosity=2)
