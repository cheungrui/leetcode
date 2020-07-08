// @Date    : 2020-06-30 18:M:25
// @Author  : ZhangRui (1484659706@qq.com)
// @Link    : None
// @Version : $Id$
func largestRectangleArea(heights []int) int {
    var result int
    result = 0
    tmpResult := 0

    heights = append(heights, 0)
    // this is the index of the value real start
    heightIndex := make([]int, 0)
    heightValue := make([]int, 0)
    
    tmpStartIndex := 0

    tmpValue := 0
    tmpIndex := 0

    for index, value := range heights {
        tmpStartIndex = index
        for {
            
            if len(heightValue) == 0 || value > heightValue[len(heightValue) - 1] {
                heightValue = append(heightValue, value)
                heightIndex = append(heightIndex, tmpStartIndex)
                break
            } else if value < heightValue[len(heightValue) - 1]{
                tmpIndex = heightIndex[len(heightIndex) - 1]
                tmpValue = heightValue[len(heightValue) - 1]
                tmpResult = (index - tmpIndex) * tmpValue
                if result < tmpResult {
                    result = tmpResult
                }
                //update this value's start index
                tmpStartIndex = tmpIndex
                
                // pop
                heightValue = heightValue[:len(heightValue) - 1]
                heightIndex = heightIndex[:len(heightIndex) - 1]
            } else {
                break
            }
        }
    }
    return result
}