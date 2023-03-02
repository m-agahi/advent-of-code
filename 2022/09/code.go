package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

const width int = 1000
const hight int = 1000

var grid [hight][width]string
var head = [2]int{hight / 2, width / 2}
var tail = [2]int{hight / 2, width / 2}

var snakepit [hight][width]string
var snake = [10][2]int{}

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

	var instructions = make([]string, 0)
	var line string
	var direction string
	var steps int

	grid[tail[0]][tail[1]] = "#"

	for i := 0; i < 10; i++ {
		snake[i][0] = hight / 2
		snake[i][1] = width / 2
	}
	snakepit[snake[9][0]][snake[9][1]] = "#"

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		line = fileScanner.Text()
		instructions = append(instructions, line)
	}
	for i := range instructions {
		direction = strings.Fields(instructions[i])[0]
		steps, _ = strconv.Atoi(strings.Fields(instructions[i])[1])
		row, col := navigate(direction)
		moving(row, col, steps)
		crawl(row, col, steps)
	}
	readFile.Close()
	fmt.Println(sum())
}

func navigate(direction string) (row int, col int) {
	row = 0
	col = 0

	switch direction {
	case "U": //up
		row = -1
	case "R": // right
		col = 1
	case "D": // down
		row = 1
	case "L": // left
		col = -1
	}
	return
}
func moving(row int, col int, steps int) {

	for move := 0; move < steps; move++ {
		head[0] = head[0] + row
		head[1] = head[1] + col
		var tr, tc int
		if math.Abs(float64(head[0]-tail[0])) > 1 || math.Abs(float64(head[1]-tail[1])) > 1 {
			if tail[0] < head[0] {
				// head below tail
				tr = 1
				if tail[1] < head[1] {
					// head SE of tail
					tc = 1
				} else if tail[1] > head[1] {
					// head SW of tail
					tc = -1
				} else {
					// head S of tail
					tc = 0
				}
			} else if tail[0] > head[0] {
				// head above tail
				tr = -1
				if tail[1] < head[1] {
					// head NE of tail
					tc = 1
				} else if tail[1] > head[1] {
					// head NW of tail
					tc = -1
				} else {
					// head N of tail
					tc = 0
				}
			} else {
				// head and tail on the same row
				tr = 0
				if tail[1] < head[1] {
					// head E of tail
					tc = 1
				} else if tail[1] > head[1] {
					// head W of tail
					tc = -1
				} else {
					// head is on the tail
					tc = 0
				}
			}
			tail[0] += tr
			tail[1] += tc
			grid[tail[0]][tail[1]] = "#"
		}
	}
}

func crawl(row int, col int, steps int) {

	for move := 0; move < steps; move++ {

		snake[0][0] = snake[0][0] + row
		snake[0][1] = snake[0][1] + col

		for body := 1; body < 10; body++ {
			var tr, tc int
			if math.Abs(float64(snake[body-1][0]-snake[body][0])) > 1 || math.Abs(float64(snake[body-1][1]-snake[body][1])) > 1 {
				if snake[body][0] < snake[body-1][0] {
					// head below tail
					tr = 1
					if snake[body][1] < snake[body-1][1] {
						// head SE of tail
						tc = 1
					} else if snake[body][1] > snake[body-1][1] {
						// head SW of tail
						tc = -1
					} else {
						// head S of tail
						tc = 0
					}
				} else if snake[body][0] > snake[body-1][0] {
					// head above tail
					tr = -1
					if snake[body][1] < snake[body-1][1] {
						// head NE of tail
						tc = 1
					} else if snake[body][1] > snake[body-1][1] {
						// head NW of tail
						tc = -1
					} else {
						// head N of tail
						tc = 0
					}
				} else {
					// head and tail on the same row
					tr = 0
					if snake[body][1] < snake[body-1][1] {
						// head E of tail
						tc = 1
					} else if snake[body][1] > snake[body-1][1] {
						// head W of tail
						tc = -1
					} else {
						// head is on the tail
						tc = 0
					}
				}
				snake[body][0] += tr
				snake[body][1] += tc

			}
		}
		snakepit[snake[9][0]][snake[9][1]] = "#"
	}

}

func sum() (sum1 int, sum2 int) {
	sum1 = 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == "#" {
				sum1++
			}
			if snakepit[i][j] == "#" {
				sum2++
			}
		}
	}
	return
}
