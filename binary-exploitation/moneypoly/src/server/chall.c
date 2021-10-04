#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include <time.h>
#define PLAYER 0
#define COMPUTER 1
#define OWNERLESS -1

void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
    srand(time(NULL));
}

char houseName[40][39] = {"\0"};
int inJailCnt[2] = {0, 0};
int haveName[40];
int money[2];
int position[2];
int isInJail[2];

int mapSize = 40;
char mapType[40][15];
char mapName[40][39];
int mapPrice[40];
int rentPrice[40];
int diceSeed = 0;
int diceNow;
int owner[40];
int turnNow = COMPUTER;

void checkWin() {
    if (money[PLAYER] < 0) {
        puts("Computer wins.");
        exit(0);
    }
    if (money[COMPUTER] < 0) {
        puts("Congratulations, You win!");
        exit(0);
    }
}

void initMap() {
    FILE *fp = fopen("map.txt", "r");

    if (fp == NULL) {
        perror("File not found!\n");
        exit(1);
    }

    char ch;
    char type[30] = {'\0'};
    char name[30] = {'\0'};
    char price[5] = {'\0'};
    int now = 0;
    int cnt = 0;
    int i = 0;
    while((ch = fgetc(fp))!= EOF) {
        if (ch == ',') {
            now++;
            cnt = 0;
            continue;
        } else if (ch == '\n') {
            strcpy(mapType[i], type);
            strcpy(mapName[i], name);
            mapPrice[i] = atoi(price);
            owner[i] = OWNERLESS;
            rentPrice[i] = mapPrice[i] / 4;
            haveName[i] = 0;
            i++;

            memset(type, 0, sizeof(type));
            memset(name, 0, sizeof(name));
            memset(price, 0, sizeof(price));

            now = 0;
            cnt = 0;
            continue;
        }

        if (now == 0) {
            type[cnt++] = ch;
        } else if (now == 1) {
            name[cnt++] = ch;
        } else {
            price[cnt++] = ch;
        }
    }

    fclose(fp);

    for (int i = 0; i < 2; i++) {
        isInJail[i] = 0;
        inJailCnt[i] = 0;
        position[i] = 0;
        money[i] = 500;
    }
}

int getDiceNumber() {
    int fullDice = 12;
    int dice;
    int correction = 1;
    long newDice;
    long newRandom = random();
    diceSeed %= 12;
    if (dice > 0) {
        newDice = (long)(((dice % fullDice) + diceSeed++) % fullDice) + correction;
    } else {
        newDice = (long)((newRandom) % fullDice) + correction;
    }
    return (int)newDice;
}

void chance() {
    int tmp = rand() % 400 - 199;
    if (turnNow == COMPUTER) {
        puts("Computer lands on CHANCE.");
        if (tmp < 0) {
            printf("The Bank fined Computer $%d.\n", -1 * tmp);
        } else {
            printf("The Bank gives Computer $%d.\n", tmp);
        }
        money[turnNow] += tmp;
    } else {
        puts("You land on CHANCE.");
        if (tmp < 0) {
            printf("The Bank fined You $%d.\n", -1 * tmp);
        } else {
            printf("The Bank gives You $%d.\n", tmp);
        }
        money[turnNow] += tmp;
    }
}

void buySomething() {
    if (turnNow == COMPUTER) {
        printf("Computer lands on %s.\n", mapName[position[turnNow]]);

        if (owner[position[turnNow]] == turnNow) {
            if ((rand() % 2 == 1) && (mapPrice[position[turnNow]] / 2 <= money[turnNow]) && (strncmp(mapType[position[turnNow]], "HOUSE", 5) == 0)) {
                money[turnNow] -= mapPrice[position[turnNow]] / 2;
                rentPrice[position[turnNow]] += mapPrice[position[turnNow]] / 5;
                printf("Computer upgrades its house, rent price = $%d.\n", rentPrice[position[turnNow]]);
            }
        } else if ((rand() % 2 == 1) && (mapPrice[position[turnNow]] <= money[turnNow])) {
            money[turnNow] -= mapPrice[position[turnNow]];
            owner[position[turnNow]] = COMPUTER;
            printf("Computer buys %s with price $%d, rent price = $%d.\n", mapName[position[turnNow]], mapPrice[position[turnNow]], rentPrice[position[turnNow]]);
        }
    } else {
        printf("You land on %s.\n", mapName[position[turnNow]]);
        if (owner[position[turnNow]] == turnNow) {
            printf("You are the owner of this property.\n");
            if (strncmp(mapType[position[turnNow]], "HOUSE", 5) == 0) {
                printf("Do you want to upgrade your house for $%d? (1/0): ", mapPrice[position[turnNow]] / 2);
                int tmp;
                scanf("%d", &tmp);
                if (tmp == 1) {
                    if (mapPrice[position[turnNow]] / 2 <= money[turnNow]) {
                        money[turnNow] -= mapPrice[position[turnNow]] / 2;
                        rentPrice[position[turnNow]] += mapPrice[position[turnNow]] / 5;
                        printf("You upgrade your house, rent price = $%d.\n", rentPrice[position[turnNow]]);
                    } else {
                        puts("You don\'t have enough money.");
                    }
                }
            }
        } else {
            printf("Do you want to buy this property (price $%d, rent price = $%d)? (1/0): ", mapPrice[position[turnNow]], rentPrice[position[turnNow]]);
            int tmp;
            scanf("%d", &tmp);
            if (tmp == 1) {
                if (mapPrice[position[turnNow]] <= money[turnNow]) {
                    owner[position[turnNow]] = PLAYER;
                    money[turnNow] -= mapPrice[position[turnNow]];
                    printf("You buy %s with price $%d, rent price = $%d.\n", mapName[position[turnNow]], mapPrice[position[turnNow]], rentPrice[position[turnNow]]);
                } else {
                    puts("You don\'t have enough money.");
                }
            }
        }
    }
}

