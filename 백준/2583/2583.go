package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func bfs(arr [][]int, visited [][]int, x int, y int) int {
	queue := [][]int{{x, y}}
	visited[y][x] = 1
	area := 0

	for len(queue) > 0 {
		x, y := queue[0][0], queue[0][1]
		queue = queue[1:]
		area++

		for i := 0; i < 4; i++ {
			nx := x + d[i][0]
			ny := y + d[i][1]

			if 0 <= nx && nx < len(arr[0]) && 0 <= ny && ny < len(arr) &&
				visited[ny][nx] == 0 && arr[ny][nx] == 0 {
				queue = append(queue, []int{nx, ny})
				visited[ny][nx] = 1
			}
		}
	}

	return area
}

var (
	d = [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
)

func main() {
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()

	var M, N, K int

	fmt.Fscan(r, &M, &N, &K)

	arr := make([][]int, M)

	for i := range arr {
		arr[i] = make([]int, N)
	}

	var lb_x, lb_y, rt_x, rt_y int

	for i := 0; i < K; i++ {
		fmt.Fscan(r, &lb_x, &lb_y, &rt_x, &rt_y)
		for y := lb_y; y < rt_y; y++ {
			for x := lb_x; x < rt_x; x++ {
				arr[y][x] = 1
			}
		}
	}

	var areaSlice []int
	visited := make([][]int, M)

	for i := range visited {
		visited[i] = make([]int, N)
	}

	for i := 0; i < M; i++ {
		for j := 0; j < N; j++ {
			if arr[i][j] == 0 && visited[i][j] == 0 {
				areaSlice = append(areaSlice, bfs(arr, visited, j, i))
			}
		}
	}

	sort.Ints(areaSlice)
	fmt.Fprintln(w, len(areaSlice))
	for _, v := range areaSlice {
		fmt.Fprintf(w, "%d ", v)
	}
}
