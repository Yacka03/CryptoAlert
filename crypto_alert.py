import requests;
import time;
import json;


from playsound import playsound



#SETTINGS:
fetch_interval = 1; # How many seconds to wait for price update
path_sound_file = "crypto_sound.wav"; # Sound which will be played


def converter_type(type):
    if (type == "1"):
        return "LAST TRADE";
    if (type == "2"):
        return "HIGHEST BUY";
    if (type == "3"):
        return "LOWEST SELL";
    return "";

def pre_check():
    global isOnTop;
    while True:
        price = get_price(moneys[b-1]);
        if (price['status'] is True):
            prices = price['data'];
            numSelected = int(a);
            if (float(prices[numSelected-1]) > c):
                isOnTop = False
            else:
                isOnTop = True;
            
            break;
         
        else:
            print("Cannot fetch current "+moneys[b-1] +" prices.. Trying again.");
            time.sleep(1);  

def get_price(type):
    r = requests.get("https://tradeogre.com/api/v1/ticker/"+type);

    if (r.status_code == 200):
        resp = json.loads(r.text);

        res = resp['success'];

        if (res):
            return {'status': True, 'data': (resp['price'], resp['bid'], resp['ask'])};
    return {'status': False}




moneys = ["USDT-KAS", "BTC-KAS", "USDT-BTC"];

b = None;
print ("Choose coin type");

while True:

    print ("1 - Kaspa - USDT");
    print ("2 - Kaspa - BTC");
    print ("3 - USDT - BTC");
    b = input();
    try:
        b = int(b)
    except ValueError:
        print ("Type in correct number")
        continue;
    if (b <= 0 or b > len(moneys)):
        print ("Type in correct number")
        continue;
    break
            

print("Select type of price for alert");
print("1 - Last trade");
print ("2 - Highest Buy")
print ("3 - Lowest Sell");

a = None;
while True:
    a = input();
    if (a == "1" or a == "2" or a == "3"):
        break;




print ("Type price for triggering");


c = None;



while True:
    c = input();
    try:
        c = float(c);
        break;
    except ValueError:
        print ("Type price in decimal format with comma example. 1.54");


    
pre_check();





terminated = False;

#TO-DO:
# Add GUI for live Kaspa price

print("Program started working!")


while (terminated is not True):
    price = get_price(moneys[b-1]);
    play_alert = False;
    if (price['status'] is True):
        


        
        prices = price['data'];
        
        numSelected = int(a);
        if ( (isOnTop and float(prices[numSelected-1]) >= c) or (isOnTop is False and float(prices[numSelected-1]) <= c) ):
            play_alert = True
        
        if (play_alert):
            print ("Yeahh! " + moneys[b-1] +" " + converter_type(a) + " reached target price of " + str(c) + " Currently: " + prices[numSelected-1])
            playsound(path_sound_file);
        else:
            print (moneys[b-1]+ " " + converter_type(a) + " Current price: " + prices[numSelected-1] + " Target price: " + str(c));
    
            
        
    

    time.sleep(fetch_interval)
    


    
        
