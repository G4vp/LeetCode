/*
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var selfDividingNumbers = function(left, right) {
    lst = new Array;
    for(let i = left;i <= right; i++){
        if(isSelfDivide(i)){
            lst.push(i);
        }
    }
    return lst;
};

function isSelfDivide(n){
    b = n;
    while(b > 0){
        if(n%(b%10) === 0) b = Math.floor(b/10);
        else return false;
    }
    return true;
}