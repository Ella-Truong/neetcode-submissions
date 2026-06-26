class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let new_nums = []
        for(let i=0; i < nums.length; i++){
            new_nums.push(nums.filter((_,index) => index !== i))
        }

        let output = new_nums.map(each => each.reduce((acc,num)=> acc*num))
        return output
}
}