# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 18:42:31 2017

@author: Administrator
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import gmtime, strftime

url = "http://fund.eastmoney.com/f10/" #基金净值
driver = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver.exe')
"""
print(driver.window_handles)
driver.switch_to_window(driver.window_handles[0])"""
"""
    主方法，用于启动程序
"""
def main():    
    driver.get(url)
    jjList,jjCounts = getFundCount()  #基金的数量    
    print('共有基金数量为:'+jjCounts+'个')
    getFundCode(jjList,1)
    #getFundJZ()    
    

''' 获取基金数量'''
def getFundCount():    
    jjList = driver.find_element_by_id("jjlist")    
    jjCount = jjList.get_attribute('length')
    return jjList,jjCount

"""获取基金编码"""
def getFundCode(jjList,jjindex):    
    loopCount = 1
    for option in jjList.find_elements_by_tag_name('option'):
        #driver.implicitly_wait(10)
        if(loopCount > 3 and loopCount < 13):
            label = option.text
            print("全称为:"+label) 
            getFundJZ(label)                    
        loopCount += 1    

"""根据基金代码获取该基金在某段时间内的净值"""
def getFundJZ(fundCodeList):   
    #模拟点击事件
    #for fundIndex in range(3,15):
        #print("当前请求的索引为:"+str(fundIndex)) 
    for label in ["000009","000003","000004","000005","000006","000007","000008"]:        
        driver.get(url+'jjjz_'+label+'.html')
        """
        select = Select(driver.find_element_by_id("jjlist"))
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        select.select_by_index(fundIndex)
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        """
        jjtablediv = driver.find_element_by_id("jztable") #找到table所在的层    
        jjtable = jjtablediv.find_element_by_class_name("w782")  
        #print("当前的基金代码为:"+label) 
        print(label+"\n")
        for row in jjtable.find_elements_by_xpath(".//tr"):                          
            for td in row.find_elements_by_xpath(".//td[text()]"):            
                print(td.text,end=" ")               
getFundJZ("f")