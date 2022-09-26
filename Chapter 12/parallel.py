from multiprocessing import Pool

pool = Pool(2)               # create pool of 2 processes

animals = ['hawk', 'hen', 'hog', 'hyena']
res = pool.map(len, animals) # apply len() to every animals item

print(res)                   # print the list of string lengths
