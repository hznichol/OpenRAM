from joblib import Parallel, delayed
import multiprocessing
    
# what are your inputs, and what operation do you want to 
# perform on each input. For example...

def processInput(i):
	return i * i

def print_text(text):
    print(text)
    
def doParallel(trials):
    inputs = range(trials) 
    num_cores = multiprocessing.cpu_count()
    results = Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in inputs)
    return results

def doParallelPrint():
    inputs = ['hello', 'world', 'foo', 'bar']
    num_cores = multiprocessing.cpu_count()
    print(num_cores) #I should not just num_cores. Should be a little smarterd
    results = Parallel(n_jobs=num_cores)(delayed(print_text)(i) for i in inputs)
    
    
if __name__ == '__main__':
    # results = doParallel(10)
    # print(results)
    #doParallelPrint()
    
    x = [1,2,3,4]
    y = ['a','b','c','d']
    inputs = zip(x,y)
    for i in inputs:
        print i[0], ' and ', i[1]
        