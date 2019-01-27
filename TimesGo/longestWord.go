package main
// Write a function that extracts the longest word from a string of space-separated words.
import (
	"fmt"
  "strings"
  "sort"
)

func main() {
  word := longest("this is a test for NYT")
  fmt.Println("This is the longest word in the string: '" + word +"'")
}

func longest(a string) string {
  words := strings.Fields(a) // split string by spaces
  sort.Strings(words) // sort string list by increasing order
  longest := words[len(words)-1]
  return longest
}
