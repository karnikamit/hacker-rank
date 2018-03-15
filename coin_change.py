# -*- coding: utf-8 -*-
__author__ = "karnikamit"


class Coins(object):
    def __init__(self, value, no_coins, coins_list):
        """

        :param (int) value: money value
        :param (int) no_coins: number of coins
        :param (list) coins_list: coins available
        """
        self.value = value
        self.coins_list = coins_list
        assert no_coins == len(self.coins_list)
        self.result_list = []

    def get_coins(self, coin):
        """

        :param (int) coin:
        :return (int) coins: number of coins required for the value
        """
        return_value = []
        if not self.value % coin:
            return_value = [coin] * (self.value / coin)
        return return_value

    @staticmethod
    def get_greater_coin(coin1, coin2):
        """
        :return: greater coin, lesser coin
        """
        if coin1 > coin2:
            return coin1, coin2
        return coin2, coin1

    def get_coin_combination_list(self, greater_coin, lesser_coin):
        temp = [greater_coin]
        while greater_coin < self.value:
            greater_coin += lesser_coin
            if greater_coin <= self.value:
                temp.append(lesser_coin)
        return temp

    def get_combination(self, coin1, coins):
        """

        :param (int) coin1: present coin
        :param (list) coins: remaining coins
        :return (list): list of coin combinations equaling to value
        """
        coins_combination = []
        for coin2 in coins:
            greater_coin, lesser_coin = self.get_greater_coin(coin1, coin2)
            temp = self.get_coin_combination_list(greater_coin, lesser_coin)
            if sum(temp) == self.value:
                coins_combination.append(temp)
        return coins_combination

    def main(self):
        for coin in self.coins_list:
            same_coins = self.get_coins(coin)
            if same_coins and same_coins not in self.result_list:
                self.result_list.append(same_coins)
            temp_coins = self.coins_list[::]
            temp_coins.remove(coin)
            coins_combi = self.get_combination(coin, temp_coins)
            for combi in coins_combi:
                if combi and combi not in self.result_list:
                    self.result_list.append(combi)
        return len(self.result_list)


c = Coins(10, 2, [7, 2])
print c.main()
# OP 5
# TODO Handle multiple coin combination
