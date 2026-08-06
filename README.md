# Anime Manager

A console application for managing a personal anime collection.

The application allows users to add, delete, search, edit, sort, and filter anime. All data is stored locally in a JSON file.

## Features

- Add anime
- Delete anime
- Search anime by title
- Edit anime information
- View anime list
- Sort anime by:
  - title
  - personal rating
  - status
- Filter anime by:
  - rating
  - status

## Anime Statuses

Available statuses:

- Watched
- Watching
- Planned to watch
- Dropped

## Technologies

- Python 3
- JSON
- pathlib

## Project Structure

```
Anime-manager/
│
├── src/
│   ├── main.py
│   ├── operations.py
│   ├── storage.py
│   ├── ui.py
│   └── utils.py
│
├── anime.json
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone <repository_url>
```

Navigate to the project folder:

```bash
cd Anime manager
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Run:

```bash
python src/main.py
```

## Data Storage

Anime information is stored in `anime.json`.

Example:

```json
{
  "title": "Attack on Titan",
  "status": "Watched",
  "personal_rating": 10,
  "review": "Amazing story"
}
```

## Future Improvements

- Add database support
- Add graphical interface
- Improve validation system

## Author

Nikita