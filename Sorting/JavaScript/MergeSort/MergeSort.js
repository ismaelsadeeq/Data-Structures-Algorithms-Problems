
const MergedArr = (arr1,arr2)=>
//First we are taking two sorted array
{
    const MergerdArr2 = [];
    //taking a blank array
    let arr1Item =arr1[0];
    //arr1[0] item  into arr1Item (eaxmple 12)
    let arr2Item = arr2[0];
    //arr2[0] item  into arr2Item (eaxmple 10)
    let i = 1;
    //Initialise i = 1
    let j = 1;
    //Initialise j =1
    
    while(arr1Item !== undefined)
    //untill arr1Item is not undefined  
    {
        if(arr2Item === undefined || arr1Item < arr2Item)
        //if arr1Item is less  than arr2Item
        {
            MergerdArr2.push(arr1Item);
            //then MergerArr2 ++
            arr1Item = arr1[i];
            //then arr1Item will be equal to arr1Item will be 32

            i++;
            //i =2  
        }
        else
        {
            MergerdArr2.push(arr2Item);
            //Else MergedArr2 ++
            arr2Item = arr2[i];
            ///arr2Item = be 31
            j++;
            //j=2
        }
    }
    return MergerdArr2;
}
console.log(MergedArr([12,32,43,54,65],[10,31,42,53,64]));