package main

import (
	"bufio"
	"fmt"
	"os"
)

func check(e error) {
	if e != nil {
		fmt.Println("fucking error man")
		panic(e)
	}
}

func debug(message string) {
	fmt.Println(message)
}

func main() {
	filePath := os.Args[1]
	readFile, err := os.Open(filePath)
	check(err)
	var treemap = make([][]int, 0)
	var word string

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		word = fileScanner.Text()
		var temp []int
		for i := 0; i < len(word); i++ {
			temp = append(temp, int(word[i])-48)
		}
		treemap = append(treemap, temp)
	}

	do(treemap)
	readFile.Close()
}

func tree(tm [][]int, row int, col int) (v bool, scenic int) {
	v = false
	scenic = 1
	scenictemp := [4]int{1, 1, 1, 1}
	var max int = 0
	var init, limit, step int = 0, 0, 0

	if col == 0 || col == len(tm[0])-1 || row == 0 || row == len(tm)-1 {
		v = true
		return v, 0
	}
	for direction := 0; direction < 4; direction++ {
		max = 0
		max_scenetic := false
		switch direction {
		case 0: //up
			init = row - 1
			limit = -1
			step = -1
		case 1: // right
			init = col + 1
			limit = len(tm[0])
			step = 1
		case 2: // down
			init = row + 1
			limit = len(tm)
			step = 1
		case 3: // left
			init = col - 1
			limit = -1
			step = -1
		}
		switch direction {
		case 0, 2:
			for r := init; r != limit; r += step {
				if tm[r][col] > max {
					max = tm[r][col]
				}
				if tm[r][col] >= tm[row][col] || r == 0 || r == len(tm)-1 {
					max_scenetic = true
				}
				if tm[r][col] < tm[row][col] && !max_scenetic {
					scenictemp[direction]++
				}
			}
		case 1, 3:
			for c := init; c != limit; c += step {
				if tm[row][c] > max {
					max = tm[row][c]
				}
				if tm[row][c] >= tm[row][col] || c == 0 || c == len(tm[0])-1 {
					max_scenetic = true
				}
				if tm[row][c] < tm[row][col] && !max_scenetic {
					scenictemp[direction]++
				}
			}
		}
		if max < tm[row][col] {
			v = true
		}
		scenic *= scenictemp[direction]
	}
	// fmt.Println(tm[row][col], ": ", scenic, scenictemp)
	return v, scenic
}

func do(tm [][]int) {
	sum1 := 0
	scenic := 0
	for row := 0; row < len(tm); row++ {
		for col := 0; col < len(tm[row]); col++ {
			var visible bool = false
			var scenictemp int
			visible, scenictemp = tree(tm, row, col)
			if visible {
				sum1++
			}
			if scenictemp > scenic {
				scenic = scenictemp
			}
		}
	}
	fmt.Println("part 1 results: ", sum1)
	fmt.Println("part 2 results: ", scenic)
}
