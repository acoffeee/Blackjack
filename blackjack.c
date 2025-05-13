#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//int create_hand(int *);
//int card(int *);
int main() {
  int random_number;
  srand(time(NULL));
  int card(), create_hand();
  //int *dealer_cards, *player_cards;
  int *dealer_cards = (int*)calloc(sizeof(int), 2);
  int *player_cards = (int*)calloc(sizeof(int), 2);
  int i;
  i = 0;
  while (i <=1) {
      dealer_cards[i] = card();
      player_cards[i] = card();
      i++;
  };
  int prompt_cards(player_cards, dealer_cards);
  //printf("your cards: %d %d \n dealers cards: %d N", player_cards[0], player_cards[1], dealer_cards[0]);
  void choice();
  
  //printf("%d, %d, %d", *player_cards, *dealer_cards, dealer_cards[1]);
  return 0;
}
int prompt_cards(int player_cards,int dealer_cards) {
    int i = 0;
    int length = player_cards / sizeof(int);
    while (i<= player_cards;) {
        printf("%d", player_cards[i])
    };
    printf("\n dealer shown card: %d", *dealer_cards);
    return 0;
};
void choice() {
    printf("what would you like to do?\n 1. hit \n 2. call \n 3. 50/50 chance of me adding other functions");
    int choice;
    scanf("%d", choice);
    
    switch (choice) {
        case 1:
            //hit();
            break;
        case 2:
            //stand():
            break;
        default:
            printf("please try again");
            break;
            
    };
};

int card() {
    int card;
    card = (rand() % 11) + 1;
    return card;
};
