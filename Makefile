# Variables
DB_FILE = mini_project1.db
SQL_INIT_FILE = setup.sql

# Default target
all: run

# Target to initialize the database
$(DB_FILE): $(SQL_INIT_FILE)
	@echo "Creating and setting up the database..."
	sqlite3 $(DB_FILE) < $(SQL_INIT_FILE)
	@echo "Database setup complete."

# Target to run the application
run: $(DB_FILE)
	@echo "Running the application..."
	python3 main.py

# Target to clean up the database file
clean:
	@echo "Cleaning up database..."
	rm -f $(DB_FILE)
	@echo "Database removed."

# Phony targets that don't represent files
.PHONY: all run clean