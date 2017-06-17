function runningLogger(){
  console.log("I am running")
}


runningLogger()


function multipleByTen(val){
  val=val * 10
  console.log(val)
}

multipleByTen(5)


function stringReturnOne(){
 return "iam string one"
}


function stringReturntwo(){
 return "iam string two"
 console.log ("string one")
}


function caller(param){
  if (typeof(param)=='function'){
    param()
  }

}

function doubleConsoleLog(param1, param2){
  if (typeof(param1)=='function' && typeof(param2)== 'function'){
    console.log(param1(), param2());
  }
}
doubleConsoleLog(stringReturnOne, stringReturntwo)


function caller(param){
  console.log("starting...")

    setTimeout(function(){
      if (typeof(param)=='function'){
        param(stringReturnOne, stringReturntwo);
    }

}, 2000);
console.log("ending")

return "interesting"
}

caller(doubleConsoleLog)
