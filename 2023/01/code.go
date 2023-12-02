package main

import (
	"bufio"
	"fmt"
	"os"
	// "strings"
)

var input, modified_input []string
var d1, d2, summary int = -1, 0, 0

var dd = []string{
	"zero",
	"one",
	"two",
	"three",
	"four",
	"five",
	"six",
	"seven",
	"eight",
	"nine",
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

	calculation(input)
	debug(summary)

	// conversion(input)
	// fmt.Println(modified_input)
}

// func conversion(instructions []string) {
// 	for line := range instructions {

//		}
//	}
func calculation(instructions []string) {
	for line := range instructions {
		var sl1 []string
		var sl2 []string
		for index, chr := range instructions[line] {
			if int(chr) >= 48 && int(chr) <= 57 {
				if d1 == -1 {
					d1 = int(chr) - 48
					d2 = d1
					sl1 = nil
					sl2 = nil
					sl1 = append(sl1, instructions[line][0:index])
					sl2 = append(sl2, instructions[line][index:])
				} else {
					d2 = int(chr) - 48
					sl2 = nil
					sl2 = append(sl2, instructions[line][index:])
				}
			}
		}
		debug(sl1)
		debug(sl2)
		d1t := search(sl1)
		// d1t += 0
		debug(d1t)
		debug("")
		summary += (d1 * 10) + d2

		d1 = -1
	}
}

func search(slice []string) int {
	startDigit := 0
	startIndex := -1
	for index, digit := range dd {
		_, tempIndex := indexOfString(slice, digit)
		debug(digit)
		// for i, str := range slice {
		// 	if strings.HasPrefix(str, digit) {
		// 		tempIndex = i
		// 		debug(digit)
		// 		break
		// 	}
		// }
		if tempIndex > -1 && tempIndex < startIndex {
			startIndex = tempIndex
			startDigit = index
		}

	}
	return (startDigit)
}
func indexOfString(slice []string, target string) (bool, int) {
	for i, s := range slice {
		if s == target {
			return true, i
		}
	}
	return false, -1
}
