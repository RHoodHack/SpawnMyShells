#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import netifaces
import json
from termcolor import colored,cprint
from display import *

def getInterfaceIp(interface):
    if interface in netifaces.interfaces():
        return netifaces.ifaddresses(interface)[2][0]['addr']
    return False


def allReverse():
    exit()

def ReverseWindows(ip,port,command=False,b64=False,quiet=False):
    with open('data/Windows.json') as json_file: 

        data = json.load(json_file)
        if command and command.lower() not in data:
            return 0
        if not quiet:
            printWindowsLogo()
            printUsefullComands("Windows",ip,port)
        printHeader("Windows Reverse Shell")
        printCommands(data,ip,port,command,b64)
        

def ReverseLinux(ip,port,command=None,quiet=False):
    with open('data/LinuxCommands.json') as json_file:

        data = json.load(json_file)
        if command and command.lower() not in data:
            return 0
        if not quiet:
            printLinuxLogo()
            printUsefullComands("Linux",ip,port)
        printHeader("Linux Reverse Shell")
        printCommands(data,ip,port,command)



def ReverseLanguages(ip,port,command=None,quiet=False):
    with open('data/LinuxProgramingLanguages.json') as json_file: 
        data = json.load(json_file)
        if command and command.lower() not in data:
            return 0
        if not quiet:
            printProgramingLogo()
        printHeader("Linux Programing Languages Reverse Shell")
        printCommands(data,ip,port,command)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Fast reverse Shell Generator')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-i','--ip', dest='ip', action='store',help='Ip to connect')
    group.add_argument('-I','--interface', dest='interface', action='store',help='select interface to connect')
    parser.add_argument('-p','--port' , dest='port', action='store',help='select port to connect',required=True)
    parser.add_argument('-L', help='generate Linux Payload',action="store_true")
    parser.add_argument('-W', help='generate Windows Payload',action="store_true")
    parser.add_argument('--b64' , help="generate base64 encoded Windows payload",action="store_true")
    parser.add_argument('-t','--tool', dest='tool', action='store',help='specify a tool')
    parser.add_argument('-q','--quiet',help="don't display logo and useful commands",action="store_true")
    args = parser.parse_args()

    if args.interface:
        args.ip = getInterfaceIp(args.interface)
        if args.L:
            ReverseLinux(args.ip,args.port,args.tool,args.quiet)
            ReverseLanguages(args.ip,args.port,args.tool,args.quiet)
        if args.W:
            ReverseWindows(args.ip,args.port,args.tool,args.b64,args.quiet)
        if not args.L and not args.W:
            ReverseLinux(args.ip,args.port,args.tool,args.quiet)
            ReverseLanguages(args.ip,args.port,args.tool,args.quiet)
            ReverseWindows(args.ip,args.port,args.tool,args.b64,args.quiet)