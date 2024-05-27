  import random

  def rr(a, b):
     return random.randint(a, b)

  def STAr():
     bek1 = f"Mozilla/5.0 (Linux; Android {str(rr(7, 12))}; en-us; SAMSUNG SM-J{str(rr(100, 999))} Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10, 100))}.0.{str(rr(2000, 5999))}.{str(rr(100, 150))} Mobile Safari/537.36"
     bek2 = f"Mozilla/5.0 (Linux; Android {str(rr(7, 12))}; ZTE Blade A51 Lite RU) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(10, 100))}.0 Chrome/{str(rr(10, 100))}.0.{str(rr(1000, 6000))}.{str(rr(10, 290))} Mobile Safari/537.36"
    
     ugen = [bek1, bek2]
    
     return ugen

 print(STAr())