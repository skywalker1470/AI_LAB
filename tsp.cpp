#include<bits/stdc++.h>
using namespace std ;
int tsp(vector<vector<int>> graph ,  vector<int> &cities){
    vector<int> best ; 
    int minDist = INT_MAX;
    
    do{
        int current_dist = 0 ; 
        int from = 0 ; 
        for(int to : cities){
            current_dist += graph[from][to];
            from = to;
        }
        current_dist += graph[from][0];
        if(current_dist < minDist) {
            best = cities;
            minDist = current_dist ; 
        }
    } while(next_permutation(cities.begin() , cities.end()));
    //priunting best route 
    cout<<"The best path is : 0 -> ";
    for(int i:best) cout<<i<<" -> ";
    cout<<"0"<<endl;
    return minDist;
} 
int main(){
    vector<vector<int>> graph = { 
        {0, 10, 13, 17},
        {10, 0, 8, 6},
        {13, 8, 0, 10},
        {17, 6, 10, 0}
    };
    vector<int> cities ; 
    for(int i=1 ; i<graph.size() ; i++){
        cities.push_back(i);
    }    
    int minDist = tsp(graph , cities);
    cout<<"The minimum distance is : "<<minDist;
    return 0; 
}