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
//private:
//	template<typename U>
//	class QRecord {
//	public:
//		QRecord<U>* next;
//		QRecord<U>* before;
//		U value;
//
//		QRecord(U value, QRecord<U>* before, QRecord<U>* next) {
//			this->value = value;
//			before->next = this;
//			this->before = before;
//			this->next = next;
//			next->before = this;
//		}
//
//		QRecord(U value) {
//			this->value = value;
//			next = this;
//			before = this;
//		}
//
//		~QRecord() {
//			this->before->next = this->next;
//			this->next->before = this->before;
//		}
//	};
//public:
//	QRecord<T>* start;
//	int cnt = 0;
//
//	Queue() {
//		start = NULL;
//	}
//
//	~Queue() {
//		while(cnt > 0) {
//			pop_front();
//		}
//		start = NULL;
//	}
//
//	void push(T item) {
//		cnt++;
//		if (!start) {//new
//			start = new QRecord<T>(item);
//		}
//		else {
//			QRecord<T>* record = new QRecord<T>(item, start->before, start);
//		}
//	}
//
//	void push_front(T item) {
//		cnt++;
//		if (!start) {//new
//			start = new QRecord<T>(item);
//		}
//		else {
//			QRecord<T>* record = new QRecord<T>(item, start, start->next);
//			start = record;
//		}
//	}
//
//	T pop() {
//		cnt--;
//		T temp = start->value;
//		start = start->next;
//		delete start->before;
//		return temp;
//	}
//
//	T pop_front() {
//		cnt--;
//		T temp = start->before->value;
//		delete start->before;
//		return temp;
//	}
//
//	int size() {
//		return cnt;
//	}
//
//	T front() {
//		start->before->value;
//	}
//
//	T back() {
//		start->value;
//	}
//
//	Queue* operator++() {
//		start = start->next;
//		return this;
//	}
//
//	Queue* operator--() {
//		start = start->before;
//		return this;
//	}
//};
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	int N, K;
//	cin >> N >> K;
//
//	Queue<int> q;
//	vector<int> result;
//
//	for (int i = 1; i <= N; i++) {
//		q.push(i);
//	}
//
//	while (q.size() > 0) {
//		for (int i = 0; i < K - 1; i++) {
//			++q;
//		}
//		result.push_back(q.pop());
//	}
//
//	cout << '<';
//	for (int i = 0; i < N-1; i++) {
//		cout << result[i] << ", ";
//	}
//	cout << result[N-1] << '>';
//
//	return 0;
//}