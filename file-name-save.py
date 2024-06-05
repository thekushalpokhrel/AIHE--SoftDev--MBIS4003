def generate_paragraph(name, age, favorite_color, favorite_food, hometown, hobby, pet_name, dream_destination, favorite_book, secret_skill, favorite_movie, music_genre, lucky_number, childhood_dream, superpower, favorite_season, nickname, favorite_quote, role_model):
    paragraph = f"Once upon a time, there was a person named {name}.\nAt the age of {age}, they embarked on a journey filled with adventures and mysteries.\nTheir favorite color, {favorite_color}, reflected their vibrant personality and their love for all things colorful.\nWhen it came to food, {name} couldn't resist indulging in {favorite_food}, which always brought a smile to their face.\nHailing from the enchanting town of {hometown}, {name} was known far and wide for their kindness and generosity.\nIn their free time, {name} enjoyed {hobby}, which provided them with moments of joy and relaxation.\nAccompanying them on their adventures was their beloved pet, {pet_name}, who was always by their side, offering companionship and unwavering loyalty.\nDespite having explored many places, {name} still harbored a dream of visiting {dream_destination}, a land of wonders and breathtaking beauty.\n{name}'s favorite book, {favorite_book}, inspired them with its timeless wisdom and captivating storytelling.\nLittle did others know, {name} possessed a secret skill in {secret_skill}, which they honed in the quiet moments of solitude.\n{name} was also an avid fan of {favorite_movie} movies and enjoyed listening to {music_genre} music.\nTheir lucky number was {lucky_number}, and their childhood dream was to become a {childhood_dream}.\nIf {name} could have any superpower, it would be {superpower}, allowing them to make a difference in the world.\n{name}'s favorite season was {favorite_season}, and their friends affectionately called them {nickname}.\nA favorite quote that resonated with {name} was '{favorite_quote}', reminding them to always strive for greatness.\n{name} looked up to {role_model} as a source of inspiration and guidance.\nWith each passing day, {name} continued to write their own story, filled with laughter, friendship, and countless unforgettable moments."

    # Print the paragraph
    print(paragraph)

    # Save the paragraph to a .txt file
    file_name = f"{name}_story.txt"
    with open(file_name, "w") as file:
        file.write(paragraph)
    print(f"The paragraph has been saved to {file_name}")

def validate_age(age):
    try:
        age = int(age)
        if age <= 0:
            print("Age must be a positive integer.")
            return False
        return True
    except ValueError:
        print("Age must be a valid integer.")
        return False

def validate_number(num):
    try:
        num = int(num)
        if num <= 0:
            print("Number must be a positive integer.")
            return False
        return True
    except ValueError:
        print("Number must be a valid integer.")
        return False

# Get inputs from the user with validation
name = input("Enter your name: ")
age = input("Enter your age: ")
while not validate_age(age):
    age = input("Enter your age: ")

favorite_color = input("Enter your favorite color: ")
favorite_food = input("Enter your favorite food: ")
hometown = input("Enter your hometown: ")
hobby = input("Enter your favorite hobby: ")
pet_name = input("Enter your pet's name: ")
dream_destination = input("Enter your dream travel destination: ")
favorite_book = input("Enter your favorite book: ")
secret_skill = input("Enter your secret skill: ")
favorite_movie = input("Enter your favorite movie: ")
music_genre = input("Enter your favorite music genre: ")
lucky_number = input("Enter your lucky number: ")
while not validate_number(lucky_number):
    lucky_number = input("Enter your lucky number: ")

childhood_dream = input("Enter your childhood dream: ")
superpower = input("If you could have any superpower, what would it be? ")
favorite_season = input("Enter your favorite season: ")
nickname = input("Enter your nickname: ")
favorite_quote = input("Enter your favorite quote: ")
role_model = input("Who is your role model? ")

# Generate the paragraph and save it to a .txt file
generate_paragraph(name, age, favorite_color, favorite_food, hometown, hobby, pet_name, dream_destination, favorite_book, secret_skill, favorite_movie, music_genre, lucky_number, childhood_dream, superpower, favorite_season, nickname, favorite_quote, role_model)
