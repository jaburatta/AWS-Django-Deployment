# import necessary libraries
import spacy
import joblib
# import speech_recognition as sr

from django.db import connection
from appfolder.models import TransactionHistory, Users
from django.db.models import Sum


class NlpAS:

    def __init__(self, secretkey=None):
        self.secretkey = secretkey

    def populateDB_SR(self, record):

        # using speech recognition, transaction record hits the classification model first, which predicts transaction type ('Trans_type)
        classifier = joblib.load(open('svcmodel.pkl', 'rb'))

        Trans_Statement = record
        Trans_type = classifier.predict([record])[0]
        
        # query the db for user using their secret key
        user = Users.objects.get(secretkey=self.secretkey)
        user = user.userid
           
        # create empty variables to be filled later
        Item = ''
        Qty = ''
        Amount = None
        
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
                        # if yes, add it as key to the interest tracker dictionary against it's valuei[0]
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
        

    def Trans_History(self):

        try:

            user = Users.objects.get(secretkey=self.secretkey)
            # history filtered by secretkey ordered by datetime in desc
            history = TransactionHistory.objects.all().filter(
                userid=user).order_by('-trans_date')
            if history != None:
                return history
        except user.DoesNotExist:
            return 'Invalid Secret Key'

    def delete_trans(self, Trans_id):

        # connection = mysql.connector.connect(host=self.host,
        #                                      user=self.user,
        #                                      passwd=self.password,
        #                                      db=self.db)
        try:
            cur = connection.cursor()
            cur.execute(
                "DELETE FROM transaction_history WHERE Trans_id = %s", (Trans_id,))
            connection.commit()

            cur.close()
            connection.close()
        except Exception as e:
            return 'Delete transaction accepts integer values'

    def hist_by_date(self, start_date, end_date):

        try:
            user = Users.objects.get(secretkey=self.secretkey)
            hist_date = TransactionHistory.objects.filter(
                trans_date__range=[start_date, end_date], userid=user).order_by('-trans_date')

            if hist_date != None:
                return hist_date
        except user.DoesNotExist:
            return 'Invalid Secret Key'

        

    def income(self):

        try:
            user = Users.objects.get(secretkey=self.secretkey)
            income = TransactionHistory.objects.filter(
                trans_type='income', userid=user)

            if income != None:
                return income
        except user.DoesNotExist:
            return 'Invalid Secret Key'

    def expense(self):

        try:
            user = Users.objects.get(secretkey=self.secretkey)
            expense = TransactionHistory.objects.filter(
                trans_type='expense', userid=user)

            if expense != None:
                return expense
        except user.DoesNotExist:
            return 'Invalid Secret Key'

    def expense_sum(self):

        try:
            user = Users.objects.get(secretkey=self.secretkey)
            expense = TransactionHistory.objects.filter(
                trans_type='expense', userid=user).aggregate(Sum('amount'))
            if expense['amount__sum'] != None:
                return expense['amount__sum']
            return 0
        except user.DoesNotExist:
            return 'Invalid Secret Key'

    def income_sum(self):

        try:
            user = Users.objects.get(secretkey=self.secretkey)
            income = TransactionHistory.objects.filter(
                trans_type='income', userid=user).aggregate(Sum('amount'))
            if income['amount__sum'] != None:
                return income['amount__sum']
            return 0
        except user.DoesNotExist:
            return 'Invalid Secret Key'

    def business_value(self):

        try:
            user = Users.objects.get(secretkey=self.secretkey)

            income = TransactionHistory.objects.filter(
                trans_type='income', userid=user).aggregate(Sum('amount'))

            expense = TransactionHistory.objects.filter(
                trans_type='expense', userid=user).aggregate(Sum('amount'))

            if income['amount__sum'] != None:
                income = income['amount__sum']
            else:
                income = 0

            if expense['amount__sum'] != None:
                expense = expense['amount__sum']
            else:
                expense = 0

            value = float(income - expense)

            return value

        except user.DoesNotExist:
            return 'Invalid Secret Key'


    def record(self):
        # Initialize recognizer class (for recognizing the speech)

        r = sr.Recognizer()

        # Reading Microphone as source
        # listening the speech and store in audio_text variable

        with sr.Microphone() as source:
            print("Record a new transaction...", '\n')
            audio_text = r.listen(source)
            print("Time over, thanks", '\n')
        try:
            # using google speech recognition
            result = r.recognize_google(audio_text)
            print(result, '\n')
            self.populateDB_SR(result)
        except Exception as e:
            print(e)
            return 'Record again'
