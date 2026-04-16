# <img src="https://www.freetogame.com/assets/images/freetogame-logo.png" width="200" style="vertical-align:middle;" /> free_to_game.py

> Web API for [FreeToGame](https://www.freetogame.com) a free-to-play games database.

## Quick Start

```python
from free_to_game import FreeToGame

ftg = FreeToGame()
games = ftg.get_live_games()
```

## Usage

### Browse Games

```python
# All live games
ftg.get_live_games()

# Filter by platform
ftg.get_games_by_platform(platform="pc")
ftg.get_games_by_platform(platform="browser")

# Filter by category
ftg.get_games_by_category(category="shooter")
ftg.get_games_by_category(category="mmorpg")

# Sort results
ftg.sort_games(sort="release-date")
ftg.sort_games(sort="popularity")

# Filter by multiple criteria
ftg.get_games_by_all(platform="browser", category="mmorpg", sort="release-date")

# Advanced tag filtering
ftg.filter_game(tag="3d.mmorpg.fantasy.pvp", platform="pc")
```

### Game Details

```python
ftg.get_game_details(game_id=452)
```

## API Reference

| Method | Description |
|---|---|
| `get_live_games()` | Get all live games |
| `get_games_by_platform(platform)` | Filter games by platform (`pc`, `browser`) |
| `get_games_by_category(category)` | Filter games by category |
| `sort_games(sort)` | Sort games by criteria |
| `get_games_by_all(platform, category, sort)` | Filter and sort in one call |
| `get_game_details(game_id)` | Get details for a specific game |
| `filter_game(tag, platform)` | Filter by dot-separated tags |
