package db

import (
	"database/sql"

	_ "github.com/lib/pq"
)

const dsn = "host=localhost port=5434 user=USER password=PASSWORD dbname=docker_psql_golang sslmode=disable"

func Open() (*sql.DB, error) {
	return sql.Open("postgres", dsn)
}
