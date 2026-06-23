from No22.res import get_data
def sum1(a):
    sum=0
    for i in range(len(a)):
        sum+=a[i]
    return sum
sum=0
for i in range(1, 101):
    data=get_data(i)
    print(f"第{i}页数据: {data}")
    sum_data=sum1(data)
    sum+=sum_data
print(sum)