void jail() {
    isInJail[turnNow] = 1;
    inJailCnt[turnNow]++;
    if (turnNow == COMPUTER) {
        printf("Computer caught in jail. Fine = $%d.\n", mapPrice[position[turnNow]]);
    } else {
        printf("You caught in jail. Fine = $%d.\n", mapPrice[position[turnNow]]);
        if (inJailCnt[turnNow] == 1) {
            printf("Have any words?\n> ");
            char yourWords[64];
            scanf("%64s", yourWords);
            printf("You said: ");
            printf(yourWords);
            printf("\n");
        }
    }
    money[turnNow] -= mapPrice[position[turnNow]];
}

void pay() {
    if (turnNow == COMPUTER) {
        printf("Computer lands on your property, %s. It pays $%d to You.\n", mapName[position[turnNow]], rentPrice[position[turnNow]]);
    } else {
        printf("You land on Computer's property, %s. You pay $%d to Computer.\n", mapName[position[turnNow]], rentPrice[position[turnNow]]);
    }
    
    money[owner[position[turnNow]]] += rentPrice[position[turnNow]];
    money[turnNow] -= rentPrice[position[turnNow]];
}

void expense() {
    if (turnNow == COMPUTER) {
        printf("Computer lands on %s. It pays $%d to The Bank.\n", mapName[position[turnNow]], mapPrice[position[turnNow]]);
    } else {
        printf("You land on %s. You pay $%d to The Bank.\n", mapName[position[turnNow]], mapPrice[position[turnNow]]);
    }

    money[turnNow] -= mapPrice[position[turnNow]];
}

void income() {
    if (turnNow == COMPUTER) {
        printf("Computer lands on %s. The Bank gives $%d to Computer.\n", mapName[position[turnNow]], mapPrice[position[turnNow]]);
    } else {
        printf("You land on %s. The Bank gives $%d to You.\n", mapName[position[turnNow]], mapPrice[position[turnNow]]);
    }

    money[turnNow] += mapPrice[position[turnNow]];
}

void freeParking() {
    if (turnNow == COMPUTER) {
        puts("Computer lands on FREE PARKING.");
        diceNow = rand() % 39 + 1;
    } else {
        puts("You land on FREE PARKING.");
        printf("How many steps do You want to take? (1 - 39): ");
        int tmp;
        scanf("%d", &tmp);
        diceNow = tmp % 39 + 1;
    }

    int cnt = 0;
    while (cnt < diceNow) {
        position[turnNow]++;
        position[turnNow] %= mapSize;
        cnt++;
        if (strncmp(mapName[position[turnNow]], "START LINE", 10) == 0) {
            if (turnNow == COMPUTER) {
                puts("The Bank gives Computer $200.");
            } else {
                puts("The Bank gives You $200.");
            }
            money[turnNow] += mapPrice[position[turnNow]];
        }
    }

    if ((strncmp(mapType[position[turnNow]], "INCOME", 6) == 0) && (strncmp(mapName[position[turnNow]], "START LINE", 10) != 0)) {
        income();
    }
    if (strncmp(mapType[position[turnNow]], "EXPENSE", 7) == 0) {
        expense();
    }
    if (strncmp(mapType[position[turnNow]], "JAIL", 4) == 0) {
        jail();
    }
    if ((strncmp(mapType[position[turnNow]], "HOUSE", 5) == 0) || (strncmp(mapType[position[turnNow]], "COMPANY", 7) == 0)) {
        if (owner[position[turnNow] != OWNERLESS]) {
            buySomething();
        } else if (owner[position[turnNow]] != turnNow) {
            pay();
        }
    }
    if (strncmp(mapType[position[turnNow]], "CHANCE", 6) == 0) {
        chance();
    }

    if (diceNow != 12) {
        if (turnNow == COMPUTER) {
            turnNow = PLAYER;
        } else {
            turnNow = COMPUTER;
        }
    }
}

