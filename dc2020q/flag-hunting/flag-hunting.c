#include <stdio.h>
#include <stdlib.h>
#define FLAG_LEN 58

struct node {
    int ch; // 0
    int cnt; // 4
    int depth; // 8
    //int pad;
    struct node * left; // 0x10
    struct node * right; // 0x18
};

int main(int argc, char ** argv){
    int i;
    char buf[FLAG_LEN + 1];
    int flag_len;

    for(i = 0; i <= 0x3b; i++)
        buf[i] = '\0';
    FILE *fp = fopen64(argv[1]);
    fread(buf, 1, 0x3c, fp);
    flag_len = get_flag_len(buf);// call 20686067138f49f491686da3dd11d1b1
    if(flag_len <= 0) // test in 4db7e59a6cab53ffe3bda0ded5f455f1
        ;//donno error?
    // flag len not equal test in 5c2d01f8616d9938d927db8b677a62eb-> jump to 29d4435c533a85c664456391da4189ed (0x555555554d51)
    gen_tree(buf, flag_len);// call 2a0711617c98b163d5d86699a4f7fc88

    
}


// subroutine 1b64d9cc243c25e429b5cca3c5e66c8b (0x555555554b98)
// called by main
int get_flag_len(char * buf/*rdi*/){ 
    int i = 0; // [rbp-0x4]
    char c; // rax
    // loop start fbe9faf6eb3e018ea5c1a2d8957ea6b4 0x555555554c28
    while((c = buf[i]) == '\0') { // test in 498d98ba90c430d0f012f350033f7ae5
        if(c == "}"){ // test in 8f5ba8691065becc3bb510d218e9a68f
            return i;
        }
        // not } 7c2b589f2cb59449f6996db5b9b31091 (0x555555554bc5)
        else if(c == "O"){// test in 124c245d4eabdfc2fa79cdc8f35268c5
            i++; //cd97512d07efe7aa3271311a5a343e98 (0x555555554bed)
        }
        else if(c == " "){ // test in 3f28186b89062ddd3716da6e41c6d15e
            i++;
        }
        // not " " (maybe ff94cb7cc26a5ea981ecba65ff4a46bc) (0x555555554bf3)
        else if(c > 0x60 && c <= 0x7b){ // [lower case + {] check in 66ff401c5c0e441728088f871c99f8bf
            i++;
        }
        else{ // error ? 0x555555554c21
            ;//donno
        }

    } 
    // loop end 0x555555554ba9
}

//subroutine bb9cc4afceb13f7385ca1ada5a386eb2 (0x555555554b31)
void gen_tree(char * buf, int len){
    /*
    66650ec45089b5cb43024d2b9aef78f5 mov QWORD PTR [rbp-0x18],rdi
    e90957e2ad35b2579f5d0f8c0d7543e6 mov DWORD PTR [rbp-0x1c],esi
    2e616ad9acc8024a9cfa3c0d6e6b4923 mov QWORD PTR [rbp-0x8],0x0
    e3608558cf7d71ffbba5d4b8b624dda9 mov DWORD PTR [rbp-0xc],0x0
    */
    int i;// 0xc
    struct node * st_ptr; //0x8
    char c; //rax
    //loop start 68bd83cd39496671142802448466d5cf (0x555555554b7a)
    while(i <= len) {// test in c055aa34f247a78975f4698490418014 
        c = buf[i];
        st_ptr = insert_node(st_ptr, c); // call ca5ab312e8886c46a899368f61547e0b
        i++;
    }
    //loop end 0x555555554b51
    print_node(st_ptr); //call dd4a4de0774ae7445a38ff9d0fb2bb70
}

