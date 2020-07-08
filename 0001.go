func twoSum(nums []int, target int) []int {
    mp := make(map[int]int)
    for index, value := range nums{
        mp[value] = index
    }
    sort.Ints(nums)
    numsLength := len(nums)
    index1 := 0
    index2 := numsLength -1
    a := nums[index1]
    b := nums[index2]
    for i:=0; i<numsLength; i++ {
        if a + b == target {
            break
        }else if a + b < target {
            index1 += 1
            a = nums[index1]
        }else {
            index2 -= 1
            b = nums[index2]
        }
    }
    result := make([]int, 2)
    result[0] = mp[a]
    result[1] = mp[b]
    return result
}