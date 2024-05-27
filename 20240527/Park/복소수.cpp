#include <iostream>
#include <cmath>
#include <fstream>
#include <cstdlib>
using namespace std;

class myComplex
{
public:
    // 생성자 (Constructor)
    myComplex(int real = 0, int imag = 0);
    // 복사 생성자 (Copy constructor)
    myComplex(const myComplex &number);

    // 접근자 (Accessor functions)
    int getRealPart() const;
    int getImaginaryPart() const;

    // 변경자 (Mutator functions)
    void setRealPart(int real);
    void setImaginaryPart(int imag);
    void set(int real, int imag);

    // 이항연산자 오버로딩 (Overloaded binary operator)
    myComplex operator+(const myComplex &number) const;
    myComplex operator+(int value) const;
    myComplex operator-(const myComplex &number) const;
    myComplex operator-(int value) const;
    myComplex operator*(const myComplex &number) const;
    myComplex operator*(int value) const;

    // Overloaded assignment operators
    myComplex &operator=(const myComplex &number);
    myComplex &operator=(int value);
    myComplex &operator+=(const myComplex &number);
    myComplex &operator+=(int value);
    myComplex &operator-=(const myComplex &number);
    myComplex &operator-=(int value);
    myComplex &operator*=(const myComplex &number);
    myComplex &operator*=(int value);

    // 관계연산자 오버로딩 (Overladed relational operators)
    bool operator==(const myComplex &number) const;
    bool operator!=(const myComplex &number) const;
    bool operator>(const myComplex &number) const;
    bool operator>=(const myComplex &number) const;
    bool operator<(const myComplex &number) const;
    bool operator<=(const myComplex &number) const;

    // 단항연산자 오버로딩 (Overloaded unary operators)
    myComplex operator-();
    myComplex operator~();
    myComplex &operator++();
    myComplex &operator--();
    myComplex operator++(int);
    myComplex operator--(int);

private:
    int realPart;
    int imaginaryPart;
    double norm() const;

    friend ostream &operator<<(ostream &outStream, const myComplex &number);
    friend istream &operator>>(istream &inStream, myComplex &number);
    friend myComplex operator+(int value, const myComplex &number);
    friend myComplex operator-(int value, const myComplex &number);
    friend myComplex operator*(int value, const myComplex &number);
};

// 생성자 (Constructor)
myComplex::myComplex(int real, int imag)
{
    realPart = real;
    imaginaryPart = imag;
}

// 복사 생성자 (Copy constructor)
myComplex::myComplex(const myComplex &number)
{
    realPart = number.realPart;
    imaginaryPart = number.imaginaryPart;
}

// 접근자 (Accessor functions)
int myComplex::getRealPart() const
{
    return realPart;
}

int myComplex::getImaginaryPart() const
{
    return imaginaryPart;
}

// 변경자 (Mutator functions)
void myComplex::setRealPart(int real)
{
    realPart = real;
}

void myComplex::setImaginaryPart(int imag)
{
    imaginaryPart = imag;
}

void myComplex::set(int real, int imag)
{
    realPart = real;
    imaginaryPart = imag;
}

// 이항연산자 오버로딩 (Overloaded binary operator)
myComplex myComplex::operator+(const myComplex &number) const
{
    return myComplex(realPart + number.realPart, imaginaryPart + number.imaginaryPart);
}

myComplex myComplex::operator+(int value) const
{
    return myComplex(realPart + value, imaginaryPart);
}

myComplex myComplex::operator-(const myComplex &number) const
{
    return myComplex(realPart - number.realPart, imaginaryPart - number.imaginaryPart);
}

myComplex myComplex::operator-(int value) const
{
    return myComplex(realPart - value, imaginaryPart);
}

myComplex myComplex::operator*(const myComplex &number) const
{
    return myComplex(realPart * number.realPart - imaginaryPart * number.imaginaryPart,
                     realPart * number.imaginaryPart + imaginaryPart * number.realPart);
}

