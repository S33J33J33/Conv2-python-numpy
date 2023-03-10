import numpy as np


def Conv2_full(martix ,psf):  
    [m1 ,n1] = np.shape(martix)  
    [m2 ,n2] = np.shape(psf)  
    img_pad = np.pad(martix ,((m2 - 1 ,n2 - 1) ,(m2 - 1 ,n2 - 1)) ,'constant' ,constant_values=(0 ,0))  
    res_t = np.zeros_like(img_pad)  
    for i in range(m1 + m2 - 1):  
        for j in range(n1 + n2 - 1):      
            temp = img_pad[i:i + m2 ,j:j + n2]  
            temp = np.multiply(temp ,psf).sum()  
            res_t[i][j] = temp  
    return res
    
 def Conv2_same(martix ,psf):  
    [m1 ,n1] = np.shape(martix)  
    [m2 ,n2] = np.shape(psf)  
    img_pad = np.pad(martix ,((m2 - 1 ,n2 - 1) ,(m2 - 1 ,n2 - 1)) ,'constant' ,constant_values=(0 ,0))  
    res_t = np.zeros_like(img_pad)     
    for i in range(int(m2 / 2) ,int(m1 + m2 / 2)):  
        for j in range(int(n2 / 2) ,int(n1 + n2 / 2)):  
            temp = img_pad[i:i + m2 ,j:j + n2]  
            temp = np.multiply(temp ,psf).sum()  
            res_t[i][j] = temp  
    res = res_t[int(m2 / 2):int(m1 + m2 / 2) ,int(n2 / 2):int(n1 + n2 / 2)]  
    return res

if __name__ == '__main__':
    A = [[1 ,2 ,3 ] ,[4 ,5 ,6 ] ,[7 ,8 ,9 ]]
    B = [[9 ,8 ,7] ,[6 ,5 ,4] ,[3 ,2 ,1]]
    C = Conv2_same(A ,B)
    print(C)
