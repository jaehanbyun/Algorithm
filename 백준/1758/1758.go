package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	var N int

	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)

	fmt.Fscanf(r, "%d\n", &N)
	arr := make([]int, N)

	for i := 0; i < N; i++ {
		fmt.Fscanf(r, "%d\n", &arr[i])
	}

	sort.Sort(sort.Reverse((sort.IntSlice(arr))))

	answer := 0

	for i, v := range arr {
		if temp := v - i; temp < 0 {
			break
		} else {
			answer += temp
		}
	}

	fmt.Fprintln(w, answer)
	w.Flush()
}
