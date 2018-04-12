from selenium import webdriver
import time

def enrol(username,password,courseload):
    #connect
    browser = webdriver.Chrome()
    browser.get('https://acorn.utoronto.ca')
    browser.implicitly_wait(10)
    #this is the error handler
    handle = 0
    #input all the information
    while(handle == 0):
        try:
            elem = browser.find_element_by_id("username")
            elem.send_keys(username)
            handle+=1
        except:
            print("username input fail")
            return 0
            
    while(handle == 1):
        try:
            elem = browser.find_element_by_id("password")
            elem.send_keys(password)
            handle+=1
        except:
            print("password input fail")
            return 0
            
    while(handle == 2):
        try:
            elec = browser.find_element_by_name("_eventId_proceed")
            elec.click()
            handle += 1
        except:
            print("onclick fail")
            return 0
    
    browser.switch_to_window(browser.window_handles[-1])
    
    while(handle == 3):
        #switch to the new window and the enrol course part
        try:
            elem = browser.find_element_by_link_text("Courses")
            elem.click()
            handle += 1
        except:
            print("switch window fail")
            return 0
    
    while(handle == 4):
        try:
            elem = browser.find_element_by_id("tablink-1")
            elem.click()
            handle += 1
        except:
            print("switch summer failed")
            return 0
    
    while(handle == 5):
        try:
            while(courseload != []):
                course= browser.find_element_by_xpath('//*[@id="{}-planCourseBox"]/div[1]/div[1]/div[2]/div[1]/a'.format(courseload[0]))
                course.click()
                courseload.pop(0)
                #input the enrol command here
                time.sleep(2)
                #close command
                try:
                    close = browser.find_element_by_xpath('//*[@id="course-modal"]/div/div[2]/div/div[1]/div[1]/button')
                    close.click()
                except:
                    print("close the current window failed")
                time.sleep(1)
            handle += 1
        except:
            print("enrol {} failed".format(i))
            return 0
    return 1
            
if(__name__ == '__main__'):
    file = open("data_enrol.txt","r")
    data = file.readlines()
    username = data[0][:-1]
    password = data[1][:-1]
    a = []
    for i in range(2,6):
        a.append(data[i][:-1])
    if(enrol(username,password,a) == 1):
        print("success")
    else:
        print("fail")

        
        
    
