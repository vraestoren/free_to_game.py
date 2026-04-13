from requests import Session

class FreeToGame:
	def __init__(self) -> None:
		self.api = "https://www.freetogame.com/api"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Linux; Android 11; RMX2086 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36"
		}
   

	def _get(self, endpoint: str, params: dict = {}) -> dict:
		return self.session.get(
			f"{self.api}{endpoint}", params=params).json()
		
	def get_live_games(self) -> dict:
		return self._get("/games")
	
	def get_games_by_platform(
			self, platform: str = "pc") -> dict:
		params = {
			"platform": platform
		}
		return self._get("/games", params)
	
	def get_games_by_category(
			self, category: str = "shooter") -> dict:
		params = {
			"category": category
		}
		return self._get("/games", params)
	
	def sort_games(self, sort: str) -> dict:
		params = {
			"sort-by": sort
		}
		return self._get("/games", params)
	
	def get_games_by_all(
			self,
			platform: str = "browser",
			category: str = "mmorpg",
			sort: str = "release-date") -> dict:
		params = {
			"platform": platform,
			"category": category,
			"sort-by": sort
		}
		return self._get("/games", params)
		
	def get_game_details(self, game_id: int) -> dict:
		params = {
			"id": game_id
		}
		return self._get("/games", params)
	
	def filter_game(
			self,
			tag: str = "3d.mmorpg.fantasy.pvp",
			platform: str = "pc") -> dict:
		params = {
			"tag": tag,
			"platform": platform
		}
		return self._get("/filter", params)
