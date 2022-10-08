function bubbleSort(arr)
{
    let temp =0;
    //Take a temp variable assing it to 0
    for(let i=0;i<arr.length;i++)
    {
        //taking i loop for comparision
        for(let j=0;j<arr.length;j++)
        //taking j loop for comparision
        {
            if(arr[i] > arr[i+j])
            //if(54 is greater than 32 ) in first itreation 
            {
                temp = arr[i];
                // 0 is now 54
                arr[i] = arr[i +j];
                //54 is now 32
                arr[i + j ] =  temp;
                //32 is now 54
            }
        }
    }
    return arr;
    //sorted array returned
}
const arr = [54,32,34,76,23,12,11,56,88,43];

console.log(bubbleSort(arr));