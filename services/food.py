from database.db import DB
from utils.cors import MethodViewWithCors, cors


class FoodView(MethodViewWithCors):
    @cors
    def get(self):
        return DB, 200
