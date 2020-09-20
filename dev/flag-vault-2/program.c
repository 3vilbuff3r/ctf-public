#include <stdio.h>
#include <string.h>
#define LIMIT 32

int check_pass(char* input){
    char* flag = "\x09\x50\x5d\xda\xe6\x5e\x02\x68\xaa\xc5\xbd\x50\x26\x2c\xf2\xb0\x1e\x57\x60\x99";
    char* key = "\x64\x63\x6b\xef\x9d\x26\x32\x1a\xf5\xa0\xd3\x33\x54\x55\x82\xc4\x77\x38\x0e\xe4";
    char out[21] = {0};
    for(int i = 0; i < 20; i++){
        out[i] = flag[i] ^ key[i];
    }
    return strncmp(input, out, strlen(flag));
}
int main(){
    char input[LIMIT];
    printf("Enter Password to unlock vault:");
    fgets(input, LIMIT, stdin);
    if(check_pass(input) == 0){
        printf("You got it. Go submit it.");
    } else {
        printf("Nope, that ain't it. Try again.");
    }
}