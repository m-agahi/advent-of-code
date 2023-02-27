package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		fmt.Println("fucking error man")
		panic(e)
	}
}

func main() {
	filePath := os.Args[1]
	readFile, err := os.Open(filePath)
	check(err)

	var word string
	var leftelf, rightelf string
	var leftelflow, leftelfhigh, rightelflow, rightelfhigh int
	var sum1 int
	var sum2 int

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		if fileScanner.Text() != "" {
			word = fileScanner.Text()
			PairSeparatorIndex := strings.IndexByte(word, ',')
			leftelf = word[:PairSeparatorIndex]
			rightelf = word[PairSeparatorIndex+1:]
			LeftRangeSeparatorIndex := strings.IndexByte(leftelf, '-')
			RightRangeSeparatorIndex := strings.IndexByte(rightelf, '-')
			leftelflow, _ = strconv.Atoi(leftelf[:LeftRangeSeparatorIndex])
			leftelfhigh, _ = strconv.Atoi(leftelf[LeftRangeSeparatorIndex+1:])
			rightelflow, _ = strconv.Atoi(rightelf[:RightRangeSeparatorIndex])
			rightelfhigh, _ = strconv.Atoi(rightelf[RightRangeSeparatorIndex+1:])
			if ((leftelflow >= rightelflow) && (leftelfhigh <= rightelfhigh)) || (rightelflow >= leftelflow) && (rightelfhigh <= leftelfhigh) {
				sum1++
			}
			if ((leftelflow >= rightelflow) && (leftelflow <= rightelfhigh)) ||
				((leftelfhigh >= rightelflow) && (leftelfhigh <= rightelfhigh)) ||
				((rightelflow >= leftelflow) && (rightelflow <= leftelfhigh)) ||
				((rightelfhigh >= leftelflow) && (rightelfhigh <= leftelfhigh)) {
				sum2++
			}
			fmt.Println(leftelflow, "*", leftelfhigh, " : ", rightelflow, "*", rightelfhigh)
		} else {
			fmt.Println("nothing")
		}
	}
	fmt.Printf("part one answer is = %d\npart two answer is = %d\n", sum1, sum2)

	readFile.Close()
}
