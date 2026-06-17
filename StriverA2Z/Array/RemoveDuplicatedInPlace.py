def RemoveDuplicates(nums:list):
    if len(nums)==0:
        return 0
    
    write = 1
    for scan in range(1,len(nums)):
        if nums[scan]!=nums[scan-1]:
            nums[write]=nums[scan]
            write = write+1
    return write

