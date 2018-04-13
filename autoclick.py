from selenium import webdriver
from datetime import datetime
import time

def enrol(username,password,courseload):
    #connect
    browser = webdriver.Chrome()
    browser.get('https://acorn.utoronto.ca')
    
    #set the maximum waiting time in acorn
    browser.implicitly_wait(60)
    #this is the error handler and the maximum try time
    max_try = 20
    handle = 0
    fail = 0
    #input all the information
    while(handle == 0):
        try:
            elem = browser.find_element_by_id("username")
            elem.send_keys(username)
            handle+=1
        except:
            print("username input fail,retry")
            fail += 1
            if(fail == max_try):return 0
            
    while(handle == 1):
        try:
            elem = browser.find_element_by_id("password")
            elem.send_keys(password)
            handle+=1
        except:
            print("password input fail,retry")
            fail += 1
            if(fail == max_try):return 0            
            
    while(handle == 2):
        try:
            elec = browser.find_element_by_name("_eventId_proceed")
            elec.click()
            handle += 1
        except:
            print("onclick fail")
            fail += 1
            if(fail == max_try):return 0            
    
    browser.switch_to_window(browser.window_handles[-1])
    
    while(handle == 3):
        #switch to the new window and the enrol course part
        try:
            elem = browser.find_element_by_link_text("Courses")
            elem.click()
            handle += 1
        except:
            print("switch window fail")
            fail += 1
            if(fail == max_try):return 0
    
    while(handle == 4):
        try:
            elem = browser.find_element_by_id("tablink-1")
            elem.click()
            handle += 1
        except:
            print("switch summer failed")
            fail += 1
            if(fail == max_try):return 0
    
    fail_course = []
    #enrol the first time
    while(handle == 5):
        try:
            while(courseload != []):
                course= browser.find_element_by_xpath('//*[@id="{}-planCourseBox"]/div[1]/div[1]/div[2]/div[1]/a'.format(courseload[0]))
                course.click()
                
                '''
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
                
                #try to close the current window
                close_time = 0
                while(close_time < 5):
                    try:
                        time.sleep(1)
                        close = browser.find_element_by_xpath('//*[@id="course-modal"]/div/div[2]/div/div[1]/div[1]/button')
                        close.click()
                        close_time = 6
                    except:
                        print("close the current window failed")
                        close_time += 1
            handle += 1
        except:
            print("enrol {} failed".format(courseload[0]))
            fail_course.append(courseload.pop(0))
            fail += 1
            if(fail == max_try):return 0
    '''
    #retry on the failed course
    while(handle == 6):
        try:
            while(fail_course != []):
                print("here is the second try")
                course= browser.find_element_by_xpath('//*[@id="{}-planCourseBox"]/div[1]/div[1]/div[2]/div[1]/a'.format(fail_course[0]))
                course.click()

                #for the course that is able to enrol, enrol
                try:
                    enrol = browser.find_element_by_xpath('//*[@id="course-modal"]/div/div[2]/div/div[3]/div[2]/ol/li[3]')
                    enrol.click()
                    print("enrol {} success".format(fail_course.pop(0)))
                except:
                    print("enrol click failed")
                    fail += 1
                    if(fail == max_try):return 0
                
                try:
                    close = browser.find_element_by_xpath('//*[@id="course-modal"]/div/div[2]/div/div[1]/div[1]/button')
                    close.click()
                except:
                    print("close the current window failed")
                    fail += 1
                    if(fail == max_try):return 0
            handle += 1
        except:
            print("enrol {} failed".format(fail_course[0]))
            fail += 1
            if(fail == max_try):return 0
    '''
    if(handle == 6):return 1
    else:return 0
    

def data_input(username,password,a):
    if(enrol(username,password,a) == 1):
        print("success")
        return 1
    else:
        print("failed, reach the max time set")
        return 0

def timer(enroltime):
    if(enroltime <= datetime.now()):
        print(datetime.now())
        return False
    else:
        print(".")
        return True

if(__name__ == '__main__'):
    file = open("data_enrol.txt","r")
    data = file.readlines()
    username = data[0][:-1]
    password = data[1][:-1]
    a = []
    for i in range(2,len(data)):
        a.append(data[i][:-1])
    print("please ensure the following information is correct")
    print(" username : {} \n password : {} \n".format(username,password))
    for i in range(0,len(a)):
        print("course{} : {}".format(i+1,a[i]))
    print(a)
    #ask permission
    enrol_time = datetime(2018,4,18,6,0,0)
    print(enrol_time)
    
    #timer and enrol start
    while(timer(enrol_time)):
        #timer error in 0.1 seconds
        time.sleep(0.1)
    data_input(username,password,a)
    