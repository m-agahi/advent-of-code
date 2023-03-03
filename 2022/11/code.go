package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var input []string
var div int64

type monkey struct {
	name          int
	items         []int64
	new_value     [3]string
	test_operand  string
	test_variable int64
	test_success  int
	test_fail     int
	inspections   int64
}

var monkies = map[int]*monkey{}

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
	var relief int64 = 3
	MonkeyInfo()
	div = divisible()
	for round := 0; round < 20; round++ {
		for m := 0; m < len(monkies); m++ {
			MonkeyAnalyze(monkies[m], relief)
		}
	}
	fmt.Println("Monkey Bussiness 1 is: ", MonkeyBusiness())

	relief = 1
	MonkeyInfo()
	for round := 0; round < 10000; round++ {
		for m := 0; m < len(monkies); m++ {
			MonkeyAnalyze(monkies[m], relief)
		}
	}
	for m := 0; m < len(monkies); m++ {
		// debug(monkies[m].inspections)
	}
	fmt.Println("Monkey Bussiness 2 is: ", MonkeyBusiness())

}

func MonkeyInfo() {

	for i := 0; i < len(input); i += 7 {
		var meymun monkey
		var tempstrings [6][]string

		for k := 0; k < 6; k++ {
			tempstrings[k] = strings.Fields(input[i+k])
		}

		meymun.name, _ = strconv.Atoi(tempstrings[0][1][:len(tempstrings[0][1])-1])
		for j := 2; j < len(tempstrings[1]); j++ {

			if tempstrings[1][j][len(tempstrings[1][j])-1:len(tempstrings[1][j])] == "," {
				tempstrings[1][j] = tempstrings[1][j][:len(tempstrings[1][j])-1]
			}
			value, _ := strconv.Atoi(tempstrings[1][j])
			meymun.items = append(meymun.items, int64(value))
		}

		for j := 3; j < 6; j++ {
			meymun.new_value[j-3] = tempstrings[2][j]
		}

		meymun.test_operand = tempstrings[3][1]
		var tempint int
		tempint, _ = strconv.Atoi(tempstrings[3][3])
		meymun.test_variable = int64(tempint)

		meymun.test_success, _ = strconv.Atoi(tempstrings[4][5])
		meymun.test_fail, _ = strconv.Atoi(tempstrings[5][5])
		meymun.inspections = 0

		monkies[meymun.name] = &meymun // add to the map
	}
}

func MonkeyAnalyze(m *monkey, relief int64) {
	for counter := len(m.items); counter > 0; counter-- {
		m.inspections++
		m.items[0] = NewWorryLevel(m, m.items[0], relief)
		MonkeyThrow(m)
	}
}

func NewWorryLevel(m *monkey, item int64, relief int64) (result int64) {
	var var1, var2 int64
	var var2temp int
	var1 = item
	var1 = WorryReduction(var1)
	if m.new_value[2] == "old" {
		var2 = var1
	} else {
		var2temp, _ = strconv.Atoi(m.new_value[2])
		var2 = int64(var2temp)
	}

	switch m.new_value[1] {
	case "*":
		result = var1 * var2
	case "/":
		result = var1 / var2
	case "-":
		result = var1 - var2
	case "+":
		result = var1 + var2
	}
	result /= relief
	return result
}

func MonkeyThrow(m *monkey) {

	var test bool = false
	var destination int
	switch m.test_operand {
	case "divisible":
		test = (m.items[0] % m.test_variable) == 0
	}

	if test {
		destination = m.test_success
	} else {
		destination = m.test_fail
	}

	monkies[destination].items = append(monkies[destination].items, m.items[0])
	m.items = m.items[1:]
}

func MonkeyBusiness() (mb int64) {
	var l1, l2 int64 = 0, 0
	for i := 0; i < len(monkies); i++ {
		if monkies[i].inspections > l1 {
			l2 = l1
			l1 = monkies[i].inspections
		} else if monkies[i].inspections > l2 {
			l2 = monkies[i].inspections
		}
	}
	mb = l1 * l2
	return
}

func divisible() (div int64) {
	div = 1
	for i := 0; i < len(monkies); i++ {
		div *= monkies[i].test_variable
	}
	return
}
func WorryReduction(worry int64) (result int64) {
	for ok := true; ok; ok = (worry > div) {
		if worry > (1000000001 * div) {
			worry -= (1000000000 * div)
		} else if worry > 1000001*div {
			worry -= (1000000 * div)
		} else if worry > 100001*div {
			worry -= (100000 * div)
		} else if worry > 1000*div {
			worry -= (999 * div)
		} else if worry > div {
			worry -= div
		}
	}
	result = worry
	return
}
