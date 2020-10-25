import os
from selenium import webdriver
import xlwt

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")
sheet1.write(1, 0, "SUBS==>")
sheet1.write(2, 0, "CREDITS==>")
sheet1.write(3, 0, "ROLLNO.")
sheet1.write(3, 1, "NAME")

#subject codeS & CREDITS
sub1 = input('Enter subject code name: ')
sheet1.write(1, 2, sub1)
cre1=input('Enter subject code credit: ')
sheet1.write(2, 2, cre1)
sub2 = input('Enter subject code name: ')
sheet1.write(1, 3, sub2)
cre2=input('Enter subject code credit: ')
sheet1.write(2, 3, cre2)
sub3 = input('Enter subject code name: ')
sheet1.write(1, 4, sub3)
cre3=input('Enter subject code credit: ')
sheet1.write(2, 4, cre3)
sub4 = input('Enter subject code name: ')
sheet1.write(1, 5, sub4)
cre4=input('Enter subject code credit: ')
sheet1.write(2, 5, cre4)
sub5 = input('Enter subject code name: ')
sheet1.write(1, 6, sub5)
cre5=input('Enter subject code credit: ')
sheet1.write(2, 6, cre5)
sub6 = input('Enter subject code name: ')
sheet1.write(1, 7, sub6)
cre6=input('Enter subject code credit: ')
sheet1.write(2, 7, cre6)
sub7 = input('Enter subject code name: ')
sheet1.write(1, 8, sub7)
cre7=input('Enter subject code credit: ')
sheet1.write(2, 8, cre7)
sub8 = input('Enter subject code name: ')
sheet1.write(1, 9, sub8)
cre8=input('Enter subject code credit: ')
sheet1.write(2, 9, cre8)
sub9 = input('Enter subject code name: ')
sheet1.write(1, 10, sub9)
cre9=input('Enter subject code credit: ')
sheet1.write(2, 10, cre9)
sub10 = input('Enter subject code name: ')
sheet1.write(1, 11, sub10)
cre10=input('Enter subject code credit: ')
sheet1.write(2, 11, cre10)
sub11 = input('Enter subject code name: ')
sheet1.write(1, 12, sub11)
cre11=input('Enter subject code credit: ')
sheet1.write(2, 12, cre11)
sub12 = input('Enter subject code name: ')
sheet1.write(1, 13, sub12)
cre12=input('Enter subject code credit: ')
sheet1.write(2, 13, cre12)
sub13 = input('Enter subject code name: ')
sheet1.write(1, 14, sub13)
cre13=input('Enter subject code credit: ')
sheet1.write(2, 14, cre13)
sub14 = input('Enter subject code name: ')
sheet1.write(1, 15, sub14)
cre14=input('Enter subject code credit: ')
sheet1.write(2, 15, cre14)
sub15 = input('Enter subject code name: ')
sheet1.write(1, 16, sub15)
cre15=input('Enter subject code credit: ')
sheet1.write(2, 16, cre15)
sub16 = input('Enter subject code name: ')
sheet1.write(1, 17, sub16)
cre16=input('Enter subject code credit: ')
sheet1.write(2, 17, cre16)
sub17 = input('Enter subject code name: ')
sheet1.write(1, 18, sub17)
cre17=input('Enter subject code credit: ')
sheet1.write(2, 18, cre17)
sub18 = input('Enter subject code name: ')
sheet1.write(1, 19, sub18)
cre18=input('Enter subject code credit: ')
sheet1.write(2, 19, cre18)
sub19 = input('Enter subject code name: ')
sheet1.write(1, 20, sub19)
cre19=input('Enter subject code credit: ')
sheet1.write(2, 20, cre19)
sub20 = input('Enter subject code name: ')
sheet1.write(1, 21, sub20)
cre20=input('Enter subject code credit: ')
sheet1.write(2, 21, cre20)
sub21 = input('Enter subject code name: ')
sheet1.write(1, 22, sub21)
cre21=input('Enter subject code credit: ')
sheet1.write(2, 22, cre21)
sub22 = input('Enter subject code name: ')
sheet1.write(1, 23, sub22)
cre22=input('Enter subject code credit: ')
sheet1.write(2, 23, cre22)
sub23 = input('Enter subject code name: ')
sheet1.write(1, 24, sub23)
cre23=input('Enter subject code credit: ')
sheet1.write(2, 24, cre23)
sub24 = input('Enter subject code name: ')
sheet1.write(1, 25, sub24)
cre24=input('Enter subject code credit: ')
sheet1.write(2, 25, cre24)
sub25 = input('Enter subject code name: ')
sheet1.write(1, 26, sub25)
cre25=input('Enter subject code credit: ')
sheet1.write(2, 26, cre25)
sub26 = input('Enter subject code name: ')
sheet1.write(1, 27, sub26)
cre26=input('Enter subject code credit: ')
sheet1.write(2, 27, cre26)
sub27 = input('Enter subject code name: ')
sheet1.write(1, 28, sub27)
cre27=input('Enter subject code credit: ')
sheet1.write(2, 28, cre27)
sub28 = input('Enter subject code name: ')
sheet1.write(1, 29, sub28)
cre28=input('Enter subject code credit: ')
sheet1.write(2, 29, cre28)
sub29 = input('Enter subject code name: ')
sheet1.write(1, 30, sub29)
cre29=input('Enter subject code credit: ')
sheet1.write(2, 30, cre29)
sub30 = input('Enter subject code name: ')
sheet1.write(1, 31, sub30)
cre30=input('Enter subject code credit: ')
sheet1.write(2, 31, cre30)
sub31 = input('Enter subject code name: ')
sheet1.write(1, 32, sub31)
cre31=input('Enter subject code credit: ')
sheet1.write(2, 32, cre31)
sub32 = input('Enter subject code name: ')
sheet1.write(1, 33, sub32)
cre32=input('Enter subject code credit: ')
sheet1.write(2, 33, cre32)
sub33 = input('Enter subject code name: ')
sheet1.write(1, 34, sub33)
cre33=input('Enter subject code credit: ')
sheet1.write(2, 34, cre33)
sub34 = input('Enter subject code name: ')
sheet1.write(1, 35, sub34)
cre34=input('Enter subject code credit: ')
sheet1.write(2, 35, cre34)
sub35 = input('Enter subject code name: ')
sheet1.write(1, 36, sub35)
cre35=input('Enter subject code credit: ')
sheet1.write(2, 36, cre35)
sub36 = input('Enter subject code name: ')
sheet1.write(1, 37, sub36)
cre36=input('Enter subject code credit: ')
sheet1.write(2, 37, cre36)
sub37 = input('Enter subject code name: ')
sheet1.write(1, 38, sub37)
cre37=input('Enter subject code credit: ')
sheet1.write(2, 38, cre37)
sub38 = input('Enter suject name: ')
sheet1.write(1, 39, sub38)
cre38=input('Enter subject code credit: ')
sheet1.write(2, 39, cre38)
sub39 = input('Enter subject code name: ')
sheet1.write(1, 40, sub39)
cre39=input('Enter subject code credit: ')
sheet1.write(2, 40, cre39)
sub40 = input('Enter subject code name: ')
sheet1.write(1, 41, sub40)
cre40=input('Enter subject code credit: ')
sheet1.write(2, 41, cre40)
sub41 = input('Enter subject code name: ')
sheet1.write(1, 42, sub41)
cre41=input('Enter subject code credit: ')
sheet1.write(2, 42, cre41)
sub42 = input('Enter subject code name: ')
sheet1.write(1, 43, sub42)
cre42=input('Enter subject code credit: ')
sheet1.write(2, 43, cre42)
sub43 = input('Enter subject code name: ')
sheet1.write(1, 44, sub43)
cre43=input('Enter subject code credit: ')
sheet1.write(2, 44, cre43)
sub44 = input('Enter subject code name: ')
sheet1.write(1, 45, sub44)
cre44=input('Enter subject code credit: ')
sheet1.write(2, 45, cre44)
sub45 = input('Enter subject code name: ')
sheet1.write(1, 46, sub45)
cre45=input('Enter subject code credit: ')
sheet1.write(2, 46, cre45)
sub46 = input('Enter subject code name: ')
sheet1.write(1, 47, sub46)
cre46=input('Enter subject code credit: ')
sheet1.write(2, 47, cre46)
sub47 = input('Enter subject code name: ')
sheet1.write(1, 48, sub47)
cre47=input('Enter subject code credit: ')
sheet1.write(2, 48, cre47)
sub48 = input('Enter subject code name: ')
sheet1.write(1, 49, sub48)
cre48=input('Enter subject code credit: ')
sheet1.write(2, 49, cre48)
sub49 = input('Enter subject code name: ')
sheet1.write(1, 50, sub49)
cre49=input('Enter subject code credit: ')
sheet1.write(2, 50, cre49)
sub50 = input('Enter subject code name: ')
sheet1.write(1, 51, sub50)
cre50=input('Enter subject code credit: ')
sheet1.write(2, 51, cre50)






