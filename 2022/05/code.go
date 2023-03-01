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
	filePath := os.Args[1]
	readFile, err := os.Open(filePath)
	check(err)

	var word string
	var linenumber1, linenumber2 int = 0, 0
	var numberofstacks int

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		if fileScanner.Text() != "" {
			word = fileScanner.Text()
			if string(word[1]) == "1" {
				numberofstacks = int(word[len(word)-2]) - 48
				break
			}
			linenumber1++
		} else {
			fmt.Println("nothing")
		}
	}

	stacks := make([][]string, 0)
	stacks2 := make([][]string, 0)

	_, err = readFile.Seek(0, 0)
	check(err)
	fileScanner = bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)
	tempstacks := make([][]string, 0)
	for fileScanner.Scan() {
		if fileScanner.Text() != "" {
			word = fileScanner.Text()
			linenumber2++
			if linenumber2 > linenumber1 {
				break
			}
			tempstack := make([]string, 0)
			for h := 0; h < len(word); h++ {
				tempstack = append(tempstack, string(word[h]))
			}
			tempstacks = append(tempstacks, [][]string{tempstack}...)
		}
	}
	for z := 0; z < numberofstacks; z++ {
		tempstack := make([]string, 0)
		for j := linenumber1 - 1; j >= 0; j-- {
			index := (z * 4) + 1
			boxname := string(tempstacks[j][index])
			if boxname != " " {
				tempstack = append(tempstack, boxname)
			}
		}
		stacks = append(stacks, [][]string{tempstack}...)
	}
	// repreated the process cause if added to the previous loop, it kept changing some of the stacks for unknown reasons.
	for z := 0; z < numberofstacks; z++ {
		tempstack := make([]string, 0)
		for j := linenumber1 - 1; j >= 0; j-- {
			index := (z * 4) + 1
			boxname := string(tempstacks[j][index])
			if boxname != " " {
				tempstack = append(tempstack, boxname)
			}
		}
		stacks2 = append(stacks2, [][]string{tempstack}...)
	}

	instrunctions := make([][]int, 0)
	for fileScanner.Scan() {
		if fileScanner.Text() != "" {
			word = fileScanner.Text()
			temp := make([]int, 0)
			var command int = 0
			if string(word[6]) != " " {
				command = ((int(word[5]) - 48) * 10) + (int(word[6]) - 48)
				temp = append(temp, command)
				command = int(word[13]) - 48
				temp = append(temp, command)
				command = int(word[18]) - 48
				temp = append(temp, command)
			} else {
				command = int(word[5]) - 48
				temp = append(temp, command)
				command = int(word[12]) - 48
				temp = append(temp, command)
				command = int(word[17]) - 48
				temp = append(temp, command)
			}
			instrunctions = append(instrunctions, [][]int{temp}...)
		}
	}

	for k := 0; k < len(instrunctions); k++ {
		for pop := 0; pop < instrunctions[k][0]; pop++ {
			from := instrunctions[k][1] - 1
			to := instrunctions[k][2] - 1
			object := stacks[from][len(stacks[from])-1]
			stacks[from] = stacks[from][:len(stacks[from])-1]
			stacks[to] = append(stacks[to], object)
		}
	}

	fmt.Println("part 1 results")
	for helia := 0; helia < numberofstacks; helia++ {
		fmt.Printf("%s", stacks[helia][len(stacks[helia])-1])
	}

	// fmt.Println("")
	// for i := 0; i < len(stacks2); i++ {
	// 	fmt.Println(stacks2[i])
	// }
	// fmt.Scanln()
	for k := 0; k < len(instrunctions); k++ {
		from := instrunctions[k][1] - 1
		to := instrunctions[k][2] - 1

		// fmt.Println("instructions:", instrunctions[k])
		// fmt.Println("from:", stacks2[from])
		// fmt.Println("to:  ", stacks2[to])

		object := stacks2[from][(len(stacks2[from]) - instrunctions[k][0]):]
		// fmt.Println("what:", object)

		for o := 0; o < instrunctions[k][0]; o++ {
			stacks2[to] = append(stacks2[to], string(object[o]))
		}

		stacks2[from] = stacks2[from][:(len(stacks2[from]) - instrunctions[k][0])]

		// fmt.Println("from:", stacks2[from])
		// fmt.Println("to:  ", stacks2[to])
		// fmt.Println("")
		// time.Sleep(2 * time.Second)
		// fmt.Scanln()
		// for line := 0; line < len(stacks2)+1; line++ {
		// 	fmt.Printf("\x1b[2K")
		// 	fmt.Printf("\033[1A")
		// 	fmt.Printf("\x1b[2K")
		// }
		// fmt.Println(instrunctions[k])
		// for i := 0; i < len(stacks2); i++ {
		// 	fmt.Println(stacks2[i])
		// }

	}
	// fmt.Println(stacks2)
	fmt.Println("\npart 2 results")
	for dana := 0; dana < numberofstacks; dana++ {
		fmt.Printf("%s", stacks2[dana][len(stacks2[dana])-1])
	}
	fmt.Println("")
	// fmt.Printf("numberofstacks = %d\nline number1 = %d\nline number2 = %d\n", numberofstacks, linenumber1, linenumber2)
	// fmt.Printf("part one answer is = %d\npart two answer is = %d\n", sum1, sum2)

	readFile.Close()

}
