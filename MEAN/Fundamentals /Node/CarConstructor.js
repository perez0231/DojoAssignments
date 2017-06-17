function CarConstructor(name, wheels, passengers, speed) {
  var self =this;
  var distance_traveled= 0
  function update_distance_traveled(){
    distance_traveled += self.speed
    console.log(distance_traveled)
  }



    this.name=name;
    this.wheels=wheels;
    this.passengers=passengers;
    this.speed=speed;

    this.make_noise= function(noise){
      var noise= noise || "honk";
      console.log(noise)
    }


    this.move= function(){
      update_distance_traveled();
      this.make_noise();
      return this
    }

    this.checkmiles= function(){
      console.log(distance_traveled)
    }

}

     var unicylce= new CarConstructor();

     var bike= new CarConstructor("Bike", 2, 1, 10)
     bike.move().move().checkmiles()

    //  bike.make_noise("ring, ring")

     var sedan =new CarConstructor("Sedan", 4, 5, 50)



    //  sedan.make_noise("Honk! Honk!")

     var bus= new CarConstructor("Bus", 6, 30, 30)

    //  sedan.make_noise("hhhooook")

     bus.pickup_passengers =function(no_people){
       bus.passengers+= no_people
     }

    //  console.log(bus.passengers)
    //  bus.pickup_passengers(7)
    //  console.log(bus.passengers)
