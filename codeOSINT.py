import asyncio
import httpx
import os
import socket
import datetime
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)
R, G, Y, C, M, W = Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.WHITE

class CodeOSINT_Atomic:
    def __init__(self):
        self.version = "3.0.0-ATOMIC"
        self.auth_key = "root404"
        self.client = httpx.AsyncClient(http2=True, timeout=12)
        self.logs = []

    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def check_auth(self):
        self.clear_screen()
        print(f"{R}{'='*65}")
        print(f"{R}          SİSTEM KİLİTLİ - ROOT404 PROTOKOLÜ AKTİF")
        print(f"{R}{'='*65}{W}")
        passwd = input(f"\n{Y}[?] YETKİ ANAHTARI: {W}")
        if passwd != self.auth_key:
            print(f"{R}\n[!] HATALI ANAHTAR! ERİŞİM REDDEDİLDİ.{W}")
            sys.exit()
        else:
            print(f"{G}\n[+] ANAHTAR DOĞRULANDI. ÇEKİRDEK YÜKLENİYOR...{W}")
            time.sleep(1)

    def ui_engine(self):
        self.clear_screen()
        print(f"{M}{'='*65}")
        print(f"{M}   █▀▀ █▀█ █▀▄ █▀▀ █▀█ █▀▀ █ █▄░█ ▀█▀   ")
        print(f"{M}   █▄▄ █▄█ █▄▀ ██▄ █▄█ ▄▄█ █ █░▀█ ░█░   [ATOMIC-STRIKE]")
        print(f"{M}{'='*65}")
        print(f"{C}   KULLANICI: Root404 | MOD: TAARRUZ | RADAR: ÇEVRİMİÇİ{W}\n")

    async def log_print(self, level, msg):
        ts = datetime.datetime.now().strftime("%H:%M:%S")
        sym = {"+": G, "-": R, "!": Y, "*": C}.get(level, W)
        line = f"{W}[{ts}] {sym}[{level}] {W}{msg}"
        print(line)
        self.logs.append(line)

    async def target_profiler(self, user):
        await self.log_print("*", f"HEDEF PROFİLLENİYOR: {user}")
        targets = {
            "Instagram": "https://www.instagram.com/{}",
            "GitHub": "https://github.com/{}",
            "Twitter": "https://twitter.com/{}",
            "OnlyFans": "https://onlyfans.com/{}",
            "Venmo": "https://venmo.com/u/{}",
            "CashApp": "https://cash.app/{}",
            "Linktree": "https://linktr.ee/{}",
            "Chess.com": "https://www.chess.com/member/{}"
        }
        
        async def check(name, url):
            try:
                resp = await self.client.get(url.format(user))
                if resp.status_code == 200:
                    await self.log_print("+", f"SİNYAL YAKALANDI: {name} | {url.format(user)}")
            except: pass

        tasks = [check(n, u) for n, u in targets.items()]
        await asyncio.gather(*tasks)

    async def threat_intelligence(self, query):
        await self.log_print("!", f"TEHDİT İSTİHBARATI VE SIZINTI ANALİZİ: {query}")
        intel_nodes = [
            f"https://intelx.io/?s={query}",
            f"https://www.shodan.io/search?query={query}",
            f"https://leak-lookup.com/search?q={query}",
            f"https://search.censys.io/search?q={query}"
        ]
        for node in intel_nodes:
            print(f"{M} [!] İSTİHBARAT DÜĞÜMÜ: {W}{node}")

    async def forensic_metadata(self):
        await self.log_print("!", "ADLİ BİLİŞİM: GÖRSEL METADATA ANALİZİ")
        print(f"{Y}[*] Fotoğraflardan GPS ve Cihaz bilgisi çekmek için Termux'ta şunu kullan:{W}")
        print(f"{G}pkg install exiftool -y && exiftool hedef_foto.jpg{W}")

    async def cyber_recon(self, ip):
        await self.log_print("*", f"SİBER KEŞİF (RECON) BAŞLATILDI: {ip}")
        try:
            res = await self.client.get(f"http://ip-api.com/json/{ip}?fields=66846719")
            data = res.json()
            print(f"{C}--- LOKASYON VE AĞ VERİSİ ---{W}")
            for k, v in data.items():
                print(f"{G} [>] {k.upper()}: {W}{v}")
        except: await self.log_print("-", "AĞ TARAMASI ENGELLENDİ.")

    async def terminal(self):
        self.check_auth()
        while True:
            self.ui_engine()
            print(f"{C}01{W} - HEDEF PROFİLLEME (SOSYAL/FİNANS)")
            print(f"{C}02{W} - SİBER KEŞİF (IP/AĞ/ISP)")
            print(f"{C}03{W} - TEHDİT RADARI (SIZINTI/SHODAN)")
            print(f"{C}04{W} - ADLİ BİLİŞİM (METADATA/EXIF)")
            print(f"{C}05{W} - SİSTEMİ KAPAT")
            
            cmd = input(f"\n{M}Root404@AtomicStrike:~$ {W}")
            
            if cmd == "1" or cmd == "01":
                u = input(f"{Y}Kullanıcı Adı: {W}")
                await self.target_profiler(u)
            elif cmd == "2" or cmd == "02":
                i = input(f"{Y}IP/Host: {W}")
                await self.cyber_recon(i)
            elif cmd == "3" or cmd == "03":
                t = input(f"{Y}Hedef Veri: {W}")
                await self.threat_intelligence(t)
            elif cmd == "4" or cmd == "04":
                await self.forensic_metadata()
            elif cmd == "5" or cmd == "05":
                print(f"{R}[!] SİSTEMDEN ÇIKILIYOR... GÜVENLİĞİNİ KORU KANKA.{W}")
                break
            input(f"\n{Y}ANA MERKEZE DÖNMEK İÇİN ENTER...{W}")

if __name__ == "__main__":
    try:
        asyncio.run(CodeOSINT_Atomic().terminal())
    except KeyboardInterrupt:
        print(f"\n{R}[!] ACİL DURUM KAPATMASI YAPILDI.")

