class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """
        Определяет победившую фракцию в сенате Dota2.

        Параметры:
        senate (str): Строка, где 'R' - Radiant, 'D' - Dire

        Возвращает:
        str: "Radiant" или "Dire" - победившая фракция

        Примеры:
        >>> predictPartyVictory("RD")
        "Radiant"  # Сенатор R(0) запрещает D(1), остается только R

        >>> predictPartyVictory("RDD")
        "Dire"     # Процесс:
                    # 1. R(0) запрещает D(1)
                    # 2. D(2) запрещает R(0)
                    # 3. D(2) запрещает D(1) - но D(1) уже запрещен
                    # Остается только D(2)
        """

        # Инициализируем две очереди для каждой фракции
        radiant = deque()  # Очередь для сенаторов Radiant
        dire = deque()  # Очередь для сенаторов Dire
        n = len(senate)  # Общее количество сенаторов

        # Заполняем очереди начальными индексами сенаторов
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)  # Добавляем индекс Radiant
            else:
                dire.append(i)  # Добавляем индекс Dire

        # Моделируем процесс голосования, пока есть оба типа сенаторов
        while radiant and dire:
            # Берем первых сенаторов из каждой очереди
            r = radiant.popleft()  # Текущий сенатор Radiant
            d = dire.popleft()  # Текущий сенатор Dire

            # Сравниваем их позиции - кто голосует первым
            if r < d:
                # Radiant голосует первым, запрещает Dire
                # Добавляем Radiant в конец очереди с индексом +n для следующего раунда
                radiant.append(r + n)
                # Пример: для "RDD" при r=0, d=1:
                # radiant становится [0+3=3], dire []
            else:
                # Dire голосует первым, запрещает Radiant
                # Добавляем Dire в конец очереди с индексом +n
                dire.append(d + n)
                # Пример: для "DR" при d=0, r=1:
                # dire становится [0+2=2], radiant []

        # Определяем победителя - какая очередь не пуста
        return "Radiant" if radiant else "Dire"