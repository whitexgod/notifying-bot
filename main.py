import mechanize
import bs4
from twilio.rest import Client

account_sid = '*****************************'
auth_token = '******************************'
client = Client(account_sid, auth_token)

def send_marks():
    #Login_module

    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]

    sign_in = br.open("http://classroom.campusx.in/")  #the login url

    br.select_form(nr = 0) #accessing form by their index. Since we have only one form in this example, nr =0.
    #br.select_form(name = "form name") Alternatively you may use this instead of the above line if your form has name attribute available.

    br["email"] = "********************@gmail.com" #the key "username" is the variable that takes the username/email value

    br["password"] = "******"    #the key "password" is the variable that takes the password value

    logged_in = br.submit()   #submitting the login credentials

    src = logged_in.read()  #reading the page body that is redirected after successful login

    soup = bs4.BeautifulSoup(src, 'html.parser')

    dashboard = soup.find('div', class_='row')
    marks = dashboard.find('p', class_='mobile display-4')
    m=str(marks.text)

    message = client.messages.create(
            from_='whatsapp:+14155238886',
            body="Today's Final marks is "+m,
            to='whatsapp:+91700399****'
    )