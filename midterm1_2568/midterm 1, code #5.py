inp_list = []
for inp_time in range(5):
    inp_list.append(int(input("")))
    inp_time+=1
inp_sum=sum(inp_list)
print(inp_sum)
avg=sum(inp_list)/len(inp_list)
print(avg)