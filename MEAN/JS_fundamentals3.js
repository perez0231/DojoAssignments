var person= {
  name: "Jimmy Mixer",
  distance: 0,


  say_name :function(name){
    console.log(person.name)
    return this
  },
  say_something :function(phrase){
    console.log(person.name+" "+ phrase)
    return this
  },
walk :function(){
  person.distance +=3
  console.log(person.name +" "+ "is walking")
  return this
},
run :function(){
  person.distance +=10
  console.log(person.name +" "+ "is running")
  return this
}
crawl :function(){
  person.distance +=1
  console.log(person.name +" "+ "is crawing")
  return this
}


}
person.say_name().walk()

person.say_something("i am dope")


function ninja_constructor(name, cohort){
  var ninja ={}
  var belts=["red", "yellow", "black"]
  ninja.name=name;
  ninja.cohort=cohort;
  ninja.beltlevel=0;
  ninja.levelup =function(){
    if(beltlevel < 2){
      ninja.belt +=1;
      ninja.belt = belts[ninja.beltlevel]
    }
    return ninja
  }
  ninja.belt = belts[ninja.beltLevel];
 return ninja;
}
