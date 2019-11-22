s = input()
if len(s) == 0:
    print('kal')
else:
    nums = []
    lettList = []
    tempList = []
    #numsList = [s[num] for num in range(-1, -len(s), -1) if s[num].isdigit() == True]
    for i in s:
        if s[s.index(i)].isdigit() == False:
            lettList.append(i)
        else:
            nums.append(i)
    #nums = int(nums)
    if nums.count('0') == len(nums):
        nums[-1] = '1'
    else:
        for i in nums:
            if i != '0':
                tempList.append(i)
            else:
                lettList.append(i)
    #tempList = int(''.join(map(str, tempList))) + 1
    s = ''.join(map(str, lettList)) + str((int(''.join(map(str, tempList))) + 1))
