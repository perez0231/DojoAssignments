// console.log("connected")

var quarters = 10;


function randomchance(quarters) {
  var winningnum = 69;

    while (quarters > 0) {
        if (winningnum === Math.ceil(Math.random() * 100)){
                quarters = quarters + Math.trunc(Math.random()*50) + 51;
                quarters = quarters - 1;
                console.log(quarters);
            } else {
                quarters = quarters - 1;
                if (quarters == 0) {
                    console.log(quarters);
                }
            }





        }



    }
randomchance(quarters);
