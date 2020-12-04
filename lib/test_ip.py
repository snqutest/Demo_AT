#-*-coding:utf-8-*-

def check_ip(str):
    #检查字符串的长度，最短应该是x.x.x.x 7位，最长应该：xxx.xxx.xxx.xxx 15位
    if (len(str) <7 or len(str)>15):  
        return False
    #检查字符串是否存在.且由4部分组成
    elif '.' not in str and len(str.split('.'))!=4:
        return False

    else:
    #检查ip地址是否大于0且小于255  
        num_list = str.split('.')
        for num in num_list:
            num = int(num)
            if num >=0 and num <=255:
                return True
            else:
                return False

if __name__ =="__main__":
    str_list = [' ','192.168.1.210','10.0.0.1','aaaa']
    for str in str_list:
        if check_ip(str):
            print (str+'是合法的IP地址!')
        else:
            print (str+'不是合法的IP地址')


    

            
        