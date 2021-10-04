# import all necessary libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from appfolder.models import TransactionHistory, Users
from chatterbot.comparisons import SpacySimilarity

import spacy

# Create a new chat bot named LedgerBot

chatbot = ChatBot(
    # the bot's name
    name='LedgerBot',
    
    # SpacySimilarity and maximum_similarity_threshold helps the bot to understand similarities between the data it's seen and the new data close to them
    statement_comparison_function=SpacySimilarity,

    #sqlite default chatterbot db
    # database_uri='sqlite:///database.sqlite3'

    # mysql db on aws- connecting mysql sqlalchemy, -- engine://user:password@hostendpoint/db
    database_uri="mysql://user:password@hostendpoint/db",

    # The logic adapter helps the bot to fucntion smartly
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            'default_response': ['Would you like to record a transaction?', 'I don\'t understand'],
            'maximum_similarity_threshold': 0.65,
            
        }
    ]
)

# creating training data for the chatbot.
# Chatterbot expect list as training input with the above statement that of the user and the statement below the bot response

greetings = [
    'Hi',
    'Hello Welcome to LedgerBot, Would you like to record a transaction?',
    'Hey',
    'Hi, Would you like to record a transaction?',
    'Hello',
    'Hi Welcome to LedgerBot, Would you like to record a transaction?',
    'Hi LedgerBot',
    'Hello Welcome, Would you like to record a transaction?',
    'Hey Bot',
    'Hi, Would you like to record a transaction?',
    'LedgerBot',
    'Welcome, Would you like to record a transaction?'
]

trans_record = [
    'yes',
    'Income or Expense Transaction ?',
    'no',
    'Bye. Thank you',
    'bye',
    'Bye. Thank you',
    'I would like to record a transaction',
    'Income or Expense Transaction ?',
    'I want to save a transaction',
    'Income or Expense Transaction ?',
    'I want to save transaction',
    'Income or Expense Transaction ?',
    'i would like to record another transaction'
    'Income or Expense Transaction ?',
    'I want to save',
    'Income or Expense Transaction ?',
    'Record a transaction',
    'Income or Expense Transaction ?',
    'I want to record a transaction',
    'Income or Expense Transaction ?',
    'I want to record',
    'Income or Expense Transaction ?',
    'I want to record a sale',
    'Proceed Now',
    'I\'d like to record a sale',
    'Proceed Now',
    'I\'d like to record income transaction',
    'Proceed Now',
    'I\'d like to record expense transaction',
    'Proceed Now',
    'expense transaction',
    'Proceed Now',
    'income transaction',
    'Proceed Now',
    'expense',
    'Proceed Now',
    'income',
    'Proceed Now'

]

