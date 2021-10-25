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
//		cnt++;
//		if (!start) {//new
//			start = new QRecord(item);
//		}
//		else {
//			QRecord* record = new QRecord(item, start->before, start);
//		}
//	}
//
//	void push_front(T item) {
//		cnt++;
//		if (!start) {//new
//			start = new QRecord(item);
//		}
//		else {
//			QRecord* record = new QRecord(item, start, start->next);
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
//	int size() { return cnt; }
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
//	int T;
//	cin >> T;
//
//	for (int t = 0; t < T; t++) {
//		int N, M;
//		cin >> N >> M;
//
//		int temp;
//		Queue<int> q;
//		Queue<int>::QRecord* target = NULL;
//
//		int num_cnt[10];
//		memset(num_cnt, 0, sizeof(int) * 10);
//		int num_cnt_idx = 0;
//
//		for (int i = 0; i < N; i++) {
//			cin >> temp;
//			num_cnt[temp]++;
//			num_cnt_idx = max(num_cnt_idx, temp);
//
//			q.push(temp);
//
//			if (i == M) {
//				target = q.front_record();
//			}
//		}
//
//		int priority = 1;
//		while (q.size() > 0) {
//			if(q.back() == num_cnt_idx) {
//				if (q.back_record() == target) {
//					// Á¤´ä!
//					cout << priority << '\n';
//					break;
//				}
//
//				q.pop();
//				--q;
//
//				num_cnt[num_cnt_idx]--;
//				while (num_cnt[num_cnt_idx] == 0) {
//					num_cnt_idx--;
//				}
//
//				priority++;
//			}
//			++q;
//		}
//
//	}
//
//	return 0;
//}