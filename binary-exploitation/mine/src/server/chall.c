#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include <time.h>
#define GROUND 0
#define COPPER 1
#define SILVER 2
#define GOLD 3
#define SPECIAL 4
#define LADDER 5
#define MAPROWSIZE 20
#define MAPCOLSIZE 20
#define BONUSLEVEL 1000000000

int stamina = 100;
int map[MAPROWSIZE][MAPCOLSIZE];
int digged[MAPROWSIZE][MAPCOLSIZE];
int i, j;
int choice;

void win() {
    system("cat flag.txt");
}

void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
    srand(time(NULL));
}

void greetings() {
    puts("Welcome to the entrance of The Mine.");
    puts("Something special is waiting for you in the highest level.");
    puts("Go dig deep and deeper to find it out!");
}

void checkStamina() {
    if (stamina == 0) {
        puts("You ran out of stamina!");
        exit(0);
    }
}

void generateMap(unsigned int level) {
    memset(map, 0, sizeof(map));
    memset(digged, 0, sizeof(digged));

    i = random() % MAPROWSIZE;
    j = random() % MAPCOLSIZE;
    int ladderRow = random() % MAPROWSIZE;
    int ladderCol = random() % MAPCOLSIZE;
    while (ladderRow == i && ladderCol ==  j) {
        ladderRow = random() % MAPROWSIZE;
        ladderCol = random() % MAPCOLSIZE;
    }
    map[ladderRow][ladderCol] = LADDER;

    if (level < BONUSLEVEL) {    
        for (int row = 0; row < MAPROWSIZE; row++) {
            for (int col = 0; col < MAPCOLSIZE; col++) {
                if (row == i && col == j) {
                    continue;
                }
                if (map[row][col] == GROUND) {
                    int tmp = random() % 12;
                    if (tmp < 6) {
                        map[row][col] = GROUND;
                    } else if (tmp < 9) {
                        map[row][col] = COPPER;
                    } else if (tmp < 11) {
                        map[row][col] = SILVER;
                    } else {
                        map[row][col] = GOLD;
                    }
                }
            }
        }
    } else {
        for (int row = 0; row < MAPROWSIZE; row++) {
            for (int col = 0; col < MAPCOLSIZE; col++) {
                if (row == i && col == j) {
                    continue;
                }
                if (map[row][col] == GROUND) {
                    int tmp = random() % 12;
                    if (tmp < 6) {
                        map[row][col] = GROUND;
                    } else {
                        map[row][col] = SPECIAL;
                    }
                }
            }
        }
    }
}

void menu1() {
    puts("\nMenu:");
    puts("1. Enter The Mine");
    puts("2. Exit");
    printf("> ");
    
	scanf("%d", &choice);
}

void menu2() {
    puts("\nMenu:");
    if (digged[i][j] == 0) {
        puts("1. Go up");
        puts("2. Go right");
        puts("3. Go down");
        puts("4. Go left");
        puts("5. Dig");
        puts("6. Exit the mine");
    } else {
        if (map[i][j] == GROUND) {
            puts("1. Go up");
            puts("2. Go right");
            puts("3. Go down");
            puts("4. Go left");
            puts("5. Exit the mine");
        } else {
            puts("1. Go to the next level");
            puts("2. Go to the previous level");
            puts("3. Exit the mine");
        }
    }
    printf("> ");
    
	scanf("%d", &choice);
}

int checkInsideMap(int i, int j) {
    if (0 <= i && i < MAPROWSIZE && 0 <= j && j < MAPCOLSIZE) {
        return 1;
    }
    return 0;
}

typedef struct {
    char tmp[8];
    unsigned int level;
    int basketCnt;
    char basket[10][8];
} MineData;