save_trans = [
    'I sold 10 litres of Kerosene for 10000 naira',
    'Transaction Saved. Thank you.',
    'I bought 5 bags of Onions for 15000 naira',
    'Transaction Saved. Thank you.',
    'I sold 15 bags of Onions for 50000 naira',
    'Transaction Saved. Thank you.',
    'I bought 2 cartons of noodles for 1700 naira',
    'Transaction Saved. Thank you.',
    'i sold 20 bags of rice for 20000 naira',
    'Transaction Saved. Thank you.',
    'we received 10 sacks of garri worth 15000 naira',
    'Transaction Saved. Thank you.',
    'We bought 7 sacks of cassava for 2300 naira',
    'Transaction Saved. Thank you.',
    'We sold 12 baskets of tomatoes for 7200 naira',
    'Transaction Saved. Thank you.',
    'The customer paid 7500 naira from last sales',
    'Transaction Saved. Thank you.',
    'I sold 2 plastics of beans for 3450 naira',
    'Transaction Saved. Thank you.',
    '75000 naira was paid by the vendor for distribution',
    'Transaction Saved. Thank you.',
    'Barbing 500 naira',
    'Transaction Saved. Thank you.',
    'Wire cable 1500 naira',
    'Transaction Saved. Thank you.',
    'glo 200 naira',
    'Transaction Saved. Thank you.',
    '12000 naira Rent fee',
    'Transaction Saved. Thank you.',
    'I gave Emeka 1200 naira',
    'Transaction Saved. Thank you.',
    'Esther borrowed 700 naira for change',
    'Transaction Saved. Thank you.',
    'I bought 2 yards of lace for 12500 naira',
    'Transaction Saved. Thank you.',
    'I sold 12 bundles of adire for 50000 naira',
    'Transaction Saved. Thank you.',
    'I paid 50000 naira for Rent',
    'Transaction Saved. Thank you.',
    'I paid 2000 naira to the delivery man',
    'Transaction Saved. Thank you.',

    '75000 naira was paid by the vendor for distribution',
    'Transaction Saved. Thank you.',
    'cable distributor 2500000 naira',
    'Transaction Saved. Thank you.',
    '3500 naira for internet Subscription',
    'Transaction Saved. Thank you.',
    'NEPA bill 4200 naira',
    'Transaction Saved. Thank you.',
    '1200 naira for PHCN bill',
    'Transaction Saved. Thank you.',
    'Ankara 3 yards 124000 naira',
    'Transaction Saved. Thank you.',
    '190000 naira for satin lace 3 yards',
    'Transaction Saved. Thank you.',
    'LG AX-023 Television for 350200 naira',
    'Transaction Saved. Thank you.',
    '50100 naira for pansaonic air conditioner',
    'Transaction Saved. Thank you.',
    '760100 naira for Scanfrost AC 2HP',
    'Transaction Saved. Thank you.',
    'i bought 2 1 Horse Power AC for 320010 naira',
    'Transaction Saved. Thank you.',
    'Apple watch series 2 for 99000 naira',
    'Transaction Saved. Thank you.',
    'i sold 2 Airpod pro for 179000 naira',
    'Transaction Saved. Thank you.',
    'Samsung Galaxy tab repairs for 32000 naira',
    'Transaction Saved. Thank you.',
    'Samsung s9 screen repairs for 62000 naira',
    'Transaction Saved. Thank you.',
    'I bought 3 Nokia touch pad 13000 naira',
    'Transaction Saved. Thank you.',
    'HP mouse sold for 7500 naira',
    'Transaction Saved. Thank you.',
    'I bought Dell mouse for 12000 naira',
    'Transaction Saved. Thank you.',
    'I sold 5 computer keyboard for 54000 naira',
    'Transaction Saved. Thank you.',
    'Cable distributor 55000 naira',
    'i paid phone accessories distributor 525000 naira',
    'Transaction Saved. Thank you.',
    'Huawei charger sold for 1200 naira',
    'Transaction Saved. Thank you.',
    'Lenovo laptop charger sold for 15000 naira',
    'Transaction Saved. Thank you.',
    'Panasonic Television X0Y2G bought for 130000 naira',
    'Transaction Saved. Thank you.',
    '4 Dell Projectors  190000 naira',
    'Transaction Saved. Thank you.',
    '3 Toshiba Projector screen for 20000 naira sold',
    'Transaction Saved. Thank you.',
    '4 yards of satin lace for 12000 naira sold',
    'Transaction Saved. Thank you.',
    '54 yards of Aso-Oke received for 1200000 naira',
    'Transaction Saved. Thank you.',
    '4 yards of Aso Oke sold at 3000 naira',
    'Transaction Saved. Thank you.',
    '3 Phillips pressing iron sold for 34050 naira',
    'Transaction Saved. Thank you.',
    '1 Phillips TV sold for 134050 naira',
    'Transaction Saved. Thank you.',
    'i sold 1 iron for 5000 naira',
    'Transaction Saved. Thank you.',
    '12 dozens of ergonomic chairs sold for 1304500 naira',
    'Transaction Saved. Thank you.',
    '1 dozen chairs sold for 45000 naira',
    'Transaction Saved. Thank you.',
    'centre table 54020 naira',
    'Transaction Saved. Thank you.',
    'Office chairs bought for 132070 naira',
    'Transaction Saved. Thank you.',
    '4 office cabinets sold for 1378295 naira',
    'Transaction Saved. Thank you.',
    '3 conference tables sold for 12054030 naira',
    'Transaction Saved. Thank you.',
    'iPhone 12 pro sold for 450000 naira',
    'Transaction Saved. Thank you.',
    'Tecno P90 bought for 123000 naira',
    'Transaction Saved. Thank you.',
    '4 units of Tecno P2 bought for 23000 naira',
    'Transaction Saved. Thank you.',
    'AC repair 8000 naira',
    'Transaction Saved. Thank you.',
    'Air Condition repair 8000 naira',
    'Transaction Saved. Thank you.',
    'I bought DELL Laptops for 1200000 naira',
    'Transaction Saved. Thank you.',
    'Electrician fee 18000 naira',
    'Transaction Saved. Thank you.',
    'I sold 2 rechargeable lamps for 32000 naira',
    'Transaction Saved. Thank you.',
    '4 inverter batteries sold for 340000 naira',
    'Transaction Saved. Thank you.',
    '1 inverter sold for 30000 naira',
    'Transaction Saved. Thank you.',
    'i sold 4 yards of atiku material for 14500 naira',
    'Transaction Saved. Thank you.',
    'we bought 3 senator materials for 75400 naira',
    'Transaction Saved. Thank you.',
    'i sold 7 T-shirt for 72000 naira',
    'Transaction Saved. Thank you.',
    'I bought 4 jeans for 35000 naira',
    'Transaction Saved. Thank you.',
    'amaka sold jeans for 12000 naira',
    'Transaction Saved. Thank you.',
    'I sold 2 rigalia for 12000 naira',
    'Transaction Saved. Thank you.',
    'Delivery man 1500 naira',
    'Transaction Saved. Thank you.',
    'Phone delivery 2000 naira',
    'Transaction Saved. Thank you.',
    'Material delivery 5000 naira',
    'Transaction Saved. Thank you.',
    'logistics 5200 naira',
    'Transaction Saved. Thank you.',
    'miscellaneous 12000 naira',
    'Transaction Saved. Thank you.',
    'phone repair 7300 naira',
    'Transaction Saved. Thank you.',
    'office chair repairs 12400 naira',
    'Transaction Saved. Thank you.',
    '2 GOTV Antenna sold 32790 naira',
    'Transaction Saved. Thank you.',
    'Transaction Saved. Thank you.',
    '4 DSTV dish sold for 56400 naira',
    'Transaction Saved. Thank you.',
    '12 DVD remote bought for 13000 naira',
    'Transaction Saved. Thank you.',
    '3 GOTV remote 19000 naira',
    'Transaction Saved. Thank you.',
    'Sharp B29 DVD sold for 32000 naira',
    'Transaction Saved. Thank you.',
    'we bought 7 Sony TVs for 1200000 naira',
    'Transaction Saved. Thank you.',
    'i bought 5 Panasonic Standing Fan for 134000 naira',
    'Transaction Saved. Thank you.',
    'i bought fan blades for 15000 naira',
    'Transaction Saved. Thank you.',
    'I paid the distributor 5000000 naira for the delivery',
    'Transaction Saved. Thank you.',
    'The fabrics distributor received 120000 naira',
    'Transaction Saved. Thank you.',
    'I sold CAT 6 cables for 750000 naira',
    'Transaction Saved. Thank you.',
    'I sold 30 yards of cable wire for 1200 naira',
    'Transaction Saved. Thank you.',
    'Emeka borrowed 10000 naira',
    'Transaction Saved. Thank you.',
    '100000 naira for children school fees',
    'Transaction Saved. Thank you.',
    '25000 naira for tithe',
    'Transaction Saved. Thank you.',
    '50000 naira bank savings',
    'Transaction Saved. Thank you.',
    'i saved 120000 naira at the bank yesterday',
    'Transaction Saved. Thank you.',
    'school fees 30000 naira',
    'Transaction Saved. Thank you.',
    'House rent 130000 naira',
    'Transaction Saved. Thank you.',
    'i sold LG Microwave oven for 45000 naira',
    'Transaction Saved. Thank you.',
    'i bought 1 Haier Thermocool Refridgerator 2 doors for 120000 naira',
    'Transaction Saved. Thank you.',
    'i sold NEXUS fridge 1 door for 20000 naira',
    'Transaction Saved. Thank you.',
    'i sold 1 scanfrost deep freezer for 130500 naira',
    'Transaction Saved. Thank you.',
    'I bought NEXUS gas cooker for 230000 naira',
    'Transaction Saved. Thank you.',
    'i sold binatone electric kettle for 12000 naira',
    'Transaction Saved. Thank you.',
    'i sold kenwood blender for 8300 naira',
    'Transaction Saved. Thank you.',
    'we bought binatone washing machine for 45000 naira',
    'Transaction Saved. Thank you.',
    'we bought Kenstar water dispenser for 32000 naira',
    'Transaction Saved. Thank you.',
    'i sold 1 unit of oraimo airpod for 12000 naira',
    'Transaction Saved. Thank you.',
    'i paid 30000000 naira for 10 Macbook pro 2020',
    'Transaction Saved. Thank you.',
    'i paid 30000000 naira for 10 Macbook air 2020',
    'Transaction Saved. Thank you.',
    'i purchased 1 Tee shirt for 2000 naira',
    'Transaction Saved. Thank you.',
    'I bought 3 G string pants for 5000 naira',
    'Transaction Saved. Thank you.',
    'I sold 2 Nike boxers short for 9800 naira',
    'Transaction Saved. Thank you.',
    'I sold 2 Air Jordan for 45000 naira',
    'Transaction Saved. Thank you.',
    'I purchased 12 sneakers for 40000 naira',
    'Transaction Saved. Thank you.',
    'I sold 2 PUMA rigalia for 12000 naira',
    'Transaction Saved. Thank you.',
    'Agribot sold 2 Adidas cap for 7000 naira',
    'Transaction Saved. Thank you.',

    'airtel 300 naira',
    'Transaction Saved. Thank you.',
    'i bought Glo 1000 naira',
    'Transaction Saved. Thank you.',
    '11000 naira for delivery',
    'Transaction Saved. Thank you.',
    'Toshiba Loudspeaker 3 169000 naira',
    'Transaction Saved. Thank you.',
    'Microsoft office package 3 56000 naira',
    'Transaction Saved. Thank you.',
    'Distributor fee 7500 naira',
    'Transaction Saved. Thank you.',
    '1TB Samsung Harddrive SSD 99000 naira',
    'Transaction Saved. Thank you.',
    '45000 naira 2 buckets',
    'Transaction Saved. Thank you.',

]
# Create a new trainer for the chatbot
list_trainer = ListTrainer(chatbot)
for item in (greetings, trans_record, save_trans):
    list_trainer.train(item)

