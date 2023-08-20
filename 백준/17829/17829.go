package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func poolingArray(x int, y int, l int) int {
	l = l / 2
	if l == 1 {
		mat := []int{arr[x][y], arr[x+1][y], arr[x][y+1], arr[x+1][y+1]}
		sort.Ints(mat)
		return mat[2]
	}

	lt := poolingArray(x, y, l)
	rt := poolingArray(x+l, y, l)
	lb := poolingArray(x, y+l, l)
	rb := poolingArray(x+l, y+l, l)

	mat := []int{lt, rt, lb, rb}
	sort.Ints(mat)

	return mat[2]
}

var (
	r   = bufio.NewReader(os.Stdin)
	w   = bufio.NewWriter(os.Stdout)
	N   int
	arr [][]int
)

func main() {
	fmt.Fscan(r, &N)
	arr = make([][]int, N)

	for i := range arr {
		arr[i] = make([]int, N)
	}

	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			fmt.Fscan(r, &arr[i][j])
		}
	}

	fmt.Fprintln(w, poolingArray(0, 0, N))
	w.Flush()
}
