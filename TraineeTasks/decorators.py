from time import perf_counter, time
from typing import List, Any
from functools import wraps


'''
Задача реализовать декоратор, который будет считать время
работы декорируемой функции и выводить его в формате
ЧЧ:ММ:СС.МС
'''


#functools стоит использовать потому, что она копирует всю информацию об оборачивающей функции в функцию обертку?
def functools_timer(func: Any) -> Any:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> float:
        start = perf_counter()
        result = func(*args, **kwargs)
        print(perf_counter() - start)
        return result
    return wrapper


'''
В качесте "подопытного" взята задача с LeetCode, которая мне компьютер уронила из-за слишком долгого выполнения, 
при первой попытке решить ее.
Само условие звучит следующим образом:
169. Majority Element
Given an array nums of size n, return the majority element. 
The majority element is the element that appears more than n / 2 times. 
You may assume that the majority element always exists in the array.
'''


@functools_timer
def majorityElement(nums: List[int]) -> int:
    set_list = set(nums)
    majority_element = 0
    check_for_majority_element = 0
    for element in set_list:
        if nums.count(element) > len(nums) / 2:
            if nums.count(element) > check_for_majority_element:
                majority_element = element
                check_for_majority_element = nums.count(element)
    return majority_element


#Достаточно большой массив данных, так как мелкие массивы функция щелкает за доли мили-секунд
check = [i for i in range(1, 10000)]


if __name__ == '__main__':
    majorityElement(check)

