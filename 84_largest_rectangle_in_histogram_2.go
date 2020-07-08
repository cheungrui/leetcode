// @Date    : 2020-06-30 18:M:25
// @Author  : ZhangRui (1484659706@qq.com)
// @Link    : None
// @Version : $Id$
func largestRectangleArea(heights []int) int {
    var result int
    result = 0
    tmpResult := 0

    heights = append(heights, 0)
    heightIndex := make([]int, 0)

    tmpValue := 0
    tmpIndex := 0

    for index, value := range heights {
        for {
            if len(heightIndex) == 0 || value > heights[heightIndex[len(heightIndex) - 1]] {
                heightIndex = append(heightIndex, index)
                break
            } else if value < heights[heightIndex[len(heightIndex) - 1]]{
                // if no pre index, the preindex should be -1, which means the num before 0
                if len(heightIndex) == 1 {
                    tmpIndex = -1
                } else {
                    tmpIndex = heightIndex[len(heightIndex) - 2]
                }
                tmpValue = heights[heightIndex[len(heightIndex) - 1]]
                tmpResult = (index - tmpIndex - 1) * tmpValue
                if result < tmpResult {
                    result = tmpResult
                }

                heightIndex = heightIndex[:len(heightIndex) - 1]
            } else {
                // two num equal use the last one
                heightIndex[len(heihgtIndex) - 1] = index
                break
            }
        }
    }
    return result
}