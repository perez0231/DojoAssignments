// //
// // function top(){
// //
// //
// // }
// //
// //
// // function Stack() {
// //     this._size = 0;
// //     this._storage = {};
// //
// // }
// // function copy (s1){
// //
// // var s2 =new Stack();
// // if (!s1.top() ){
// //   return s2
// // }
// // var current = s1.top();
// // var temp= [];
// // while(current){
// //   temp.push(current);
// //   s1.pop();
// //   current= s1.top()
// // }
// // var copy= temp.top();
// // while(copy){
// //   s1.push(copy);
// //   s2.push(copy);
// //   temp.pop();
// //   copy=temp.pop();
// // }
// // return s2
// //
// //
// //
// // //
// // // }

// // //console.log(copy())



// // function remove_dups(arr){
// // var count = 0
// // for (var i=1; i <arr.length; i++){
// //   for (var x=1 ; x<arr.length; i++){
// //     if(arr[x]==arr[i]){
// //       count ++
// //       for (var y = i; y <arr.length-1; y++){
// //         arr[y]=arr[y+1]
// //       }
// //     }
// //   }
// // }




// // }
// // remove_dups([1,2,4,2])

// function rBinarySearch(str){
//   var arr =[];
//   var curr = "";
//   (function helper(str,curr,arr){
//     if(curr.length == str.length){
//       arr.push(curr);
//     }
//     else {
//       helper(str, curr + "0", arr);
//       helper(str, curr + "1", arr);
//     }
//   }) (str, curr, arr);
//   return arr

// }

// console.log(rBinarySearch("???"))





// function rBinarySearchexp(str){
//  return helper(str, "", [])

//  function helper(str, substr, arr){
//   if


//  }

//   if (!str[substr.length]){
//     arr.push(substr)
//     return arr
//   }else{
//     while(str[substr.length] != "?"){
// rBinarySearchexp(str, substr +str[substr.length], arr)   
//  }
//  else{
//    if(str[substr.length != "?"]){
//      rBinarySearchexp(str, substr +str[substr.length], arr)
//    }
//  }
//     if(!str[substr.length]){
//       rBinarySearchexp(str, substr, + "0", arr)
//       return rBinarySearchexp(str, substr +"1", arr)
//     }else{
//       arr.push(substr)
//       return arr 
//     }
//   }
arr = [10,2,39,3,5,6,89,3]

function bubblesort(arr){
  var temp = 0

  for( var i = arr.length -1; i > 0; i -- ){
    for (var x = 0; x < i; x++ ){
      if( arr[x] > arr[x +1]){
        temp = arr[x +1]
        arr[x + 1] = arr[x]
        arr[x]= temp
      }
    }

  }
  return arr

}

bubblesort(arr)