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
//	class QRecord {
//	public:
//		QRecord* next;
//		QRecord* before;
//		T value;
//
//		QRecord(T value, QRecord* before, QRecord* next) {
//			this->value = value;
//			before->next = this;
//			this->before = before;
//			this->next = next;
//			next->before = this;
//		}
//
//		QRecord(T value) {
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
//	QRecord* start;
//	int cnt = 0;
//
//	Queue() {
//		start = NULL;
//	}
//
//	~Queue() {
//		while (cnt > 0) {
//			pop_front();
//		}
//		start = NULL;
//	}
//
//	void push(T item) {
//		if (cnt == 0) {//new
//			start = new QRecord(item);
//		}
//		else {
//			QRecord* record = new QRecord(item, start->before, start);
//		}
//		cnt++;
//	}
//
//	void push_back(T item) {
//		if (cnt == 0) {//new
//			start = new QRecord(item);
//		}
//		else {
//			QRecord* record = new QRecord(item, start->before, start);
//			start = record;
//		}
//		cnt++;
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
//	int size() { return cnt; }
//	bool empty() { return (cnt == 0); }
//
//	T front() { return start->before->value; }
//	T back() { return start->value; }
//
//	QRecord* front_record() { return start->before; }
//	QRecord* back_record() { return start; }
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
//
//	int N;
//	cin >> N;
//
//	string cmd;
//	int param;
//
//	Queue<int> q;
//	for (int i = 0; i < N; i++) {
//		cin >> cmd;
//
//		if (cmd.compare("push_front") == 0) {
//			cin >> param;
//			q.push(param);
//		}
//		else if (cmd.compare("push_back") == 0) {
//			cin >> param;
//			q.push_back(param);
//		}
//		else if (cmd.compare("pop_front") == 0) {
//			if (!q.empty()) {
//				cout << q.pop_front() << '\n';
//			}
//			else {
//				cout << -1 << '\n';
//			}
//		}
//		else if (cmd.compare("pop_back") == 0) {
//			if (!q.empty()) {
//				cout << q.pop() << '\n';
//			}
//			else {
//				cout << -1 << '\n';
//			}
//		}
//		else if (cmd.compare("size") == 0) {
//			cout << q.size() << "\n";
//		}
//		else if (cmd.compare("empty") == 0) {
//			cout << (q.empty()?1:0) << "\n";
//		}
//		else if (cmd.compare("front") == 0) {
//			if (!q.empty()) {
//				cout << q.front() << "\n";
//			}
//			else {
//				cout << -1 << '\n';
//			}
//		}
//		else if (cmd.compare("back") == 0) {
//			if (!q.empty()) {
//				cout << q.back() << "\n";
//			}
//			else {
//				cout << -1 << '\n';
//			}
//		}
//	}
//
//	return 0;
//}