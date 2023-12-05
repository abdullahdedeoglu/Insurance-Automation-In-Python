#Abdullah Dedeoglu 20010011046

import os

staff_info=[]
company=[]
co_info=[]
def add():
    os.system('cls')
    temp_staff=[]
    co_name=input("Sirketin ismini giriniz: ")     #Sirket ismi bosluksuz girilecek
    co_id=int(input("Sirketin id'sini giriniz: "))
    price=int(input("Sirketin hizmet icin odedigi ucreti giriniz: "))
    s_num=int(input("Kac tane personel eklemek istiyorsunuz: "))
    co_info.append([co_name, co_id, s_num, price])
    for i in range(s_num):
        s_id=int(input("{}. Personelin id numarasini giriniz: ".format(i+1)))    #Personel ismi bosluksuz girilecek
        s_name=input("{}. Personelin adi: ".format(i+1))
        s_year=int(input("{}. Personelin sirkette calisma yili: ".format(i+1)))
        s_salary=int(input("{}. Personelin aldigi maas ne kadar: ".format(i+1)))
        temp_staff.insert(co_id, [s_id, s_name, s_year, s_salary])
        
    ttemp_staff=temp_staff.copy()
    company.append(ttemp_staff)
    temp_staff.clear()
    with open("20010011046(1).txt", "w") as co:
        for i in range(len(co_info)):
            co.write(co_info[i][0]+"\t"+str(co_info[i][1])+"\t"+str(co_info[i][2])+"\t"+str(co_info[i][3])+"\n")
    with open("20010011046(2).txt", "w") as staff:
        for i in range(len(co_info)):
            a=int(co_info[i][2])
            for j in range(a):
                staff.writelines([str(company[i][j][0])+" "+company[i][j][1]+" "+str(company[i][j][2])+" "+str(company[i][j][3])+"\n"])
            


def colist():
    os.system('cls')
    for i in range(len(co_info)):
        print("{}. Sirketin: \nAdi: {} Id: {} Odedigi Hizmet Bedeli: {} Personel Sayisi: {} ".format(i+1, co_info[i][0], co_info[i][1], co_info[i][3], co_info[i][2]))
        a=int(co_info[i][2])
        for j in range(a):
            print("{} Sirketinin {}. Personelinin: \nId: {} Ad: {} {} Yildir Calisiyor Maasi: {}".format(co_info[i][0], j+1, company[i][j][0], company[i][j][1], company[i][j][2], company[i][j][3]))

def update():
    os.system('cls')
    search=int(input("Guncellemek istediginiz personelin id'sini giriniz: "))
    for i in range(len(co_info)):
        a=int(co_info[i][2])
        for j in range(a):
            if search==int(company[i][j][0]):
                choose2=int(input("Personelin calistigi yili guncellemek icin 1'i, maasini guncellemek icin 2'yi giriniz: "))
                if choose2==1:
                    r=int(input("Guncellenen yili giriniz: "))
                    company[i][j][2]=r
                elif choose2==2:
                    t=int(input("Personelin yeni maasini giriniz: "))
                    company[i][j][3]=t
                with open("20010011046(2).txt", "w") as staff:
                    for i in range(len(co_info)):
                        a=int(co_info[i][2])
                        for j in range(a):
                            staff.writelines([str(company[i][j][0])+" "+company[i][j][1]+" "+str(company[i][j][2])+" "+str(company[i][j][3])+"\n"])

def delet(pprim):
    os.system('cls')
    choose3=int(input("Sirketi silmek icin 1'i personel silmek icin 2'yi giriniz: "))
    if choose3==1:
        h=int(input("Silmek istediginiz sirketin id'sini giriniz: "))
        for i in range(len(co_info)):
            if h==int(co_info[i][1]):                
                del company[i]                  
                del co_info[i]
                del pprim[i] 
                break
    if choose3==2:
        n=int(input("Silmek istediginiz personelin id'sini giriniz: "))
        for i in range(len(co_info)):
            a=int(co_info[i][2])
            for j in range(a):
                if n==int(company[i][j][0]):
                    del company[i][j]
                    del pprim[i][j]
                    co_info[i][2]=a-1
                    c=i
                    break
        if co_info[c][2]==0:
            del co_info[c]
            del company[c]
            del pprim[c]
    with open("20010011046(1).txt", "w") as co:
        for i in range(len(co_info)):
            co.write(co_info[i][0]+"\t"+str(co_info[i][1])+"\t"+str(co_info[i][2])+"\t"+str(co_info[i][3])+"\n")
    with open("20010011046(2).txt", "w") as staff:
        for i in range(len(co_info)):
            a=int(co_info[i][2])
            for j in range(a):
                staff.writelines([str(company[i][j][0])+" "+company[i][j][1]+" "+str(company[i][j][2])+" "+str(company[i][j][3])+"\n"])
    with open ("20010011046(3).txt", "w") as prim:
        for i in range(len(co_info)):
            a=int(co_info[i][2])
            for j in range(a):
                prim.write(co_info[i][0]+" "+str(pprim[i][j][1]))
    

