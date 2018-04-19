from selenium import webdriver
from datetime import datetime
import time

def enrol(username,password,courseload):
    #connect
    browser = webdriver.Chrome()
    browser.get('https://acorn.utoronto.ca')
    
    #set the maximum waiting time in acorn
    browser.implicitly_wait(10)
    #this is the error handler and the maximum try time
    max_try = 5
    handle = 0
    fail = 0
    #input all the information
    while(handle == 0):
        try:
            elem = browser.find_element_by_id("username")
            elem.send_keys(username)
            handle+=1
        except:
            fail += 1
            if(fail == max_try):return handle
            
    while(handle == 1):
        try:
            elem = browser.find_element_by_id("password")
            elem.send_keys(password)
            handle+=1
        except:
            fail += 1
            if(fail == max_try):return handle           
            
    while(handle == 2):
        try:
            elec = browser.find_element_by_name("_eventId_proceed")
            elec.click()
            handle += 1
        except:
            fail += 1
            if(fail == max_try):return handle         
    
    browser.switch_to_window(browser.window_handles[-1])
    
    while(handle == 3):
        #switch to the new window and the enrol course part
        try:
            elem = browser.find_element_by_link_text("Courses")
            elem.click()
            handle += 1
        except:
            fail += 1
            if(fail == max_try):return handle
    
    while(handle == 4):
        try:
            elem = browser.find_element_by_id("tablink-1")
            elem.click()
            handle += 1
        except:
            fail += 1
            if(fail == max_try):return handle
            
    #enrol the first time
    while(handle == 5):
        try:
            while(courseload != []):
                course= browser.find_element_by_xpath('//*[@id="{}-planCourseBox"]/div[1]/div[1]/div[2]/div[1]/a'.format(courseload[0]))
                course.click()
                
                
                #for the course that is able to enrol, enrol
                enrol = browser.find_element_by_xpath('//*[@id="course-modal"]/div/div[2]/div/div[3]/div[2]/ol/li[3]')
                enrol.click()
                print("enrol {} success".format(courseload.pop(0)))
                
                '''
                #this test part is for current time before the enrol time
                #test part begin
                courseload.pop(0)
                time.sleep(1)
                #test part end
                '''
                
                #try to close the current window
                time.sleep(1)
                close = browser.find_element_by_xpath('//*[@id="course-modal"]/div/div[2]/div/div[1]/div[1]/button')
                close.click()
            handle += 1
        except:
            print("enrol {} failed".format(courseload[0]))
            fail += 1
            if(fail == max_try):return 0
            
    if(handle == 6):return -1

def info(code):
    print("error code {}".format(code))
    
def main(username,password,a):
    max_try = 10
    counter = 0
    while (counter < max_try):
        try:
            code = enrol(username,password,a)
            if(code == -1):
                counter = max_try
                print("success")
            else:
                counter += 1
                info(code)
        except:
            print("fatal error")
            time.sleep(1)
            counter += 1

if(__name__ == '__main__'):
    file = open("data_enrol.txt","r")
    data = file.readlines()
    username = data[0][:-1]
    password = data[1][:-1]
    a = []
    for i in range(2,len(data)):
        a.append(data[i][:-1])
    print("please ensure the following information is correct")
    print("username : {} \npassword : {}".format(username,password))
    for i in range(0,len(a)):
        print("course{} : {}".format(i+1,a[i]))
    print(a)
    
    #ask permission
    enrol_time = datetime(2018,4,19,16,0,3)
    print("start time {}".format(enrol_time))
    
    sleep_time = enrol_time - datetime.now()
    print("sleep time: {} seconds".format(sleep_time.total_seconds()))
    
    i = input("please confirm all the information correct Y/N")
    
    if(i.lower() == 'y'):
        time.sleep(sleep_time.total_seconds())
        #main(username,password,a)
    elif(i.lower() == 'n'):
        print("quit program")
    
    
