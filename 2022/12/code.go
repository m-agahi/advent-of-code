package main

import (
	"bufio"
	"fmt"
	"os"
)

var input []string
var heightmap []*coordination
var neighbors = [4][2]int{
	{-1, 0},
	{1, 0},
	{0, -1},
	{0, 1},
}

var invoked int

type coordination struct {
	coordination  [2]int
	height        int
	height_char   byte
	destination   bool
	shortest_path int
	through       [2]int
	deadend       bool
}

func check(e error) {
	if e != nil {
		fmt.Println("fucking error man")
		panic(e)
	}
}

func debug(message interface{}) {
	fmt.Println(message)
}

func ReadInput(FilePath string) {
	var line string

	readFile, err := os.Open(FilePath)
	check(err)

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)
	for fileScanner.Scan() {
		line = fileScanner.Text()
		input = append(input, line)
	}
	readFile.Close()
}

func main() {
	filePath := os.Args[1]
	ReadInput(filePath)

	object_creation()
	for i := range heightmap {
		if heightmap[i].shortest_path == 0 {
			pathfinder(heightmap[i])
		}
	}

	for i := range heightmap {
		// debug(heightmap[i].shortest_path)
		if heightmap[i].destination {
			fmt.Println("shortest path: ", heightmap[i].shortest_path)
			// debug(heightmap[i].through)
			// backtrack(heightmap[i])
		}
	}
	// debug(invoked)
}

func object_creation() {
	for i := 0; i < len(input); i++ {
		for j := 0; j < len(input[0]); j++ {
			var o coordination
			o.coordination[0] = i
			o.coordination[1] = j
			if input[i][j] == 'S' {
				o.height = 0
				o.through[0] = -1
				o.through[1] = -1
				o.shortest_path = 0
				o.destination = false
				o.height_char = 'S'
				o.deadend = true
			} else if input[i][j] == 'E' {
				o.height = 26
				o.destination = true
				o.height_char = 'z'
				o.shortest_path = len(input) * len(input[0])
				o.deadend = false
			} else {
				o.height = int(input[i][j]) - 97
				o.height_char = input[i][j]
				o.shortest_path = len(input) * len(input[0])
				o.destination = false
				o.deadend = false
			}
			heightmap = append(heightmap, &o)
		}
	}
}

func find_object(row int, col int) (address *coordination) {
	for i := range heightmap {
		if heightmap[i].coordination[0] == row && heightmap[i].coordination[1] == col {
			address = heightmap[i]
			break
		}
	}
	return
}

func pathfinder(c *coordination) {
	if !c.destination {
		for coor := range neighbors {
			if c.coordination[0]+neighbors[coor][0] < 0 ||
				c.coordination[1]+neighbors[coor][1] < 0 ||
				c.coordination[0]+neighbors[coor][0] >= len(input) ||
				c.coordination[1]+neighbors[coor][1] >= len(input[0]) {
				continue
			}
			nb := find_object(c.coordination[0]+neighbors[coor][0], c.coordination[1]+neighbors[coor][1])
			if (nb.coordination[0] != c.through[0]) || (nb.coordination[1] != c.through[1]) {
				if nb.shortest_path+1 > c.shortest_path {
					if (nb.height-c.height <= 1) && (nb.height-c.height >= 0) {
						nb.shortest_path = c.shortest_path + 1
						nb.through[0] = c.coordination[0]
						nb.through[1] = c.coordination[1]
						fmt.Println(string(nb.height_char), nb.coordination, nb.shortest_path)
						pathfinder(nb)
					}
				}
			}
		}
	} else {
		debug(c.shortest_path)
	}
}

func backtrack(o *coordination) {
	if o.shortest_path != 0 {
		debug(string(o.height_char))
		backtrack(find_object(o.through[0], o.through[1]))
	}
}
