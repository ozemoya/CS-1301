import random

Quote = ["Nah I'd win", "Stand Proud", "You're Strong"]


random.shuffle(Quote)

for quote in range(50):
    quote = random.choice(Quote)
    print(quote)