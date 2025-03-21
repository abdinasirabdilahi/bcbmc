#include "acode.h"
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h> 
// generate an unpredictable 6-digit code 
// use OS rng + pairwise independent hash function
int gen_auth_code() {
    int urand = open("/dev/urandom",O_RDONLY);
    long randseed = 0;
    // want exactly 6 digit code
    while (randseed > 999999 || randseed < 100000) {
        // read one long int
        read(urand, &randseed, 1);
        // Make it extra random with hash function
        randseed = (randseed * 0xa3d7 + 0xd3ad) % 0xFFFFF;
    }
    close(urand);
    return randseed;
}

int main(){
    for(int i = 0; i < 10000; i++){
        printf("%d\n", gen_auth_code());
    }
}
