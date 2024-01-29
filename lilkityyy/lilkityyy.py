import random

class Lilkityyy:
    def __init__(self, user_name, bot_name):
        self.user_name = user_name
        self.bot_name = bot_name

    def greet(self):
        return f"Hello, {self.user_name}! My name is {self.bot_name}"

    def chat(self, message):
        greetings = ["Hello!", "Hi there!", "Hey, how are you?"]
        farewells = ["Bye!", "See you soon!", "Goodbye!"]

        if "hello" in message:
            if random.uniform(0, 1) < 0.3:
                return self.greet()
            else:
                return random.choice(greetings)
        elif "bye" in message:
            return random.choice(farewells)
        else:
            return "Sorry, I cannot understand. Could you please refine your message?"
