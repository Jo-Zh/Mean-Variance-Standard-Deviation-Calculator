import numpy as np

def calculate(list):
    list=np.array(list)
    
    if len(list)<10:
        raise ValueError("List must contain nine numbers.")
    else:
        myArray=list.reshape((5,2))
        output_mean_1=np.mean(myArray, axis=1)
        output_mean_0=np.mean(myArray, axis=0)
        output_mean=np.mean(myArray)
        output_var_1=np.var(myArray, axis=1)
        output_var_0=np.var(myArray, axis=0)
        output_var=np.var(myArray)
        output_std_1=np.std(myArray, axis=1)
        output_std_0=np.std(myArray, axis=0)
        output_std=np.std(myArray)
        output_max_1=np.max(myArray, axis=1)
        output_max_0=np.max(myArray, axis=0)
        output_max=np.max(myArray)
        output_min_1=np.min(myArray, axis=1)
        output_min_0=np.min(myArray, axis=0)
        output_min=np.min(myArray)
        output_sum_1=np.sum(myArray, axis=1)
        output_sum_0=np.sum(myArray, axis=0)
        output_sum=np.sum(myArray)
        result={
        'mean': [output_mean_0.tolist(), output_mean_1.tolist(), output_mean.tolist()],
        'variance':[output_var_0.tolist(), output_var_1.tolist(), output_var.tolist()],
        'standard deviation':[output_std_0.tolist(), output_std_1.tolist(), output_std.tolist()],
        'max':[output_max_0.tolist(), output_max_1.tolist(), output_max.tolist()],
        'min':[output_min_0.tolist(), output_min_1.tolist(), output_min.tolist()],
        'sum':[output_sum_0.tolist(), output_sum_1.tolist(), output_sum.tolist()],
        }
        return result
    
