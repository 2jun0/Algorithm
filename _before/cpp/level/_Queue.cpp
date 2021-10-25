#include <iostream>
#include<cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <stack>
#include <vector>
#include <set>
#include <queue>

#define ABS(x) (((x) < 0)?-(x):(x))
#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
#define PI 3.1415926535897932384

using namespace std;

namespace queue1{
	template<typename T>
	class Queue {
	public:
		T* data;
		int front_idx;
		int back_idx;
		int capacity;

		Queue(int n) {
			capacity = n;
			data = new T[n];
			back_idx = 0;
			front_idx = -1;
		}

		~Queue() {
			delete[] data;
		}

		void push(T item) {
			front_idx++;
			if (front_idx >= capacity) {
				front_idx -= capacity;
			}
			data[front_idx] = item;
		}

		void push_back(T item) {
			back_idx--;
			if (back_idx < 0) {
				back_idx += capacity;
			}
			data[back_idx] = item;
		}

		T pop() {
			int temp = data[back_idx++];
			if (back_idx >= capacity) {
				back_idx -= capacity;
			}
			return temp;
		}

		T pop_front() {
			int temp = data[front_idx--];
			if (front_idx < 0) {
				front_idx += capacity;
			}
			return temp;
		}

		int size() {
			int temp = front_idx - back_idx + 1;
			if (temp < 0) {
				temp += capacity;
			}

			return temp;
		}

		T front() {
			return data[front_idx];
		}

		T back() {
			return data[back_idx];
		}
	};
}

namespace queue2 {
	template<typename T>
	class Queue {
	public:
		class QRecord {
		public:
			QRecord* next;
			QRecord* before;
			T value;

			QRecord(T value, QRecord* before, QRecord* next) {
				this->value = value;
				before->next = this;
				this->before = before;
				this->next = next;
				next->before = this;
			}

			QRecord(T value) {
				this->value = value;
				next = this;
				before = this;
			}

			~QRecord() {
				this->before->next = this->next;
				this->next->before = this->before;
			}
		};
	public:
		QRecord* start;
		int cnt = 0;

		Queue() {
			start = NULL;
		}

		~Queue() {
			while (cnt > 0) {
				pop_front();
			}
			start = NULL;
		}

		void push(T item) {
			if (cnt == 0) {//new
				start = new QRecord(item);
			}
			else {
				QRecord* record = new QRecord(item, start->before, start);
			}
			cnt++;
		}

		void push_back(T item) {
			if (cnt == 0) {//new
				start = new QRecord(item);
			}
			else {
				QRecord* record = new QRecord(item, start->before, start);
				start = record;
			}
			cnt++;
		}

		T pop() {
			cnt--;
			T temp = start->value;
			start = start->next;
			delete start->before;
			return temp;
		}

		T pop_front() {
			cnt--;
			T temp = start->before->value;
			delete start->before;
			return temp;
		}

		int size() { return cnt; }
		bool empty() { return (cnt == 0); }

		T front() { return start->before->value; }
		T back() { return start->value; }

		QRecord* front_record() { return start->before; }
		QRecord* back_record() { return start; }

		Queue* operator++() {
			start = start->next;
			return this;
		}

		Queue* operator--() {
			start = start->before;
			return this;
		}
	};
}