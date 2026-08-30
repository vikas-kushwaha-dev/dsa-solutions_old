class Solution {

    /**
     * @param Integer[] $nums
     * @return NULL
     */
    function sortColors(&$nums) {
        $n = count($nums);
        for($i = 0; $i < $n - 1; $i++){
            for($j = 0; $j < $n - $i - 1; $j++){
                if($nums[$j] > $nums[$j + 1]){
                    $temp = $nums[$j];
                    $nums[$j] = $nums[$j + 1];
                    $nums[$j + 1] = $temp;
                }
            }
        }
    }
}