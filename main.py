import pyautogui as pag
from getpass import getpass
import sys
import json
import requests
import keyboard
import time
import random
import webbrowser
from os import system, name
from colorama import Fore, Back, Style
import os

os.system('cls')

def clear():
    if name == 'nt':
        _ = system('cls')

def sendsnap():
    print(Style.BRIGHT + Fore.LIGHTRED_EX +
          'Kaç döngü kullanmak istersiniz? (döngü başına 1200 puan): ')
    print(Fore.CYAN + '\n\n\n\n\nSnapify> ', end='')
    amount = float(input(Fore.WHITE + ''))
    clear()
    while True:
        print(Style.BRIGHT + Fore.LIGHTRED_EX +
              'Mikrofonunuzun sesini kapatmak ister misiniz?(Not: bu programı yavaşlatır)(yes/no) ')
        print(Fore.CYAN + '\n\n\n\n\nSnapify> ', end='')
        mute = input(Fore.WHITE + '').lower()
        clear()
        if mute == 'yes':
            break
        elif mute == 'no':
            break
        else:
            getpass(Style.BRIGHT + Fore.LIGHTRED_EX +
                    'Hata. Geçersiz bir seçenek eklediniz. Lütfen tekrar deneyin.')
            clear()
            continue
    print(Style.BRIGHT + Fore.LIGHTRED_EX +
          ":: Chat Button' ::")
    if keyboard.read_key() == "enter":
        ChatButton = pag.position()
        print(f"Yakalanan An: {ChatButton}")
    time.sleep(1)
    print(Style.BRIGHT + Fore.LIGHTRED_EX +
          ":: Fareniz 'Kamera Düğmesi' üzerindeyken enter'a tıklayın ::")
    if keyboard.read_key() == "enter":
        CameraButton = pag.position()
        print(f"Yakalanan An: {CameraButton}")
    time.sleep(1)
    if mute == 'yes':
        print(":: 3 saniyelik bir video çekin ve fareniz 'Sessiz Düğmesi' üzerine geldiğinde enter'a tıklayın ::")
        if keyboard.read_key() == "enter":
            MuteButton = pag.position()
            print(f"Yakalanan An: {MuteButton}")
        time.sleep(1)
        print(":: 'Sessiz Düğmesine' tıklayın, ardından fareniz 'Gönder Düğmesinin üzerine geldiğinde enter'a tıklayın' ::")
        if keyboard.read_key() == "enter":
            SendToButton = pag.position()
            print(f"Yakalanan An: {SendToButton}")
        time.sleep(1)
    elif mute == 'no':
        print(":: Bir resim çekin ve fareniz 'Gönder Düğmesinin üzerine geldiğinde enter'a tıklayın.' ::")
        if keyboard.read_key() == "enter":
            SendToButton = pag.position()
            print(f"Yakalanan An: {SendToButton}")
        time.sleep(1)
    print("::'Gönder Düğmesine' tıklayın, ardından fareniz 'Son Yapış Düğmesi'nin üzerine geldiğinde enter'a tıklayın' ::")
    if keyboard.read_key() == "enter":
        LastSnapButton = pag.position()
        print(f"Yakalanan An: {LastSnapButton}")
    time.sleep(1)
    print(":: Fareniz 'Çabuk Gönder Oku'nun üzerindeyken enter'a tıklayın.' ::")
    if keyboard.read_key() == "enter":
        SendSnapArrow = pag.position()
        print(f"Yakalanan An: {SendSnapArrow}")
    time.sleep(1)
    print(":: Fareniz alt ortadaki 'Kamera Logosu'nun üzerindeyken enter'a tıklayın' ::")
    if keyboard.read_key() == "enter":
        CameraLogo = pag.position()
        print(f"Yakalanan An: {CameraLogo}")
    # countdown screen
    TimeToHomePage = 2
    while TimeToHomePage >= 0:
        clear()
        print(
            f'Var {TimeToHomePage} Takviye başlamadan önce snapchat ana ekranına geri dönmek için saniyeler.')
        time.sleep(1)
        TimeToHomePage -= 1
    clear()
    print(
        f"Artırmaya başladı! Lütfen çalışırken telefonunuzu kapatmayın veya bu pencereyi kapatmayın. Bunun için koşacak {amount} Döngü('s)")
    print('\n\n\n\n\n\n')
    while amount > 0:
        # move to camera button and record for one minute
        pag.moveTo(ChatButton[0], ChatButton[1], 1.5)
        time.sleep(0.5)
        pag.click()
    
        pag.moveTo(CameraButton[0], CameraButton[1], 1.5)
        pag.mouseDown()
        pag.mouseUp()

        # if mute click yes
        if mute == 'yes':
            pag.moveTo(MuteButton[0], MuteButton[1], 1.5)
            time.sleep(0.5)
            pag.click()

        # move to send to button and click
        pag.moveTo(SendToButton[0], SendToButton[1], 1.5)
        time.sleep(0.5)
        pag.click()

        # move to last snap and click
        pag.moveTo(LastSnapButton[0], LastSnapButton[1], 1.5)
        time.sleep(0.5)
        pag.click()

        # move to send snap button and click
        pag.moveTo(SendToButton[0], SendToButton[1], 1.5)
        time.sleep(0.5)
        pag.click()

        # move to send snap arrow and click
        pag.moveTo(SendSnapArrow[0], SendSnapArrow[1], 1.5)
        time.sleep(0.5)
        pag.click()

        # move to camera logo and click
        pag.moveTo(CameraLogo[0], CameraLogo[1], 1.5)
        time.sleep(0.5)
        pag.click()

        amount -= 1
        print(f'Bir döngü tamamlandı. {amount} gitmek için çıktı')
    clear()
    print(Fore.GREEN + 'Puan Kasma İşlemi Başarılı Şekilde Sona Ermiştir..')
    print(Fore.MAGENTA + '\n\n Sosyal Medya Hesaplarımızı Takip Ediniz: @b3zkurt', end='')
    getpass(Fore.WHITE + '')
    sys.exit()

while True:
    print(
        'Mod Seçiniz:\n\n 1) Snap Puan Kasma\n\n')
    print(Fore.CYAN + 'Snapify> ', end='')
    option = input(Fore.WHITE + '')
    if option == '1':
        while True:
            clear()
            print(Style.BRIGHT + Fore.LIGHTRED_EX +
                  "Bu türü nasıl kullanacağınızı biliyorsanız, 'no' yazmazsanız 'yes'\n\n")
            print(Fore.CYAN + 'Snapify> ', end='')
            watchvid = input(Fore.WHITE + '').lower()
            if watchvid == 'yes':
                clear()
                sendsnap()
            elif watchvid == 'no':
                clear()
                sendsnap()
            else:
                getpass(Style.BRIGHT + Fore.LIGHTRED_EX +
                        'Hata. Geçersiz bir seçenek eklediniz. Lütfen tekrar deneyin.')
                clear()
                continue
