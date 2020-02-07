import webbrowser
import random
import tkinter as tk

request = ''
ans = ''

def there_exists(terms):
    for term in terms:
        if term in request:
            return True

def submit(win, q):
    global request
    request = q
    win.destroy()
    main()

def window():
    win = tk.Tk()
    win.geometry('350x350+10+10')

    inp = tk.Entry(win, width=50)
    btn = tk.Button(win, text='Enter', width=50, command=lambda:submit(win, inp.get()))
    query = tk.Label(win, text=request, width=600)
    answer = tk.Message(win, text=ans, width=600)

    inp.pack(side='top')
    btn.pack(side='top')
    query.pack(side='top')
    answer.pack(side='top')

    win.mainloop()

def main():
    #request = input("Enter your query:")
    global ans

    # 1: greeting
    if there_exists(['hey','hi','hello']):
        greetings = ["hey, how can I help you" , "hey, what's up?" , "I'm listening" , "how can I help you?" , "hello" ]
        greet = greetings[random.randint(0,len(greetings)-1)]
        ans = (greet)
        #(voice_data) # respond
    
    #2: ques1
    if there_exists(["what is child helpline number in chennai?"]):
        greetings = ["Child helpline number is 1098" , "1098" , "1098 is the child helpline number"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        ans = (greet)
    
    #3: ques2
    if there_exists(["what is women's helpline number in chennai?"]):
        greetings = ["Women helpline number is 1091","1091","1091 is womens helpline number"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        ans = (greet)
    
    #4: ques3
    if there_exists(["do the police do a good job in your country?"]):
        greetings = ["yes","of course","obviously every policemen is trying their level best"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        ans = (greet)
    
    #5 ques4
    if there_exists(["how do stores prevent shoplifting?"]):
        greetings = ["Watching for loiterers","Expanding their team","Installing an entrance alert sensor"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        ans = (greet)
    
    #6 ques5
    if there_exists(["what is the punishment for drunk driving?"]):
        greetings = ["Rs 10,000","6 months prison","Rs. 10,000 and 6 months prison"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        ans = (greet)

    #7 ques6
    if there_exists(["what is penalty for travelling without a license?"]):
        greetings = ["Penalty for travelling without ticket has been increased from up to Rs 200 to Rs 500","Penalty is Rs 500","Individuals driving without licence will be fined from up to Rs 500 to Rs 5,000"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        ans = (greet)

    #8 ques7
    if there_exists(["how to report an accident?"]):
        greetings = ["calling police","by messaging respective department"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        ans = (greet)

    #9 ques8
    if there_exists(["what are the emergency numbers?"]):
        greetings = ["100,1098,1091,102,101"]
        #greet = greetings[random.randint(0,len(greetings)-1)]
        ans = (greet)    
    
    #10 ques9
    if there_exists(["senior citizens helpline number?"]):
        greetings = ["1253 is the Senior Citizen Helpline Number","1253","Senior Citizen Helpline Number is 1253"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        ans = (greet)    
    
    #11 ques10
    if there_exists(["do crime programmes influence crime related risk perception of audience?"]):
        greetings = ["yes","definitely","obviously"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        ans = (greet)    

    #12 ques11
    elif there_exists(["search for"]):
        search_term = request.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        ans = ("taking you to the required page")

    #13 ques12
    elif there_exists(["report a complaint"]):
        search_term = request.split("for")[-1]
        url = "https://digitalpolice.gov.in/ncr/login.aspx"
        webbrowser.get().open(url)
        ans = ("taking you to the required page")

    #14 ques13
    elif there_exists(["report a women complaint","report a child complaint"]):
        #search_term = request.split("for")[-1]
        url = "https://cybercrime.gov.in/Webform/Crime_AuthoLogin.aspx?rnt=1"
        webbrowser.get().open(url) 
        ans = ("taking you to the required page")

    #15 ques14
    elif there_exists(["report a complaint anonymously"]):
        #search_term = request.split("for")[-1]
        url = "https://cybercrime.gov.in/Webform/Crime_ReportAnonymously.aspx"
        webbrowser.get().open(url)
        ans = ("taking you to the required page")      

    #16 ques15
    elif there_exists(["report a missing person report"]):
        #search_term = request.split("for")[-1]
        url = "https://www.myham.in/?i=1"
        webbrowser.get().open(url)
        ans = ("taking you to the required page")

    #17  ques16
    elif there_exists(["crime statistics for"]):
        #search_term = request.split("for")[-1]

        x = request.split('for')[1]
        y = x.split(',')
        city = y[0].strip()
        state = y[1].strip()
        
        url = "http://www.neighbourhoodinfo.co.in/crime/"+city+"/"+state
        webbrowser.get().open(url)
        ans = ("taking you to the required page")

    window()

window()