//subroutine d670e25f0b1e4b298321e687f777ec14 (0x555555554954)
// nested called by f2
struct node * insert_node(struct node * a, int c){ 
    // c in [rbp-0xc], st_ptr in [rbp-0x8]
    struct node * st_ptr = a;//rax
    if(a == 0){// test in 0bca589eb2bdab13fc6510db9f78bc45
        // a is zero, 7e8d3d12f9987acc83634394bb225179
        st_ptr = make_node(c);// call 3451c5a6ba2ffdb8e245446115e5ea11
        return st_ptr; //return 035619afe13a4b106de53674a406125f
    }
    else{
        // a is nonzero, 62c2cd053dfa2c78589308e078cb3740
        if (st_ptr->ch != c){// test in 75cb9102252003130f34c1868b880e80
            // not equal, e1e3ec730b3d9aca7cc552d86413a373 (0x55555555499d)
            if(c >= st_ptr->ch) {// test in c8f426f59afa2865488b57a2831ff5b6
                //jge taken, c622d85d8eac36de71a2da9b7c141eec 0x5555555549ce
                st_ptr->right = insert_node(st_ptr->right, c); //a2648a849526903f1553126aa4119b79
            }
            // not jge, 5f694f9d4d0ea82638f21bae6503ee8c
            else if(c <= st_ptr->ch) { // test in 147d1876f6fb6972436bcd96bf1d2f17
                //jle, e6918d0d6ce05fead702b9b15f995eb3 (0x5555555549fd)
                st_ptr->left= insert_node(st_ptr->left, c);  // 9fd18c435279a11cc106c4933676a7d9
            }
            /*5c365a9be9d344f23cf83434377b32f1 mov rax,QWORD PTR [rbp-0x8]
            5bfce57c46d719473911896d64e8d767 mov eax,DWORD PTR [rax]
            c8f426f59afa2865488b57a2831ff5b6 cmp edx,eax
            c6da03fb51bc6a158efcda7c7bd491c3 jge 0x5555555549ce
            5f694f9d4d0ea82638f21bae6503ee8c movsx edx,BYTE PTR [rbp-0xc]
            c23e7603b844a7b0c0b484ac1b5a3fbe mov rax,QWORD PTR [rbp-0x8]
            9263633f8946f9fd6fe29a1b744698e2 mov eax,DWORD PTR [rax]
            147d1876f6fb6972436bcd96bf1d2f17 cmp edx,eax
            4b191ce185bce3bc951ebb28fbea3cab jle 0x5555555549fd
            e6918d0d6ce05fead702b9b15f995eb3 movsx edx,BYTE PTR [rbp-0xc]
            1b49e0db8c3fc339122dade721d00538 mov rax,QWORD PTR [rbp-0x8]
            e7dc04f329e817f3adc2ba521f6347fe mov rax,QWORD PTR [rax+0x18]
            64e79e00bcdef6896d98a5a7cca76a97 mov esi,edx
            b5432679e3f6c75bc66fad3604983784 mov rdi,rax
            a2648a849526903f1553126aa4119b79 call 0x555555554954*/
        }
        else{
            //equal, b39fabb14ca48dfa222944f6b24fff4b (via OOO)
            /*
            fd0ee7ba6fc0792269664ab855f65f66 mov eax,DWORD PTR [rax+0x4]
            7b49c2cba9528b1e0f63c75367b13be4 lea edx,[rax+0x1]
            244894dc026e8c8788d9ce5f4c201377 mov rax,QWORD PTR [rbp-0x8]
            998316bd2eb99e250f9bd5e6ab38720f mov DWORD PTR [rax+0x4],edx
            */
            st_ptr->ch += 1;
        }
        st_ptr = rotate_left(st_ptr); // 83558aaf42e5b6c58859338ad3e67ec6
        st_ptr = rotate_right(st_ptr);
        // idk what this node stands for. fxxk ds
        return st_ptr; //return 035619afe13a4b106de53674a406125f
    }
    // not equal (0x55555555497c)
}

