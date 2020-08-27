from termcolor import colored,cprint
import json
import base64

def printLinuxLogo(): 
    LinuxLogo = """


                                 .--.
                                |o_o |
                                |:_/ |
                               //   \ \\
                              (|     | )
                             /'\_   _/`\\
                             \___)=(___/

    """
    print(colored(LinuxLogo, "yellow" ))

def printWindowsLogo(): 
    WinndowsLogo = """

                                                                   
                                                   */  
                                  /#################/  
                  ##############  ##################/  
                  ##############  ##################/  
                  ##############  ##################/  
                  ##############  ##################/  
                  ##############  ##################/  
                                                       
                  ##############  ##################/  
                  ##############  ##################/  
                  ##############  ##################/  
                  ##############  ##################/  
                  ,(############  ##################/  
                                    ./##############/
    """
    print(colored(WinndowsLogo, "blue" ))


def printProgramingLogo():          
    print("\n\n")           
    print(colored("                                     ((((((((((((((         ","blue"))   
    print(colored("                                     ((  /((((((((##        ","blue"))   
    print(colored("                                     (((((((((((####        ","blue"))   
    print(colored("                              ,(((((((((((((((######","blue")+colored(" ...... ","yellow")) 
    print(colored("                             ((((((((((((((#########","blue")+colored(" .......","yellow")) 
    print(colored("                            ,((((((((((((##########","blue")+colored(" ........","yellow")) 
    print(colored("                            *((((((((","blue")+colored("  .....................","yellow")) 
    print(colored("                             (((((((","blue")+colored(" .......................","yellow")) 
    print(colored("                              ((((##","blue")+colored(" ...................... ","yellow")) 
    print(colored("                                     .......                ","yellow"))  
    print(colored("                                     ........... ...        ","yellow"))  
    print(colored("                                     ...........  ..        ","yellow"))  
    print(colored("                                         ......             ","yellow")) 


def printHeader(title):
    print(colored("\n----------------------", "green" ) +  colored("   "+ title +"   ", "red" ) + colored("----------------------\n", "green" ) )


def printTool(tool):
    print(colored(tool.upper(),"yellow",attrs=['bold','underline']) + ":\n")

def printUsefullComands(OS,ip,port):
    print(colored("\n----------------------", "cyan" ) +  colored("   Useful Command   ", "magenta" ) + colored("----------------------\n", "cyan" ) )
    with open('data/Usefull.json') as json_file: 
        data = json.load(json_file)
        data = data[OS]
        for tips in data:
            print(colored(tips,"green",attrs=['bold','underline']) + " :\n")
            for cmd in data[tips]:
                cmd = cmd.replace("<IP>",str(ip)).replace("<PORT>",str(port))
                print(cmd)
            print("\n")

def printCommands(data,ip,port,command,b64=False):
    if command:
        printTool(command)
        cpt=0
        for reverse in data[command]:
            payload = reverse['reverse'].replace("<IP>",str(ip)).replace("<PORT>",str(port))
            if "description" in reverse:
                    print(colored(reverse['description'].replace("<IP>",str(ip)).replace("<PORT>",str(port)) + " :\n",'cyan',attrs=['bold']))
            if command == "powershell" and b64:
                print(payload)
                payload = "powershell -NoP -NonI -W Hidden -Exec Bypass -e " +  base64.b64encode(payload.encode('utf16')[2:]).decode() + "\n"
            if cpt % 2 == 0:
                print(colored(payload))
            else : 
                print(colored(payload,attrs=['dark']))
            cpt =cpt+1
        print("\n")
    else :
        for i in data:
            printTool(i)
            cpt=0
            for reverse in data[i]:
                payload = reverse['reverse'].replace("<IP>",str(ip)).replace("<PORT>",str(port))
                if "description" in reverse:
                    print(colored(reverse['description'].replace("<IP>",str(ip)).replace("<PORT>",str(port)) + " :\n",'magenta'))
                if i == "powershell" and b64:

                    payload = "powershell -NoP -NonI -W Hidden -Exec Bypass -e " +  base64.b64encode(payload.encode('utf16')[2:]).decode() + "\n"

                if cpt % 2 == 0:
                    print(colored(payload))
                else : 
                    print(colored(payload,attrs=['dark']))
                cpt =cpt+1
            print("\n")