Name = ""

Fathers_Name = ""

Course = ""


HallTicketNo = 0

i = 0
j = 160417735000
k=0

url = "https://www.osmania.ac.in/res07/20200270.jsp"

driver=webdriver.Chrome(executable_path="C:/Users/owais/OneDrive/Desktop/chromedriver.exe")

driver.get(url)


while True:
    try:
        i=2
        
        driver.find_element_by_xpath('//*[@id="AutoNumber6"]/tbody/tr[1]/td/b/font/input[1]').send_keys(j)

        driver.find_element_by_xpath('//*[@id="AutoNumber6"]/tbody/tr[1]/td/b/font/input[2]').click()

        Name = driver.find_element_by_xpath('//*[@id="AutoNumber3"]/tbody/tr[3]/td[2]/b/font').text

        FatherName = driver.find_element_by_xpath('//*[@id="AutoNumber3"]/tbody/tr[3]/td[4]/b/font').text

        print( Name, FatherName)
        sheet1.write(4+k, 0, str(j))
        sheet1.write(4+k, 1, Name)
        k=k+1
        while True:
            try:
                i=i+1
                
                subname = (driver.find_element_by_xpath("//*[@id='AutoNumber4']/tbody/tr["+str(i)+"]/td[1]/b/font").text)

                subcode = (driver.find_element_by_xpath("//*[@id='AutoNumber4']/tbody/tr["+str(i)+"]/td[2]/b/font").text)

                credital = (driver.find_element_by_xpath("//*[@id='AutoNumber4']/tbody/tr["+str(i)+"]/td[3]/b/font").text)

                grade = (driver.find_element_by_xpath("//*[@id='AutoNumber4']/tbody/tr["+str(i)+"]/td[4]/b/font").text)

                print(type(subcode), subname, credital, grade)

                if subname in sub1:
                    sheet1.write(3+k, 2, grade)
                elif subname in sub2:
                    sheet1.write(3+k, 3, grade)
                elif subname in sub3:
                    sheet1.write(3+k, 4, grade)
                elif subname in sub4:
                    sheet1.write(3+k, 5, grade)
                elif subname in sub5:
                    sheet1.write(3+k, 6, grade)
                elif subname in sub6:
                    sheet1.write(3+k, 7, grade)
                elif subname in sub7:
                    sheet1.write(3+k, 8, grade)
                elif subname in sub8:
                    sheet1.write(3+k, 9, grade)
                elif subname in sub9:
                    sheet1.write(3+k, 10, grade)
                elif subname in sub10:
                    sheet1.write(3+k, 11, grade)
                elif subname in sub11:
                    sheet1.write(3+k, 12, grade)
                elif subname in sub12:
                    sheet1.write(3+k, 13, grade)
                elif subname in sub13:
                    sheet1.write(3+k, 14, grade)
                elif subname in sub14:
                    sheet1.write(3+k, 15, grade)
                elif subname in sub15:
                    sheet1.write(3+k, 16, grade)
                elif subname in sub16:
                    sheet1.write(3+k, 17, grade)
                elif subname in sub17:
                    sheet1.write(3+k, 18, grade)
                elif subname in sub18:
                    sheet1.write(3+k, 19, grade)
                elif subname in sub19:
                    sheet1.write(3+k, 20, grade)
                elif subname in sub20:
                    sheet1.write(3+k, 21, grade)
                elif subname in sub21:
                    sheet1.write(3+k, 22, grade)
                elif subname in sub22:
                    sheet1.write(3+k, 23, grade)
                elif subname in sub23:
                    sheet1.write(3+k, 24, grade)
                elif subname in sub24:
                    sheet1.write(3+k, 25, grade)
                elif subname in sub25:
                    sheet1.write(3+k, 26, grade)
                elif subname in sub26:
                    sheet1.write(3+k, 27, grade)
                elif subname in sub27:
                    sheet1.write(3+k, 28, grade)
                elif subname in sub28:
                    sheet1.write(3+k, 29, grade)
                elif subname in sub29:
                    sheet1.write(3+k, 30, grade)
                elif subname in sub30:
                    sheet1.write(3+k, 31, grade)
                elif subname in sub31:
                    sheet1.write(3+k, 32, grade)
                elif subname in sub32:
                    sheet1.write(3+k, 33, grade)
                elif subname in sub33:
                    sheet1.write(3+k, 34, grade)
                elif subname in sub34:
                    sheet1.write(3+k, 35, grade)
                elif subname in sub35:
                    sheet1.write(3+k, 36, grade)
                elif subname in sub36:
                    sheet1.write(3+k, 37, grade)
                elif subname in sub37:
                    sheet1.write(3+k, 38, grade)
                elif subname in sub38:
                    sheet1.write(3+k, 39, grade)
                elif subname in sub39:
                    sheet1.write(3+k, 40, grade)
                elif subname in sub40:
                    sheet1.write(3+k, 41, grade)
                elif subname in sub41:
                    sheet1.write(3+k, 42, grade)
                elif subname in sub42:
                    sheet1.write(3+k, 43, grade)
                elif subname in sub43:
                    sheet1.write(3+k, 44, grade)
                elif subname in sub44:
                    sheet1.write(3+k, 45, grade)
                elif subname in sub45:
                    sheet1.write(3+k, 46, grade)
                elif subname in sub46:
                    sheet1.write(3+k, 47, grade)
                elif subname in sub47:
                    sheet1.write(3+k, 48, grade)
                elif subname in sub48:
                    sheet1.write(3+k, 49, grade)
                elif subname in sub49:
                    sheet1.write(3+k, 50, grade)
                elif subname in sub50:
                    sheet1.write(3+k, 51, grade)                
                
            except:
                break
        j=j+1
        
    except:
        j=j+1
        if(j > 160417735120):
            break 
    
    

print("Saving....................")
book.save("Results3rdyearECEMJCET.xls") 
        