from django.db import connection
from acctapp.models import Users

class Responses:

    def __init__(self, record=None, Trans_type=None):
        self.record = record
        self.Trans_type = Trans_type

# This method populates the database using the chatbot
    def populateDB_ChatBot(self, secretkey, record, Trans_type):

        # create empty variables to be filled later
        Item = ''
        Qty = ''
        Amount = None
        Trans_Statement = record
        Trans_type = Trans_type

        # query the db for user using their secret key
        user = Users.objects.get(secretkey=secretkey)
        user = user.userid

        # This dictionary variable ensures entities are tracked and saved however they are being represented
        # so basically either of the element in our interest could come first and the trackers does well to save the key and value pairs
        # appropriately
        interest_tracker = {}

        # interest hold entities from the NER model we want to save in the db
        # note that price came in from the ner model but saved as amount in the db
        interest = ['QUANTITY', 'ITEM', 'PRICE']

        # load our custom trained NER model called model6
        # nlp = spacy.load('./model6')
        nlp = spacy.load('./output/model-last')

        try:
            # the first step to using spacy models after loading them to create a doc of tokens
            doc = nlp(record)
            # using spacy's ner ents class we got the entity's text and lable_ from the doc created above
            entities = [(ent.text, ent.label_) for ent in doc.ents]

            # iterate through the entities
            for i in entities:
                # iterate through interest
                for j in interest:
                    # check if the returned entities from the doc contains our interest
                    if i[1] in interest:
                        # if yes, add it as key to the interest tracker dictionary against it's value i[0]
                        interest_tracker[i[1]] = (i[0])
                    # iterate through interest tracker if our interest is not in there give it an empty string
                    # so this line ensures all interest are taken care of even if they are not part of the return entities from doc.ents
                    if j not in interest_tracker:
                        interest_tracker[j] = ''

            # update the intial empty variables above
            Item = interest_tracker['ITEM']
            Amount = float(interest_tracker['PRICE'])
            Qty = interest_tracker['QUANTITY']

            cur = connection.cursor()
            cur.execute("CALL insert_trans (%s,%s,%s,%s,%s,%s);", (user, Trans_Statement, Item, Qty, Amount, Trans_type,))
            result = cur.fetchall()
            cur.close()
            return result[0][0]

        except user.DoesNotExist:
            return 'Invalid Secret Key'

    def get_bot_response(self, userText):

        #     userText = request.args.get('msg')
        
        while True:
            if userText in ['yes', 'Yes','YES']:
                userText = userText.lower()
                # chatbot response to user input or userText
                return str(chatbot.get_response(userText))

            elif userText in ['income', 'Income', 'INCOME','expense', 'Expense','EXPENSE']:

                # this line enables the chatbot to save the user's input if the bot response is "proceed now" and returns a boolean
                # print(chatbot.get_response(userText.lower()).serialize()[
                #     'text'] == 'Proceed Now')

                # user input saved to class variable (Trans_type) using the "in_response_to" property of the chatbot serialize method
                # "in_response_to" is the user input the bot gave the response "proceed now" to and can only be accessed via serialize method of the bot
                self.Trans_type = chatbot.get_response(
                    userText.lower()).serialize()['in_response_to']

            
                # chatbot response to user input or userText
                return str(chatbot.get_response(userText.lower()))

            # The bot response to the transaction statement being recorded
            # This line enables the chatbot to save the user's input if the bot response is "Transaction Saved. Thank you."           
            elif chatbot.get_response(userText.lower()).serialize()['text'] == 'Transaction Saved. Thank you.':
        
                # just like in Trans_type above, the user input is being saved to record variable
                self.record = chatbot.get_response(userText.lower()).serialize()[
                    'in_response_to']
                
                # chatbot response to user input or userText
                return str(chatbot.get_response(userText.lower()))
                

            # This last condition ensures the bot give response to user input or userText that is not bound by the "if" and "elif" constraints
            else:
                return str(chatbot.get_response(userText.lower()))
