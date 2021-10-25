#include <iostream>
#include<cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <stack>
#include <vector>
#include <set>
#include <queue>
#include <map>

#define ABS(x) (((x) < 0)?-(x):(x))
#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
#define PI 3.1415926535897932384

using namespace std;

namespace matrix {

	class Matrix {
	public:
		int** data;
		int row;
		int col;

		Matrix(int row, int col) :row(row), col(col) {
			data = new int* [row];
			for (int i = 0; i < row; i++) {
				data[i] = new int[col];
			}
		}

		Matrix(const Matrix& m) :row(m.row), col(m.col) {
			data = new int* [row];
			for (int i = 0; i < row; i++) {
				data[i] = new int[col];
				for (int k = 0; k < col; k++) {
					this->data[i][k] = m.data[i][k];
				}
			}
		}

		~Matrix() {
			for (int i = 0; i < row; i++) {
				delete[] data[i];
			}
			delete[] data;
		}

		Matrix operator*(const Matrix& m) {
			Matrix result(this->row, m.col);
			for (int i = 0; i < this->row; i++) {
				for (int k = 0; k < m.col; k++) {
					result.data[i][k] = 0;
					for (int j = 0; j < this->col; j++) {
						result.data[i][k] += this->data[i][j] * m.data[j][k];
					}
				}
			}
			return result;
		}

		Matrix operator%(const int& mod) {
			Matrix result(*this);
			for (int i = 0; i < result.row; i++) {
				for (int k = 0; k < result.col; k++) {
					result.data[i][k] %= mod;
				}
			}
			return result;
		}

		int* operator[] (const int& idx) {
			return data[idx];
		}
		int* operator[] (const int& idx) const {
			return data[idx];
		}

		static Matrix getIdentity(const int& N) {
			Matrix I(N, N);
			for (int i = 0; i < I.row; i++) {
				for (int k = 0; k < I.col; k++) {
					I[i][k] = 0;
				}
			}
			for (int i = 0; i < N; i++) {
				I[i][i] = 1;
			}
			return I;
		}
	};

	ostream& operator << (ostream& c, const Matrix& m) {
		for (int i = 0; i < m.row; i++) {
			for (int k = 0; k < m.col; k++) {
				c << m[i][k] << ' ';
			}
			c << '\n';
		}
		return c;
	}
}