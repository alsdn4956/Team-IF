#ifndef _MYRATIONAL_H_
#define _MYRATIONAL_H_

#include <fstream>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class myRational
{
private:
    // 분수는 항상 내부적으로 기약분수로 표현하며, 또한 항상 _den>0 이다. long _num; // numerator
    long _num;
    long _den; // denominator

    long gcd(long m, long n); // 최대공약수
    void reduce();

public:
    myRational(long num = 0, long den = 1);
    myRational(const myRational &r);
    long getNumerator() const;
    long getDenominator() const;
    myRational reciprocal() const;
    myRational operator+(const myRational &r) const;
    myRational operator-(const myRational &r) const;
    myRational operator*(const myRational &r) const;
    myRational operator*(long num) const;
    myRational operator/(long num) const;
    myRational operator/(const myRational &r) const;
    bool operator<(const myRational &r) const;
    bool operator<=(const myRational &r) const;
    bool operator>(const myRational &r) const;
    bool operator>=(const myRational &r) const;
    bool operator==(const myRational &r) const;
    bool operator!=(const myRational &r) const;
    myRational operator=(const myRational &r);
    myRational operator+=(const myRational &r);
    myRational operator-=(const myRational &r);
    myRational operator*=(const myRational &r);
    myRational operator/=(const myRational &r);
    myRational operator-();
    myRational &operator++();
    myRational operator++(int);
    myRational operator--();
    myRational operator--(int);
    friend myRational operator+(long num, const myRational &r);
    friend myRational operator-(long num, const myRational &r);
    friend myRational operator*(long num, const myRational &r);
    friend myRational operator/(long num, const myRational &r);
    friend ostream &operator<<(ostream &outStream, const myRational &r);
    friend istream &operator>>(istream &inStream, myRational &r);
};
#endif

using namespace std;

myRational::myRational(long num, long den) : _num(num), _den(den)
{
    reduce();
}
myRational::myRational(const myRational &r)
{
    _num = r._num;
    _den = r._den;
}
long myRational::getNumerator() const
{
    return _num;
}
long myRational::getDenominator() const
{
    return _den;
}
myRational myRational::reciprocal() const
{
    return myRational(_den, _num);
}
ostream &operator<<(ostream &outStream, const myRational &r)
{
    if (r._num == 0)
        outStream << 0;
    else if (r._den == 1)
        outStream << r._num;
    else
        outStream << r._num << "/" << r._den;
    return outStream;
}
istream &operator>>(istream &inStream, myRational &r)
{
    inStream >> r._num >> r._den;
    if (r._den == 0)
    {
        r._num = 0;
        r._den = 1;
    }
    r.reduce();
    return inStream;
}

myRational myRational::operator+(const myRational &r) const
{
    long newNum = (_num * r._den) + (_den * r._num);
    long newDen = _den * r._den;
    myRational tmp(newNum, newDen);
    tmp.reduce();
    return tmp;
}

myRational myRational::operator-(const myRational &r) const
{
    long newNum = (_num * r._den) - (_den * r._num);
    long newDen = _den * r._den;
    myRational tmp(newNum, newDen);
    tmp.reduce();
    return tmp;
}

myRational myRational::operator*(const myRational &r) const
{
    long newNum = _num * r._num;
    long newDen = _den * r._den;
    myRational tmp(newNum, newDen);
    tmp.reduce();
    return tmp;
}

myRational myRational::operator*(long num) const
{
    long newNum = _num * num;
    myRational tmp(newNum, _den);
    tmp.reduce();
    return tmp;
}

myRational myRational::operator/(const myRational &r) const
{
    long newNum = _num * r._den;
    long newDen = _den * r._num;
    myRational tmp(newNum, newDen);
    tmp.reduce();
    return tmp;
}

myRational myRational::operator/(long num) const
{
    long newDen = _den * num;
    myRational tmp(_num, newDen);
    tmp.reduce();
    return tmp;
}

bool myRational::operator<(const myRational &r) const
{
    return (_num * r._den) < (r._num * _den);
}

bool myRational::operator<=(const myRational &r) const
{
    return (_num * r._den) <= (r._num * _den);
}

bool myRational::operator>(const myRational &r) const
{
    return (_num * r._den) > (r._num * _den);
}

bool myRational::operator>=(const myRational &r) const
{
    return (_num * r._den) >= (r._num * _den);
}

bool myRational::operator==(const myRational &r) const
{
    return (_num * r._den) == (r._num * _den);
}

bool myRational::operator!=(const myRational &r) const
{
    return (_num * r._den) != (r._num * _den);
}

myRational myRational::operator=(const myRational &r)
{
    _num = r._num;
    _den = r._den;
    reduce();
    return *this;
}

myRational myRational::operator+=(const myRational &r)
{
    *this = *this + r;
    reduce();
    return *this;
}

