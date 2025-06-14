/**
 * 验证C++的函数传值传的是值的拷贝，而不是值的本身
 */

 #include <iostream>
 #include <vector>
 #include <unordered_map>
 #include <cstdint>
 
 using namespace std;
 
 // 测试代码
 intptr_t changeValue(int* ptr) {
    return reinterpret_cast<intptr_t>(&ptr);
}

intptr_t changeValue(int x1) {
    return reinterpret_cast<intptr_t>(&x1);
}

int main() {
    int x = 10;
    int* p = &x;
    cout << "指针地址是否相同：" << (reinterpret_cast<intptr_t>(&p) == changeValue(p))  << endl;
    cout << "值的地址是否相同：" << (changeValue(x) == reinterpret_cast<intptr_t>(&x)) << endl;
}