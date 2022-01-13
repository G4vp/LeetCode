/*
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function(mat) {
    let sm=0,l=0,r=mat.length-1;
    while(l<=r){
        sm += mat[l][l] + mat[l][r];
        sm += mat[r][l] + mat[r][r];
        if(l===r){
            sm -= mat[r][l] + mat[r][r] + mat[r][l];
        }    
        l += 1;
        r -= 1;
    }
    return sm;
};