package main

import (
	"fmt"
	"sort"
)

func groupAnagrams(strs []string) [][]string {
	myMap := make(map[string][]string)

	for _, v := range strs {
		runes := []rune(v)
		sort.Slice(runes, func(i int, j int) bool {
			return runes[i] < runes[j]
		})

		s := string(runes)
		myMap[s] = append(myMap[s], v)
	}

	var answer [][]string

	for _, s := range myMap {
		answer = append(answer, s)
	}

	return answer
}

func main() {
	strs := []string{"eat", "tea", "tan", "ate", "nat", "bat"}
	fmt.Println(groupAnagrams(strs))
}
