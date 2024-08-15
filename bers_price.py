#!/usr/bin/python3
import pandas as pd
import os
import sys

cards = {}
card_prices = {}
set_dict = {}
total_info = {}
order_num = 0

def read_card_prices():
 global card_prices, set_dict, total_info
 data = pd.read_csv('prices_bers.txt', sep='\t')
 for row in data.itertuples():
  card_prices[row[3].strip().lower()] = [row[2].strip(), row[5].strip(), row[6].strip(), row[7].strip().split(' ')[0]]
  if row[2].strip() not in set_dict:
   set_dict[row[2].strip()] = []
  if row[2].strip() not in total_info:
   total_info[row[2].strip()] = [0, 0]


def read_cards_file(file_name):
 global cards, order_num
 with open(file_name, "r") as file:
  contents = file.readlines()

 for line in contents:
  line = line.strip()
  if line:
   if line not in cards:
    cards[line] = [1, file_name, order_num]
    order_num += 1
   else:
    cards[line][0] +=1

def print_cards_prices():
 global cards, card_prices, set_dict, total_info
 errors = []
 for card_name in cards.keys():
  card_name_l = card_name.lower()
  if card_name_l in card_prices:
   set_name = card_prices[card_name_l][0]
   total_info[set_name][0] += cards[card_name][0]
   total_info[set_name][1] += cards[card_name][0]*int(card_prices[card_name_l][3])
   set_dict[set_name].append(str(cards[card_name][0])+'; '+card_name+'; '+card_prices[card_name_l][2]+'; '+card_prices[card_name_l][3])
  else:
   errors.append((card_name, cards[card_name]))
 
 for set_name in set_dict.keys():
  print(set_name+':')
  for line in set_dict[set_name]:
   print(line)
  print('')
 print('Всего карт и стоимость:');
 for set_name in total_info.keys():
  print(set_name+': '+str(total_info[set_name][0])+' : '+str(total_info[set_name][1])+' руб')
 print('')
 
 print('Не найдены карты:')
 for err in errors:
  print(err)
  

def main():
 read_card_prices()
 for filename in sys.argv[1:]:
  read_cards_file(filename)
 print_cards_prices()

if __name__ == "__main__":
 main()
 
