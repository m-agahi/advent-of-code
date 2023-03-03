package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var register int = 1
var cycle int = 0
var sum1 int
var display [6][40]string

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
	var line, command string
	var value int

	display_init()

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		line = fileScanner.Text()
		instructions = append(instructions, line)
	}
	for i := range instructions {
		command = strings.Fields(instructions[i])[0]
		var adding bool = false
		if command == "noop" {
			value = 0
		} else {
			adding = true
			value, _ = strconv.Atoi(strings.Fields(instructions[i])[1])
		}

		do(adding, value)
	}
	readFile.Close()
	fmt.Println(sum1)
	display_draw()
}

func do(adding bool, value int) {
	sprite()
	cycle++
	check_cycle()
	if adding {
		sprite()
		cycle++
		check_cycle()
		register += value
	}
}

func check_cycle() {
	if cycle == 20 || (cycle-20)%40 == 0 {
		sum()
	}
}

func sum() {
	fmt.Println(register, cycle, register*cycle)
	sum1 += (int(register) * cycle)
}

func display_init() {
	for row := 0; row < 6; row++ {
		for col := 0; col < 40; col++ {
			display[row][col] = "."
		}
	}
}

func sprite() {
	var row, pixel int
	row = cycle / 40
	pixel = cycle % 40
	sl := register
	switch pixel {
	case sl, (sl + 1), (sl - 1):
		display[row][pixel] = "#"
		if pixel == 0 {
		}
	}
}

func display_draw() {
	var s string
	for row := 0; row < 6; row++ {
		s = ""
		for col := 0; col < 40; col++ {
			s += display[row][col]
		}
		fmt.Println(s)
	}
}
