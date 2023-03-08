# Conv2-python-numpy

在学习lucy-richardson算法过程中，发现numpy中没有自带的二维卷积函数。因此用numpy写一个。
二维卷积的原理是，先在矩阵周围填充上0，之后再滑动卷积核，在卷积范围内的矩阵与卷积核对应位置相乘再相加,其中卷积核要翻转180度，但在本程序中没有写。
假如矩阵是$m_1,n_1$ 大小，卷积核是$m_2,n_2$ ，在矩阵前后填充$m_2-1,n_2-1$ 排列的0.

输出形状为$full$ 
```python
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
```
输出形状为$same$ 
```python
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
```
