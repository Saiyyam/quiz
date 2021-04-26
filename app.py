from pywebio.input import *
from pywebio.output import *
from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
import os

app=Flask(__name__)

def exam():

    c=0
    style(put_text("Welcome to Saiyyam's Quiz"),"text-align:center")
    
    name=input("Enter your name to start the exam",type="text")

    q1=radio("Which of the following devices is a volatile storage?",["Hard disk","RAM","Floppy Disk","Magnetic Tape"])
    if q1=="RAM":
        c+=1

    q2=radio("The structure of the Indian Constitution is:",["Federal in form and unitary in spirit","Unitary","Unitary in form and federal in spirit","Pure federal"])
    if q2=="Federal in form and unitary in spirit":
        c+=1

    q3=radio("Which is the largest state in India in terms of area?",["Rajasthan","Uttar Pradesh","Madhya Pradesh","Maharashtra"])
    if q3=="Rajasthan":
        c+=1

    q4=radio("who among the following is known as Mother of Indian Revolutionaries?",["Usha Mehta","Annie Besant","Madam Cama","Sarojini Naidu"])
    if q4=="Madam Cama":
        c+=1

    q5=radio("What does price flooring mean?",["Shortage","Surpluses","Equilibrium","None of the above"])
    if q5=="Surpluses":
        c+=1

    q6=radio("Which of these body systems causes allergic reactions?",["Lymph","Immune","Nervous","Circulatory"])
    if q6=="Immune":
        c+=1

    q7=radio("Under the Indian Constitution, the residuary powers are vested in the ________",["Judiciary","Executive","Parliament","State legislatures"])
    if q7=="Parliament":
        c+=1

    q8=radio("Who wrote Kadambari?",["Charak","Banabhatta","Chanakya","Radhagupt"])
    if q8=="Banabhatta":
        c+=1

    q9=radio("Mount Merapi, was observed to have released ash and debris, is an active volcano in which country?",["Philippines","Australia","Indonesia","Japan"])
    if q9=="Indonesia":
        c+=1

    q10=radio("In which continent scientists have found particles of rare isotope of Iron(Fe-60)?",["Africa","Europe","Australia","Antartica"])
    if q10=="Antartica":
        c+=1

    style(put_text("Correct Answers are:"),"color:Green")

    style(put_text("1. RAM"),"color:SandyBrown")
    style(put_text("2. Federal in form and unitary in spirit"),"color:SandyBrown")
    style(put_text("3. Rajasthan"),"color:SandyBrown")
    style(put_text("4. Madam Cama"),"color:SandyBrown")
    style(put_text("5. Surpluses"),"color:SandyBrown")
    style(put_text("6. Immune"),"color:SandyBrown")
    style(put_text("7. Parliament"),"color:SandyBrown")
    style(put_text("8. Banabhatta"),"color:SandyBrown")
    style(put_text("9. Indonesia"),"color:SandyBrown")
    style(put_text("10. Antartica\n\n\n"),"color:SandyBrown")

    if c>=5:
        style(put_text(name +", your score is: "+ str(c)),"color:MediumBlue")
        style(put_text("Result : Passed"),"color:Turquoise")

    else:
        style(put_text(name +", your score is: "+ str(c)),"color:Maroon")
        style(put_text("Result : failed"),"color:red")

    style(put_text("Thank you for your participation.."),"font-family:Cursive,sans-serif")

app.add_url_rule('/','webio_view',webio_view(exam),methods=['GET','POST','OPTIONS'])

if __name__=="__main__":
    port=os.environ.get('PORT',33507)
    app.run(host='localhost',port=port,debug=False)





