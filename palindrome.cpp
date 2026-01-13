#include<iostream>
using namespace std;


class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0)
            return false;
        int n=x;
        
        long long rev=0;
        while (n>0){
            int digit=n%10;
            rev=rev*10+digit;
            n=n/10;
        }
         return x==rev;
    }
};
int main(){
    Solution obj;
    int x;
    cout<<"Enter any number:";
    cin>>x;

    if (obj.isPalindrome(x))
        cout << x << " is a palindrome" << endl;
    else
        cout << x << " is not a palindrome" << endl;

    return 0;

}
