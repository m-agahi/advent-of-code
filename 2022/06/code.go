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

	var word string

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		word = fileScanner.Text()
		do(word)
	}
	readFile.Close()

}
func do(word string) {
	var packet_check [4]string
	var message_check [14]string
	var equals bool = false
	var index1, index2 int

	debug(word)

	for i := 0; i < 4; i++ {
		packet_check[i] = string(word[i])
	}
	for i := 0; i < 14; i++ {
		message_check[i] = string(word[i])
	}

	for i := 4; i < len(word); i++ {
		for j := 0; j < 4; j++ {
			for k := j + 1; k < 4; k++ {
				if packet_check[j] == packet_check[k] {
					equals = true
				}
			}
		}
		if equals == false {
			index1 = i
			break
		}
		equals = false
		for j := 0; j < 3; j++ {
			packet_check[j] = packet_check[j+1]
		}
		packet_check[3] = string(word[i])
	}

	for i := 14; i < len(word); i++ {
		for j := 0; j < 14; j++ {
			for k := j + 1; k < 14; k++ {
				if message_check[j] == message_check[k] {
					equals = true
				}
			}
		}
		if equals == false {
			index2 = i
			break
		}
		equals = false
		for j := 0; j < 13; j++ {
			message_check[j] = message_check[j+1]
		}
		message_check[13] = string(word[i])
	}

	fmt.Println("part 1 results: ", index1)
	fmt.Println("part 2 results", index2)
}
