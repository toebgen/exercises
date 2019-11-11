// https://www.hackerrank.com/challenges/variable-sized-arrays/problem

// #include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

struct Params {
    int n;
    int q;

    void read_in() {
        cin >> n;
        cin >> q;
        // cout << "Read in n=" << n << ", q=" << q << endl;
    }    
};

class NestedVector {
    public:
        NestedVector(Params params): params(params) {}

        int get(const int i, const int j) const {
            return vec.at(i).at(j);
        }

        void read_in() {
            for(int i=0; i<params.n; i++){
                // cout << "Reading in i=" << i << endl;
                int k, val;
                cin >> k;
                // cout << "Reading in k=" << k << endl;
                std::vector<int> v;
                for (int j=0; j<k; j++){
                    cin >> val;
                    // cout << "Reading in val=" << val << endl;
                    v.push_back(val);
                }
                vec.push_back(v);
            }
        }

        void print() {
            cout << "NestedVector size " << vec.size() << " content:" << endl;
            for (auto i=0; i<vec.size(); i++){
                printf("%d: ", i);
                for (auto val: vec.at(i)) {
                    printf("%d ", val);
                }
                printf("\n");
            }
        }
    
    private:
        std::vector<std::vector<int> > vec;
        Params params;
};

void handle_queries(const NestedVector& vec, const Params& params) {
    for (int k=0; k<params.q; ++k){
        int i, j;
        cin >> i >> j;
        // printf("Querying i=%d, j=%d...\n", i, j);
        printf("%d\n", vec.get(i, j));
    }
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    // cout << "Running the program..." << endl;

    Params params;
    params.read_in();

    NestedVector vec(params);
    vec.read_in();
    // vec.print();

    handle_queries(vec, params);
    
    return 0;
}