def searchh():
    os.system('cls')
    s=int(input("Aradiginiz sirketin id'sini giriniz: "))
    for i in range(len(co_info)):
        if s==int(co_info[i][1]):
            print("{}. Sirketin: \nAdi: {} Id: {} Odedigi Hizmet Bedeli: {} Personel Sayisi: {} ".format(i+1, co_info[i][0], co_info[i][1], co_info[i][3], co_info[i][2]))
            a=int(co_info[i][2])
            for j in range(a):
                print("{} Sirketinin {}. Personelinin: \nId: {} Ad: {} {} Yildir Calisiyor Maasi: {}".format(co_info[i][0], j+1, company[i][j][0], company[i][j][1], company[i][j][2], company[i][j][3]))

def primm(tempprim, pprim, temprim):
    os.system('cls')
    pprim.clear()
    for i in range(len(co_info)):
        a=int(co_info[i][2])
        for j in range(a):
            if int(company[i][j][2]) < 7:
                temprim.insert(int(co_info[i][1]), [co_info[i][1], int(int(company[i][j][3]) / 10)])
            elif int(company[i][j][2]) < 14:
                temprim.insert(int(co_info[i][1]),[co_info[i][1],int(int(company[i][j][3]) / 5)])
            else:
                temprim.insert(int(co_info[i][1]), [co_info[i][1], int(3*(int(company[i][j][3]) / 10))])
        tempprim=temprim.copy()
        pprim.append(tempprim)
        temprim.clear()
    for i in range(len(co_info)):
        a=int(co_info[i][2])
        for j in range(a):
            print("{} sirketinin {} isimli personeli {} tl prim almaktadır".format(co_info[i][0], company[i][j][1], pprim[i][j][1])) 
                

    with open ("20010011046(3).txt", "w") as prim:
        for i in range(len(co_info)):
            a=int(co_info[i][2])
            for j in range(a):
                prim.writelines([str(co_info[i][1])+" "+str(pprim[i][j][1])+"\n"])

def ciroo(pprim, ciro):
    os.system('cls')
    tciro=0   
    nett2=0
    for i in range(len(co_info)):
        ciro[co_info[i][1]] = int(co_info[i][3])
        tciro += int(co_info[i][3])
    print("Sirketin cirosu: {}".format(tciro))
    def nett(tciro, nett2):
        tprim=0
        for i in range(len(co_info)):
            a=int(co_info[i][2])
            for j in range(a):
                tprim+=int(pprim[i][j][1])
        nett2=int(tciro-tprim)
        print("Sirketin net kazanci: {}".format(nett2))
    nett(tciro, nett2)

            


def main():
    ciro={}
    tempprim=[]
    temprim=[]
    pprim=[]
    temp=[]
    ttemp=[]
    toplam=0
    temptoplam=0
    with open ("20010011046(1).txt", "r") as co:
        for i in co:
            a=i.strip()
            b=a.split()
            co_info.append(b)
    with open ("20010011046(2).txt", "r") as staff:
        for i in range(len(co_info)):
            staff.seek(0)
            b=0
            temptoplam=toplam
            toplam+=int(co_info[i][2])
            for j in staff:               
                if toplam>b and temptoplam<=b:    
                    x=j.strip()
                    y=x.split()
                    temp.append(y)
                b+=1               
                if(b==toplam):
                    ttemp=temp.copy()
                    company.append(ttemp)
                    temp.clear()
    with open ("20010011046(3).txt", "r") as prim:
        for i in range(len(co_info)):
            prim.seek(0)
            b=0
            temptoplam=toplam
            toplam+=int(co_info[i][2])
            for j in prim:               
                if toplam>b and temptoplam<=b:    
                    x=j.strip()
                    y=x.split()
                    temp.append(y)
                b+=1               
                if(b==toplam):
                    ttemp=temp.copy()
                    pprim.append(ttemp)
                    temp.clear()
                
    
    while True:
        os.system('cls')
        choose=int(input("1.Ekleme\n2.Listeleme\n3.Guncelleme\n4.Prim Gosterme\n5.Arama\n6.Net ve Ciro Gosterme\n7.Silme\n8.Cikis\nYapmak istediginiz islemi seciniz: "))

        if choose==1:
            add()
            x=int(input("Ana menuye donmek icin 1'i programdan cikmak icin herhangi bir tusu giriniz: "))
            if x==1:
                continue
            else:
                break   
        elif choose==2:
            colist()
            x=int(input("Ana menuye donmek icin 1'i programdan cikmak icin herhangi bir tusu giriniz: "))
            if x==1:
                continue
            else:
                break           
        elif choose==3:
            update()
            x=int(input("Ana menuye donmek icin 1'i programdan cikmak icin herhangi bir tusu giriniz: "))
            if x==1:
                continue
            else:
                break
        elif choose==4:
            primm(tempprim, pprim, temprim)
            x=int(input("Ana menuye donmek icin 1'i programdan cikmak icin herhangi bir tusu giriniz: "))
            if x==1:
                continue
            else:
                break
        elif choose==5:
            searchh()
            x=int(input("Ana menuye donmek icin 1'i programdan cikmak icin herhangi bir tusu giriniz: "))
            if x==1:
                continue
            else:
                break
        elif choose==6:
            ciroo(pprim, ciro)
            x=int(input("Ana menuye donmek icin 1'i programdan cikmak icin herhangi bir tusu giriniz: "))
            if x==1:
                continue
            else:
                break
        elif choose==7:
            delet(pprim)
            x=int(input("Ana menuye donmek icin 1'i programdan cikmak icin herhangi bir tusu giriniz: "))
            if x==1:
                continue
            else:
                break
        elif choose==8:
            break
        
main()

    

