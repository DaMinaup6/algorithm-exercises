# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()

# -----------------------------------------
# My Solution: Heap
#
# Space Complexity: O(n)
# -----------------------------------------
# q := number of queries
from collections import defaultdict
import heapq

class MovieRentingSystem:

    # -----> Time Complexity: O(nlog(n))
    def __init__(self, n: int, entries: List[List[int]]):
        # basic info
        self.shop_movie_map_price  = defaultdict(int)
        self.shop_movie_map_rented = defaultdict(bool)

        # we don't remove elements from heap immediately right after rent or drop so need to record if element already in heap or not
        # to prevent duplicated elements in heap
        self.movie_map_unrented_price_shops  = defaultdict(list)
        self.shop_movie_map_in_unrented_heap = defaultdict(bool)

        self.rented_movies_with_shop_price = [] # [(price, shop, movie)]
        self.shop_movie_map_in_rented_heap = defaultdict(bool)

        # entries[i] = [shop_i, movie_i, price_i]
        for shop, movie, price in entries:
            self.shop_movie_map_price[(shop, movie)] = price
            heapq.heappush(self.movie_map_unrented_price_shops[movie], (price, shop))
            self.shop_movie_map_in_unrented_heap[(shop, movie)] = True

    # -----> Time Complexity: Amortized O(log(n))
    def search(self, movie: int) -> List[int]:
        search_results = []
        while (len(self.movie_map_unrented_price_shops[movie]) > 0 and len(search_results) < 5):
            price, shop = heapq.heappop(self.movie_map_unrented_price_shops[movie])
            self.shop_movie_map_in_unrented_heap[(shop, movie)] = False

            # since we don't remove elements from heap immediately right after rent so only add info back to heap if unrented
            if not self.shop_movie_map_rented[(shop, movie)]:
                search_results.append(shop)

        for shop in search_results:
            self.add_unrented_shop_to_movie(shop, movie)

        return search_results

    # -----> Time Complexity: O(log(n))
    def rent(self, shop: int, movie: int) -> None:
        self.shop_movie_map_rented[(shop, movie)] = True
        if not self.shop_movie_map_in_rented_heap[(shop, movie)]:
            self.add_rented_movies_with_shop_price(shop, movie)

    # -----> Time Complexity: O(log(n))
    def drop(self, shop: int, movie: int) -> None:
        self.shop_movie_map_rented[(shop, movie)] = False
        if not self.shop_movie_map_in_unrented_heap[(shop, movie)]:
            self.add_unrented_shop_to_movie(shop, movie)

    # -----> Time Complexity: Amortized O(log(n))
    def report(self) -> List[List[int]]: # res[j] = [shop_j, movie_j]
        report_movies = []
        while (len(self.rented_movies_with_shop_price) > 0 and len(report_movies) < 5):
            price, shop, movie = heapq.heappop(self.rented_movies_with_shop_price)
            self.shop_movie_map_in_rented_heap[(shop, movie)] = False

            # since we don't remove elements from heap immediately right after drop so only add info back to heap if rented
            if self.shop_movie_map_rented[(shop, movie)]:
                report_movies.append([shop, movie])

        for shop, movie in report_movies:
            self.add_rented_movies_with_shop_price(shop, movie)

        return report_movies

    def add_unrented_shop_to_movie(self, shop, movie):
        price = self.shop_movie_map_price[(shop, movie)]
        heapq.heappush(self.movie_map_unrented_price_shops[movie], (price, shop))
        self.shop_movie_map_in_unrented_heap[(shop, movie)] = True

    def add_rented_movies_with_shop_price(self, shop, movie):
        price = self.shop_movie_map_price[(shop, movie)]
        heapq.heappush(self.rented_movies_with_shop_price, (price, shop, movie))
        self.shop_movie_map_in_rented_heap[(shop, movie)] = True
