sum = 0
def story():
    print("从前有座山，山上有做庙，庙里有个老和尚将故事")
    global sum
    sum+=1
    if sum > 30:
        return
    story()
story()
print(sum)