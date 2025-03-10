from tkinter import Tk
from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:
    def __init__(self):

        #create db object
        self.dbo = Database()
        #CREATE API OBJECT
        self.apio = API()

        # Initialize the Tkinter root window
        self.root = Tk()

        self.root.title("NLP Application")
        #self.root.iconbitmap("resources/favicon.ico")
        self.root.geometry("350x600")
        self.root.configure(bg="#34495E")

        self.login_gui()

        # Start the Tkinter main loop to keep the window open
        self.root.mainloop()

    def login_gui(self):

        self.clear()
        #using label function we can add heading
        #it is considered a good practice to put the label func. in a variable
        heading = Label(self.root, text="NLPApp", bg="#34495E", fg="white")

        #to display ui we use grid or pack, here pack is used because it is intelligent enough to decide what too place where
        heading.pack(pady=(30, 30))

        #change font size
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text="Login", bg="#34495E", fg="white")
        heading2.pack()
        heading2.configure(font=("verdana", 23, "bold"))

        label1 = Label(self.root, text="Enter your email", width=20)
        label1.pack(pady=(20,20))

        #self is used before those variables which are going to used in other methods
        self.email_input = Entry(self.root, width=40)
        self.email_input.pack(pady=(5,10), ipady=3)


        label2 = Label(self.root, text="Enter your Password", width=20)
        label2.pack(pady=(20,20))

        #self is used before those variables which are going to used in other methods
        self.password_input = Entry(self.root, width=40, show="*")
        self.password_input.pack(pady=(5,10), ipady=3)

        login_btn = Button(self.root, text="Login", width=30, command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root, text="not a member?", width=20)
        label3.pack(pady=(10,10))

        redirect_btn = Button(self.root, text="Register Now", command=self.register_gui)
        redirect_btn.pack(pady=(10,10))

    def register_gui(self):
        #print("register function")

        #clear the existing gui
        #here pack_slaves are all the elements and destroy remove those elements
        #since the function can be reuse many times to make a sparate utility function for this
       # for i in self.root.pack_slaves():
           # print(i.destroy())
        self.clear()

        heading = Label(self.root, text="NLPApp", bg="#34495E", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text="Register", bg="#34495E", fg="white")
        heading2.pack()
        heading2.configure(font=("verdana", 23, "bold"))

        label1 = Label(self.root, text="Enter your name", width=20)
        label1.pack(pady=(20, 20))

        self.name_input = Entry(self.root, width=40)
        self.name_input.pack(pady=(5, 10), ipady=3)

        label1 = Label(self.root, text="Enter your email", width=20)
        label1.pack(pady=(20, 20))

        self.email_input = Entry(self.root, width=40)
        self.email_input.pack(pady=(5, 10), ipady=3)

        label2 = Label(self.root, text="Enter your Password", width=20)
        label2.pack(pady=(20, 20))

        # self is used before those variables which are going to used in other methods
        self.password_input = Entry(self.root, width=40, show="*")
        self.password_input.pack(pady=(5, 10), ipady=3)

        login_btn = Button(self.root, text="Register", width=30, command=self.perform_registration)
        login_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text="Already a member?", width=20)
        label3.pack(pady=(10, 10))

        redirect_btn = Button(self.root, text="Login Here", command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))


    def clear(self):
        for i in self.root.pack_slaves():
                i.destroy()

    def perform_registration(self):
        #fetch data from the gui
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        print(name, email, password)

        response = self.dbo.add_data(name, email, password)

        if response:
            messagebox.showinfo('success', "registration successful")
        else:
            messagebox.showinfo('Error', "Email already exists")

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email, password)

        if response:
            messagebox.showinfo('success', "Login successful")
            self.home_gui()
        else:
            messagebox.showinfo('Error', "Incorrect password or email")

    def home_gui(self):

        self.clear()

        heading = Label(self.root, text="NLPApp", bg="#34495E", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        sentiment_btn = Button(self.root, text="Sentiment Analysis", width=30, height=4,
        command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text="Named Entity Recoginition", width=30, height=4, command=self.ner_gui)
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text="Emotion Prediction", width=30, height=4, command=self.emotion_prediction_gui)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text="Logout", command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):

        self.clear()

        heading = Label(self.root, text="NLPApp", bg="#34495E", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text="Sentiment Analysis", bg="#34495E", fg="white")
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 24))

        label1 = Label(self.root, text="Enter the text", width=20)
        label1.pack(pady=(20, 20))

        self.sentiment_input = Entry(self.root, width=40)
        self.sentiment_input.pack(pady=(5, 10), ipady=7)

        sentiment_btn = Button(self.root, text="Analyze Sentiment",
        command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text="", width=20, bg="#34495E", fg="white", wraplength=300)
        self.sentiment_result.pack(pady=(20, 20))
        self.sentiment_result.configure(font=('verdana', 16))


        goback_btn = Button(self.root, text="go to home",
        command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        #print(text)
        result = self.apio.analyze_sentiment(text)

        txt = ''
        for i in result:
            txt = txt + i + ' -> ' + str(result[i]) + '\n'

        print(txt)
        self.sentiment_result['text'] = txt

        print(result)

    def ner_gui(self):

        self.clear()

        heading = Label(self.root, text="NLPApp", bg="#34495E", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text="Named Entity Recoginition", bg="#34495E", fg="white")
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 16))

        label1 = Label(self.root, text="Enter the text", width=20)
        label1.pack(pady=(20, 20))

        self.name_input = Entry(self.root, width=40)
        self.name_input.pack(pady=(5, 10), ipady=7)

        sentiment_btn = Button(self.root, text="Recognize entity",
        command=self.do_entity_recognition)
        sentiment_btn.pack(pady=(10, 10))

        self.entity_recognition_result = Label(self.root, text="", width=40, bg="#34495E", fg="white", wraplength=300)
        self.entity_recognition_result.pack(pady=(20, 20), ipady=9)
        self.entity_recognition_result.configure(font=('verdana', 10))


        goback_btn = Button(self.root, text="go to home",
        command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_entity_recognition(self):
        text = self.name_input.get()

        result = self.apio.name_entity_recognition(text)

        entities = [(ent.text, ent.label_) for ent in result.ents]

        print(entities)
        self.entity_recognition_result['text'] = str(entities)

    def emotion_prediction_gui(self):

        self.clear()

        heading = Label(self.root, text="NLPApp", bg="#34495E", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text="Emotion Prediction", bg="#34495E", fg="white")
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 24))

        label1 = Label(self.root, text="Enter the text", width=20)
        label1.pack(pady=(20, 20))

        self.emotion_input = Entry(self.root, width=40)
        self.emotion_input.pack(pady=(5, 10), ipady=7)

        emo_prediction_btn = Button(self.root, text="predict emotion",
        command=self.do_emotion_prediction)
        emo_prediction_btn.pack(pady=(10, 10))

        self.emo_prediction_result = Label(self.root, text="", width=50, bg="#34495E", fg="white", wraplength=300)
        self.emo_prediction_result.pack(pady=(20, 20))
        self.emo_prediction_result.configure(font=('verdana', 10))


        goback_btn = Button(self.root, text="go to home",
        command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_emotion_prediction(self):
        text = self.emotion_input.get()

        results = self.apio.emotion_prediction(text)

        filtered_results = [(emotion, score) for emotion, score in results if score > 0]
        print(filtered_results)

        self.emo_prediction_result['text'] = filtered_results

# Create an instance of NLPApp
nlp = NLPApp()