//subroutine b58310a1d83b616fca1491b8ddaa4051 (0x55555555481a)
// nested called by f3
struct node * make_struct(int c){
    struct node * st_ptr = malloc(sizeof(struct node)); // 0x20 with pad
    /*
    e48bb2b249e29029dcfedd87f37ef96e mov QWORD PTR [rbp-0x8],rax
    04c9b7c627c5720ffaac396ff2ebe75b mov rax,QWORD PTR [rbp-0x8]
    6624ee53c02de99b3544b4d862bc5450 mov edx,DWORD PTR [rbp-0x14]
    1a659c221aae07f59745a7569cbff667 mov DWORD PTR [rax],edx
    c472bda6b7d69acc2c79cd7c8c131c84 mov rax,QWORD PTR [rbp-0x8]
    2bace30c1836c5ffa9810b093f57c4e1 mov QWORD PTR [rax+0x10],0x0
    4aa68f6d2cc17489f850b13b8a664b14 mov rax,QWORD PTR [rbp-0x8]
    0ebbaef4775e907ce76db5ef8f7eb01f mov QWORD PTR [rax+0x18],0x0
    67137b52239902c417d1604dbfe00af2 mov rax,QWORD PTR [rbp-0x8]
    3e6d2b87d522414ee84abb63c7df80d5 mov DWORD PTR [rax+0x8],0x1
    a58ea2aa6dd28a2d8572b6642c469cbd mov rax,QWORD PTR [rbp-0x8]
    5f410c6e5753042095803f8bb1b35b7a mov DWORD PTR [rax+0x4],0x1
    b1a36760bf05b012e34b9c9b235fe735 mov rax,QWORD PTR [rbp-0x8]
    */
    st_ptr->ch = c;
    st_ptr->cnt = 1;
    st_ptr->depth = 1;

    st_ptr->left = 0;
    st_ptr->right = 0;
    return st_ptr; // return 3d2780ae16ad8e2b889d4e6bd96e184a
}

//subroutine 83be5e65d5010b6ce1fd4da060e07888 (0x555555554870)
// nested called by f3
struct node * rotate_left(struct node * ptr){
    if(ptr->left== 0) { // test in 435df3d33fc8b844387998f0a0b4cb1a
        //equal, 3f22294678ad1d8370ac9af2a3313c8f (0x5555555548c9)
        return ptr; // return dcbbcb5adba5bad2455abdb581562cf1
    }
    else{
        //not equal, 72740ca10ff290d30652b7b96433e230
        if(ptr->left->depth == ptr->depth){//test in 0997c9d5280dfd357bf2095997a40f66
            //not equal, 0x5555555548c9 3f22294678ad1d8370ac9af2a3313c8f (0x5555555548c9)
            return ptr; // return dcbbcb5adba5bad2455abdb581562cf1
        }
        else{
            struct node * tmp= ptr->left;
            ptr->left = tmp->right;
            tmp->right = ptr;
            //todo
        }
    }
}

//subroutine 1f7aa429199eac8a7c6017e9e57df7fc (0x5555555548cf)
// nested called by f3
struct node * rotate_rigth(struct node * ptr){
    if(ptr->right == 0) { // test in 1924ea13917ecc82ff4a198c792f81b8
    }
    else{
        //not equal, 04608c8c42945be650a05ad604ed4e59 (0x55555555494e)
        if(ptr->right->right == 0) { // test in 3f85036e520339d32ced394d2e6a80db
        } 
        else{
            if(ptr->right->right->depth == ptr->depth){
                return ptr;
            }
            else{
                //57c4fb55862a54ce50f667af48b390e7
                struct node * tmp = ptr->right;
                ptr->right = tmp->left;
                //todo
            } 
        }
    }
    //equal, 40e0f0d7c4a81e18cc330857a716b6b0 (0x55555555494e)
    return ptr; // return cf5f0b33655019af58d902ef007338f9
}

//subroutine 05ac00e1e7aae89912d1ee1d234e3f19 (0x555555554a23)
// nested called by gen_tree
void print_node(struct node * n){
    if(n == 0) {// test in 302516a6643756848a3cf572de673677
        //end, b293bbfa9e7fe427413f71aac870b8ee (0x555555554a76)
        return ;
    }
    else{
        print_node(n->right);
        printf("%s",n->ch);
        print_node(n->left);
    }
}