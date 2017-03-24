var arr = [1, "apple", -3, "orange", .5]

function newArray(arr) {

  var newarr = [];

    for (var i = 0; i < arr.length; i++) {
        if (typeof arr[i] === "number") {
            newarr.push(arr[i])
        }

    }
    return newarr;
}
newArray(arr);
