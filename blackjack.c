#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//int create_hand(int *);
//int card(int *);
int main() {
  int random_number;
  srand(time(NULL));
  int card();
  int *dealer_cards = (int*)malloc(2*sizeof(int));
  int *player_cards = (int*)malloc(2*sizeof(int));
  *dealer_cards = card();
  *player_cards = card();
  printf("%d, %d", *player_cards, dealer_cards);
  return 0;
}
int card() {
    int card;
    card = (rand() % 11) + 1;
    return card;
};
