#include<stdio.h>
#include<stdlib.h>

void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
}

struct item {
    long int price;
    char *name;
};

int N = 20;
int idx = 0;
struct item *items[20];

void addItem() {
    if (idx == N) {
        puts("Our shop is full.");
        return;
    }

    items[idx] = malloc(sizeof(struct item));
    items[idx]->name = malloc(32);
    
    printf("Item name: ");
    scanf("%s", items[idx]->name);

    printf("Item price: ");
    scanf("%ld", &(items[idx]->price));

    idx++;
    puts("Item added successfully.");
}


void deleteItem() {
    if (idx == 0) {
        puts("Our shop is empty.");
        return;
    }
    printf("Item index (0 - %d): ", idx - 1);

    int deletedIdx;
    scanf("%d", &deletedIdx);
    if (deletedIdx < 0 || deletedIdx >= idx) {
        puts("Item index not found.");
        return;
    }

    free(items[deletedIdx]);

    for (int i = deletedIdx; i < idx; i++) {
        struct item *tmp = items[i];
        items[i] = items[i + 1];
        items[i + 1] = tmp;
    }

    idx--;
    puts("Item deleted successfully.");
}

void editItem() {
    if (idx == 0) {
        puts("Our shop is empty.");
        return;
    }
    printf("Item index (0 - %d): ", idx - 1);

    int editedIdx;
    scanf("%d", &editedIdx);
    if (editedIdx < 0 || editedIdx >= idx) {
        puts("Item index not found.");
        return;
    }

    printf("Item name: ");
    scanf("%s", items[editedIdx]->name);

    printf("Item price: ");
    scanf("%ld", &(items[editedIdx]->price));

    puts("Item edited successfully.");
}

void listItem() {
    puts("\n===========================================");
    puts("Item List");
    for (int i = 0; i < idx; i++) {
        printf("Name: %s\n", items[i]->name);
        printf("Price: %ld\n", items[i]->price);
        puts("");
    }
    puts("===========================================\n");
}

void sellItem() {
    if (idx == 0) {
        puts("Our shop is empty.");
        return;
    }
    printf("Item index (0 - %d): ", idx - 1);

    int sellIdx;
    scanf("%d", &sellIdx);
    if (sellIdx < 0 || sellIdx >= idx) {
        puts("Item index not found.");
        return;
    }

    char testimony[24];
    puts("What do you want to say about this item?");
    scanf("%65s", testimony);
    printf("You said: %s\n", testimony);

    free(items[sellIdx]);

    for (int i = sellIdx; i < idx; i++) {
        struct item *tmp = items[i];
        items[i] = items[i + 1];
        items[i + 1] = tmp;
    }

    idx--;
    puts("Item sold successfully.");
}

int menu() {
    puts("Menu:");
    puts("1. Add item");
    puts("2. Delete item");
    puts("3. Edit item");
    puts("4. List of added items");
    puts("5. Sell item");
    puts("6. Exit");
    printf("> ");
    

    char choice[3];
	fgets(choice, 3, stdin);
	return atoi(choice);
}

void greetings() {
    puts("Welcome to our shop :D");
    puts("You are our new manager.");
    puts("Your job is to fill our shop with new items and sell them.");
    puts("For now, you can add up to 20 items in your list.");
    puts("Good luck.");
}

int main(int argc, char const *argv[]) {
    init();
    greetings();

    while (1) {
        int choice = menu();
        if (choice == 1) {
            addItem();
        }
        if (choice == 2) {
            deleteItem();
        }
        if (choice == 3) {
            editItem();
        }
        if (choice == 4) {
            listItem();
        }
        if (choice == 5) {
            sellItem();
        }
        if (choice == 6) {
            puts("Bye.");
            exit(0);
        }
    }
}