myRational myRational::operator-=(const myRational &r)
{
    *this = *this - r;
    reduce();
    return *this;
}

myRational myRational::operator*=(const myRational &r)
{
    *this = *this * r;
    reduce();
    return *this;
}

myRational myRational::operator/=(const myRational &r)
{
    *this = *this / r;
    this->reduce();
    return *this;
}

myRational myRational::operator-()
{
    *this *= -1;
    return *this;
}

myRational &myRational::operator++()
{
    *this += 1;
    return *this;
}

myRational myRational::operator++(int)
{
    myRational tmp(*this);
    *this += 1;
    return tmp;
}

myRational operator+(long num, const myRational &r)
{
    long newNum = r._den * num + r._num;
    myRational tmp(newNum, r._den);
    tmp.reduce();
    return tmp;
}

myRational myRational::operator--()
{
    *this -= 1;
    return *this;
}

myRational myRational::operator--(int)
{
    myRational tmp(*this);
    *this -= 1;
    return tmp;
}

myRational operator-(long num, const myRational &r)
{
    long newNum = r._den * num - r._num;
    myRational tmp(newNum, r._den);
    tmp.reduce();
    return tmp;
}

myRational operator*(long num, const myRational &r)
{
    long newNum = num * r._num;
    myRational tmp(newNum, r._den);
    tmp.reduce();
    return tmp;
}

myRational operator/(long num, const myRational &r)
{
    long newDen = num * r._den;
    myRational tmp(newDen, r._num);
    tmp.reduce();
    return tmp;
}

long myRational::gcd(long m, long n)
{
    if (m == n)
        return n;
    else if (m < n)
        return gcd(m, n - m);
    else
        return gcd(m - n, n);
}

void myRational::reduce()
{
    if (_num == 0 || _den == 0)
    {
        _num = 0;
        _den = 1;
        return;
    }
    if (_den < 0)
    {
        _den *= -1;
        _num *= -1;
    }
    if (_num == 1)
        return;
    int sgn = (_num < 0 ? -1 : 1);
    long g = gcd(sgn * _num, _den);
    _num /= g;
    _den /= g;
}

void testSimpleCase();
void testDataFromFile();

int main()
{
    testSimpleCase();
    testDataFromFile();
    return 0;
}
void testSimpleCase()
{
    myRational frac1(2), frac2(3, 2), frac3(6, 4), frac4(12, 8), frac5, frac6, frac7;
    cout << frac1 << " " << frac2 << " " << frac3 << " "
         << frac4 << " " << frac5 << endl;
    cout << frac1.getNumerator() << " " << frac1.getDenominator() << endl;

    // Check arithmetic operators
    cout << frac1 * frac2 << " "
         << frac1 + frac3 << " "
         << frac2 - frac1 << " "
         << frac3 / frac2 << endl;

    // Check comparison operators
    cout << ((frac1 < frac2) ? 1 : 0) << " "
         << ((frac1 <= frac2) ? 1 : 0) << " "
         << ((frac1 > frac2) ? 1 : 0) << " "
         << ((frac1 >= frac2) ? 1 : 0) << " "
         << ((frac1 == frac2) ? 1 : 0) << " "
         << ((frac1 != frac2) ? 1 : 0) << " "
         << ((frac2 < frac3) ? 1 : 0) << " "
         << ((frac2 <= frac3) ? 1 : 0) << " "
         << ((frac2 > frac3) ? 1 : 0) << " "
         << ((frac2 >= frac3) ? 1 : 0) << " "
         << ((frac2 == frac3) ? 1 : 0) << " "
         << ((frac2 != frac3) ? 1 : 0) << endl;

    cout << (frac6 = frac3) << " ";
    cout << (frac6 += frac3) << " ";
    cout << (frac6 -= frac3) << " ";
    cout << (frac6 *= frac3) << " ";
    cout << (frac6 /= frac3) << endl;
    cout << -frac6 << endl;
    frac6 = (++frac4) + 2;
    frac7 = 2 + (frac4++);
    cout << frac4 << " " << frac6 << " " << frac7 << endl;
    frac6 = (--frac4) - 2;
    frac7 = 2 - (frac4--);
    cout << frac4 << " " << frac6 << " " << frac7 << endl;
    cout << 2 * frac3 << " " << frac3 * 2 << " "
         << 2 / frac3 << " " << frac3 / 2 << endl;
}

void testDataFromFile()
{
    int t, tt, num, den;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> tt;
        vector<myRational> v;
        for (int j = 0; j < tt; j++)
        {
            cin >> num >> den;
            v.push_back(myRational(num, den));
        }
        sort(v.begin(), v.end());
        for (int j = 0; j < v.size(); j++)
        {
            cout << v[j] << " ";
        }
        cout << endl;
    }
}