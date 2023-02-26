package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
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

	var sum, max1, max2, max3, elf_counter, elf int = 0, 0, 0, 0, 0, 0

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		if fileScanner.Text() != "" {
			intVar, _ := strconv.Atoi(fileScanner.Text())
			// fmt.Println(intVar, err, reflect.TypeOf(intVar))
			sum += intVar
			// fmt.Println(fileScanner.Text())
		} else {
			elf_counter++
			fmt.Printf("\n%d sum is = %d", elf_counter, sum)
			if sum > max1 {
				max3 = max2
				max2 = max1
				max1 = sum
				elf = elf_counter
			} else if sum > max2 {
				max3 = max2
				max2 = sum
			} else if sum > max3 {
				max3 = sum
			}
			sum = 0
		}
	}
	fmt.Printf("\nmax1 = %d by number %d\nmax2 = %d\nmax3 = %d\nsum of max = %d\n", max1, elf, max2, max3, max1+max2+max3)

	readFile.Close()
}
