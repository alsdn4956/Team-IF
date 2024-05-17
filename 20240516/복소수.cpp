#include <iostream>
#include <cmath>
using namespace std;

class myComplex
{
public:
    // Constructor
    myComplex(int real = 0, int imag = 0);

    // Copy constructor
    myComplex(const myComplex &number);

    // Accessor functions
    int getRealPart() const;
    int getImaginaryPart() const;

    // Mutator functions
    void setRealPart(int real);
    void setImaginaryPart(int imag);
    void set(int real, int imag);

    // Overloaded binary operators
    myComplex operator+(const myComplex &number) const;
    myComplex operator+(int value) const;
    myComplex operator-(const myComplex &number) const;
    myComplex operator-(int value) const;
    myComplex operator*(const myComplex &number) const;

    // Overloaded assignment operators
    myComplex &operator=(const myComplex &number);
    myComplex &operator=(int value);
    myComplex &operator+=(const myComplex &number);
    myComplex &operator-=(const myComplex &number);
    myComplex &operator*=(const myComplex &number);

    // Overloading relational operators
    bool operator==(const myComplex &number) const;
    bool operator!=(const myComplex &number) const;
    bool operator>(const myComplex &number) const;
    bool operator>=(const myComplex &number) const;
    bool operator<(const myComplex &number) const;
    bool operator<=(const myComplex &number) const;

    // Overloaded unary operators
    myComplex operator-(); // unary minus
    myComplex operator~();
    myComplex operator++();
    myComplex operator++(int);
    myComplex operator--();
    myComplex operator--(int);

    // Friend functions for input/output
    friend ostream &operator<<(ostream &outStream, const myComplex &number);
    friend istream &operator>>(istream &inStream, myComplex &number);
    friend myComplex operator+(int value, const myComplex &number);
    friend myComplex operator-(int value, const myComplex &number);
    friend myComplex operator*(int value, const myComplex &number);

private:
    int realPart;
    int imaginaryPart;
    int norm() const;
};

// Constructor
myComplex::myComplex(int real, int imag) : realPart(real), imaginaryPart(imag) {}

// Copy constructor
myComplex::myComplex(const myComplex &number) : realPart(number.realPart), imaginaryPart(number.imaginaryPart) {}

// Accessor functions
int myComplex::getRealPart() const
{
    return realPart;
}

int myComplex::getImaginaryPart() const
{
    return imaginaryPart;
}

// Mutator functions
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

// Overloaded binary operators
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
    return myComplex(realPart * number.realPart - imaginaryPart * number.imaginaryPart, realPart * number.imaginaryPart + imaginaryPart * number.realPart);
}

// Assignment operators
myComplex &myComplex::operator=(const myComplex &number)
{
    if (this != &number)
    {
        realPart = number.realPart;
        imaginaryPart = number.imaginaryPart;
    }
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

myComplex &myComplex::operator-=(const myComplex &number)
{
    realPart -= number.realPart;
    imaginaryPart -= number.imaginaryPart;
    return *this;
}

myComplex &myComplex::operator*=(const myComplex &number)
{
    int real = realPart * number.realPart - imaginaryPart * number.imaginaryPart;
    imaginaryPart = realPart * number.imaginaryPart + imaginaryPart * number.realPart;
    realPart = real;
    return *this;
}

// Overloading comparison operators
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

// Overloaded unary operators
myComplex myComplex::operator-()
{
    return myComplex(-realPart, -imaginaryPart);
}

myComplex myComplex::operator~()
{
    return myComplex(realPart, -imaginaryPart);
}

myComplex myComplex::operator++()
{
    ++realPart;
    return *this;
}

myComplex myComplex::operator++(int)
{
    myComplex temp(*this);
    ++(*this);
    return temp;
}

myComplex myComplex::operator--()
{
    --realPart;
    return *this;
}

myComplex myComplex::operator--(int)
{
    myComplex temp(*this);
    --(*this);
    return temp;
}

// Friend functions for input/output
ostream &operator<<(ostream &outStream, const myComplex &number)
{
    outStream << "(" << number.realPart << "," << number.imaginaryPart << ")";
    return outStream;
}

istream &operator>>(istream &inStream, myComplex &number)
{
    inStream >> number.realPart >> number.imaginaryPart;
    return inStream;
}

myComplex operator+(int value, const myComplex &number)
{
    return myComplex(value + number.realPart, number.imaginaryPart);
}

myComplex operator-(int value, const myComplex &number)
{
    return myComplex(value - number.realPart, -number.imaginaryPart);
}

myComplex operator*(int value, const myComplex &number)
{
    return myComplex(value * number.realPart, value * number.imaginaryPart);
}

// Private function
int myComplex::norm() const
{
    return realPart * realPart + imaginaryPart * imaginaryPart;
}

int main()
{
    int t;
    cin >> t;

    for (int i = 0; i < t; ++i)
    {
        myComplex c1, c2, c3, c4;
        myComplex c5, c6, c7, c8, c9;

        cin >> c1 >> c2 >> c3 >> c4;

        cout << "Input complex numbers: " << c1 << " " << c2 << " " << c3 << " " << c4 << endl;

        cout << "Results of operations:" << endl;
        cout << "(2 + c1 + 3) + (2 - c2 - 3) * (2 * c3 * 3) - (2 * c4 - 3) = "
             << (2 + c1 + 3) + (2 - c2 - 3) * (2 * c3 * 3) - (2 * c4 - 3) << endl;

        c5 = c6 = c7 = c8 = c1;

        cout << "(c5 == c2) = " << (c5 == c2) << ", (c5 != c2) = " << (c5 != c2) << endl;
        cout << "(c5 > c2) = " << (c5 > c2) << ", (c5 >= c2) = " << (c5 >= c2)
             << ", (c5 < c2) = " << (c5 < c2) << ", (c5 <= c2) = " << (c5 <= c2) << endl;
        cout << "(c5 == c6) = " << (c5 == c6) << ", (c5 != c6) = " << (c5 != c6) << endl;
        cout << "(c5 > c6) = " << (c5 > c6) << ", (c5 >= c6) = " << (c5 >= c6)
             << ", (c5 < c6) = " << (c5 < c6) << ", (c5 <= c6) = " << (c5 <= c6) << endl;

        c5 += c2;
        c6 -= c3;
        c7 *= c4;
        c8 = c2.getRealPart();
        c9 = c3.getImaginaryPart();
        cout << "After operations: " << c5 << " " << c6 << " " << c7 << " " << c8 << " " << c9 << endl;

        c7 = -c6;
        c8 = (++c7) * 2;
        c9 = 2 * (c7++);
        cout << "Unary operations: " << c7 << " " << c8 << " " << c9 << endl;

        c7 = ~c6;
        c8 = (++c7) * 2;
        c9 = 2 * (c7++);
        cout << "Unary operations with conjugate: " << c7 << " " << c8 << " " << c9 << endl;
    }

    return 0;
}
