#include <stdio.h>

#include <vector>
std::vector<long long> eygptian_fractions(long long a, long long b) {
  std::vector<long long> res = {};
  if (a == 1) {
    res.push_back(b);
    return res;
  }
  while (true) {
    long long biggest = (b - b % a) / a + 1;
    res.push_back(biggest);
    a = a * biggest - b;

    b = b * biggest;
    if (a == 1) {
      res.push_back(b);
      break;
    }
  }
  return res;
}
std::vector<long long> test() { return std::vector<long long>{1, 2}; }
int main() {
  std::vector v = eygptian_fractions(5, 13);
  for (long long i : v) {
    printf("%d ", i);
  }
}
