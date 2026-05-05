package main

import (
	"fmt"
	"log"
	"os"

	"github.com/suma-web/hc-practice/internal/app"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: go run ./cmd/importer <logfile>")
		os.Exit(1)
	}

	if err := app.ImportLogs(os.Args[1]); err != nil {
		log.Fatal(err)
	}

	fmt.Println("All inserts committed successfully")
}
