function CarConstructor(name, wheels, passengers, speed) {
  var self =this;
  var distance_traveled= 0
  CarConstructor.prototype.update_distance_traveled =function(){
    distance_traveled += self.speed
    console.log(distance_traveled)
    return this;
  }
    var chars = "0123456789ABCEDGHIJKLMNOPQRSTUVWXYZ";
    function vin(){
      var vin= ""

      for(var i= 0; i < 18; i++ ){
        vin +=chars[Math.floor(Math.random()*35)]
      }
      return vin
    }

    this.name=name;
    this.wheels=wheels;
    this.passengers=passengers;
    this.speed=speed;
    this.vin= vin()



    CarConstructor.prototype.make_noise= function(noise){
      var noise= noise || "honk";
      console.log(noise)
      return this;
    }


    CarConstructor.prototype.move= function(){
      this.update_distance_traveled();
      this.make_noise();
      return this;
    }



    CarConstructor.prototype.checkmiles= function(){
      console.log(distance_traveled)
      return this;
    }

}


     var bike= new CarConstructor("Bike", 2, 1, 10)
     bike.move().move().checkmiles()

    //  bike.make_noise("ring, ring")




    //  sedan.make_noise("Honk! Honk!")

     var bus= new CarConstructor("Bus", 6, 30, 30)
     console.log(bus)

    //  sedan.make_noise("hhhooook")

     bus.pickup_passengers =function(no_people){
       bus.passengers+= no_people
     }

    //  console.log(bus.passengers)
    //  bus.pickup_passengers(7)
    //  console.log(bus.passengers)