myComplex myComplex::operator*(int value) const
{
    return myComplex(realPart * value, imaginaryPart * value);
}

// Overloaded assignment operators
myComplex &myComplex::operator=(const myComplex &number)
{
    if (this == &number)
    {
        return *this;
    }
    realPart = number.realPart;
    imaginaryPart = number.imaginaryPart;
    return *this;
}

myComplex &myComplex::operator=(int value)
{
    realPart = value;
    imaginaryPart = 0;
    return *this;
}

myComplex &myComplex::operator+=(const myComplex &number)
{
    realPart += number.realPart;
    imaginaryPart += number.imaginaryPart;
    return *this;
}

myComplex &myComplex::operator+=(int value)
{
    realPart += value;
    return *this;
}

myComplex &myComplex::operator-=(const myComplex &number)
{
    realPart -= number.realPart;
    imaginaryPart -= number.imaginaryPart;
    return *this;
}

myComplex &myComplex::operator-=(int value)
{
    realPart -= value;
    return *this;
}

myComplex &myComplex::operator*=(const myComplex &number)
{
    int r = realPart * number.realPart - imaginaryPart * number.imaginaryPart;
    int i = realPart * number.imaginaryPart + imaginaryPart * number.realPart;
    realPart = r;
    imaginaryPart = i;
    return *this;
}

myComplex &myComplex::operator*=(int value)
{
    realPart *= value;
    imaginaryPart *= value;
    return *this;
}

// 관계연산자 오버로딩 (Overladed relational operators)
bool myComplex::operator==(const myComplex &number) const
{
    return (realPart == number.realPart) && (imaginaryPart == number.imaginaryPart);
}

bool myComplex::operator!=(const myComplex &number) const
{
    return !(*this == number);
}

bool myComplex::operator>(const myComplex &number) const
{
    return norm() > number.norm();
}

bool myComplex::operator>=(const myComplex &number) const
{
    return norm() >= number.norm();
}

bool myComplex::operator<(const myComplex &number) const
{
    return norm() < number.norm();
}

bool myComplex::operator<=(const myComplex &number) const
{
    return norm() <= number.norm();
}

// 단항연산자 오버로딩 (Overloaded unary operators)
myComplex myComplex::operator-()
{
    return myComplex(-realPart, -imaginaryPart);
}

myComplex myComplex::operator~()
{
    return myComplex(realPart, -imaginaryPart);
}

myComplex &myComplex::operator++()
{
    realPart++;
    return *this;
}

myComplex &myComplex::operator--()
{
    realPart--;
    return *this;
}

myComplex myComplex::operator++(int)
{
    myComplex tmp(*this);
    realPart++;
    return tmp;
}

myComplex myComplex::operator--(int)
{
    myComplex tmp(*this);
    realPart--;
    return tmp;
}

// private 함수들
double myComplex::norm() const
{
    return sqrt(realPart * realPart + imaginaryPart * imaginaryPart);
}

// 입출력 연산자 오버로딩
ostream &operator<<(ostream &outStream, const myComplex &number)
{
    outStream << "(" << number.realPart << "," << number.imaginaryPart << ")";
    return outStream;
}

istream &operator>>(istream &isStream, myComplex &number)
{
    isStream >> number.realPart >> number.imaginaryPart;
    return isStream;
}

myComplex operator+(int value, const myComplex &number)
{
    return myComplex(value) + number;
}

myComplex operator-(int value, const myComplex &number)
{
    return myComplex(value) - number;
}

myComplex operator*(int value, const myComplex &number)
{
    return myComplex(value) * number;
}

void testSimpleCase();
void testDataFromFile();

int main(void)
{
    testSimpleCase();
    testDataFromFile();
    return 0;
}

