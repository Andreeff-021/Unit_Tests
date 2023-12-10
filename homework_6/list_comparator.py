class ListComparator:

    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def calculate_average(self, num_list):
        if len(num_list) > 0:
            return sum(num_list) / len(num_list)
        else:
            return 0

    def compare_lists(self):
        avg_1 = self.calculate_average(self.list_1)
        avg_2 = self.calculate_average(self.list_2)
        if avg_1 > avg_2:
            return "Первый список имеет большее среднее значение"
        elif avg_1 < avg_2:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"
