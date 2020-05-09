# put your python code here
duration = int(input())
food_cost = int(input())
flight_cost = int(input())
hotel_cost = int(input())
print(flight_cost * 2 + food_cost * duration
      + hotel_cost * (duration - 1))