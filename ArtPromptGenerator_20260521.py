import random

mood_list = ["Anger", "Bored", "Creepy", "Disgust", "Dreamy", "Embarrassed",
             "Excited", "Fear", "Funny", "Happy", "Nostalgia", "Sad", "Surprise", "Surreal", "Uncertain"]
color_list = [["Red", "Orange", "Yellow",
              "Green", "Blue", "Purple", "White", "Black"],
              ["Cool", "Monochrome", "Neutral", "Pastel", "Vibrant", "Warm"]]
genre_list = [["Fall", "Spring", "Summer", "Winter"],
              ["Funeral", "Halloween", "Holiday",
                  "Revolution", "Thanksgiving", "Wedding"],
              ["Ancient", "Classical", "Jurassic",
                  "Medieval", "Modern", "Myth", "Renaissance"],
              ["Action", "Adventure", "Anime", "Crime", "Cyberpunk", "Fantasy", "History", "Horror", "Isekai", "Mystery",
               "Romance", "Sci-fi", "Thriller"]]
location_list = [["East", "North", "South", "West"],
                 ["Cloud", "Rain", "Snow", "Sun", "Storm"],
                 ["America", "Arctic", "Atlantis", "California", "Canada", "Earth",
                     "Greece", "Hong Kong", "Japan", "Mars", "Moon", "Space"],
                 ["Apartment", "Beach", "Bridge", "Castle", "Circus", "City", "Crypt", "Desert", "Downtown", "Forest", "Garden", "Graveyard",
                  "Hole", "Home", "Kitchen", "Maze", "Mountain", "Ocean", "Outhouse", "Outpost", "Park", "Passage", "Rainforest", "River",
                  "Road", "Ruins", "School", "Skyscraper", "Street", "Theater", "Tomb", "Tower", "Trail"]]
subject_list = [["Bear", "Bee", "Bird", "Bug", "Butterfly", "Cat", "Chicken", "Clam", "Cryptid", "Deer", "Dodo", "Dog", "Dragon", "Duck", "Elephant",
                 "Fish", "Fly", "Fox", "Frog", "Goat", "Giraffe", "Hamster", "Lion", "Lizard", "Mouse", "Ostrich", "Panda", "Penguin",
                 "Pest", "Rabbit", "Shark", "Shrimp", "Snail", "Spider", "Unicorn", "Walrus", "Whale", "Wolf", "Worm"],
                ["Actor", "Artist", "Astronaut", "Baker", "Builder", "Chef", "Choir", "Clown", "Cook", "Dancer", "Demon", "Doctor", "Executioner",
                 "Firefighter", "General", "Hero", "Hunter", "Idol", "Jester", "Jock", "King", "Knight", "Mechanic",
                 "Nerd", "Nun", "Pilot", "Pirate", "Prince", "Princess", "Queen", "Robot", "Sailor", "Scientist", "Spy", "Taxi",
                 "Teacher", "Twins", "Uber", "Villain"],
                ["Fairy", "Giant", "Gnome", "Spirit", "Troll", "Vampire", "Werewolf", "Witch", "Zombie"]]
object_list = [["Bag", "Balloon", "Book", "Cage", "Candle", "Cannon", "Clock", "Chimney", "Cobweb", "Coin", "Cold",
                "Computer", "Cup", "Dice", "Doll", "Door", "Fire", "Flashlight", "Flower", "Fork", "Game", "Garbage",
                "Glass", "Globe", "Hot", "Ink", "Instrument", "Key", "Knife", "Marble", "Mask", "Melt", "Moss", "Music", "Numbers",
                "Map", "Movie", "Origami", "Paper", "Paste", "Phone", "Ring", "Rocket", "Scarecrow", "Slime", "Spoon", "Star",
                "Stone", "Sword", "Teapot", "Telephone", "Test", "Throne", "Time", "Torch", "Tornado", "Trap", "Tree",
                "Umbrella", "Vase", "Watch", "Water", "Wheel", "Wood"],
               ["Airplane", "Bicycle", "Bike", "Boat", "Carriage", "Motorcycle", "Plane", "Rollercoaster",
                   "Spaceship", "Submarine", "Taxi", "Truck"],
               ["Apple", "Banana", "Breakfast", "Brunch", "Butter", "Cabbage", "Cake", "Candy", "Cupcake", "Dessert", "Dinner", "Egg", "Feast", "Fruit",
                   "Grape", "Hot Dog", "Lunch", "Orange", "Peach", "Pear", "Pie", "Plum", "Soup", "Watermelon"],
               ["Arm", "Ear", "Eye", "Finger", "Foot", "Hand",
                   "Hair", "Heart", "Nose", "Skull", "Tooth"],
               ["One", "Two", "Three", "Four", "Five", "Ten", "Twelve", "Hundred"]]
action_list = ["Climb", "Cry", "Cut", "Dance", "Fall", "Float", "Hear", "Hide", "Jump", "Run",
               "See", "Slay", "Smell", "Swim", "Talk", "Taste", "Touch", "Watch"]

mood = random.choice(mood_list)
color = random.choice(random.choice(color_list))
genre = random.choice(random.choice(genre_list))
location = random.choice(random.choice(location_list))
subject = random.choice(random.choice(subject_list))
object = random.choice(random.choice(object_list))
action = random.choice(action_list)

prompt_1_list = [mood, color, genre]
prompt_2_list = [location, subject, object, action]
prompt_1 = random.sample(prompt_1_list, 2)
prompt_2 = random.sample(prompt_2_list, 2)

print(f"""
      Here are your Art Prompts:
      - {prompt_1[0]}
      - {prompt_1[1]}
      - {prompt_2[0]}
      - {prompt_2[1]}
      """)
