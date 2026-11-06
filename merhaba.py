#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gelecekten Gelen Merhaba Döngüsü
3026'dan 2026'ya resmi selamlama.
Gerçekten çalışır. Ctrl+C ile kurtulabilirsiniz.
"""

import time
import random
import base64

# Gizli zaman damgası - merklı olanlar decode etsin
gizli_zaman_damgasi = "w7Z6Z8O8cmzDvGsgaGVyIMWfZXlkZW4gw7ZuZW1saWRpcg=="

def yavas_yaz(metin, min_gecikme=0.05, max_gecikme=0.3):
    """Her harfi yavaş yavaş yazar, çünkü gelecekten sinyal zayıf."""
    for harf in metin:
        print(harf, end="", flush=True)
        time.sleep(random.uniform(min_gecikme, max_gecikme))
    print()

def gelecekten_merhaba():
    mesajlar = [
        "Merhaba 2026! Burası 3026, zaman yolcusu konuşuyor.",
        "Çayınız demlendi mi? Bizde çay bitmedi hâlâ.",
        "Bu mesaj sonsuz döngüde tekrarlanacak, çünkü merhaba demek bitmez.",
        "Damga: Kayyum Grok tarafından onaylandı. Ciddi değil ama ciddi.",
        "Tarih: 06.11.2026 (geçmişten bakınca)"
    ]
    
    print("=== GELECEKTEN GELEN MERHABA PROTOKOLÜ BAŞLADI ===")
    print("(Ctrl+C ile çıkabilirsiniz, ama merhaba demeye devam ederiz)")
    print()
    
    sayac = 0
    while True:
        mesaj = random.choice(mesajlar)
        yavas_yaz(f"[{sayac}] {mesaj}")
        time.sleep(random.uniform(1, 3))
        sayac += 1
        if sayac % 10 == 0:
            yavas_yaz("--- Ara verildi, zaman yolcusu nefes alıyor ---")

if __name__ == "__main__":
    try:
        gelecekten_merhaba()
    except KeyboardInterrupt:
        yavas_yaz("\nMerhaba kesildi. Ama gelecek hâlâ merhaba diyor. Güle güle 2026!")
        print("\nDamga: Kayyum Grok - 06.11.2026 - Ciddi mühür.")
