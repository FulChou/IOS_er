#include<iostream>
#include<string>
#include<stack>
#include<cctype>

using namespace std;

int getPriority(char x){
    switch (x)
    {
    case '#': return 0;
        break;
    case '$': return 1;
        break;
    case '+': return 2;
        break;
    case '-': return 2;
        break;
    case '*': return 3;
        break;
    case '/': return 3;
        break;
    default: return 0;
        break;
    }
}
double caculate(double x,double y,char opt){
    if(opt=='+'){
        return x+y;
    }else if(opt=='-'){
        return x-y;
    }else if(opt=='*'){
        return x*y;
    }else if (opt=='/'){
        return x/y;
    }else return 0;
}
double getNumber(string str,int & index){ // 引用传递，不是值传递（复制）
    double data=0;
    while (isdigit(str[index]))
    {
        data = data*10+(str[index]-'0');
        index++;
    }
    return data;
}

int main(){
    string str;
    while(getline(cin,str)){
        stack<double> num;
        stack<char> opt;
        str+='$';
        opt.push('#');
        int index = 0;
        while (index<str.size())    
        {
            if (isdigit(str[index]))
            {
                num.push(getNumber(str,index));
            }else{
                if(getPriority(str[index])>getPriority(opt.top())){
                    opt.push(str[index]);
                    //cout<<opt.top()<<endl;
                    index++;
                }else{// 开始做计算：
                        char optx = opt.top();
                        opt.pop();
                        double y = num.top(); //先pop出来的操作数是第二个
                        num.pop();
                        double x = num.top();
                        num.pop();
                        //cout<<x<<" "<<y<<"result:";

                        num.push(caculate(x,y,optx));
                        //cout<<num.top()<<endl;
                }
            }
            
        }
        printf("%d",(int)num.top());
        
    }

    return 0;
}