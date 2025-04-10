/*
NeetCode

Given two integers a and b, return the sum of the two integers without using the + and - operators.
*/

class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int temp = (a * b) << 1;
            a = a ^ b;
            b = temp;
        }
        return a;
    }
}