void testSimpleCase()
{
    myComplex c0, c1(1), c2(2, 2);
    myComplex c3(c2);
    myComplex c4, c5, c6, c7, c8, c9;

    // test constructor
    cout << c0 << endl
         << c1 << endl
         << c2 << endl;
    // test copy constructor
    cout << c3 << endl;
    // test accessor function
    cout << c3 << endl;
    // test mutator function
    c3.set(3, 3);
    cout << c3 << endl;
    c3.setRealPart(4);
    cout << c3 << endl;
    c3.setImaginaryPart(4);
    cout << c3 << endl;
    // test binary operators
    c4 = c1 + c3;
    c5 = c1 - c3;
    c6 = c4 * c5;
    cout << c4 << endl
         << c5 << endl
         << c6 << endl;
    c7 = c6 + 2;
    c8 = c6 - 2;
    c9 = c6 * 2;
    cout << c7 << endl
         << c8 << endl
         << c9 << endl;
    c7 += c4;
    c8 -= c5;
    c9 *= c6;
    cout << c7 << endl
         << c8 << endl
         << c9 << endl;
    c7 += 2;
    c8 -= 2;
    c9 *= 2;
    cout << c7 << endl
         << c8 << endl
         << c9 << endl;
    // test comparison operators
    cout << (c8 != c9) << " " << (c8 == c9) << endl;
    cout << (c8 > c9) << " " << (c8 >= c9) << " " << (c8 < c9) << " " << (c8 <= c9) << endl;
    c7 = c8 = c9;
    cout << (c8 != c9) << " " << (c8 == c9) << endl;
    cout << (c8 > c9) << " " << (c8 >= c9) << " " << (c8 < c9) << " " << (c8 <= c9) << endl;
    // test prefix operators
    c7 = -myComplex(2, 3);
    c8 = (++c7) * 2;
    c9 = 2 * (c7++);
    cout << c7 << " " << c8 << " " << c9 << endl;
    c7 = ~myComplex(2, 3);
    c8 = (--c7) * 2;
    c9 = 2 * (c7--);
    cout << c7 << " " << c8 << " " << c9 << endl;
    // test expressions with myComplex numbers
    c1 = myComplex(1, 2);
    c2 = myComplex(2, 3);
    c3 = myComplex(4, 5);
    c4 = myComplex(5, 6);
    c5 = myComplex(6, 7);
    c6 = 3;
    cout << -(c1 * c2) - 2 * c3 + ~c4 * c5 * 3 + 2 - c6 << endl;
}

void testDataFromFile()
{
    ifstream inStream;
    int numTestCases;
    inStream.open("input.txt");
    if (inStream.fail())
    {
        cerr << "Input file opening failed.\n";
        exit(1);
    }
    inStream >> numTestCases;
    for (int i = 0; i < numTestCases; i++)
    {
        myComplex c1, c2, c3, c4;
        myComplex c5, c6, c7, c8, c9;
        inStream >> c1 >> c2 >> c3 >> c4;
        cout << c1 << " " << c2 << " " << c3 << " " << c4 << endl;
        cout << (2 + c1 + 3) + (2 - c2 - 3) * (2 * c3 * 3) - (2 * c4 - 3) << endl;
        c5 = c6 = c7 = c8 = c1;
        cout << (c5 == c2) << " " << (c5 != c2) << endl;
        cout << (c5 > c2) << " " << (c5 >= c2) << " " << (c5 < c2) << " " << (c5 <= c2) << endl;
        cout << (c5 == c6) << " " << (c5 != c6) << endl;
        cout << (c5 > c6) << " " << (c5 >= c6) << " " << (c5 < c6) << " " << (c5 <= c6) << endl;
        c5 += c2;
        c6 -= c3;
        c7 *= c4;
        c8 = c2.getRealPart();
        c9 = c3.getImaginaryPart();
        cout << c5 << " " << c6 << " " << c7 << " " << c8 << " " << c9 << endl;
        c7 = -c6;
        c8 = (++c7) * 2;
        c9 = 2 * (c7++);
        cout << c7 << " " << c8 << " " << c9 << endl;
        c7 = ~c6;
        c8 = (++c7) * 2;
        c9 = 2 * (c7++);
        cout << c7 << " " << c8 << " " << c9 << endl;
    }
    inStream.close();
}