void mine() {
    MineData mineData;
    mineData.basketCnt = 0;
    mineData.level = 1;
    memset(mineData.tmp, 0, sizeof(mineData.tmp));
    generateMap(mineData.level);
    printf("Welcome to level %u\n", mineData.level);

    while (1) {
        checkStamina();
        printf("\nStamina: %d\n", stamina);
        printf("Position: row = %d, col = %d\n", i, j);
        printf("You have %d item(s) in the basket.\n", mineData.basketCnt);
        menu2();

        if (digged[i][j] == 0) {
            if (choice == 1) {
                if (checkInsideMap(i - 1, j) == 0) {
                    puts("You cannot go there.");
                } else {
                    i--;
                }
            } else if (choice == 2) {
                if (checkInsideMap(i, j + 1) == 0) {
                    puts("You cannot go there.");
                } else {
                    j++;
                }
            } else if (choice == 3) {
                if (checkInsideMap(i + 1, j) == 0) {
                    puts("You cannot go there.");
                } else {
                    i++;
                }
            } else if (choice == 4) {
                if (checkInsideMap(i, j - 1) == 0) {
                    puts("You cannot go there.");
                } else {
                    j--;
                }
            } else if (choice == 5) {
                puts("Digging...");
                stamina--;
                digged[i][j] = 1;
                
                if (map[i][j] == LADDER) {
                    puts("You find a ladder!");
                } else {
                    if (map[i][j] == COPPER) {
                        puts("You find a copper!");
                    } else if (map[i][j] == SILVER) {
                        puts("You find a silver!");
                    } else if (map[i][j] == GOLD) {
                        puts("You find a gold!");
                    } else if (map[i][j] == SPECIAL) {
                        puts("You find a special item!");
                        puts("Here is a gift for you because you find a special item:");
                        printf("%p\n", &win);
                    } else {
                        puts("Nothing here.");
                    }
                    if (map[i][j] != GROUND) {
                        printf("Want to put this in the basket? (1/0): ");
                        scanf("%d", &choice);
                        if (choice == 1) {
                            printf("Want to give your newly found mineral a name? (1/0): ");
                            scanf("%d", &choice);
                            if (choice == 1) {
                                printf("Name: ");
                                scanf("%8s", mineData.tmp);
                                strncpy(mineData.basket[mineData.basketCnt], mineData.tmp, 8);
                                printf("You put %s to the basket.", mineData.tmp);
                            }
                            mineData.basketCnt++;
                        }
                    }
                    map[i][j] = GROUND;
                }
            } else if (choice == 6) {
                break;
            }
        } else {
            if (map[i][j] == GROUND) {
                if (choice == 1) {
                    if (checkInsideMap(i - 1, j) == 0) {
                        puts("You cannot go there.");
                    } else {
                        i--;
                    }
                } else if (choice == 2) {
                    if (checkInsideMap(i, j + 1) == 0) {
                        puts("You cannot go there.");
                    } else {
                        j++;
                    }
                } else if (choice == 3) {
                    if (checkInsideMap(i + 1, j) == 0) {
                        puts("You cannot go there.");
                    } else {
                        i++;
                    }
                } else if (choice == 4) {
                    if (checkInsideMap(i, j - 1) == 0) {
                        puts("You cannot go there.");
                    } else {
                        j--;
                    }
                } else if (choice == 5) {
                    break;
                }
            } else if (map[i][j] == LADDER) {
                if (choice == 1) {
                    mineData.level++;
                    generateMap(mineData.level);
                    printf("Welcome to level %u\n", mineData.level);
                } else if (choice == 2) {
                    mineData.level--;
                    if (mineData.level == 0) {
                        break;
                    }
                    generateMap(mineData.level);
                    printf("Welcome to level %u\n", mineData.level);
                } else if (choice == 3) {
                    break;
                }
            }
        }
    }
}

int main() {
    init();
    greetings();

    while (1) {
        menu1();
        if (choice == 1) {
            mine();
        } else if (choice == 2) {
            puts("Bye.");
            exit(0);
        }
        stamina++;
    }
}