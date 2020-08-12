
#include "aux.cpp"
#include "1514.path-with-maximum-probability.cpp"

int main(int argc, char const *argv[]) {
	Solution s;
	int n = 3, start=0, end=2; 
	vvi edges = {{0,1},{1,2},{0,2}};
	vector<double> succProb = {0.5,0.5,0.2};
	say(s.maxProbability(n, edges, succProb, start, end));

class CompareDist
{
public:
    bool operator()(pair<double,int> n1,pair<double,int> n2) {
        return n1.first < n2.first;
    }
};
	    priority_queue<pair<double, int>, vector<pair<double, int>>, CompareDist>
        pq;

	pq.push(mp(1.0, 0));
	pq.pop();
	pq.push(mp(0.2, 2));
	pq.push(mp(0.5, 1));
	pq.push(mp(0.3, 1));
	pq.push(mp(0.9, 1));
	double p = pq.top().first;
	say(p);

	pq.pop(); 
	p = pq.top().first;
	say(p);
	
	pq.pop();
	p = pq.top().first;
	say(p);
	return 0;
}

