import random
import json
import torch
from ReplyBot.model import NeuralNet
from ReplyBot.nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as f:
    intents = json.load(f)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# #this is where we start using the model respond to our input
# bot_name = "armaan"
# print("Let's chat! type 'quit' to exit")
# while True:
#     sentence = input('You: ')
#     if sentence == "quit":
#         break
#     #tokenize sentence and collect bag of words
#     sentence = tokenize(sentence)
#     x = bag_of_words(sentence, all_words)
#     x = x.reshape(1, x.shape[0])
#     x = torch.from_numpy(x)
#
#     output = model(x)
#     _, predicted = torch.max(output, dim=1)
#     tag = tags[predicted.item()]
#
#     probs = torch.softmax(output, dim=1)
#     prob = probs[0][predicted.item()]
#
#     if prob.item() > 0.75:
#         for intent in intents["intents"]:
#             if tag == intent["tag"]:
#                 print(f"{bot_name}: {random.choice(intent['responses'])}")
#     else:
#         print(f"{bot_name}: I do not understand")

def twitter_reply(tweet_text):
    bot_name = "armaan"
    # tokenize sentence and collect bag of words
    sentence = tokenize(tweet_text)
    x = bag_of_words(sentence, all_words)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x)

    output = model(x)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75: #prob of right intent category, lower for less accuracy
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                return f"{random.choice(intent['responses'])}" # change from print to tweet
    else:
        response = ["A crisis is an opportunity riding the dangerous wind",
                    "It's better to be without a book than to believe a book entirely.",
                    "A little impatience will spoil great plans.",
                    "If you bow at all, bow low.",
                    "A journey of a thousand miles begins with a single step.",
                    "A smile will gain you ten more years of life.",
                    "A bird does not sing because it has an answer. It sings because it has a song.",
                    "A book holds a house of gold.",
                    "Talk does not cook rice.",
                    "A man who cannot tolerate small misfortunes can never accomplish great things.",
                    "Experience is a comb which nature gives us when we are bald.",
                    "Be not afraid of growing slowly, be afraid only of standing still.",
                    "Behave toward everyone as if receiving a guest.",
                    "A fall into a ditch makes you wiser.",
                    "Better a diamond with a flaw than a pebble without one.",
                    "He who asks is a fool for five minutes, but he who does not ask remains a fool forever.",
                    "An inch of time is an inch of gold but you can't buy that inch of time with an inch of gold.",
                    "A closed mind is like a closed book; just a block of wood",
                    "Better to light a candle than to curse the darkness.",
                    "A needle is not sharp at both ends.",
                    "Even a hare will bite when it is cornered.",
                    "Habits are cobwebs at first; cables at last.",
                    "The best time to plant a tree was 20 years ago. The second best time is today.",
                    "In a group of many words, there is bound to be a mistake somewhere in them.",
                    "Govern a family as you would cook a small fish - very gently.",
                    "Patience is a bitter plant, but its fruit is sweet.",
                    "Listening well is as powerful as talking well, and is also as essential to true conversation.",
                    "Two good talkers are not worth one good listener.",
                    "A hundred no's are less agonizing than one insincere yes.",
                    "He who cheats the earth will be cheated by the earth.",
                    "Only one who can swallow an insult is a man.",
                    "One beam, no matter how big, cannot support an entire house on its own.",
                    "Better the cottage where one is merry than the palace where one weeps.",
                    "Distant water does not put out a nearby fire.",
                    "The more acquaintances you have, the less you know them."]
        return f"{random.choice(response)}" # change from print to tweet
