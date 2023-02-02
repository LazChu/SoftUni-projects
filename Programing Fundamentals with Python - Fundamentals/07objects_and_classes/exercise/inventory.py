class Inventory:
    __capacity = 0

    def __init__(self, __capacity: int):
        self.items = []
        self.__capacity = __capacity

    def add_item(self, item: str):
        if self.__capacity > 0:
            self.items.append(item)
            self.__capacity -= 1
            Inventory.__capacity +=1
        return "not enough room in the inventory"

    def get_capacity(self):
        return Inventory.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.__capacity}"
