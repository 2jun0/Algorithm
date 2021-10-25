//#include <iostream>
//#include<cstring>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//#include <vector>
//#include <set>
//#include <queue>
//
//#define ABS(x) (((x) < 0)?-(x):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//template<typename T>
//class Queue {
//public:
//	T* data;
//	int front_idx;
//	int back_idx;
//	int capacity;
//
//	Queue(int n) {
//		capacity = n;
//		data = new T[n];
//		back_idx = 0;
//		front_idx = -1;
//	}
//
//	~Queue() {
//		delete[] data;
//	}
//
//	void push(T item) {
//		front_idx++;
//		if (front_idx >= capacity) {
//			front_idx -= capacity;
//		}
//		data[front_idx] = item;
//	}
//
//	void push_back(T item) {
//		back_idx--;
//		if (back_idx < 0) {
//			back_idx += capacity;
//		}
//		data[back_idx] = item;
//	}
//
//	T pop() {
//		int temp = data[back_idx++];
//		if (back_idx >= capacity) {
//			back_idx -= capacity;
//		}
//		return temp;
//	}
//
//	T pop_front() {
//		int temp = data[front_idx--];
//		if (front_idx < 0) {
//			front_idx += capacity;
//		}
//		return temp;
//	}
//
//	int size() {
//		int temp = front_idx - back_idx + 1;
//		if (temp < 0) {
//			temp += capacity;
//		}
//
//		return temp;
//	}
//
//	T front() {
//		return data[front_idx];
//	}
//
//	T back() {
//		return data[back_idx];
//	}
//};
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int N;
//	cin >> N;
//
//	Queue<int> q(500000);
//
//	for (int i = N; i >= 1; i--) {
//		q.push(i);
//	}
//
//	int temp;
//	while (q.size() > 1) {
//		q.pop_front();
//		temp = q.pop_front();
//		q.push_back(temp);
//	}
//
//	cout << q.pop();
//
//	return 0;
//}