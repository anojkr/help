    #include<bits/stdc++.h>
     
    using namespace std;
     
    string PrimeDigitNumber (string N) {
     
       // Write your code here
       int number[N.length()],set = 0,k=N.length();
       //cout<<N.length();
       for(int i=N.length()-1;i>=0;i--)
       {
           number[i]=N[i]-'0';
       }
       
       for(int i=N.length()-1;i>=0;i--)
       {
           if(number[i]>=7)
           {
               N[i] ='7';
               if(number[i]>7)
               {
                   set = 1;
               }
           }else if(number[i]>=5)
           {
               N[i] ='5';
               
               if(number[i]>5)
               {
                   set = 1;
               }
           } else if(number[i]>=3)
           {
               N[i] ='3';
               if(number[i]>3)
               {
                   set = 1;
               }
           }else if(number[i]>=2)
           {
               
               N[i] ='2';
               
               if(number[i]>2)
               {
                   set = 1;
               }
           }else if(number[i]<2)
           {
               if(i==0)
               {
                   
                    for(int j = i+1;j<k;j++){
                        N[j] ='7';
                    }
                    k=i+1;
                    return N.substr(1);
                    break;
               }
               set = 1;
               N[i] ='7';
               number[i-1] =  number[i-1] -1;
           }
           if(set == 1){
               for(int j = i+1;j<k;j++){
                   N[j] ='7';
               }
               k=i+1;
               set = 0;
           }
       }
       
       return N;
    }
     
    int main() {
     
        ios::sync_with_stdio(0);
        cin.tie(0);
        string N;
        getline(cin, N);
     
        string out_;
        out_ = PrimeDigitNumber(N);
        cout << out_;
    }