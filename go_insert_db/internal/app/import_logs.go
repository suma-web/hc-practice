package app

import (
	"bufio"
	"encoding/json"
	"os"

	"github.com/suma-web/hc-practice/internal/db"
	"github.com/suma-web/hc-practice/internal/model"
)

func ImportLogs(filePath string) (err error) {
	file, err := os.Open(filePath)
	if err != nil {
		return err
	}
	defer file.Close()

	conn, err := db.Open()
	if err != nil {
		return err
	}
	defer conn.Close()

	tx, err := conn.Begin()
	if err != nil {
		return err
	}
	defer func() {
		if err != nil {
			_ = tx.Rollback()
		}
	}()

	stmt, err := tx.Prepare(`
		INSERT INTO users (age, name, role)
		VALUES ($1, $2, $3)
	`)
	if err != nil {
		return err
	}
	defer stmt.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		var logData model.Log
		if err = json.Unmarshal(scanner.Bytes(), &logData); err != nil {
			return err
		}

		if _, err = stmt.Exec(logData.User.Age, logData.User.Name, logData.User.Role); err != nil {
			return err
		}
	}

	if err = scanner.Err(); err != nil {
		return err
	}

	return tx.Commit()
}