void move() {
    if (turnNow == COMPUTER) {
        printf("Computer rolled %d.\n", diceNow);
    } else {
        printf("You rolled %d.\n", diceNow);
    }

    if (isInJail[turnNow] == 1) {
        if (diceNow < 6) {
            if (turnNow == COMPUTER) {
                puts("Computer can't move. It needs 6 or more to get out from the jail.");
            } else {
                puts("You can't move. You need 6 or more to get out from the jail.");
            }
            return;
        }
        isInJail[turnNow] = 0;
        if (turnNow == COMPUTER) {
            puts("Computer gets out from the jail.");
        } else {
            puts("You get out from the jail.");
        }
    }

    int cnt = 0;
    while (cnt < diceNow) {
        position[turnNow]++;
        position[turnNow] %= mapSize;
        cnt++;
        if (strncmp(mapName[position[turnNow]], "START LINE", 10) == 0) {
            puts("The Bank gives You $200.");
            money[turnNow] += mapPrice[position[turnNow]];
        }
    }

    if ((strncmp(mapType[position[turnNow]], "INCOME", 6) == 0) && (strncmp(mapName[position[turnNow]], "START LINE", 10) != 0)) {
        income();
    }
    if (strncmp(mapType[position[turnNow]], "EXPENSE", 7) == 0) {
        expense();
    }
    if (strncmp(mapType[position[turnNow]], "JAIL", 4) == 0) {
        jail();
    }
    if ((strncmp(mapType[position[turnNow]], "HOUSE", 5) == 0) || (strncmp(mapType[position[turnNow]], "COMPANY", 7) == 0)) {
        if (owner[position[turnNow] != OWNERLESS]) {
            buySomething();
        } else if (owner[position[turnNow]] != turnNow) {
            pay();
        }
    }
    if (strncmp(mapType[position[turnNow]], "CHANCE", 6) == 0) {
        chance();
    }
    if (strncmp(mapType[position[turnNow]], "PARK", 4) == 0) {
        freeParking();
    }
}

void nextTurn() {
    move();
    if (diceNow != 12) {
        if (turnNow == COMPUTER) {
            turnNow = PLAYER;
        } else {
            turnNow = COMPUTER;
        }
    }
}

int menu() {
    puts("\nMenu:");
    puts("1. Next turn");
    puts("2. Computer status");
    puts("3. Your status");
    puts("4. Exit");
    printf("> ");
    
    int choice;
	scanf("%d", &choice);
	return choice;
}

void greetings() {
    puts("Moneypoly board game. The first one to have money (assets not included) below zero, lose.");
    puts("As a player, you can buy an ownerless property if you have enough money, get a free parking, or have a chance to get more money.");
    puts("Be careful to not land on computer's property, jail, or any kind of disadvantegous things!");
}

void computerStatus() {
    puts("===== COMPUTER STATUS =====");
    printf("Money = $%d\n", money[COMPUTER]);
    printf("Position = %s\n", mapName[position[COMPUTER]]);
    puts("");
    puts("Property list:");

    int cnt = 0;
    for (int i = 0; i < mapSize; i++) {
        if (owner[i] == COMPUTER) {
            printf("%d. %s, rent price = $%d\n", ++cnt, mapName[i], rentPrice[i]);
        }
    }
    if (cnt == 0) {
        puts("- Computer doesn't have any property right now.");
    }

    puts("===========================");
}

void playerStatus() {
    puts("======= YOUR STATUS =======");
    printf("Money = $%d\n", money[PLAYER]);
    printf("Position = %s\n", mapName[position[PLAYER]]);
    puts("");
    puts("Property list:");

    int cnt = 0;
    for (int i = 0; i < mapSize; i++) {
        if (owner[i] == PLAYER) {
            if (haveName[i] == 0) {
                printf("%d. %s, rent price = $%d\n", ++cnt, mapName[i], rentPrice[i]);
            } else {
                printf("%d. %s (a.k.a. %s), rent price = $%d\n", ++cnt, mapName[i], houseName[i], rentPrice[i]);
            }
        }
    }

    if (cnt == 0) {
        puts("- You don't have any property right now.");
    } else {
        printf("As a special feature, would you like to give your house a name? (1/0): ");
        int tmp;
        scanf("%d", &tmp);
        if (tmp == 1) {
            printf("Which property you want to set the name?\n> ");
            scanf("%d", &tmp);
            int x = 0, found = 0, i;
            for (i = 0; i < mapSize; i++) {
                if (owner[i] == PLAYER) {
                    x++;
                }
                if (x == tmp) {
                    found = 1;
                    break;
                }
            }
            if (found == 0) {
                puts("Property not found.");
            } else {
                printf("New name: ");
                char newHouseName[39];
                scanf("%39s", newHouseName);
                strcpy(houseName[i], newHouseName);
                haveName[i] = 1;
            }
        }
    }

    puts("===========================");
}

int main() {
    init();
    initMap();
    greetings();

    while (1) {
        diceNow = getDiceNumber();
        checkWin();
        int choice = menu();
        if (choice == 1) {
            nextTurn();
        }
        if (choice == 2) {
            computerStatus();
        }
        if (choice == 3) {
            playerStatus();
        }
        if (choice == 4) {
            puts("Bye.");
            exit(0);
        }
    }
}