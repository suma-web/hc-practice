package db

import (
	"database/sql"
	"errors"
	"fmt"
	"os"

	"github.com/joho/godotenv"
	_ "github.com/lib/pq"
)


func Open() (*sql.DB, error) {
	// Load .env for local runs (ignore when not present in prod).
	_ = godotenv.Load()

	requiredKeys := []string{
		"DB_HOST",
		"DB_PORT",
		"DB_USER",
		"DB_PASSWORD",
		"DB_NAME",
		"DB_SSLMODE",
	}
	for _, key := range requiredKeys {
		if os.Getenv(key) == "" {
			return nil, errors.New("missing required environment variable: " + key)
		}
	}

	dsn := fmt.Sprintf(
		"host=%s port=%s user=%s password=%s dbname=%s sslmode=%s",
		os.Getenv("DB_HOST"),
		os.Getenv("DB_PORT"),
		os.Getenv("DB_USER"),
		os.Getenv("DB_PASSWORD"),
		os.Getenv("DB_NAME"),
		os.Getenv("DB_SSLMODE"),
	)
	return sql.Open("postgres", dsn)
}

func CreateUsersTable(conn *sql.DB) error {
	_, err := conn.Exec(`
		CREATE TABLE IF NOT EXISTS users (
			id SERIAL PRIMARY KEY,
			age INTEGER NOT NULL,
			name TEXT NOT NULL,
			role TEXT NOT NULL
		)
	`)
	return err
}