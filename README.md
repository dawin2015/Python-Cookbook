# Python-Cookbook
供平时学习查询使用,中文为简单提示，代码详见源码对应的题号，如1.3对应1_3.py
## 第一章
1.1 将序列分解为单独的变量</br>
任何序列（可迭代的对象）都可以通过一个简单的赋值操作来分解为单独的变量，唯一的要求是变量的总数和结构要和序列相吻合。</br>
1.2 从任意长度的可迭代对象中分解元素</br>
“*表达式”</br>
1.3 保存最后N个元素</br>
from collections import deque</br>
1.4 找出最大或最小的N个元素</br>
import heapd<\br>
返回nums中前三个最大值heap.nlargest(3, nums)<\br>
返回nums中前三个最小值heap.nsmallest(3, nums)<\br>
生成小端堆heap.heapify(nums)<\br>
讲第一个元素（最小的）弹出heap.heappop()<\br>
1.5 实现优先级队列
实现一个队列，能够以给定的优先级来对元素排序，且每次pop操作时都会返回优先级最高的那个元素<\br>
import heapq<\br>

