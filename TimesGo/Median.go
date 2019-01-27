package main
// Write a function that returns the median integer from an array of integers.
import (
	"fmt"
  "math"
  "sort"
)

func main() {
	fmt.Println("Hello, playground")
  nums := []int{1,2,4, 5, 89}
  num := median(nums)
  fmt.Println("Median: ", num)
}

func median(nums []int) int{
  sort.Ints(nums)
  length := len(nums)
  medianIndex := int64(math.Floor(float64(length)/2))
  if(length % 2 == 0 ){
    // even numbered list so take mean of two middle most numbers and round up
    low := nums[medianIndex-1]
    high := nums[medianIndex]
    mean := int(math.Ceil(float64(low + high)/2))
    return mean
  }
  // if the list number is odd just take the middle number
  return nums[medianIndex]
}
