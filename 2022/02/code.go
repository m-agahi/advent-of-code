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

func main() {

	readFile, err := os.Open("./puzzle.txt")
	check(err)

	var elfC, meC, word string = "", "", ""

	var elf, me1, me2, score1, score2, sum1, sum2 int = 0, 0, 0, 0, 0, 0, 0

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		if fileScanner.Text() != "" {
			word = fileScanner.Text()
			elfC = string([]rune(word)[0])
			meC = string([]rune(word)[2])
			switch elfC {
			case "A":
				elf = 1
			case "B":
				elf = 2
			case "C":
				elf = 3
			}
			switch meC {
			case "X":
				me1 = 1
				score2 = 0
			case "Y":
				me1 = 2
				score2 = 3
			case "Z":
				me1 = 3
				score2 = 6
			}
			if (me1 == 1 && elf == 3) || (me1 == 2 && elf == 1) || (me1 == 3 && elf == 2) {
				score1 = 6
			} else if me1 == elf {
				score1 = 3
			} else {
				score1 = 0
			}
			if (score2 == 0 && elf == 1) || (score2 == 3 && elf == 3) || (score2 == 6 && elf == 2) {
				me2 = 3
			} else if (score2 == 0 && elf == 3) || (score2 == 3 && elf == 2) || (score2 == 6 && elf == 1) {
				me2 = 2
			} else {
				me2 = 1
			}
			sum1 += score1 + me1
			sum2 += score2 + me2
			fmt.Printf("%d - %d - %d - %d\n", elf, me1, score1, score2)
			score1, me1, elf, score2, me2 = 0, 0, 0, 0, 0
		} else {
			fmt.Println("nothing")
		}
	}
	fmt.Printf("part one answer is = %d\npart two answer is = %d\n", sum1, sum2)

	readFile.Close()
}
